# Independent ONE Verification Mirror — Current Status

Updated: 2026-10-24

Canonical repository: `panglimanetizen01/one`
Canonical branch: `milestone/100-ecosystem-20261023`
Canonical source SHA: `e745b6b46ec436e7f7d005a95cb24333a4128533`
PR #80: open, draft, unmerged. No merge was performed.

The `CANONICAL_COMMIT.txt` selector points to the exact source SHA above. The following mirror runs checked out that source SHA and provide inspectable verification evidence:

- Cross-platform Windows Server 2025 + Ubuntu: [run 40064964712](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064964712) — **PASS**. Build, AST contract tests, Clippy, full workspace tests, real-network tests, and offline verification passed on both jobs.
- Linux distro matrix: [run 40064688215](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064688215) — **PASS**. Ubuntu 24.04 and Debian 12 passed contract checks, build, Clippy, workspace tests, and real-network tests.
- Focused standard library/database: [run 40064936650](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064936650) — **PASS**. UTC and database resource-bound regression tests plus one-core Clippy passed.
- Cargo lockfile bootstrap: [run 40064936639](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064936639) — **PASS**.

The Android AArch64 runtime gate is **pending**: [run 40064964681](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064964681) is attempting to boot an ARM64 Android emulator on the Linux x86-64 runner using software acceleration and then execute the actual AArch64 ELF. This is not credited as a pass until the workflow completes and its ELF execution assertion succeeds.

A separate earlier Android attempt on the same source SHA is also still running: [run 40064936624](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40064936624). Neither in-progress run is considered evidence of successful Android runtime execution.

The canonical repository's Actions runner provisioning failures are not treated as source-test results; the independent mirror is the active exact-SHA verification route. A passing Linux/Windows matrix does not by itself satisfy the complete milestone gate. The completion ledger and checkpoint in the canonical repository remain authoritative for implementation/verified scores and E1–E6 acceptance.


## Protected verifier remediation integration — 2026-11-19 16:27Z

The user explicitly authorized continuing the proposed integration of verifier remediation PRs #45–#48 into protected `verification`. All four were converted from draft to ready-for-review and squash-merged with expected-head SHA guards:

| PR | Change | PR head tested | Protected merge commit |
|---|---|---|---|
| #45 | Candidate artifact integrity; Rust/Cargo metadata aligned to source pin | `9a72e04b7e2992d655f8e3fc4e478892e91b7ae5` | `42feff8bc11d9b17d04ac9cff4abea4e80a7a832` |
| #46 | SEC-05 bounded APT retries/timeouts/source diagnostics | `8a880ad00225ed8a78a3fd58adfbc329f0df5b11` | `d539a162aeed9d22988c7ffb0c7a893e8d33f571` |
| #47 | Windows native runtime uses canonical source pin and source-pinned Rust toolchain | `bd100d10c12c7b0849f01e9481111b0b0c859dd1` | `4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4` |
| #48 | E1/focused stdlib workflows aligned to normative v0.1 test targets | `06bf1d7cbd10adadb74c79d7296f951244ae9839` | `b14abf0020472dc45842be30854e0a09317d6cb4` |

Protected `verification` now points to `b14abf0020472dc45842be30854e0a09317d6cb4`. The canonical ONE source pin remains `722d662e7a81711ba3607d26571f4048a292b3ed`; neither canonical pin nor fixed-weight ledger/DoD values were changed.

### Protected post-merge exact-SHA execution (status at 2026-11-19 16:27Z)

