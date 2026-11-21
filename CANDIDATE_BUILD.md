# Candidate build matrix — non-acceptance evidence

`CANDIDATE_BUILD_COMMIT.txt` pins the current ONE PR #108 CircleCI migration candidate for a dedicated Linux/Windows `cargo test --locked -p one-core` matrix. This pin is intentionally independent from both `CANONICAL_COMMIT.txt` (E4 security acceptance) and `LEDGER_SOURCE_COMMIT.txt` (fixed-weight ledger/DoD documentation). The build matrix establishes a repeatable compile/test route and provides detailed logs; it does not award fixed-weight points, satisfy E1–E6, or authorize a release. Advance only this build pin when the PR #108 source candidate advances; do not change the E4 pin until the required security implementation and adversarial test inventory are committed.

## Rust toolchain identity

The source repository pins Rust `1.100.0` in `rust-toolchain.toml`. Both Linux and Windows matrix jobs explicitly install the same exact toolchain release. A toolchain or source-pin change requires a new exact-SHA matrix run; prior results are not transferable.

## Native backend toolchain prerequisites

The full `one-core` suite includes a contract test that builds a Windows GNU artifact from both Linux and Windows hosts. The Linux runner installs `clang`, `lld`, and `mingw-w64`, then sets `ONE_WINDOWS_CLANG=clang`. The Windows runner uses the pinned `msys2/setup-msys2` action and installs `mingw-w64-x86_64-clang` plus `mingw-w64-x86_64-lld`, then sets the same override. These are test-host prerequisites, not changes to ONE target semantics or security acceptance.

## 2026-11-18 candidate update

The candidate pin now follows PR #108's exact source SHA after the Rust 1.100.0 reproducibility change. This remains a non-acceptance build/test matrix; the E4 canonical acceptance pin is unchanged.


## Exact source pin correction — 2026-11-18

The candidate pin has been advanced from the initial toolchain commit to its immediate fix-up SHA `a20676be53e5f78c465832379d86c3675a2ed7c8`. The fix-up corrects static CircleCI toolchain parsing before acceptance. This new SHA receives its own Linux/Windows run; no result from the previous candidate pin is transferred.


## Reconciliation candidate — 2026-11-18

- Non-acceptance build pin advanced to exact ONE source SHA `e47b3b52eeb7e1b25fc24f741d5bb5cc1b01f24d` on reconciliation branch `reconciliation/pr-110-base-sync-20261118`.
- Verifier commit: `46ba6c5beb028db6c1bec036fcf7f189999a5c74`; the push to `verification` changes `CANDIDATE_BUILD_COMMIT.txt`, which is a configured trigger for `.github/workflows/candidate-build-matrix.yml`.
- Expected jobs: Ubuntu 24.04 and Windows Server 2025, each checking out the exact pinned ONE SHA and running `cargo test --locked -p one-core -- --nocapture`.
- This is baseline compile/test evidence only. It does not run or satisfy E4 adversarial acceptance, does not alter `CANONICAL_COMMIT.txt`, and does not alter the independent ledger source pin.
- At update time, the newly triggered workflow has not yet been observed to completion. Record each job's exact terminal result and logs before claiming parity.


## Verifier bootstrap correction — 2026-11-18

- Static inspection found that the matrix workflow still used the full Linux `mingw-w64` metapackage, despite a documented prior timeout on that package (277 MB download / 1,293 MB installed; apt exit 124).
- The matrix workflow now uses bounded apt retries/timeouts and the previously proven minimal toolchain route: `clang-18` + `gcc-mingw-w64-x86-64-posix`, followed by a PE32+ smoke link.
- Workflow fix commit: `2ebf939dd939f23e0e1bf349d8ed0fe12da2c7e9`.
- First candidate run `44283817583` was already running with the old workflow and is not evidence for the fix.
- Fresh matrix run `44284002056` was triggered by the workflow change. Linux job `134731808510` and Windows job `134731808090` are in progress; no test result is yet claimed.


## Windows process-test remediation candidate — 2026-11-18

- The previous baseline matrix on ONE source SHA `e47b3b52eeb7e1b25fc24f741d5bb5cc1b01f24d` completed Windows job `134731808090` with 124 passed and 3 failed. Failures: stdout/stderr hard-limit test diagnostics and the Job Object descendant probe exceeding its 10-second helper deadline. The Linux job from run `44284002056` was still provisioning its MinGW toolchain at last observation; it is not transferred to this new candidate.
- Follow-up draft PR #112: https://github.com/panglimanetizen01/one/pull/112.
- New exact source candidate pin: `dc9896d1f525db6ce1e462d250bd68b8f5b28cb8`.
- Verifier pin update commit: `6cbd20a7435a9fe84867a804ff43518e4eb2aa1c`.
- This run will determine whether the Windows test harness remediation is correct. The production process deadline remains 10 seconds; only the private integration probe gets a longer test setup budget.
- This remains a non-acceptance baseline matrix and is not Issue #104/E4 evidence.


