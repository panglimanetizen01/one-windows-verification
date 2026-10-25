# ONE Prompt 3 — SEC-05 bounded subprocess implementation verification (2026-10-25)

## Candidate implementation

- ONE candidate commit: `33474016345702628d0df90382e69a57f799a23b`
- Source file: `crates/one-core/src/interop.rs`
- Independent test workflow: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40189771567
- Full-suite workflow attempt: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40189865620

## Implemented

- Default wall-clock deadline: 10 seconds.
- Default per-stream capture limits: 1 MiB stdout and 1 MiB stderr.
- Default aggregate capture limit: 2 MiB.
- Concurrent stdout/stderr reader threads to prevent pipe deadlocks.
- Custom `ProcessLimits` and `run_process_with_limits` for deterministic tests and caller-specific limits.
- On timeout/output limit breach, terminate and wait for the direct child.
- On Unix, launch in a new process group and kill that group on timeout/limit; clean up remaining group members after the leader exits so descendants cannot keep inherited pipes open.
- Explicit documentation: Windows currently guarantees direct-child termination/reaping only; arbitrary descendant tree termination is not claimed.

## Focused Linux and Windows CI result

Workflow run `40189771567` completed successfully on both platforms:

- Linux Ubuntu 24.04: PASS.
- Windows Server 2025: PASS.
- On each platform, all six `interop::tests` passed:
  - capability denial does not spawn a process;
  - non-zero exit status and stdout/stderr are preserved;
  - timeout is enforced;
  - stdout flood is stopped at the output limit;
  - stderr flood is stopped at the output limit;
  - aggregate output limit is enforced.
- Static SEC-05 guard passed on both platforms.

## Full one-core suite attempt and environment blocker

The follow-up workflow run `40189865620` attempted `cargo test --locked -p one-core` on both platforms. Both full-suite jobs failed in the unrelated existing integration test `windows_x86_64_dapat_membangun_artifact_native` because the required compiler executable `clang` was not found:

- Linux: `NATIVE-TOOLCHAIN-INVOKE`, OS error 2 (compiler not found).
- Windows: `NATIVE-TOOLCHAIN-INVOKE`, “program not found”.

The six SEC-05 tests had passed earlier in the same workflow on both platforms. This full-suite failure is recorded, not reclassified as a pass. The CI environment needs its Windows-target clang/MinGW toolchain provisioned (or the test's toolchain precondition fixed) before the full one-core suite can be used as final acceptance evidence.

## Remaining verification before SEC-05 can be closed

- Re-run the complete locked one-core test suite on Linux and Windows after toolchain setup is corrected.
- Add explicit descendant-cleanup tests, especially to demonstrate the documented Windows direct-child-only semantics and ensure inherited pipe handles cannot cause an unbounded wait.
- Run `cargo fmt --check --all` and the full suite on the final candidate SHA.
- Keep SEC-05 open until all acceptance criteria are satisfied.