| Workflow | Run | Exact protected commit | Status |
|---|---:|---|---|
| Candidate Artifact Integrity | [#44566172841](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566172841) | `42feff8bc11d9b17d04ac9cff4abea4e80a7a832` | SUCCESS |
| SEC-05 subprocess baseline | [#44566187162](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566187162) | `d539a162aeed9d22988c7ffb0c7a893e8d33f571` | IN PROGRESS (Linux + Windows) |
| Windows Native Backend Runtime | [#44566197814](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566197814) | `4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4` | IN PROGRESS (Windows Server 2025) |
| E1 cross-platform acceptance | [#44566212975](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212975) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS (Ubuntu + Windows) |
| Focused stdlib/database regressions | [#44566212982](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212982) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS |
| E1 Windows acceptance | [#44566212997](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212997) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS |

These are protected-branch push validations and are distinct from the earlier PR-branch PASS runs. Do not mark pending scopes PASS until all jobs complete and their logs establish non-zero tests. Existing protected E4 #44519577693 remains SUCCESS for its declared scope; it was not rerun because no E4 source/test input changed.

### Acceptance and safety boundary

The fixed-weight ledger gate #44519577312 remains FAILURE on its recorded run. Its inspected log reported 92/100 implementation, 0/100 verified, 18 rows checked, 10 unchecked DoD items, exact-SHA evidence timeout, failed protected SEC-05/artifact/E1/focused workflow attempts, no protected exact-source Windows Native Runtime run, and no protected ONE Package Provenance Release. The new post-merge runs must become terminal and be reconciled before any new gate evaluation. Do not alter fixed weights, award points without row evidence, check DoD items speculatively, or dispatch package provenance release. Full v0.1 provenance envelope remains outside implemented scope.

Issue #104 remains OPEN / NOT ACCEPTED. This verifier-only integration does not merge ONE PR #113 or change ONE `main`. ONE main remains `d35db95153f6ddd79885494c72f5aee16c899751`; ONE PR #113 remains OPEN / DRAFT / UNMERGED at HEAD `64c490e9045aa29506772f74e3697a63a66b9695`. CircleCI `ci/circleci: one-linux` on that exact ONE SHA was PENDING at 2026-11-19T16:24:23Z (workflow `b16121d3-51f0-4297-bb05-16e15b0434ea`, job `148c47ea-a1ac-4574-8a61-1980d6c5a55a`). No CircleCI connector/action is available in this session; no provider logs or terminal status are claimed.

Next: poll the six protected verifier runs above, inspect failed-step logs if any, and update this checkpoint only with terminal exact-SHA evidence. Do not repeat already-passing PR-branch checks or protected E4 without relevant input changes.

## Protected workflow terminal-result correction — 2026-11-19 16:32Z

The first protected-branch push workflows have now reached terminal results. This section supersedes the earlier IN PROGRESS labels above where the exact run is now terminal.

- Candidate artifact integrity #44566172841: SUCCESS on merge commit 42feff8bc11d9b17d04ac9cff4abea4e80a7a832; exact job log confirms Linux and Windows candidate metadata use Rust/Cargo 1.100.0.
- SEC-05 #44566187162: SUCCESS on merge commit d539a162aeed9d22988c7ffb0c7a893e8d33f571; Linux job 135708430394 and Windows job 135708430883 SUCCESS. Logs show bounded APT setup, Linux interop tests 12 passed, full one-core suite Linux 148 passed / Windows 133 passed, and SEC-05 static fail-closed guards completed.
- Windows Native Backend Runtime #44566197814: SUCCESS on merge commit 4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4; Windows Server 2025 job 135708473420 verified exact source 722d662, Rust/Cargo 1.100.0, PE32+ AMD64, runtime exit 0, output Budi, exact-SHA manifest.
- Focused stdlib/database #44566212982: SUCCESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4; log shows stdlib 6/6, core pipeline 6/6, conformance 5/5, database unit 1/1, database vertical slice 9/9, one-core 148/148, Clippy PASS.
- E1 Windows #44566212997: SUCCESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4; log shows stdlib 6/6, core pipeline 6/6, conformance 5/5, one-core 133/133, Clippy PASS.
- E1 cross-platform #44566212975: still IN PROGRESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4. Windows job 135708526901 SUCCESS; Ubuntu job 135708526288 has completed APT/toolchain setup and is executing full workspace tests. No overall E1 cross-platform PASS until Ubuntu completes and the workflow is terminal.

The earlier fixed-weight gate #44519577312 remains FAILURE; no new gate run was dispatched while E1 cross-platform is active. The gate additionally requires row-level verified evidence, checked DoD, and protected source-bound package provenance release. Do not change fixed weights, DoD checkboxes, canonical pin, or dispatch package release to force acceptance. The canonical source pin remains 722d662e7a81711ba3607d26571f4048a292b3ed.

ONE PR #113 HEAD d20036c0ad7b00caf6b68e4807102c6ee3b895a4 remains OPEN / DRAFT / UNMERGED. CircleCI ci/circleci: one-linux remains PENDING on that exact SHA at 2026-11-19T16:30:42Z (workflow fc7039a6-8cde-464b-8c06-387e291d6d67, job 1a030227-696e-490d-bb16-dd288947976d). The previous ONE SHA 64c490e... was SUCCESS, but evidence does not transfer. No CircleCI CLI/provider connection is exposed in this session. ONE main remains d35db95153f6ddd79885494c72f5aee16c899751; Issue #104 remains OPEN / NOT ACCEPTED.

No architecture diagram changes are required for this verifier-workflow-only change. PR #50 remains documentation-only and draft pending review.

## Final E1 cross-platform result — 2026-11-19 16:33Z

Protected run #44566212975 is now COMPLETED / SUCCESS on exact protected verifier HEAD b14abf0020472dc45842be30854e0a09317d6cb4. Ubuntu 24.04 job 135708526288 and Windows Server 2025 job 135708526901 both succeeded.

Retrieved Ubuntu log confirms bounded APT source diagnostics/install, Rust/Cargo 1.100.0, stdlib helper 6/6, core pipeline 6/6, conformance 5/5, one-core library 148/148, full workspace test targets, workspace Clippy with warnings denied, and repository contract checker. Retrieved Windows log confirms Rust/Cargo 1.100.0, stdlib 6/6, core pipeline 6/6, conformance 5/5, one-core library 133/133, full workspace test targets, Clippy with warnings denied, and repository contract checker. The named E1 acceptance targets and full suites executed non-zero tests. No unsupported future APIs were implemented to satisfy E1.

All six protected post-merge runs for the authorized PR #45–#48 integration are now terminal SUCCESS:

| Scope | Run | Exact protected verifier commit |
|---|---:|---|
| Candidate artifact integrity | [#44566172841](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566172841) | 42feff8bc11d9b17d04ac9cff4abea4e80a7a832 |
| SEC-05 Linux + Windows | [#44566187162](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566187162) | d539a162aeed9d22988c7ffb0c7a893e8d33f571 |
| Windows Native Backend Runtime | [#44566197814](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566197814) | 4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4 |
| E1 cross-platform | [#44566212975](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212975) | b14abf0020472dc45842be30854e0a09317d6cb4 |
| Focused stdlib/database | [#44566212982](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212982) | b14abf0020472dc45842be30854e0a09317d6cb4 |
| E1 Windows | [#44566212997](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212997) | b14abf0020472dc45842be30854e0a09317d6cb4 |

These are scoped protected workflow successes, not acceptance of all E1–E6 or Issue #104. The fixed-weight gate #44519577312 remains a historical FAILURE and has not been rerun. Reconcile exact-SHA evidence, row-level verified points, unchecked DoD, and protected provenance-release requirements before considering a new gate evaluation. Do not alter weights, check DoD items without evidence, or dispatch release without its acceptance prerequisites.

ONE PR #113 HEAD d20036c0ad7b00caf6b68e4807102c6ee3b895a4 remains OPEN / DRAFT / UNMERGED. CircleCI ci/circleci: one-linux on that exact SHA was PENDING at last read (workflow fc7039a6-8cde-464b-8c06-387e291d6d67, job 1a030227-696e-490d-bb16-dd288947976d). The previous ONE SHA 64c490e... had SUCCESS but that result does not transfer. No CircleCI CLI/provider connection is exposed in this session. ONE main remains d35db95153f6ddd79885494c72f5aee16c899751; Issue #104 remains OPEN / NOT ACCEPTED.

## ONE CircleCI newest exact-HEAD correction — 2026-11-19 16:35Z

ONE PR #113 has advanced to documentation HEAD eeafcab579cebb762af34d1daf4830f95cba87e7. GitHub now reports ci/circleci: one-linux PENDING for this exact SHA (workflow 0621c480-6054-4fc1-8c82-b9028f105735, job 49178c86-d311-49ac-835a-6fa49985a980; updated 2026-11-19T16:35:00Z). The prior PR #113 SHA 64c490e... was SUCCESS; d20036c... was PENDING; neither transfers to eeafcab.... This session has no CircleCI CLI or provider connector and cannot inspect CircleCI step logs. Treat the current exact SHA as PENDING, not PASS or FAIL, until a terminal status is observed.

The six protected verifier integration workflows remain terminal SUCCESS on their exact verifier merge/source identities as recorded above. Verifier protected branch remains b14abf0020472dc45842be30854e0a09317d6cb4; canonical source pin remains 722d662e7a81711ba3607d26571f4048a292b3ed. Fixed-weight gate #44519577312 remains FAILURE; Issue #104 remains OPEN / NOT ACCEPTED; no ledger weights, DoD boxes, source pins, or ONE main changes.

## E3 exact-source row verification — 2026-11-19 16:39Z

ONE ledger/DoD source is updated in draft PR #103 to exact SHA f4249c231b02634a926f28d5caa71903cd0ead71. The verifier draft pin LEDGER_SOURCE_COMMIT.txt is updated to that exact 40-character SHA in this PR branch only; protected verification has not been changed. The source ledger now records E3 as 8/8 VERIFIED and the total as 92/100 implementation, 8/100 verified. The matching E3 DoD item is checked, making the count 4 checked / 9 unchecked / 13 total. Fixed weights remain unchanged.

The E3 promotion is supported by the exact canonical source pin 722d662e7a81711ba3607d26571f4048a292b3ed and terminal successful protected evidence: cross-platform #44519577496, Linux distro #44519577570, artifact integrity #44566172841, and Android API 35 AArch64 native ARM64 runtime #44519577666. The Android job log confirms API 35 arm64-v8a emulator boot, AArch64 ELF execution, exit code 0, and exact-source evidence artifact. The current protected verifier branch b14abf0 and prior protected verifier commit a44c32e both read the same canonical source pin.

This is a scoped E3 verification only. E1, E2, E4, E5, E6 remain incomplete/not verified as full rows; Issue #104 remains OPEN / NOT ACCEPTED; package-provenance release remains absent. Historical fixed-weight gate #44519577312 remains FAILURE. No overall release acceptance is claimed and no fixed weights were altered. The updated ledger-source pin is staged only in draft PR #50 and has not been merged into protected verification.