## Windows command-fixture correction — 2026-11-18

- Candidate run [44284769779](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44284769779) checked out source SHA `dc9896d1f525db6ce1e462d250bd68b8f5b28cb8`.
- Windows job `134734468629`: 125 passed, 2 failed. The Windows Job Object descendant probe now passes with the test-only 30-second setup budget. The two output-limit probes failed because `cmd.exe` rejected the quoted temp path with `The filename, directory name, or volume label syntax is incorrect.`; this is a test-fixture command-line issue, not evidence that the production output cap failed.
- Linux job `134734469111` was still running the bounded MinGW bootstrap at the time of this update; no Linux conclusion is attributed to this run.
- Follow-up source candidate in draft PR #112 is now `181ad350d8f0db53cda654c4d378425fbdd6ab24`. The Windows output-limit probes return to PowerShell byte writes, but use the private test-only 30-second timeout budget; production `run_process` remains fixed at 10 seconds.
- Verifier candidate pin advanced to `181ad350d8f0db53cda654c4d378425fbdd6ab24`; verifier pin commit `a790668f266ba23ac730cf018655a6035a0399db`.
- A new exact-SHA matrix is triggered. This remains non-acceptance baseline testing, not E4 security evidence.


## Exact-SHA cross-platform baseline PASS — 2026-11-18

- Independent verifier run [44285138516](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44285138516) completed with overall conclusion SUCCESS.
- Exact ONE candidate source SHA checked out and identity-verified by both jobs: `181ad350d8f0db53cda654c4d378425fbdd6ab24`.
- Linux Ubuntu 24.04 job `134735739281`: SUCCESS. Parsed per-test-binary totals from the complete job log: 239 passed, 0 failed, 1 ignored.
- Windows Server 2025 job `134735739823`: SUCCESS. Parsed per-test-binary totals from the complete job log: 232 passed, 0 failed, 1 ignored.
- The platform totals differ because platform-gated test binaries/cases differ. Both jobs completed the candidate `cargo test --locked -p one-core -- --nocapture` workflow successfully.
- Verifier workflow-run HEAD is `a790668f266ba23ac730cf018655a6035a0399db`; this is the verifier repository commit, not the ONE source candidate SHA.
- This is a non-acceptance compile/test baseline only. It does not satisfy Issue #104, E4, symlink/TOCTOU/reparse-point adversarial testing, or Android runtime execution.
- Candidate remains draft PR #112 pending independent CircleCI status and further review. Do not merge on the strength of this matrix alone.


## Issue #104 native API compile spike — 2026-11-18

