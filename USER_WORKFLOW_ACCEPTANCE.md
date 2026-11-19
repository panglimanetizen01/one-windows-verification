# ONE v0.1 — User Workflow Acceptance Review

**Reviewed documentation/code baseline:** source SHA `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f` (reconciled ledger/DoD candidate)  
**Current source candidate:** `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f` (E5 verified-point reconciliation; exact-SHA cross-platform, focused, distro, lockfile and artifact-integrity workflows passed; Android runtime and overall E1–E6 gate remain open)  
**Review status:** Manual review complete; exact-SHA cross-platform, focused, distro, lockfile and CLI/docs acceptance passes; final E5 credit pending whole-milestone gate reconciliation  
**Evidence:** [candidate verification index](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/CANDIDATE_VERIFICATION.md), [cross-platform run 40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236), [focused run 40084595238](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595238), [distro run 40084595259](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595259)

## User workflow reviewed

1. **Create → check → run:** documented CLI names and aliases match the CLI contract; beginner guide correctly states that source syntax is grammar-governed, not arbitrary natural-language execution.
2. **Test → build → package:** docs accurately distinguish local project/conformance testing, deterministic `.oneir` intermediate artifacts, and deterministic `.onepkg` packages from native executables or signed release packages.
3. **Filesystem read/write:** commands require explicit capability and exact target; write remains experimental and docs explicitly state that `--root` is not a complete sandbox.
4. **SQLite query:** documentation now states the tested boundary accurately: explicit `database.query`, resource-scoped target, parameterized read-only `SELECT`, normalized output, bounded resources, and no claim of complete persistence APIs.
5. **HTTP GET:** documentation now states the tested boundary accurately: explicit `network.connect`, exact `http://` URL, HTTP/1.1 GET, bounded/normalized response body; no claim of HTTPS or a general API client.
6. **Package provenance:** user docs correctly warn that `one package` does not sign automatically, that trust material must be provisioned independently, and that the protected release workflow must exist on the default branch before dispatch.
7. **Evidence vocabulary:** docs distinguish experimental, in-development, supported, and historical exact-SHA evidence; a later documentation commit must be retested before current-head claims.

## Corrections made

- Reconciled stale filesystem-write verification wording in `docs/panduan-pengguna/perintah-cli.md` with the exact-SHA Ubuntu/Windows evidence.
- Changed SQLite and HTTP user-facing status from “not executable-verified” to “experimental with exact-SHA cross-platform test evidence,” while preserving their narrow scope limits.
- Replaced stale claims that database/HTTP evidence existed only on Termux with explicit run links for `database_vertical_slice`, `database_orchestration`, `http_get_vertical_slice`, and `http_get_orchestration`.
- Corrected the verification-boundary paragraph to label run `40084595236` as evidence for SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, not the later documentation-only candidate.

## Test evidence and limits

At the current candidate SHA `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`, the cross-platform workflow passed CLI smoke tests, contract and user-doc consistency checks, workspace tests, real-network tests, offline verification, and release-bundle generation on Ubuntu and Windows Server 2025. Focused stdlib/SQLite/provenance tests, Ubuntu/Debian distro tests, lockfile bootstrap and artifact integrity also passed on this candidate.

The current source SHA `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f` has passed the cross-platform, focused, distro, lockfile, and artifact-integrity mirror workflows listed above. Android runtime remains open; these passes do not close E1, E2, E3, E4 or E6.

## Decision

**Manual user-workflow review: PASS. E5 implementation is recorded as 4/4; final E5 verified credit remains 0/4 pending exact-SHA rerun and ledger acceptance.** This review does not close E1, E2, E3 Android runtime, E4 security/root confinement, or E6 forensic audit.


## Exact-SHA continuation update — 2026-10-24

- Current canonical source SHA: `9d5d319b88cbee17b18554cfe7641ec1008ba62a`.
- Exact-SHA cross-platform workflow [40086990528](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528) completed successfully on Ubuntu and Windows Server 2025; CLI smoke, docs checks, offline verification, and workspace tests passed.
- Exact-SHA distro workflow [40086990470](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990470), focused workflow [40086990463](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990463), and lockfile workflow [40086990479](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990479) completed successfully.
- Android [40086990457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990457) is still in the macOS ARM64 emulator boot step. No Android ELF runtime PASS is recorded.
- Current canonical CI runs failed before execution with `runner_id: 0` and `steps: []`: [40086935480](https://github.com/panglimanetizen01/one/actions/runs/40086935480), [40086935432](https://github.com/panglimanetizen01/one/actions/runs/40086935432), and [40086935441](https://github.com/panglimanetizen01/one/actions/runs/40086935441).
- New Linux/Windows candidate artifact metadata and digests are recorded in the candidate index. ZIP contents, embedded SHA256SUMS and executable formats are not independently inspected yet because the available GitHub connector exposes metadata/logs but does not provide artifact ZIP bytes.
- Gate remains **NOT PASSED**. E1 full API acceptance, E2 protected release dispatch/signature acceptance, E3 Android, E4 security acceptance, and E6 final forensic audit remain open.


## 2026-10-24 — current candidate exact-SHA continuation

The current source candidate is `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`. Commit inspection confirms its only change relative to parent `9d5d319b88cbee17b18554cfe7641ec1008ba62a` is +49 lines in `crates/one-core/tests/stdlib_builtins.rs`; no production source files changed in that commit.

Current-SHA workflow evidence:
- Cross-platform Ubuntu + Windows Server 2025 [40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116): **PASS**, both jobs, including contract/user-doc checks, build/release build, Clippy, workspace tests, real-network tests, and platform offline verification.
- Ubuntu 24.04 + Debian 12 [40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098): **PASS**, both jobs.
- Focused stdlib/SQLite/provenance regressions [40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099): **PASS**.
- Cargo lockfile bootstrap [40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148): **PASS**.
- Candidate artifact integrity [40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284): **PASS** for both Linux and Windows candidate bundles, including metadata and executable headers.
- Android AArch64 runtime [40088230097](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230097): emulator boot is still active; no ELF execution PASS recorded.

Manual user workflow review remains PASS, but **final E5 verified credit is still not awarded independently** until final ledger/DoD reconciliation. This review does not close E1 full stdlib scope, E2 protected release environment and signed source-bound provenance, E3 Android execution, E4 residual security findings, or E6 final forensic audit.


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
