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

## ONE CircleCI terminal result and refreshed docs SHA — 2026-11-19 16:40Z

ONE PR #113 parent documentation SHA eeafcab579cebb762af34d1daf4830f95cba87e7 has CircleCI ci/circleci: one-linux SUCCESS (workflow 0621c480-6054-4fc1-8c82-b9028f105735, job 49178c86-d311-49ac-835a-6fa49985a980, status updated 2026-11-19T16:38:52Z). This result is exact-SHA only. CircleCI provider step logs were not separately retrieved; no step-level test count is claimed. The next ONE PR #113 docs commit is 54b92ab9703b9c3450cb33f5eb4f34861aae107b and requires a fresh CircleCI status; at the first read its status had not yet been reported.

ONE draft PR #103 ledger/DoD source is now exact SHA 36bba2e45a629c4fa39677b0ea07a2489d37bc99. It records E3 8/8 VERIFIED on canonical source 722d662 and DoD 4 checked / 9 unchecked. This verifier draft branch now pins LEDGER_SOURCE_COMMIT.txt to 36bba2e45a629c4fa39677b0ea07a2489d37bc99; CANONICAL_COMMIT.txt remains 722d662e7a81711ba3607d26571f4048a292b3ed. These pin/document changes are staged in draft PR #50 only; not merged to protected verification.

Protected verifier branch verification remains b14abf0020472dc45842be30854e0a09317d6cb4 and all 12 required mirror workflow groups have terminal SUCCESS for canonical source 722d662. The historical fixed-weight gate #44519577312 remains FAILURE. E1, E2, E4, E5, E6 are not fully verified; Issue #104 remains OPEN / NOT ACCEPTED; protected source-bound package provenance release is absent. No fixed weights, DoD beyond the evidence-backed E3 item, canonical pin, or protected release state were changed.


## Ledger source reconciliation — 2026-11-19 16:42Z

The proposed ledger source pointer in this PR now targets ONE PR #103 draft commit `36bba2e45a629c4fa39677b0ea07a2489d37bc99`. That exact draft ledger records E3 VERIFIED 8/8 from the exact-source Linux/Windows/distro/artifact/Android runtime evidence. The proposed draft ledger totals are 92/100 IMPLEMENTED and 8/100 VERIFIED; Definition of Done is 4 checked / 9 unchecked / 13 total. E1 remains 7/10 implementation and 0/10 verified; E2 7/8 and 0/8; E4 6/6 and 0/6; E5 4/4 and 0/4; E6 0/4 and NOT IMPLEMENTED.

Important separation: protected `LEDGER_SOURCE_COMMIT.txt` still points to `d6c382a245c49a028bc60809f22ca956c7f894cc`. This PR's new pointer is a proposed draft change only. The historical protected gate #44519577312 therefore still reports the old 0/100 verified / 10 unchecked state. No protected ledger pin, weights, or DoD boxes were changed by this PR.

## Exact-source matrix and acceptance boundary refresh — 2026-11-19 16:42Z

- Protected verifier HEAD: `b14abf0020472dc45842be30854e0a09317d6cb4`; canonical ONE source: `722d662e7a81711ba3607d26571f4048a292b3ed`.
- All 12 required verifier workflow names plus the Android runtime alternative have terminal SUCCESS runs recorded in the exact-source matrix above.
- E3 is VERIFIED 8/8 only in the draft ONE ledger source PR #103. This does not imply E1/E2/E4/E5/E6 or final project acceptance.
- Protected fixed-weight gate #44519577312 remains historical FAILURE. No new gate run was triggered. If this PR is authorized and merged, its `CANDIDATE_VERIFICATION.md` and `LEDGER_SOURCE_COMMIT.txt` changes will trigger a new ledger-gate evaluation; expected result remains NOT PASSED until remaining row-level/DoD and protected package-provenance requirements are satisfied.
- Issue #104 remains OPEN / NOT ACCEPTED; Linux nested writes and unsupported filesystem adapters remain fail-closed. Issue #105 escaped-descendant containment remains unresolved.
- Issue #82 has protected Android runtime SUCCESS (#44519577666) on API 35 arm64-v8a / exit 0. PR #49's build job passes but metadata runtime job #135708475823 is still IN_PROGRESS; keep Issue #82 open pending the retained metadata artifact.
- ONE PR #113 HEAD `54b92ab9703b9c3450cb33f5eb4f34861aae107b` is OPEN / DRAFT / UNMERGED; CircleCI `ci/circleci: one-linux` is PENDING on that exact SHA (workflow `f9bd8ac7-a741-4bf6-8536-37af4798f3a1`, job `77951c98-1242-4c47-b45b-90011ecebfd6`). Parent `eeafcab...` SUCCESS does not transfer.

This is a documentation/evidence-pointer update only. It does not merge this PR, change the protected ledger source, modify fixed weights, check DoD items, or publish a package.


## Android API 35 runtime metadata evidence — 2026-11-20

- Verifier PR #49 exact HEAD `fa0b5cffe52bf31fedef81ed945d6cc3a6dc2e19` completed Android runtime workflow [#44565956781](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44565956781) with terminal SUCCESS. Build job `135707610069` and API 35 ARM64 runtime job `135708475823` both completed SUCCESS.
- Downloaded and inspected retained artifact ID `14553867982`, name `one-api35-arm64-runtime-evidence-722d662e7a81711ba3607d26571f4048a292b3ed`. `ANDROID_RUNTIME_METADATA.txt` records exact source SHA `722d662e7a81711ba3607d26571f4048a292b3ed`, API 35, ABI `arm64-v8a`, model `Android SDK built for arm64`, host architecture `aarch64`, ELF digest, local/remote paths, exact ADB invocation, exit code 0, and output `ONE_NATIVE_BACKEND_OK`.
- The artifact ELF is ELF64 AArch64 with interpreter `/system/bin/linker64`. Recomputed ELF SHA-256 `5b05504a0167beeae1d15e267c2e7af1f1a7c62b163d459289be1d663c380a0c` matches the metadata. Archive SHA-256 is `69eaac89b1a6946ab0ced4f51029dc87d7ccc20a33f425d469b9617df2344c08`.
- ONE Issue #82 was updated with the inspected artifact evidence and closed as COMPLETED. This closes only the Android AArch64 runtime-evidence task for source pin `722d662...`; it does not change the fixed-weight ledger, protected pins, or overall E3/release acceptance.
- PR #49 remains OPEN / DRAFT / UNMERGED; no protected verifier branch or pin changed. PR #50's proposed `LEDGER_SOURCE_COMMIT.txt` remains `5f616ae08e303081666a5e0d6a4b8b63b9d69c16`; this documentation update does not promote it to the protected branch.
