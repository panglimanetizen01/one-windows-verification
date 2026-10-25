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

## Follow-up final-candidate CI result (2026-10-25)

- Final candidate tested: `65ec5aa66e7ebf77595fe2839f096cfc36def5d8`
- Workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40195243449
- Workflow harness commit: `0c7156e42da90ab09260337c45391bd556457b4b`
- Overall conclusion: **SUCCESS**; both Linux and Windows jobs completed successfully.
- Linux Ubuntu 24.04: complete `cargo test --locked -p one-core` passed, with the main test binary reporting 234 passed and 0 failed; additional test binaries also passed. Scoped `rustfmt --edition 2024 --check crates/one-core/src/interop.rs` passed.
- Windows Server 2025: focused subprocess contract tests passed (6 passed, 0 failed); complete `cargo test --locked -p one-core` passed (main test binary 223 passed, 0 failed; additional test binaries passed); scoped rustfmt and static SEC-05 guard passed.
- Windows toolchain selection was verified in logs: `C:\\Program Files\\LLVM\\bin\\clang.exe`, clang 20.1.8.
- The prior compiler-not-found and formatting blockers are resolved for this candidate and workflow.

## Acceptance caveat — not yet a full security sign-off

This successful workflow validates the current focused implementation and full `one-core` test suite on both OSes at the exact candidate SHA above. It does **not** close every SEC-05 security criterion: the Windows implementation explicitly guarantees direct-child termination/reaping only, and explicit descendant-process cleanup / inherited-pipe bounded-wait tests remain outstanding. `cargo fmt --check --all` has not been established as passing for the whole repository. Keep issue #81 open until those remaining acceptance criteria are either implemented and tested or explicitly resolved in the issue's acceptance contract.



## Windows Job Object descendant-cleanup candidate (2026-10-25)

- Candidate source SHA: `5fa0faa32c9114cccdb42e18fd0568109a653003`
- Lab workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40196588909
- Workflow harness commit: `1b6119051d088a2521fb96fb170769b4d85f19f7`
- Overall conclusion: **SUCCESS**; Linux and Windows jobs completed successfully.
- Windows Server 2025 focused subprocess contract suite: **7 passed, 0 failed**; includes `windows_job_object_terminates_descendant_after_parent_exits`.
- Windows full `cargo test --locked -p one-core`: main test binary **224 passed, 0 failed**; auxiliary test binaries also passed (one existing ignored test in an auxiliary binary).
- Windows scoped rustfmt and static SEC-05 marker guard passed.
- Linux job passed the workflow's corresponding subprocess, formatting, and static guard steps.

This is stronger evidence for descendant cleanup than the prior candidate, but it is not a blanket release/security sign-off. The test exercises a descendant launched by a child that exits; the current spawn-then-assign Job Object sequence may still have a race if a child creates descendants before assignment. The workflow also uses a scoped rustfmt check, not whole-repository `cargo fmt --check --all`. Keep issue #81 open until the race/containment semantics and the complete SEC-05 acceptance criteria are reviewed and explicitly verified.

## Verification-gate correction (2026-10-25)

- Lab workflow update commit: `a9bcd1684cdced75ee69aad0ea57834581955897`.
- Corrected the PowerShell/.NET regular expressions in the Windows fail-closed guard. The prior doubled backslashes would have matched literal backslashes rather than the intended whitespace/parenthesis pattern, so that guard was not reliable evidence before this correction.
- The guard now rejects `AssignProcessToJobObject(...)` and requires `PROC_THREAD_ATTRIBUTE_JOB_LIST` plus `CreateProcessW(...)`. This is a static launch-path gate only; it does not prove correct handle inheritance, argument quoting, cleanup, or runtime behavior.
- Microsoft documents `PROC_THREAD_ATTRIBUTE_JOB_LIST` as assigning job handles during process creation on Windows 10 / Windows Server 2016 and newer: https://learn.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute
- The pinned candidate `5fa0faa32c9114cccdb42e18fd0568109a653003` still uses spawn-then-assign and is expected to fail the corrected gate. No pass is claimed for that candidate under this stricter gate.
- Required next step remains a reviewed process-creation implementation and Linux/Windows dynamic tests on the exact same candidate SHA. SEC-05 remains open.

## Guard self-test added (2026-10-25)

- Workflow commit: `0ba11df6e16b5642e9e05f6689ffe6f1f805e47a`.
- Added PowerShell regex self-tests for direct calls, calls with intervening whitespace, the required `CreateProcessW(...)` marker, and a negative unrelated-call case before scanning the pinned candidate.
- The workflow is configured to run on changes to this workflow file on branch `verification`; however, the connector has not returned a run result for this commit. Treat these checks as authored and read-back verified, not as runtime-passing until the GitHub Actions run logs confirm them.
- The pinned candidate remains expected to fail the later fail-closed source gate because it uses `AssignProcessToJobObject` after spawning. This is intentional and must not be relabeled as a test pass.

## Candidate-selectable lab workflow (2026-10-25)

- Workflow commit: `2879785ce7389f17636dacc5c1dcee096c0f95b5`.
- Added optional `workflow_dispatch` input `candidate_sha`; both Linux and Windows jobs check out and assert the exact selected SHA. The default remains `5fa0faa32c9114cccdb42e18fd0568109a653003` for historical reproducibility.
- Read-back verification confirmed both checkout refs and both SHA assertions use the input/default expression. This makes the lab reusable for a future rewritten candidate without silently changing which source was tested.
- This workflow update is not a test result. No Actions run conclusion has been confirmed here. The default candidate is still expected to fail the race-free Windows launch gate because its source uses spawn-then-assign.
- To test a future candidate, use the workflow's **Run workflow** UI on branch `verification`, supply its full source commit SHA, then retain the run URL and logs as evidence. Linux and Windows jobs must report the same source SHA.

## Expanded Windows process-creation guard (2026-10-25)

- Workflow commits: `35d09a5b7e9ffb55e28856e88b4ac9a990b01ae4` and self-test simplification `691e6d4f578725c535321327df5d3ed47fb6a6b8`.
- The Windows static gate now requires the job-list attribute and `EXTENDED_STARTUPINFO_PRESENT`, and checks for calls to `CreateProcessW`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute`, and `DeleteProcThreadAttributeList`. It continues to reject `AssignProcessToJobObject(...)`.
- Added focused regex self-tests for each attribute-list API call. Read-back inspection confirmed the guard text is present alongside the candidate-SHA input.
- This remains a fail-closed static gate, not proof of correct pointer lifetimes, handle inheritance, argument quoting, or process cleanup. No new Actions run result is confirmed here; SEC-05 remains open until implementation and dynamic Windows/Linux verification pass on one exact SHA.
