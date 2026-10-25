//! Bounded subprocess execution.
//!
//! Defaults: 10 seconds wall-clock time, 1 MiB stdout, 1 MiB stderr, and
//! 2 MiB combined captured output. Capture is read concurrently to avoid
//! stdout/stderr pipe deadlocks. A timeout or output-limit breach kills and
//! reaps the direct child. On Unix, the child is placed in a new process group
//! and the whole group is killed on timeout/limit (and cleaned up after the
//! leader exits, so descendants cannot keep inherited pipes open). On Windows,
//! the child is assigned to a kill-on-close Job Object during `CreateProcessW`,
//! so timeout and output-limit cleanup also terminates descendants.
#[cfg(windows)]
use std::fs::File;
use std::io::Read;
#[cfg(windows)]
use std::mem::{size_of, zeroed};
#[cfg(windows)]
use std::os::windows::io::{FromRawHandle, RawHandle};
#[cfg(not(windows))]
use std::process::{Child, Command, ExitStatus, Stdio};
#[cfg(windows)]
use std::ptr::{null, null_mut};
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::thread;
use std::time::{Duration, Instant};
#[cfg(windows)]
use windows_sys::Win32::Foundation::{
    CloseHandle, HANDLE, HANDLE_FLAG_INHERIT, SetHandleInformation, WAIT_FAILED, WAIT_OBJECT_0,
    WAIT_TIMEOUT,
};
#[cfg(windows)]
use windows_sys::Win32::Security::SECURITY_ATTRIBUTES;
#[cfg(windows)]
use windows_sys::Win32::System::JobObjects::{
    CreateJobObjectW, JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE, JOBOBJECT_EXTENDED_LIMIT_INFORMATION,
    JobObjectExtendedLimitInformation, SetInformationJobObject, TerminateJobObject,
};
#[cfg(windows)]
use windows_sys::Win32::System::Pipes::CreatePipe;
#[cfg(windows)]
use windows_sys::Win32::System::Threading::{
    CreateProcessW, DeleteProcThreadAttributeList, EXTENDED_STARTUPINFO_PRESENT,
    GetExitCodeProcess, INFINITE, InitializeProcThreadAttributeList, PROCESS_INFORMATION,
    STARTF_USESTDHANDLES, STARTUPINFOEXW, UpdateProcThreadAttribute, WaitForSingleObject,
};

use crate::capability::{Capability, CapabilitySet};