- Exact ONE source candidate pin advanced to `7f092b0f030aa9a182a952fdafc9630221b5d038` (PR #113, draft).
- Verifier pin commit: `c613adbccf975206f07fd4d15b2da7efbb808047`.
- The source change enables windows-sys 0.61 WDK Foundation + WDK Storage/FileSystem features and adds a compile-time-only reference to OBJECT_ATTRIBUTES and NtCreateFile. It performs no filesystem I/O.
- The candidate matrix is being used strictly to compile and run the unchanged one-core baseline on Ubuntu and Windows, confirming that the native API feature gates resolve on both target builds. This is not E4 and does not test filesystem confinement.
- Issue #104 remains unimplemented; do not treat this spike as a security acceptance candidate.


## Windows compile failure triage — missing Win32_System_IO gate — 2026-11-18

- Matrix run `44286515256` checked exact ONE source SHA `7f092b0f030aa9a182a952fdafc9630221b5d038`.
- Windows Server 2025 job `134740467537` failed at `cargo test --locked -p one-core -- --nocapture`, compile error E0432: `NtCreateFile` unresolved in `windows_sys::Wdk::Storage::FileSystem`.
- The source binding declaration is gated by `Wdk_Foundation`, `Win32_Security`, `Win32_Storage_FileSystem`, and `Win32_System_IO`; the project's existing dependency already enabled the first three but omitted `Win32_System_IO`. This is a deterministic dependency feature-gate omission, not a reason to replace the native API.
- Corrective commit `14d81a93a60ea2bba1ebfd2ddf7d85baf0893e24` adds only the missing `Win32_System_IO` feature to the Windows target dependency.
- Independent candidate pin advanced to the corrected exact source SHA. The next matrix run will validate it; no compile PASS is claimed yet.
- The original run's Linux job was still running at triage time. Its final result is not inferred from the Windows failure.


## Corrected NtCreateFile feature-gate candidate — Linux baseline PASS, Windows pending — 2026-11-18

- Exact ONE source SHA: `14d81a93a60ea2bba1ebfd2ddf7d85baf0893e24`.
- Matrix run [44286988623](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44286988623).
- Linux Ubuntu 24.04 job `134742079698`: SUCCESS; complete job logs report 239 passed, 0 failed, 1 ignored. Source identity was explicitly checked against `14d81a93...`.
- Windows Server 2025 job `134742079233`: still IN_PROGRESS at the time of this record, in step `Install Windows GNU cross toolchain`. No Windows compile/test result yet.
- CircleCI `ci/circleci: one-linux` for the same exact source SHA remains PENDING.
- Linux success confirms the corrected dependency feature change does not regress Linux; it cannot validate Windows-only NtCreateFile imports.
- This is still a compile/test baseline, not Issue #104 or E4 security acceptance.


## Corrected NtCreateFile feature-gate candidate — full Linux + Windows baseline PASS — 2026-11-18

- Independent verifier run [44286988623](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44286988623) completed SUCCESS.
- Both jobs explicitly checked out and identity-verified exact ONE source SHA `14d81a93a60ea2bba1ebfd2ddf7d85baf0893e24`.
- Linux Ubuntu 24.04 job `134742079698`: SUCCESS; complete logs total 239 passed, 0 failed, 1 ignored.
- Windows Server 2025 job `134742079233`: SUCCESS; complete logs total 232 passed, 0 failed, 1 ignored.
- Windows compilation confirms the missing `Win32_System_IO` feature gate fix exposes the `NtCreateFile` binding and the complete existing one-core suite passes.
- The platform test counts differ due to platform-specific binaries/cases. Both test commands completed successfully.
- This is a non-acceptance build/test baseline only. No filesystem I/O has been implemented; it does not satisfy Issue #104 or E4 and contains no adversarial filesystem regression tests.
- CircleCI `ci/circleci: one-linux` for exact source SHA `14d81a93...` remains PENDING at last check.
- Verifier ledger update commit: pending readback after this append.


## Issue #104 native backend design + exact E4 test inventory — 2026-11-18

- Exact ONE candidate source SHA: `98c3f8a9f2f145a2155a763d47e1131ae075b3ce` (PR #113).
- Design document sections 23–24 record: native implementation decision; rejection of cap-std as the strict no-symlink enforcement boundary; parent-rename race threat; and exact E4 test-name/count contract.
- Independent candidate run [44288122054](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44288122054) is IN_PROGRESS on verifier HEAD `b881cae4de286d278b7eff0e6d1be6c88806e8b1`; Windows job `134745983528` is checking out the exact ONE candidate, Linux job `134745983669` is verifying source identity.
- CircleCI `ci/circleci: one-linux` for exact source SHA `98c3f8a...` is PENDING.
- The preceding code candidate SHA `14d81a93...` has independent Linux+Windows SUCCESS (239/0/1 and 232/0/1) and CircleCI SUCCESS. The new candidate adds documentation only; don't transfer results across SHAs.
- E4 inventory currently has 0/5 Unix filter groups and 0/6 Windows named tests implemented/accepted. Generic test-suite success is not E4 acceptance.
- No filesystem operations or authority object exist yet. Issue #104 remains OPEN / NOT IMPLEMENTED / NOT ACCEPTED. E4 and ledger acceptance pins remain unchanged.


## 2026-11-21 — PR #113 exact-SHA independent Windows/Linux matrix queued

- Advanced only the non-acceptance `CANDIDATE_BUILD_COMMIT.txt` selector to ONE PR #113 exact HEAD `3a9badf1aa281a6dbe37de2338776caa90288cdd`.
- This source SHA includes the Android compile correction commit `ed30f41fb9e69392c926a83dd9a8b6ac2e61efc4` in its ancestry. The corrected Android candidate had not yet received a dedicated Termux rerun in the checkpoint; do not treat this independent matrix as Android runtime evidence.
- The change intentionally leaves `CANONICAL_COMMIT.txt` (E4 acceptance pin) and `LEDGER_SOURCE_COMMIT.txt` untouched. This workflow is a non-acceptance `cargo test --locked -p one-core -- --nocapture` matrix on Ubuntu 24.04 and Windows Server 2025.
- Verifier pin commit: `1e3116c90904e1cabcee838cb1806a14dd3cb720`. A fresh push-triggered matrix is expected; record the actual run ID and both terminal job outcomes before claiming independent Windows/Linux PASS.
- The source repository's own GitHub Actions run #44854675780 on the same exact source SHA has Ubuntu and Windows Server 2025 Build, Clippy, and Tests steps SUCCESS. CircleCI status `ci/circleci: one-linux` is also SUCCESS on that exact SHA. These are separate CI evidence and do not substitute for this mirror's run.
- PR #113 remains OPEN / DRAFT / UNMERGED. Issue #104 remains OPEN / NOT ACCEPTED.
