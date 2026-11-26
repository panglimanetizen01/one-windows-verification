# Issue #104 exact-source independent verifier rerun — 2026-11-22

## Source and verifier identity

- ONE source SHA under test: `be454b76ac24bec3477ad387168d2fb7f9dded5a`.
- Verifier repository: `panglimanetizen01/one-windows-verification`.
- Verifier PR: #51, branch `probe/issue-104-platform-metadata-20261120`, OPEN / DRAFT / UNMERGED.
- Latest verifier branch HEAD when this record was prepared: `97751c7bbc60f0f920b3f08d52716a7449e73fb9`.
- Branch-local `CANONICAL_COMMIT.txt` and `LOCAL_CI_CANONICAL_COMMIT.txt` both pin the exact ONE source SHA above.
- Protected `verification` branch and its protected source pin were not changed.

## Exact-source ONE CI result

ONE repository GitHub Actions run #44978648595 on source SHA `be454b76...` completed SUCCESS:
- Ubuntu job #137074071574: SUCCESS; contract checks, Build, Clippy, workspace Tests, and focused vertical-slice steps all passed.
- Windows Server 2025 job #137074071682: SUCCESS; contract checks, Build, Clippy, workspace Tests, and focused vertical-slice steps all passed.
- macOS Native Filesystem run #44978648554 also completed SUCCESS on the same source SHA.

These are standard hosted CI results. They do not establish privileged Linux nested-write execution or CircleCI success.

## Independent verifier first-run findings

Verifier HEAD `e0460da7683147dc55d766c6d825bea479e7aa09`, pinned to ONE source `be454b76...`:

- Linux distro run #44978711124: SUCCESS on Ubuntu 24.04 job #137074254494 and Debian 12 job #137074254780. Both passed exact source checkout, contract checks, build, Clippy, workspace tests, and real-network tests.
- E4 adversarial filesystem run #44978711120: FAILURE in harness assertions, not a demonstrated product regression.
  - Unix job #137074254632 executed the hard-link regression and three database tests successfully, but the harness expected one `database::tests` result and observed three. It stopped before later selectors.
  - Windows job #137074254630 passed the NtCreateFile / OBJ_DONT_REPARSE junction contract probe. The filesystem harness selected the oversized-content filter in two modules (one in `adapter::tests`, one in `adapter::filesystem_windows_tests`) but incorrectly required exactly one match. Both selected tests passed; the wrapper rejected the count.
- Exact-SHA parity run #44978711155: Linux job #137074254797 failed before running any project tests because the workflow invoked `tools/ci_unittest.py` and `tools/ci_local_evidence.py` inside the checked-out ONE source directory. Those files do not exist in either repository at the pinned source. The workflow was stale and its missing-script failure is not a source-code failure. Windows job #137074254906 was still running at the last observation.

## Harness corrections

1. E4 workflow commit `bc1344ea0b60aa932bca88497cea12b4d4f91594`:
   - Corrected Linux expected database regression count from 1 to 3, matching the exact source inventory and observed execution.
   - Fully qualified the Windows oversized-content regression as `adapter::filesystem_windows_tests::filesystem_write_adapter_rejects_oversized_content` so the test harness selects the intended single test rather than two same-named tests from different modules.
   - No assertion was weakened; exact test execution and PASS output remain mandatory.
2. Exact-SHA parity workflow commit `97751c7bbc60f0f920b3f08d52716a7449e73fb9`:
   - Removed references to absent `tools/ci_unittest.py`, `tools/ci_local.py`, and `tools/ci_local_evidence.py`.
   - Replaced them with commands that exist in the exact checked-out ONE source: contract/user-documentation checks, workspace build, Clippy, and OS-appropriate workspace tests.
   - Windows skips only the Android-specific target test; Linux runs the complete workspace suite.
   - No missing artifact manifest is fabricated.

## Fresh reruns on corrected verifier HEAD

At the latest readback, the following runs had been created for verifier HEAD `97751c7...` with the same exact ONE source pin `be454b76...`:

- E4 adversarial filesystem #44979050559: QUEUED.
- Linux distro #44979050730: PENDING.
- Cross-platform #44979050610: PENDING.
- Exact-SHA CI parity #44979050576: PENDING.
- Windows native backend runtime #44979050523: PENDING.
- Additional E1, SEC-05, artifact, Android build/runtime, and focused standard-library/database runs were queued or in progress.

These are NOT PASS until terminal conclusions and job logs confirm the expected tests executed. The first-run failures remain historical evidence and are not erased by the harness fixes.

## CircleCI and acceptance boundary

- CircleCI `ci/circleci: one-linux` is FAILURE on both source SHA `be454b76...` and later docs HEAD `cda19bde24514449106cd7ceca91ab4a801468b7`. The status contexts identify workflow/job targets, but the provider pipeline/error/log mapping has not yet been collected in this record.
- The user's Termux CircleCI CLI `config validate` crashed at startup with SIGSYS in `faccessat2`; this is a local Android syscall restriction, not a YAML validation result. Use the exact-SHA diagnostic utility on the user's device and share only its redacted output; never share the CircleCI token.
- Issue #104 remains OPEN / NOT ACCEPTED. This record does not establish privileged native Linux nested-write support, full E4 acceptance, all-platform support, or CircleCI PASS.
