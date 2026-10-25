# SEC-05 Windows race-free subprocess launch — acceptance plan

Status: **BLOCKED / NOT ACCEPTED** until every required check below passes on the same candidate SHA.

## Why this plan exists

The currently tested candidate `5fa0faa32c9114cccdb42e18fd0568109a653003` uses `std::process::Command::spawn()` followed by `AssignProcessToJobObject`. A child may execute before assignment, so a passing descendant-cleanup test does not establish race-free containment.

The lab's stricter static guard was corrected in commit `a9bcd1684cdced75ee69aad0ea57834581955897`. It intentionally rejects the currently pinned source candidate.

## Implementation requirements

- Create/configure the kill-on-close Job Object before launching the child.
- Use `STARTUPINFOEXW`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute` with `PROC_THREAD_ATTRIBUTE_JOB_LIST`, and `CreateProcessW` so job membership is established during process creation.
- Keep attribute storage and the job handle valid for the documented lifetime; destroy the attribute list and close every owned handle exactly once on all success/error paths.
- Preserve `ProcessSpec` semantics: executable path, argument boundaries, optional working directory, stdout/stderr capture, exit status, timeout, output caps, and error behavior.
- Restrict inherited handles to the intended standard streams. Do not accidentally inherit unrelated handles.
- On every launch failure, close partial resources; on timeout/output-limit/error, terminate and reap the direct process and close the job to clean up descendants before joining pipe-reader threads.
- Document minimum Windows support and behavior when nested-job assignment is rejected. Do not silently fall back to the race-prone spawn-then-assign path.

## Required dynamic tests on Windows

1. Existing contract tests: capability denied/no spawn; exit code and both streams preserved; timeout; stdout flood; stderr flood; aggregate output limit.
2. Parent exits while a descendant remains alive: the descendant must be terminated and inherited pipe handles must not make the API hang.
3. Immediate descendant-spawn adversarial test: repeatedly launch a parent that creates a long-lived descendant as its first action, then exits. Verify no descendant survives after the runner returns. Repeat enough times to exercise scheduling variation; do not treat a single pass as proof on its own.
4. Timeout and output-limit tests where the child has already spawned descendants: confirm process tree cleanup and bounded return time.
5. Working-directory and arguments containing spaces, quotes, Unicode, and empty arguments must arrive intact at the child.
6. Handle-leak regression: repeat success, spawn failure, timeout, and output-limit paths; ensure no growing handle count / leaked reader threads.
7. Test nested-job or unsupported-environment failure paths explicitly; failure must be bounded and must not leave an uncontained child.

## Required cross-platform/release checks

- Run focused subprocess tests and `cargo test --locked -p one-core` on Linux and Windows from the exact same source SHA.
- Run `rustfmt --edition 2024 --check crates/one-core/src/interop.rs` and `cargo fmt --check --all`; report these separately.
- Record source SHA, lab harness commit, workflow run URL, OS image, Rust/Cargo versions, every job conclusion, and test counts.
- Keep issue #81 open unless all required checks pass and the acceptance evidence is linked there. A static marker check is a gate, not runtime proof.

## Current evidence

- Prior candidate `5fa0faa32c9114cccdb42e18fd0568109a653003` passed the earlier suite, including a descendant-cleanup test, but it still has the spawn-then-assign race.
- Corrected static gate commit: `a9bcd1684cdced75ee69aad0ea57834581955897`.
- Microsoft API references:
  - https://learn.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute
  - https://learn.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessw
  - https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-startupinfoexw

This plan is deliberately not a pass report. It defines the evidence needed before SEC-05 can be accepted.
