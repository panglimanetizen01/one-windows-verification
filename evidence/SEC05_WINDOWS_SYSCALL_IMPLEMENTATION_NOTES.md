# SEC-05 Windows process-creation implementation notes

Date: 2026-10-25
Scope: supporting notes for issue ONE #81; this is not a pass report.

## Confirmed repository baseline

- Candidate branch: `sec05/windows-job-object-containment`
- Candidate SHA currently reviewed: `5fa0faa32c9114cccdb42e18fd0568109a653003`
- `crates/one-core/Cargo.toml` already enables `windows-sys 0.61.2` features `Win32_Foundation`, `Win32_Security`, `Win32_System_JobObjects`, and `Win32_System_Threading`.
- The existing `Win32_System_Threading` feature exposes `STARTUPINFOEXW`, `CreateProcessW`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute`, `DeleteProcThreadAttributeList`, `EXTENDED_STARTUPINFO_PRESENT`, and `PROC_THREAD_ATTRIBUTE_JOB_LIST`. A dependency/lockfile change should not be assumed necessary; confirm against the selected exact version at implementation time.
- Current code still calls `Command::spawn()` and then `AssignProcessToJobObject`, so the race remains.

## Implementation constraints

1. Create an unnamed Job Object and set `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE` before process creation.
2. Initialize a `STARTUPINFOEXW` attribute list with enough space for one attribute, then use `UpdateProcThreadAttribute` with `PROC_THREAD_ATTRIBUTE_JOB_LIST` and a pointer to the Job Object handle.
3. Set `STARTUPINFOEXW.StartupInfo.cb` to `size_of::<STARTUPINFOEXW>()`, pass `EXTENDED_STARTUPINFO_PRESENT`, and call `CreateProcessW`. Do not fall back to spawn-then-assign if the attribute setup or process creation fails.
4. Preserve the existing `ProcessSpec` contract: executable lookup behavior, argument boundaries and Windows quoting, optional working directory, stdout/stderr pipes, exit status, timeout, output caps, and child reaping.
5. Avoid broad handle inheritance. If inheritable handles are required for redirected pipes, explicitly constrain which handles are inherited and close parent-side duplicates at the correct time.
6. Keep all pointers and backing buffers alive through `CreateProcessW`; destroy the attribute list and close thread/process/job handles exactly once on every success and error path.
7. The current loop expects a `std::process::Child`. A raw `PROCESS_INFORMATION` does not produce a standard-library `Child`; design and review the Windows-specific wait/terminate/exit-code and pipe-reader lifecycle instead of pretending a raw handle can be wrapped as `Child` without a supported API.

## Required tests before acceptance

- Windows: direct-child exit status and stdout/stderr capture; arguments containing spaces, quotes, Unicode, and empty strings; working directory containing spaces; timeout and output-limit termination; parent exits while descendant remains; immediate-descendant-spawn stress test repeated enough to expose the former race; cleanup and handle-leak checks.
- Linux: same cross-platform contract tests remain green.
- On the same exact source SHA: focused tests, full `cargo test --locked -p one-core`, scoped formatting, and whole-repo `cargo fmt --check --all` (record any pre-existing unrelated failures precisely).
- Preserve workflow run URLs, exact source SHA for both OS jobs, toolchain versions, and unedited test logs.

## Acceptance rule

Static symbol checks are only a guardrail. They do not prove the Job Object was passed as the correct attribute value or that pointer lifetimes, quoting, handle inheritance, exit status, timeout, and cleanup are correct. SEC-05 stays open until code review and dynamic tests pass on one exact SHA. This note does not claim implementation completion or test success.

## References

- `windows-sys 0.61.2` Threading API index: https://docs.rs/windows-sys/0.61.2/windows_sys/Win32/System/Threading/
- `STARTUPINFOEXW`: https://docs.rs/windows-sys/0.61.2/windows_sys/Win32/System/Threading/struct.STARTUPINFOEXW.html
- `CreateProcessW`: https://docs.rs/windows-sys/0.61.2/windows_sys/Win32/System/Threading/fn.CreateProcessW.html
- Rust standard-library Windows process implementation reference: https://github.com/rust-lang/rust/blob/main/library/std/src/sys/process/windows.rs