pub const DEFAULT_PROCESS_TIMEOUT: Duration = Duration::from_secs(10);
pub const DEFAULT_STDOUT_LIMIT: usize = 1024 * 1024;
pub const DEFAULT_STDERR_LIMIT: usize = 1024 * 1024;
pub const DEFAULT_TOTAL_OUTPUT_LIMIT: usize = 2 * 1024 * 1024;
const POLL_INTERVAL: Duration = Duration::from_millis(10);

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ProcessSpec {
    pub program: String,
    pub args: Vec<String>,
    pub working_directory: Option<String>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct ProcessLimits {
    pub timeout: Duration,
    pub stdout_bytes: usize,
    pub stderr_bytes: usize,
    pub total_output_bytes: usize,
}

impl Default for ProcessLimits {
    fn default() -> Self {
        Self {
            timeout: DEFAULT_PROCESS_TIMEOUT,
            stdout_bytes: DEFAULT_STDOUT_LIMIT,
            stderr_bytes: DEFAULT_STDERR_LIMIT,
            total_output_bytes: DEFAULT_TOTAL_OUTPUT_LIMIT,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ProcessResult {
    pub status_code: Option<i32>,
    pub success: bool,
    pub stdout: String,
    pub stderr: String,
}

pub fn run_process(
    spec: &ProcessSpec,
    capabilities: &CapabilitySet,
) -> Result<ProcessResult, String> {
    run_process_with_limits(spec, capabilities, ProcessLimits::default())
}

pub fn run_process_with_limits(
    spec: &ProcessSpec,
    capabilities: &CapabilitySet,
    limits: ProcessLimits,
) -> Result<ProcessResult, String> {
    if !capabilities.permits(Capability::Process) {
        return Err("Kemampuan proses belum diberikan kepada program.".into());
    }
    if limits.timeout.is_zero() {
        return Err("Batas waktu proses harus lebih besar dari nol.".into());
    }

    #[cfg(windows)]
    {
        run_process_windows_with_limits(spec, limits)
    }
    #[cfg(not(windows))]
    {
        let mut command = Command::new(&spec.program);
        command
            .args(&spec.args)
            .stdout(Stdio::piped())
            .stderr(Stdio::piped());
        if let Some(dir) = &spec.working_directory {
            command.current_dir(dir);
        }
        #[cfg(unix)]
        {
            use std::os::unix::process::CommandExt;
            command.process_group(0);
        }

        let mut child = command
            .spawn()
            .map_err(|error| format!("Gagal menjalankan proses '{}': {}", spec.program, error))?;
        let stdout = child.stdout.take().expect("piped stdout must be available");
        let stderr = child.stderr.take().expect("piped stderr must be available");

        let total = Arc::new(AtomicUsize::new(0));
        let exceeded = Arc::new(AtomicBool::new(false));
        let stdout_reader = spawn_bounded_reader(
            stdout,
            limits.stdout_bytes,
            limits.total_output_bytes,
            Arc::clone(&total),
            Arc::clone(&exceeded),
        );
        let stderr_reader = spawn_bounded_reader(
            stderr,
            limits.stderr_bytes,
            limits.total_output_bytes,
            Arc::clone(&total),
            Arc::clone(&exceeded),
        );

        let deadline = Instant::now() + limits.timeout;
        let mut status: Option<ExitStatus> = None;
        let mut timed_out = false;
        loop {
            if exceeded.load(Ordering::Acquire) {
                terminate_child(&mut child);
                break;
            }
            match child.try_wait() {
                Ok(Some(exit_status)) => {
                    status = Some(exit_status);
                    break;
                }
                Ok(None) => {}
                Err(error) => {
                    terminate_child(&mut child);
                    let _ = stdout_reader.join();
                    let _ = stderr_reader.join();
                    return Err(format!(
                        "Gagal memeriksa proses '{}': {}",
                        spec.program, error
                    ));
                }
            }
            if Instant::now() >= deadline {
                timed_out = true;
                terminate_child(&mut child);
                break;
            }
            thread::sleep(POLL_INTERVAL);
        }

        // On Unix this also closes pipes inherited by descendants. On Windows,
        // only the direct child is guaranteed to be terminated; reader joins may
        // therefore be blocked by a descendant that inherited a pipe handle.
        #[cfg(unix)]
        if status.is_some() {
            kill_process_group(child.id());
        }

        let stdout = stdout_reader
            .join()
            .map_err(|_| "Pembaca stdout proses gagal.".to_owned())?;
        let stderr = stderr_reader
            .join()
            .map_err(|_| "Pembaca stderr proses gagal.".to_owned())?;

        if timed_out {
            return Err(format!(
                "Proses '{}' melewati batas waktu {:?} dan dihentikan.",
                spec.program, limits.timeout
            ));
        }
        if exceeded.load(Ordering::Acquire) {
            return Err(format!(
                "Proses '{}' melewati batas output (stdout={} byte, stderr={} byte, total={} byte) dan dihentikan.",
                spec.program, limits.stdout_bytes, limits.stderr_bytes, limits.total_output_bytes
            ));
        }
        let status = match status {
            Some(status) => status,
            None => child
                .try_wait()
                .map_err(|error| {
                    format!(
                        "Gagal mengambil status proses '{}': {}",
                        spec.program, error
                    )
                })?
                .ok_or_else(|| {
                    format!(
                        "Status proses '{}' tidak tersedia setelah dihentikan.",
                        spec.program
                    )
                })?,
        };

        Ok(ProcessResult {
            status_code: status.code(),
            success: status.success(),
            stdout: String::from_utf8_lossy(&stdout).into_owned(),
            stderr: String::from_utf8_lossy(&stderr).into_owned(),
        })
    }
}

#[cfg(windows)]
const PROC_THREAD_ATTRIBUTE_HANDLE_LIST_VALUE: usize = 0x0002_0002;
#[cfg(windows)]
const PROC_THREAD_ATTRIBUTE_JOB_LIST_VALUE: usize = 0x0002_000D;

#[cfg(windows)]
struct OwnedWindowsHandle(HANDLE);

#[cfg(windows)]
impl OwnedWindowsHandle {
    fn new(handle: HANDLE) -> Self {
        Self(handle)
    }
    fn raw(&self) -> HANDLE {
        self.0
    }
    fn take(&mut self) -> HANDLE {
        let handle = self.0;
        self.0 = null_mut();
        handle
    }
}

#[cfg(windows)]
impl Drop for OwnedWindowsHandle {
    fn drop(&mut self) {
        if !self.0.is_null() {
            // SAFETY: this wrapper uniquely owns this handle and closes it once.
            unsafe {
                CloseHandle(self.0);
            }
            self.0 = null_mut();
        }
    }
}

#[cfg(windows)]
struct WindowsAttributeList {
    _storage: Vec<usize>,
    ptr: *mut core::ffi::c_void,
}

#[cfg(windows)]
impl WindowsAttributeList {
    fn new(attribute_count: u32) -> Result<Self, String> {
        let mut bytes = 0usize;
        // SAFETY: the first call requests the required allocation size.
        unsafe {
            InitializeProcThreadAttributeList(null_mut(), attribute_count, 0, &mut bytes);
        }
        if bytes == 0 {
            return Err(format!(
                "Gagal menentukan ukuran process attribute list: {}",
                std::io::Error::last_os_error()
            ));
        }
        let mut storage = vec![0usize; bytes.div_ceil(size_of::<usize>())];
        let ptr = storage.as_mut_ptr().cast::<core::ffi::c_void>();
        // SAFETY: storage is sufficiently sized and aligned for the opaque list.
        if unsafe { InitializeProcThreadAttributeList(ptr.cast(), attribute_count, 0, &mut bytes) }
            == 0
        {
            return Err(format!(
                "Gagal menginisialisasi process attribute list: {}",
                std::io::Error::last_os_error()
            ));
        }
        Ok(Self {
            _storage: storage,
            ptr,
        })
    }
}

#[cfg(windows)]
impl Drop for WindowsAttributeList {
    fn drop(&mut self) {
        // SAFETY: this list was successfully initialized and its backing storage is alive.
        unsafe {
            DeleteProcThreadAttributeList(self.ptr.cast());
        }
    }
}

#[cfg(windows)]
fn quote_windows_argument(argument: &str) -> String {
    if !argument.is_empty()
        && !argument
            .chars()
            .any(|character| character.is_whitespace() || character == '"')
    {
        return argument.to_owned();
    }
    let mut quoted = String::from("\"");
    let mut backslashes = 0usize;
    for character in argument.chars() {
        match character {
            '\\' => backslashes += 1,
            '"' => {
                quoted.push_str(&"\\".repeat(backslashes.saturating_mul(2).saturating_add(1)));
                quoted.push('"');
                backslashes = 0;
            }
            _ => {
                quoted.push_str(&"\\".repeat(backslashes));
                backslashes = 0;
                quoted.push(character);
            }
        }
    }
    quoted.push_str(&"\\".repeat(backslashes.saturating_mul(2)));
    quoted.push('"');
    quoted
}

#[cfg(windows)]
fn windows_command_line(program: &str, args: &[String]) -> Vec<u16> {
    let mut command_line = quote_windows_argument(program);
    for argument in args {
        command_line.push(' ');
        command_line.push_str(&quote_windows_argument(argument));
    }
    command_line
        .encode_utf16()
        .chain(std::iter::once(0))
        .collect()
}

#[cfg(windows)]
fn run_process_windows_with_limits(
    spec: &ProcessSpec,
    limits: ProcessLimits,
) -> Result<ProcessResult, String> {
    let mut security: SECURITY_ATTRIBUTES = unsafe { zeroed() };
    security.nLength = size_of::<SECURITY_ATTRIBUTES>() as u32;
    security.bInheritHandle = 1;

    let mut stdin_read_raw: HANDLE = null_mut();
    let mut stdin_write_raw: HANDLE = null_mut();
    let mut stdout_read_raw: HANDLE = null_mut();
    let mut stdout_write_raw: HANDLE = null_mut();
    let mut stderr_read_raw: HANDLE = null_mut();
    let mut stderr_write_raw: HANDLE = null_mut();

    // SAFETY: output pointers are valid; SECURITY_ATTRIBUTES requests inheritable pipe handles.
    let stdin_pipe_ok =
        unsafe { CreatePipe(&mut stdin_read_raw, &mut stdin_write_raw, &security, 0) };
    let stdin_read = OwnedWindowsHandle::new(stdin_read_raw);
    let stdin_write = OwnedWindowsHandle::new(stdin_write_raw);
    if stdin_pipe_ok == 0 {
        return Err(format!(
            "Gagal membuat pipe stdin: {}",
            std::io::Error::last_os_error()
        ));
    }

    // SAFETY: output pointers are valid; SECURITY_ATTRIBUTES requests inheritable pipe handles.
    let stdout_pipe_ok =
        unsafe { CreatePipe(&mut stdout_read_raw, &mut stdout_write_raw, &security, 0) };
    let mut stdout_read = OwnedWindowsHandle::new(stdout_read_raw);
    let stdout_write = OwnedWindowsHandle::new(stdout_write_raw);
    if stdout_pipe_ok == 0 {
        return Err(format!(
            "Gagal membuat pipe stdout: {}",
            std::io::Error::last_os_error()
        ));
    }

    // SAFETY: output pointers are valid; SECURITY_ATTRIBUTES requests inheritable pipe handles.
    let stderr_pipe_ok =
        unsafe { CreatePipe(&mut stderr_read_raw, &mut stderr_write_raw, &security, 0) };
    let mut stderr_read = OwnedWindowsHandle::new(stderr_read_raw);
    let stderr_write = OwnedWindowsHandle::new(stderr_write_raw);
    if stderr_pipe_ok == 0 {
        return Err(format!(
            "Gagal membuat pipe stderr: {}",
            std::io::Error::last_os_error()
        ));
    }

    // Parent-side pipe ends must not be inherited by the child.
    for handle in [stdin_write.raw(), stdout_read.raw(), stderr_read.raw()] {
        // SAFETY: handle is valid and owned above.
        if unsafe { SetHandleInformation(handle, HANDLE_FLAG_INHERIT, 0) } == 0 {
            return Err(format!(
                "Gagal membatasi pewarisan handle pipe: {}",
                std::io::Error::last_os_error()
            ));
        }
    }

    // PROC_THREAD_ATTRIBUTE_JOB_LIST assigns the child before its first instruction,
    // eliminating the vulnerable spawn-then-AssignProcessToJobObject interval.
    // SAFETY: null attributes/name request a private unnamed job.
    let job_raw = unsafe { CreateJobObjectW(null(), null()) };
    if job_raw.is_null() {
        return Err(format!(
            "Gagal membuat Windows Job Object: {}",
            std::io::Error::last_os_error()
        ));
    }
    let job = OwnedWindowsHandle::new(job_raw);
    let mut job_limits: JOBOBJECT_EXTENDED_LIMIT_INFORMATION = unsafe { zeroed() };
    job_limits.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;
    // SAFETY: job handle and correctly sized limits structure are valid.
    if unsafe {
        SetInformationJobObject(
            job.raw(),
            JobObjectExtendedLimitInformation,
            &job_limits as *const _ as *const core::ffi::c_void,
            size_of::<JOBOBJECT_EXTENDED_LIMIT_INFORMATION>() as u32,
        )
    } == 0
    {
        return Err(format!(
            "Gagal mengonfigurasi Windows Job Object: {}",
            std::io::Error::last_os_error()
        ));
    }

    let attributes = WindowsAttributeList::new(2)?;
    let child_handles = [stdin_read.raw(), stdout_write.raw(), stderr_write.raw()];
    // SAFETY: the attribute list is initialized and the handle array stays alive for the call.
    if unsafe {
        UpdateProcThreadAttribute(
            attributes.ptr.cast(),
            0,
            PROC_THREAD_ATTRIBUTE_HANDLE_LIST_VALUE,
            child_handles.as_ptr() as *mut core::ffi::c_void,
            size_of::<[HANDLE; 3]>(),
            null_mut(),
            null_mut(),
        )
    } == 0
    {
        return Err(format!(
            "Gagal membatasi handle yang diwariskan: {}",
            std::io::Error::last_os_error()
        ));
    }
    let mut job_for_child = job.raw();
    // SAFETY: the job handle pointer and attribute list are valid for CreateProcessW.
    if unsafe {
        UpdateProcThreadAttribute(
            attributes.ptr.cast(),
            0,
            PROC_THREAD_ATTRIBUTE_JOB_LIST_VALUE,
            &mut job_for_child as *mut HANDLE as *mut core::ffi::c_void,
            size_of::<HANDLE>(),
            null_mut(),
            null_mut(),
        )
    } == 0
    {
        return Err(format!(
            "Gagal mengikat Windows Job Object saat pembuatan proses: {}",
            std::io::Error::last_os_error()
        ));
    }

    let mut startup: STARTUPINFOEXW = unsafe { zeroed() };
    startup.StartupInfo.cb = size_of::<STARTUPINFOEXW>() as u32;
    startup.StartupInfo.dwFlags = STARTF_USESTDHANDLES;
    startup.StartupInfo.hStdInput = stdin_read.raw();
    startup.StartupInfo.hStdOutput = stdout_write.raw();
    startup.StartupInfo.hStdError = stderr_write.raw();
    startup.lpAttributeList = attributes.ptr.cast();

    let mut command_line = windows_command_line(&spec.program, &spec.args);
    let working_directory = spec.working_directory.as_ref().map(|directory| {
        directory
            .encode_utf16()
            .chain(std::iter::once(0))
            .collect::<Vec<u16>>()
    });
    let current_directory = working_directory
        .as_ref()
        .map_or(null(), |directory| directory.as_ptr());

    let mut process_info: PROCESS_INFORMATION = unsafe { zeroed() };
    // SAFETY: command line is writable/NUL-terminated; startup attributes and stdio handles
    // remain alive through CreateProcessW. Handle inheritance is restricted by HANDLE_LIST.
    let created = unsafe {
        CreateProcessW(
            null(),
            command_line.as_mut_ptr(),
            null(),
            null(),
            1,
            EXTENDED_STARTUPINFO_PRESENT,
            null(),
            current_directory,
            &startup.StartupInfo,
            &mut process_info,
        )
    };
    if created == 0 {
        return Err(format!(
            "Gagal membuat proses '{}' dengan Job Object: {}",
            spec.program,
            std::io::Error::last_os_error()
        ));
    }

    let process = OwnedWindowsHandle::new(process_info.hProcess);
    let _thread = OwnedWindowsHandle::new(process_info.hThread);
    // Close our copies of the child's pipe ends; stdin now reaches EOF.
    drop(stdin_read);
    drop(stdin_write);
    drop(stdout_write);
    drop(stderr_write);

    // Transfer ownership of the read handles to File so the bounded readers close them.
    let stdout = unsafe { File::from_raw_handle(stdout_read.take() as RawHandle) };
    let stderr = unsafe { File::from_raw_handle(stderr_read.take() as RawHandle) };
    let total = Arc::new(AtomicUsize::new(0));
    let exceeded = Arc::new(AtomicBool::new(false));
    let stdout_reader = spawn_bounded_reader(
        stdout,
        limits.stdout_bytes,
        limits.total_output_bytes,
        Arc::clone(&total),
        Arc::clone(&exceeded),
    );
    let stderr_reader = spawn_bounded_reader(
        stderr,
        limits.stderr_bytes,
        limits.total_output_bytes,
        Arc::clone(&total),
        Arc::clone(&exceeded),
    );

    let deadline = Instant::now() + limits.timeout;
    let poll_ms = POLL_INTERVAL.as_millis().clamp(1, u32::MAX as u128) as u32;
    let mut timed_out = false;
    loop {
        if exceeded.load(Ordering::Acquire) {
            // SAFETY: job handle owns the child and all descendants.
            unsafe {
                TerminateJobObject(job.raw(), 1);
            }
            break;
        }
        // SAFETY: process handle remains valid until this function returns.
        match unsafe { WaitForSingleObject(process.raw(), poll_ms) } {
            WAIT_OBJECT_0 => break,
            WAIT_TIMEOUT => {
                if Instant::now() >= deadline {
                    timed_out = true;
                    // SAFETY: job handle owns the child and all descendants.
                    unsafe {
                        TerminateJobObject(job.raw(), 1);
                    }
                    break;
                }
            }
            WAIT_FAILED => {
                let error = std::io::Error::last_os_error();
                // SAFETY: terminate the job and wait for the direct child before cleanup.
                unsafe {
                    TerminateJobObject(job.raw(), 1);
                    WaitForSingleObject(process.raw(), INFINITE);
                }
                drop(job);
                let _ = stdout_reader.join();
                let _ = stderr_reader.join();
                return Err(format!("Gagal menunggu proses '{}': {error}", spec.program));
            }
            _ => {}
        }
    }

    // Reap the direct child after timeout/output-limit termination, then close the
    // kill-on-close job before joining readers so descendants cannot retain pipe handles.
    // SAFETY: process handle remains valid; waiting on an exited process returns immediately.
    unsafe {
        WaitForSingleObject(process.raw(), INFINITE);
    }
    drop(job);

    let stdout = stdout_reader
        .join()
        .map_err(|_| "Pembaca stdout proses gagal.".to_owned())?;
    let stderr = stderr_reader
        .join()
        .map_err(|_| "Pembaca stderr proses gagal.".to_owned())?;

    if timed_out {
        return Err(format!(
            "Proses '{}' melewati batas waktu {:?} dan dihentikan.",
            spec.program, limits.timeout
        ));
    }
    if exceeded.load(Ordering::Acquire) {
        return Err(format!(
            "Proses '{}' melewati batas output (stdout={} byte, stderr={} byte, total={} byte) dan dihentikan.",
            spec.program, limits.stdout_bytes, limits.stderr_bytes, limits.total_output_bytes
        ));
    }

    let mut exit_code = 0u32;
    // SAFETY: process handle is valid and has signaled termination.
    if unsafe { GetExitCodeProcess(process.raw(), &mut exit_code) } == 0 {
        return Err(format!(
            "Gagal mengambil status proses '{}': {}",
            spec.program,
            std::io::Error::last_os_error()
        ));
    }
    let status_code = exit_code as i32;
    Ok(ProcessResult {
        status_code: Some(status_code),
        success: status_code == 0,
        stdout: String::from_utf8_lossy(&stdout).into_owned(),
        stderr: String::from_utf8_lossy(&stderr).into_owned(),
    })
}

fn spawn_bounded_reader<R: Read + Send + 'static>(
    mut reader: R,
    stream_limit: usize,
    total_limit: usize,
    total: Arc<AtomicUsize>,
    exceeded: Arc<AtomicBool>,
) -> thread::JoinHandle<Vec<u8>> {
    thread::spawn(move || {
        let mut captured = Vec::with_capacity(stream_limit.min(8192));
        let mut buffer = [0u8; 8192];
        loop {
            match reader.read(&mut buffer) {
                Ok(0) => break,
                Ok(count) => {
                    if captured.len().saturating_add(count) > stream_limit {
                        exceeded.store(true, Ordering::Release);
                        break;
                    }
                    let mut current = total.load(Ordering::Acquire);
                    let reserved = loop {
                        let Some(next) = current
                            .checked_add(count)
                            .filter(|next| *next <= total_limit)
                        else {
                            break false;
                        };
                        match total.compare_exchange_weak(
                            current,
                            next,
                            Ordering::AcqRel,
                            Ordering::Acquire,
                        ) {
                            Ok(_) => break true,
                            Err(observed) => current = observed,
                        }
                    };
                    if !reserved {
                        exceeded.store(true, Ordering::Release);
                        break;
                    }
                    captured.extend_from_slice(&buffer[..count]);
                }
                Err(error) if error.kind() == std::io::ErrorKind::Interrupted => continue,
                Err(_) => break,
            }
        }
        captured
    })
}

#[cfg(not(windows))]
fn terminate_child(child: &mut Child) {
    #[cfg(unix)]
    kill_process_group(child.id());
    let _ = child.kill();
    let _ = child.wait();
}

#[cfg(unix)]
fn kill_process_group(child_id: u32) {
    // The child was started in a new process group whose ID is its PID.
    // SAFETY: kill is called with a negative process-group ID and no pointers.
    unsafe {
        libc::kill(-(child_id as libc::pid_t), libc::SIGKILL);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn allowed() -> CapabilitySet {
        CapabilitySet::none().allow(Capability::Process)
    }

    fn spec(script: &str) -> ProcessSpec {
        #[cfg(windows)]
        let (program, args) = (
            "powershell".to_owned(),
            vec![
                "-NoProfile".into(),
                "-NonInteractive".into(),
                "-Command".into(),
                script.into(),
            ],
        );
        #[cfg(not(windows))]
        let (program, args) = ("sh".to_owned(), vec!["-c".into(), script.into()]);
        ProcessSpec {
            program,
            args,
            working_directory: None,
        }
    }

    fn tight_limits() -> ProcessLimits {
        ProcessLimits {
            timeout: Duration::from_secs(3),
            stdout_bytes: 4096,
            stderr_bytes: 4096,
            total_output_bytes: 6144,
        }
    }

    #[test]
    fn denied_process_capability_never_spawns() {
        let process = ProcessSpec {
            program: "one-test-process-that-must-not-run".into(),
            args: vec![],
            working_directory: None,
        };
        let error =
            run_process(&process, &CapabilitySet::none()).expect_err("process must be denied");
        assert_eq!(error, "Kemampuan proses belum diberikan kepada program.");
    }

    #[test]
    fn allowed_process_preserves_exit_status_and_streams() {
        let process = if cfg!(windows) {
            spec("Write-Output stdout; [Console]::Error.Write('stderr'); exit 7")
        } else {
            spec("printf stdout; printf stderr >&2; exit 7")
        };
        let result =
            run_process(&process, &allowed()).expect("process capability permits execution");
        assert!(!result.success);
        assert_eq!(result.status_code, Some(7));
        assert!(result.stdout.contains("stdout"));
        assert!(result.stderr.contains("stderr"));
    }

    #[test]
    fn process_timeout_is_enforced_and_child_is_reaped() {
        let process = if cfg!(windows) {
            spec("Start-Sleep -Seconds 5")
        } else {
            spec("sleep 5")
        };
        let limits = ProcessLimits {
            timeout: Duration::from_millis(100),
            ..ProcessLimits::default()
        };
        let error = run_process_with_limits(&process, &allowed(), limits)
            .expect_err("long process must time out");
        assert!(error.contains("melewati batas waktu"), "{error}");
    }

    #[cfg(windows)]
    #[test]
    fn windows_job_object_terminates_descendant_after_parent_exits() {
        let process = spec(
            "$child = Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-NonInteractive','-Command','Start-Sleep -Seconds 30') -PassThru; Write-Output $child.Id; exit 0",
        );
        let result = run_process(&process, &allowed())
            .expect("parent should exit successfully while descendant is contained");
        let child_pid: u32 = result
            .stdout
            .trim()
            .parse()
            .expect("child PID should be printed");
        let deadline = Instant::now() + Duration::from_secs(3);
        loop {
            let child_exists = std::process::Command::new("powershell.exe")
                .args([
                    "-NoProfile",
                    "-NonInteractive",
                    "-Command",
                    &format!("if (Get-Process -Id {child_pid} -ErrorAction SilentlyContinue) {{ exit 0 }} else {{ exit 1 }}"),
                ])
                .status()
                .expect("PowerShell process query should run")
                .success();
            if !child_exists {
                break;
            }
            assert!(
                Instant::now() < deadline,
                "descendant process {child_pid} survived Job Object closure"
            );
            std::thread::sleep(Duration::from_millis(50));
        }
    }

    #[cfg(windows)]
    #[test]
    fn windows_job_object_immediate_descendant_spawn_stress() {
        for _ in 0..10 {
            let process = spec(
                "$child = Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-NonInteractive','-Command','Start-Sleep -Seconds 30') -PassThru; Write-Output $child.Id; exit 0",
            );
            let result = run_process(&process, &allowed())
                .expect("parent should exit while its descendant is contained");
            let child_pid: u32 = result
                .stdout
                .trim()
                .parse()
                .expect("child PID should be printed");
            let deadline = Instant::now() + Duration::from_secs(3);
            loop {
                let child_exists = std::process::Command::new("powershell.exe")
                    .args([
                        "-NoProfile",
                        "-NonInteractive",
                        "-Command",
                        &format!("if (Get-Process -Id {child_pid} -ErrorAction SilentlyContinue) {{ exit 0 }} else {{ exit 1 }}"),
                    ])
                    .status()
                    .expect("PowerShell process query should run")
                    .success();
                if !child_exists {
                    break;
                }
                assert!(
                    Instant::now() < deadline,
                    "iteration left descendant {child_pid} alive"
                );
                std::thread::sleep(Duration::from_millis(20));
            }
        }
    }

    #[cfg(windows)]
    #[test]
    fn windows_command_line_quotes_paths_and_arguments() {
        assert_eq!(
            windows_command_line(
                r"C:\Program Files\tool.exe",
                &["".into(), "two words".into(), "plain".into()],
            )
            .iter()
            .copied()
            .take_while(|unit| *unit != 0)
            .collect::<Vec<_>>(),
            "\"C:\\Program Files\\tool.exe\" \"\" \"two words\" plain"
                .encode_utf16()
                .collect::<Vec<_>>()
        );
    }

    #[cfg(windows)]
    #[test]
    fn windows_process_preserves_arguments_unicode_and_working_directory() {
        let suffix = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .expect("system clock should be after Unix epoch")
            .as_nanos();
        let working_directory = std::env::temp_dir().join(format!(
            "one process args 日本語 {} {suffix}",
            std::process::id()
        ));
        std::fs::create_dir_all(&working_directory)
            .expect("temporary working directory should be created");
        let script_path = working_directory.join("echo args 日本語.ps1");
        std::fs::write(
            &script_path,
            r#"[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::WriteLine("cwd:" + (Get-Location).Path)
foreach ($arg in $args) {
    $encoded = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes([string]$arg))
    [Console]::WriteLine("arg:" + $encoded)
}
"#,
        )
        .expect("PowerShell argument probe should be written");

        let expected_arguments = ["two words", "", "quote\"value", "日本語", "trailing\\"];
        let process = ProcessSpec {
            program: "powershell.exe".into(),
            args: vec![
                "-NoProfile".into(),
                "-NonInteractive".into(),
                "-File".into(),
                script_path.to_string_lossy().into_owned(),
                expected_arguments[0].into(),
                expected_arguments[1].into(),
                expected_arguments[2].into(),
                expected_arguments[3].into(),
                expected_arguments[4].into(),
            ],
            working_directory: Some(working_directory.to_string_lossy().into_owned()),
        };
        let result = run_process(&process, &allowed())
            .expect("PowerShell should receive the exact argument vector");
        assert!(result.success, "{}", result.stderr);

        let canonical_working_directory = std::fs::canonicalize(&working_directory)
            .expect("working directory should canonicalize")
            .to_string_lossy()
            .into_owned();
        let expected_working_directory = canonical_working_directory
            .strip_prefix(r"\\?\")
            .unwrap_or(&canonical_working_directory);
        let lines: Vec<&str> = result.stdout.lines().collect();
        assert!(
            lines.first().is_some_and(|line| {
                line.strip_prefix("cwd:").is_some_and(|actual| {
                    actual
                        .strip_prefix(r"\\?\")
                        .unwrap_or(actual)
                        .eq_ignore_ascii_case(expected_working_directory)
                })
            }),
            "working directory mismatch: {}",
            result.stdout
        );
        assert_eq!(
            &lines[1..],
            [
                "arg:dHdvIHdvcmRz",
                "arg:",
                "arg:cXVvdGUidmFsdWU=",
                "arg:5pel5pys6Kqe",
                "arg:dHJhaWxpbmdc",
            ],
            "argument boundaries, empty argument, quotes, Unicode, and trailing backslash must survive CreateProcessW"
        );
        std::fs::remove_dir_all(&working_directory)
            .expect("temporary working directory should be cleaned up");
    }

    #[cfg(windows)]
    #[test]
    fn windows_job_object_terminates_descendant_on_timeout() {
        let marker = std::env::temp_dir().join(format!(
            "one-sec05-descendant-{}-{}.txt",
            std::process::id(),
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("system clock should be after Unix epoch")
                .as_nanos()
        ));
        let marker_literal = marker.to_string_lossy().replace('\'', "''");
        let process = spec(&format!(
            "$child = Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-NonInteractive','-Command','Start-Sleep -Seconds 30') -PassThru; Set-Content -LiteralPath '{marker_literal}' -Value $child.Id; Start-Sleep -Seconds 30"
        ));
        let limits = ProcessLimits {
            timeout: Duration::from_secs(2),
            ..ProcessLimits::default()
        };
        let error = run_process_with_limits(&process, &allowed(), limits)
            .expect_err("parent and descendant must be terminated on timeout");
        assert!(error.contains("melewati batas waktu"), "{error}");

        let pid_text = std::fs::read_to_string(&marker).expect("child PID marker should exist");
        let _ = std::fs::remove_file(&marker);
        let child_pid: u32 = pid_text
            .trim()
            .parse()
            .expect("child PID should be numeric");
        let deadline = Instant::now() + Duration::from_secs(3);
        loop {
            let child_exists = std::process::Command::new("powershell.exe")
                .args([
                    "-NoProfile",
                    "-NonInteractive",
                    "-Command",
                    &format!("if (Get-Process -Id {child_pid} -ErrorAction SilentlyContinue) {{ exit 0 }} else {{ exit 1 }}"),
                ])
                .status()
                .expect("PowerShell process query should run")
                .success();
            if !child_exists {
                break;
            }
            assert!(
                Instant::now() < deadline,
                "descendant process {child_pid} survived timeout"
            );
            std::thread::sleep(Duration::from_millis(50));
        }
    }

    #[test]
    fn stdout_flood_is_bounded() {
        let process = if cfg!(windows) {
            spec(
                "while ($true) { [Console]::Out.Write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') }",
            )
        } else {
            spec("yes x")
        };
        let error = run_process_with_limits(&process, &allowed(), tight_limits())
            .expect_err("stdout flood must be stopped");
        assert!(error.contains("batas output"), "{error}");
    }

    #[test]
    fn stderr_flood_is_bounded() {
        let process = if cfg!(windows) {
            spec(
                "while ($true) { [Console]::Error.Write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') }",
            )
        } else {
            spec("yes x >&2")
        };
        let error = run_process_with_limits(&process, &allowed(), tight_limits())
            .expect_err("stderr flood must be stopped");
        assert!(error.contains("batas output"), "{error}");
    }

    #[test]
    fn aggregate_output_limit_is_enforced() {
        let process = if cfg!(windows) {
            spec(
                "1..1000 | ForEach-Object { [Console]::Out.Write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'); [Console]::Error.Write('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') }",
            )
        } else {
            spec(
                "i=0; while [ $i -lt 1000 ]; do printf 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; printf 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy' >&2; i=$((i+1)); done",
            )
        };
        let limits = ProcessLimits {
            total_output_bytes: 1024,
            stdout_bytes: 4096,
            stderr_bytes: 4096,
            ..tight_limits()
        };
        let error = run_process_with_limits(&process, &allowed(), limits)
            .expect_err("aggregate flood must be stopped");
        assert!(error.contains("batas output"), "{error}");
    }
}
