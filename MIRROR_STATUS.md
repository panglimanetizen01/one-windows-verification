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
