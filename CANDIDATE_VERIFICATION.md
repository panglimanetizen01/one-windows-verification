# ONE v0.1 — Candidate Verification Index

**Canonical repository:** [panglimanetizen01/one](https://github.com/panglimanetizen01/one)  
**PR:** [#80](https://github.com/panglimanetizen01/one/pull/80) — open, draft, unmerged  
**Current source SHA:** `dca9a22c242905b97275161d9fdda933b986ec0d`  
**Fixed-weight ledger:** [one-completion-ledger.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md)  
**Release gate:** **NOT PASSED** — fixed-weight ledger is 91/100 provisional implementation and 64/100 verified. The current exact-SHA matrix for `dca9a22c242905b97275161d9fdda933b986ec0d` has passing focused (including package signature/trusted-publisher tests), lockfile, Linux distro, cross-platform Ubuntu/Windows, and artifact-integrity gates. Android API 35 is still booting with no ELF execution result. The fixed-weight gate is NOT PASSED; E1/E2/E3/E4/E6 remain unaccepted as full ledger rows, and protected canonical release evidence remains unavailable.

This file is the live exact-SHA evidence index. A workflow run counts only if its job logs assert the current source SHA and all required steps pass. Prior-SHA results are historical evidence, not current-candidate acceptance.


## Current canonical source revision — `dca9a22c242905b97275161d9fdda933b986ec0d`

This candidate contains documentation-only E2 ledger/checkpoint updates based on the preceding tested code snapshot. Exact-SHA verification has now been rerun against this canonical SHA; all completed matrix jobs below explicitly pin this SHA. Android runtime remains in progress.

| Gate | Run | Current exact-SHA status |
|---|---|---|
| Focused Standard Library/database + package provenance + package/lock regression | [40110118430](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40110118430) | **PASS** — exact-SHA checkout; UTC/database regressions, CLI signature/trust/tamper, full `package_provenance::tests`, deterministic artifact bytes, module-lock generation and stale-lock rejection, and unsupported-dependency fail-closed tests all passed |
| Cargo lockfile bootstrap | [40108646762](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646762) | **PASS** — deterministic lockfile bootstrap on exact canonical SHA |
| Linux distro conformance | [40108646764](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646764) | **PASS** — Ubuntu 24.04 and Debian 12 jobs passed |
| Cross-platform Ubuntu + Windows Server 2025 | [40108646717](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646717) | **PASS** — Ubuntu and Windows Server 2025 jobs completed successfully |
| Candidate artifact integrity | [40108646691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646691) | **PASS** — exact-SHA Linux/Windows bundles discovered; archive digests, embedded manifests, metadata, executable formats validated |
| Android AArch64 ELF execution | [40108646751](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646751) | **IN PROGRESS** — API 35 arm64 emulator boot has not yet produced an ELF execution result |
| Fixed-weight ledger gate | [40109744699](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40109744699) | **NOT PASSED** — latest gate confirmed 9 unchecked DoD items, E1/E2/E3/E4/E6 full-row acceptance missing, Android runtime still in progress, and canonical protected-release evidence inaccessible with current token permissions |

## Previous exact-SHA candidate — `15e6ac358742b89076f21e079e16aa6ca5a2124a`

The canonical source SHA for this historical matrix was pinned in `CANONICAL_COMMIT.txt`. These results remain valid only for this exact source SHA; verifier-repository commits are not source commits.

| Gate | Run | Previous exact-SHA result |
|---|---|---|
| Focused Standard Library/database + source-bound package signature | [40105784848](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784848) | **PASS** — all 26 focused steps succeeded, including E1 boundary regressions, SQLite resource/symlink tests, and CLI package-signature/trusted-publisher/tampering test |
| Cargo lockfile bootstrap | [40105784758](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784758) | **PASS** — deterministic lockfile generation succeeded |
| Linux distro conformance | [40105784831](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784831) | **PASS** — Ubuntu 24.04 and Debian 12 jobs completed successfully, including contract checks, workspace build/tests, Clippy, and real-network tests |
| Cross-platform Ubuntu + Windows Server 2025 | [40105784872](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784872) | **PASS** — Ubuntu and Windows Server 2025 jobs completed successfully; workspace, Clippy, tests, real-network, and offline verification steps passed |
| Candidate artifact integrity | [40105784844](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784844) | **PASS** — exact-SHA Linux/Windows bundles were found; archive digests, embedded manifests, metadata, and executable formats passed |
| Android AArch64 ELF execution | [40105784785](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784785) | In progress at API 30 arm64 emulator boot; no ELF execution result yet |
| Fixed-weight ledger gate | [40105784763](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784763) | **NOT PASSED** — gate evaluated before matrix completion; index was stale, nine DoD items unchecked, E1/E2/E3/E4/E6 unaccepted, and canonical release-workflow evidence could not be queried because the mirror token lacks Actions:read on the private canonical repository |

The focused pass proves only the API/resource-bound tests listed in its executed steps; it does not award the complete E1 row while the broader reusable-standard-library scope remains incomplete. The synthetic-key CLI test verifies signing, trusted-publisher matching, package tampering detection, and source-tree mismatch rejection, but does not prove that the protected `one-release` environment or its secrets are configured. Do not convert these scoped passes into full E1/E2 credit. Rerun the fixed-weight gate after all matrix jobs finish; the gate must remain fail-closed for unaccepted requirements.

## Historical exact-SHA matrix — source `25b9b2385281c01280b46589c3bf9346bfdc2ea4` (2026-10-24 14:22 UTC)

**Canonical source SHA:** `25b9b2385281c01280b46589c3bf9346bfdc2ea4` (branch `milestone/100-ecosystem-20261023`; PR #80 remains open/draft/unmerged). All runs below checked out this exact source SHA; the verifier repository's own head SHA is not the canonical source SHA.

| Gate | Run | Exact-SHA result |
|---|---|---|
| Focused Standard Library/database | [40102204980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204980) | PASS — focused E1 regression target and `cargo --locked clippy -p one-core --all-targets -- -D warnings` succeeded |
| Linux distro conformance | [40102204891](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204891) | PASS — Ubuntu 24.04 and Debian 12; contract checker, workspace build/tests and Clippy passed |
| Cargo lockfile bootstrap | [40102204901](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204901) | PASS — deterministic lockfile bootstrap on the exact source SHA |
| Cross-platform Ubuntu + Windows Server 2025 | [40102204904](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204904) | PASS — both jobs succeeded, workspace tests and offline checks passed |
| Candidate artifact integrity | [40102204878](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204878) | PASS — exact-SHA Linux/Windows bundles downloaded; archive digests, embedded checksums, build metadata and ELF64/PE32+ headers validated |
| Android AArch64 ELF execution | [40103088590](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103088590) | IN PROGRESS — switched verifier workflow from API 35 to smaller API 30 arm64 image after the previous emulator boot stalled. No ELF execution result yet |
| Fixed-weight ledger gate | [40102204973](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204973) | NOT PASSED — evaluated before the current-SHA matrix finished; evidence index was stale, 9 DoD items unchecked, E1/E2/E3/E4/E6 not accepted, and canonical protected-release workflow evidence returned 404/403 due token access |

The focused and cross-platform test matrix verifies the documented source-level built-ins (text, collections, integer arithmetic, mappings, JSON, UTC) on the pinned source SHA. It does **not** by itself award full E1 credit while the ledger's broader reusable-standard-library requirement remains marked incomplete. Android is not accepted until the workflow demonstrates actual AArch64 ELF execution and output. The canonical repository's own hosted CI still has the separately documented runner-infrastructure failure; independent mirror evidence is not relabelled as canonical CI.

### Current exact-SHA results — `a4a146ae22c6629fe606185481055b667321d203`

| Gate | Run | Result |
|---|---|---|
| Focused Standard Library/database | [40103543035](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543035) | PASS — 30 workflow steps completed; focused stdlib/database regressions and core Clippy succeeded |
| Linux distro conformance | [40103543045](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543045) | PASS — Ubuntu 24.04 and Debian 12; workspace tests, Clippy and contract checks passed |
| Cargo lockfile bootstrap | [40103542984](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542984) | PASS |
| Cross-platform Ubuntu + Windows Server 2025 | [40103543039](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543039) | PASS — both jobs succeeded; Ubuntu 22 steps, Windows 21 steps |
| Candidate artifact integrity | [40103542987](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542987) | PASS — exact source SHA, ZIP digests, embedded manifests, metadata, ELF64 and PE32+ formats validated |
| Android AArch64 ELF execution | [40103542978](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542978) | IN PROGRESS at API 30 arm64 emulator boot; no ELF execution result yet |
| Fixed-weight ledger gate | [40103542993](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542993) | FAILED before the matrix completed; stale evidence and pending jobs caused a fail-closed result. Rerun after Android completes; other E1/E2/E4/E6, DoD and canonical release-token gaps still prevent global release acceptance |



## Final candidate after ledger/DoD reconciliation

Current canonical source SHA: `54f3de667e05075805fcc5cd5dc621b653075667`. The completion ledger and Definition of Done E5 references were reconciled to the passing matrix on the prior candidate. That documentation-only reconciliation creates source SHA `54f3de667e05075805fcc5cd5dc621b653075667`; a fresh exact-SHA matrix is mandatory, and the prior candidate's results below remain historical until the rerun completes:

| Gate | Exact-SHA evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40095539284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539284) | PASS — both jobs succeeded; Windows test log includes all 23 `stdlib_builtins.rs` tests passing, including the new edge-contract tests |
| Linux distro conformance | [40095539287](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539287) | PASS — Ubuntu 24.04 and Debian 12 succeeded |
| Focused stdlib/database | [40095539311](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539311) | PASS |
| Cargo lockfile bootstrap | [40095539351](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539351) | PASS |
| Linux/Windows artifact integrity | [40095539261](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539261) | PASS — both bundle digests matched GitHub metadata; embedded source SHA, toolchain metadata, checksum manifests, and ELF64/PE32+ headers validated |
| Android AArch64 ELF runtime | [40095539358](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539358) | IN PROGRESS at emulator boot; ELF execution/output not yet observed |
| Fixed-weight ledger gate | [40095563933](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095563933) | NOT PASSED — evaluated before all matrix jobs completed; E1/E2/E3/E4/E6 remain unaccepted and canonical release evidence token permission is still missing |

The previous candidate `6d1577e078dfcf23295afdaf41568b85d3ba07bb` passed the same cross-platform, distro, focused, lockfile, and artifact checks; it is historical. Current ledger remains 91/100 implementation and 64/100 verified. E5's row now points to the last passing matrix on `533744e33e8e95ab83e239c2751846701b2604ea`; rerun this candidate before treating that evidence as current. Do not award E1 full credit: its implementation score remains 7/10 because the broader reusable standard-library scope is incomplete. The canonical hosted CI retries for this final SHA failed before executing any steps; this is an infrastructure failure, not source-test evidence. Protected release evidence remains inaccessible because `CANONICAL_READ_TOKEN` needs Actions:read on the private canonical repository.

## Latest candidate rerun — E1 boundary contracts

Current canonical source SHA `6d1577e078dfcf23295afdaf41568b85d3ba07bb` adds three regression tests for invalid text conversion/replacement/splitting inputs, strict UTC parser forms and full year-range boundaries, checked numeric overflow, and invalid collection inputs. Initial test attempts caught two fixture issues before acceptance: One source has no leading negative numeric literal, and Rust fixture newlines must be single escaped `\\n` sequences. Both were corrected using supported subtraction syntax and valid Rust string escapes. Fresh exact-SHA verification was triggered by pinning this source; no result is accepted until each job completes:

| Gate | Result |
|---|---|
| Cross-platform Ubuntu + Windows | Awaiting fresh run for `6d1577e078dfcf23295afdaf41568b85d3ba07bb` |
| Linux distro | Awaiting fresh run |
| Focused stdlib/database | Awaiting fresh run; includes the new E1 tests through the workspace test suite only if configured to run that integration target |
| Cargo lockfile | Awaiting fresh run |
| Candidate artifact integrity | Awaiting fresh run |
| Android AArch64 ELF runtime | Awaiting fresh run; execution remains unproven |
| Fixed-weight ledger gate | NOT PASSED until current-SHA evidence is complete; E1/E2/E3/E4/E6 acceptance is not yet recorded |

The previous `82e249879131323d015a1c93aea4fd986db1b271` candidate's cross-platform, Linux distro, focused, and lockfile runs passed, but those results are historical after the E1 test commit and do not certify this source SHA.

## Current exact-SHA verification

| Gate | Evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [Run 40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; both Ubuntu and Windows Server 2025 jobs completed successfully, including workspace tests, real-network tests, offline verification, CLI smoke tests, documentation consistency checks, and candidate bundle generation. |
| Linux distro conformance | [Run 40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; Ubuntu 24.04 and Debian 12 jobs completed successfully. |
| Focused stdlib / SQLite / provenance | [Run 40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; UTC/calendar, JSON byte budget, source-level text/integer integrations, SQLite bounds and final-symlink NOFOLLOW, trusted-publisher signature/tampering tests, and Clippy completed successfully. This is still a subset, not full E1 acceptance. |
| Deterministic Cargo lockfile bootstrap | [Run 40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148) | **PASS**; generated the lockfile from canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`. Lockfile SHA-256 is present in workflow output; do not infer that it is a release signature. |
| Android AArch64 native ELF runtime | [Run 40090809569](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40090809569) | **IN PROGRESS — NOT ACCEPTED**. Exact source checkout passed; emulator workflow now uses a smaller API 30 arm64 image to address the previous 30-minute API 35 TCG boot timeout. ELF execution/output has not yet been observed. |
| Current canonical hosted CI | [One CI 40088066589](https://github.com/panglimanetizen01/one/actions/runs/40088066589); [Linux distro 40088066594](https://github.com/panglimanetizen01/one/actions/runs/40088066594); [focused stdlib 40088066614](https://github.com/panglimanetizen01/one/actions/runs/40088066614) | **INFRASTRUCTURE FAILURE** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`: retries again failed with no executable steps or logs. Canonical CI for the new `e8156e7d6c0a0f999f24ad00bf670e46f21dc128` candidate has not yet produced an executable run. They are not source-test results. Independent mirror runs do not convert canonical CI to PASS. |

## Current candidate bundles

The following bundles are **historical**, produced on prior source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` by run [40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236). They were downloaded and inspected; embedded checksums pass, but they are not current-candidate acceptance. Fresh bundles for source SHA `e8156e7d6c0a0f999f24ad00bf670e46f21dc128` were uploaded by run 40091247192 and independently downloaded/extracted by [artifact integrity workflow 40091607139](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40091607139). Both ZIP hashes matched GitHub artifact metadata; embedded `SHA256SUMS`, build metadata, source SHA, toolchain versions, CLI version, and binary formats passed. Exact binary hashes and metadata are recorded in the dedicated section below.

- **Linux:** [artifact 12556841440](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236/artifacts/12556841440)  
  ZIP SHA-256: `e7266614dc9a5feb5e3673a63c409542b16d86c6d36fbea6a17be498b6fa3797`  
  Binary: ELF 64-bit LSB PIE, x86-64. Embedded binary SHA-256: `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`.
- **Windows:** [artifact 12556821645](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236/artifacts/12556821645)  
  ZIP SHA-256: `7bd88e7197ae6d7a12fd946e6c2cb226c2be9c216379342fa229425ad4c60c95`  
  Binary: PE32+ console executable, x86-64. Embedded binary SHA-256: `0d4245cc51336f393a902370b1cb5095dd9169ea87132820cefa3a366024468f`.

Both `BUILD-METADATA.txt` files pin source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, target triple, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. The current candidate `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` requires fresh bundles. All bundles are unsigned candidates, not a signed final release.

## Standard-library evidence

On the prior candidate SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, both cross-platform logs asserted the exact commit and reported the stdlib integration suite passing (18 tests) and `one-core` library tests passing (228 tests). Focused tests also passed UTC/JSON/SQLite/provenance regressions and the SQLite final-symlink test. These are historical for the new candidate `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`; its exact-SHA reruns are pending. This verifies only the implemented API subset, not every broader E1 requirement.

## Canonical CI infrastructure

The canonical repo's current-candidate runs on source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a` again failed before executing any steps:

- [One CI 40086935480](https://github.com/panglimanetizen01/one/actions/runs/40086935480)
- [Linux distro 40086935432](https://github.com/panglimanetizen01/one/actions/runs/40086935432)
- [Focused stdlib 40086935441](https://github.com/panglimanetizen01/one/actions/runs/40086935441)

Every job has empty `steps: []`; they provide no source build/test evidence. Independent mirror workflows provide executable exact-SHA evidence, but the canonical runner/infrastructure issue remains an open release limitation.

## Android investigation history

- [Run 40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013): macOS nested HVF failed with `HV_UNSUPPORTED`; Android Emulator injected `-enable-hvf` even with `-accel off`.
- [Run 40084595188](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595188): Ubuntu x86_64 rejected an ARM64 AVD because the emulator requires a system image matching the host architecture.
- Current [run 40086990457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990457) returns to macOS ARM64 and wraps the emulator's QEMU binary to remove only the injected `-enable-hvf` argument. As last checked, the emulator boot step remained in progress; API 35 / arm64-v8a, ADB push, ELF header, and execution output remain unproven.

## Security review and remaining fixed-ledger gates

The focused [security release review](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/SECURITY_RELEASE_REVIEW.md) records the final-component SQLite symlink hardening and remaining risks. It does not claim complete sandboxing.

- **E1 — Standard library (10 points):** complete required API acceptance is not proven; broader domains such as concurrency, logging/configuration, and complete persistence APIs remain outside the currently implemented stable subset.
- **E2 — Packaging/provenance (8 points):** package-signature/trusted-publisher tests pass, but protected `one-release` environment dispatch and source-bound signed release acceptance have not been exercised.
- **E3 — Cross-platform (8 points):** Linux/Windows/distro matrix passed on prior SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; the current candidate's cross-platform and distro reruns are in progress, and Android runtime remains open.
- **E4 — Security/recovery (6 points):** open parent-component TOCTOU, root/mount confinement, non-Unix/non-Windows fallback guarantees, and runtime-wide quota/threat review.
- **E5 — Docs/tooling (4 points):** implementation 4/4 after manual user-workflow review; exact-SHA cross-platform CLI smoke and documentation consistency tests now pass in run 40086990528. Verified credit remains unawarded pending full release-gate reconciliation.
- **E6 — Forensic audit (4 points):** open until E1–E5 are accepted and all release evidence, source SHA, ledger, and provenance are reconciled.

The canonical PR now includes the [Definition of Done](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/DEFINITION_OF_DONE.md). Do not change the fixed weights to manufacture a passing score. Do not claim **PASS GREEN LOCKED — FINAL RELEASE** while any gate above remains open.

**Final-SHA candidate bundles (source `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`):** [Linux artifact 12556803021](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12556803021), ZIP SHA-256 `8b7685c892fd335b1f39231a9224ab46580020d2f0823d8089867c5502b46507`; [Windows artifact 12557131610](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12557131610), ZIP SHA-256 `ecc0c0aadec6a04a8fb0f4b49ed40acc548f1e00fb50bf285ac3d412a8c6f8ba`. Both were downloaded and independently inspected. Embedded checksums pass; Linux payload is ELF x86-64 with binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; Windows payload is PE32+ x86-64 with binary SHA-256 `8c5558996d4e643243cbe0165b7a841d881e5c664617bd7e3217a7de55ebcf53`. Build metadata pins source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. These remain unsigned candidate bundles, not a signed final release.


## New exact-SHA candidate — 2026-10-24 ledger/checkpoint reconciliation

- **Pinned source SHA:** `9d5d319b88cbee17b18554cfe7641ec1008ba62a`.
- This candidate contains documentation-only corrections reconciling the fixed-weight ledger total with its row values and adding the checkpoint evidence summary. The prior four passing mirror runs listed above are tied to `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` and are **historical for this new SHA**.
- Required current-SHA runs: cross-platform Ubuntu/Windows, Linux distro, focused standard-library/SQLite/provenance, Cargo lockfile bootstrap, artifact integrity, and Android AArch64 ELF build-and-execute. The first five now pass against source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`; Android remains in progress and unaccepted.
- Android run `40085406752` was still booting the emulator on the prior SHA at the last check; it does not prove ELF execution on this candidate.
- Fixed weights unchanged. Implementation: **91/100 provisional**; verified: **60/100**; gate **NOT PASSED**. E1–E6 acceptance remains open, including full stdlib scope, protected release dispatch/signature, Android execution, security disposition, and final forensic audit.


## Exact-SHA bundle metadata — source `9d5d319b88cbee17b18554cfe7641ec1008ba62a`

Run [40086990528](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528) uploaded:
- Linux candidate artifact [12557347980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557347980), ZIP digest from GitHub artifact metadata: `sha256:33cc3445cbccc3780bb776a6d9b2ec846d1687e8d45a8526adf27aa120cf237f`, size 1,738,836 bytes.
- Windows candidate artifact [12557247338](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557247338), ZIP digest from GitHub artifact metadata: `sha256:564f7105d3f12face750d68431699d3f2491c28ff526c75e7951d766f21d8c0a`, size 1,488,731 bytes.

Both names embed the canonical source SHA. Independent download, extraction, ZIP digest comparison, embedded checksum validation, metadata review, and executable-header inspection have now been completed by [artifact integrity run 40087385932](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40087385932). See the PASS section below. These remain unsigned candidate bundles, not final release artifacts.


## Candidate artifact integrity — PASS for source `9d5d319b88cbee17b18554cfe7641ec1008ba62a`

Independent workflow [40087385932](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40087385932) passed. It downloaded both artifact archives by ID, compared ZIP SHA-256 against GitHub artifact metadata, extracted them, verified each embedded `SHA256SUMS`, checked metadata fields, and inspected executable headers.

- Linux artifact [12557347980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557347980): ZIP SHA-256 `33cc3445cbccc3780bb776a6d9b2ec846d1687e8d45a8526adf27aa120cf237f`; embedded binary `one` SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; ELF64 little-endian `EM_X86_64`; target `x86_64-unknown-linux-gnu`.
- Windows artifact [12557247338](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557247338): ZIP SHA-256 `564f7105d3f12face750d68431699d3f2491c28ff526c75e7951d766f21d8c0a`; embedded binary `one.exe` SHA-256 `f5749302ef052c6f192939a9d0c96b54edc2c12cba606551383c3e194d7890a9`; PE32+ x86-64; target `x86_64-pc-windows-msvc`.
- Both metadata files assert source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`, Rust/Cargo 1.99.0, and CLI `one 0.1.0`.
- These are checksum-verified **unsigned candidate bundles**, not signed final release artifacts. This does not close E2.


## Supplemental Linux bundle execution — manual, not hosted CI

The Linux candidate ZIP from artifact `12557347980` was downloaded and its embedded `SHA256SUMS` checked in the current ChatGPT execution container. The binary's `BUILD-METADATA.txt` pins source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`. Manual smoke commands executed successfully: `one version` reported `one 0.1.0`; `one help` displayed the documented CLI commands; `one buat` created a temporary project; `one periksa`, `one jalankan`, `one bangun`, `one test` (1 fixture), and `one package` all succeeded on the generated example. The temporary project was removed after the test. This is supplemental direct artifact execution, **not GitHub-hosted CI**, and does not replace the required Windows/Android or release-provenance gates.


## 2026-10-24 — exact-SHA matrix refresh for PR #80 HEAD

The canonical source pin was refreshed from the stale prior target to the current PR head **`2ead9dba45db4ce4105deaa81720aacc8fcadd6c`**. The pin update commit is `5560edbb625e740f3c2c1a67bfedafda225ea104`; that is the verification-mirror commit, not the ONE source SHA.

Fresh workflows were triggered against the pinned source:
- Cross-platform Ubuntu + Windows Server 2025: [40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) — **both jobs PASS**, including full workspace, Clippy, real-network, offline checks and release candidate bundle generation.
- Ubuntu 24.04 + Debian 12: [40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098) — **both jobs PASS**.
- Focused standard-library / SQLite / package-signature regressions: [40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099) — **PASS**.
- Cargo lockfile bootstrap: [40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148) — **PASS**.
- Android AArch64 ELF build-and-execute: [40088230097](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230097) — still running at Android emulator boot; **not yet runtime evidence**.

All previous workflow results tied to source SHAs other than `2ead9dba45db4ce4105deaa81720aacc8fcadd6c` are historical and do not satisfy final-SHA acceptance. The artifact-inspection workflow still has hard-coded artifact IDs and source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`; it must be refreshed after the new cross-platform run publishes candidate artifacts. Until then, no artifact-integrity claim is made for the new candidate.

Fixed-weight score remains implementation **91/100 provisional** by row arithmetic, verified **60/100**, release gate **NOT PASSED**. Open acceptance includes the full E1 API scope, protected release-environment signing/trust-store exercise (E2), actual Android AArch64 ELF execution (E3), complete security/threat review and runtime-wide bounds (E4), final exact-SHA doc/tooling acceptance (E5), and the final forensic reconciliation (E6).

### Candidate Linux bundle published for source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Cross-platform run [40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) has uploaded Linux candidate artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853), ZIP digest from GitHub artifact metadata `sha256:1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`, size 1,738,835 bytes. Its artifact name embeds the exact source SHA. The Windows candidate bundle has now appeared; paired artifact-integrity workflow [40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284) is queued to validate both bundles.

- Windows candidate artifact [12558350265](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12558350265): ZIP digest from GitHub artifact metadata `sha256:0686d79036c5ce4f4f95bf861c3e82ce8bd9813dbf5dcbe748053ed9c749ee9e`, size 1,488,730 bytes.
- Linux candidate artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853): ZIP digest `sha256:1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`, size 1,738,835 bytes.


### Candidate artifact integrity PASS — source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Independent inspection [40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284) passed against both exact-SHA bundles. The job downloaded artifacts by ID, compared archive digests with GitHub artifact metadata, checked embedded `SHA256SUMS`, source/build metadata, Rust/Cargo/CLI versions, and executable headers.
- Linux artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853): ZIP SHA-256 `1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`; binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; ELF64 little-endian EM_X86_64; target `x86_64-unknown-linux-gnu`.
- Windows artifact [12558350265](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12558350265): ZIP SHA-256 `0686d79036c5ce4f4f95bf861c3e82ce8bd9813dbf5dcbe748053ed9c749ee9e`; binary SHA-256 `0abae22d28b34ffe266090679786132323dd7508f0f38b8a79c8229aa6cff279`; PE32+ x86-64; target `x86_64-pc-windows-msvc`.
- Both metadata files pin source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`, Rust/Cargo 1.99.0 and CLI `one 0.1.0`.
- This is artifact-integrity evidence, not signed package provenance or final release authorization; E2 remains open.


### Canonical repository CI retry classification — source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Canonical runs [40088066589](https://github.com/panglimanetizen01/one/actions/runs/40088066589) (main CI), [40088066594](https://github.com/panglimanetizen01/one/actions/runs/40088066594) (Linux distro), and [40088066614](https://github.com/panglimanetizen01/one/actions/runs/40088066614) (focused stdlib) failed. I invoked the supported rerun-failed-jobs action for all three. The retry attempts again returned completed-failure jobs with `steps: null` and `logs_url: null`; no executable test step or source failure diagnostic is available. These are **unusable runner/infrastructure attempts**, not evidence of a source test failure and certainly not PASS. The independent exact-SHA mirror remains the executable evidence path; canonical hosted CI infrastructure remains an open item.


### Supplemental current-SHA Linux bundle execution — manual, not hosted CI

Downloaded Linux artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853) into the current execution container. Its archive SHA-256 matched GitHub metadata: `1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`. The embedded `SHA256SUMS` passed; metadata pins source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; CLI reports `one 0.1.0`. Manual smoke succeeded for `one version`, `one help`, `one buat`, `one periksa`, `one jalankan`, `one bangun`, `one test` (1 fixture), and `one package`. The temporary project was removed after the run. This is supplemental direct Linux artifact execution, **not GitHub-hosted CI**, and does not close Windows runtime, Android, signed-provenance, full E1, E4 or E6 gates.


## Current candidate — ledger/DoD reconciliation source SHA `f9a320e67145f7806f55123dbe72e578679d3f2e`

The current source candidate is `f9a320e67145f7806f55123dbe72e578679d3f2e`. The fixed-weight ledger TOTAL row has been corrected to `91/100 implementation, 64/100 verified`; E5 is the only newly credited verified row. This is not a final release gate pass.

Exact-SHA matrix triggered by verification pin commit [`07f2f4dcd3689b2903f6e5f17fd487ea1de61a58`](https://github.com/panglimanetizen01/one-windows-verification/commit/07f2f4dcd3689b2903f6e5f17fd487ea1de61a58), pinning the canonical source above:

| Required workflow | Run | State |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40092009937](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009937) | PASS; Ubuntu and Windows Server 2025 jobs both completed successfully, including build, tests, Clippy, CLI/docs checks, and candidate bundle generation |
| Linux distro conformance | [40092009933](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009933) | PASS; Ubuntu 24.04 and Debian 12 completed successfully |
| Focused standard library / SQLite / provenance | [40092009976](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009976) | PASS; subset only, not full E1 acceptance |
| Cargo lockfile bootstrap | [40092009942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009942) | PASS |
| Android AArch64 native ELF runtime | [40092009961](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009961) | In progress at API 30 emulator boot; no ELF execution evidence yet |
| Candidate artifact integrity | [40092478797](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092478797) | PASS; workflow dynamically selected exact-SHA bundles, matched ZIP SHA-256 against GitHub artifact metadata, and verified embedded checksums, source/build metadata, ELF64 x86-64 and PE32+ x86-64 |
| Fixed-weight ledger gate | [40092009911](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009911) | NOT PASSED: matrix was still running when evaluated; canonical release evidence API returned HTTP 403; E1–E4 and E6 are not fully verified |

The prior bundle integrity and manual Linux bundle execution evidence refer to older source SHAs and are historical only. They do not satisfy current-source artifact integrity or Android execution. The canonical repository's hosted CI has repeatedly failed before executable steps (`runner_id: 0`, `steps: []`); independent verification does not relabel those canonical CI runs as PASS.

The release gate remains **NOT PASSED**. E1 requires the full public API contract suite; E2 requires independently configured trusted publisher and protected release-path evidence; E3 requires actual Android AArch64 ELF execution; E4 requires the complete security/root-confinement and resource-bound review; E6 requires a final forensic reconciliation after E1–E5 acceptance. Do not merge PR #80 or publish a release under this state.


## Exact-SHA candidate evidence — source `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`

The current canonical candidate source is `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`. This is the source SHA selected by `CANONICAL_COMMIT.txt` and the open PR #80 head. The fixed-weight ledger is `91/100 implementation, 64/100 verified`; weights were not changed. E5 is the only ecosystem row currently credited as verified.

| Required workflow | Exact-SHA run | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40092715740](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715740) | PASS — both jobs completed successfully |
| Linux distro conformance, Ubuntu 24.04 + Debian 12 | [40092715691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715691) | PASS — both jobs completed successfully |
| Focused UTC/database resource-bound regressions | [40092715735](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715735) | PASS — focused subset only; not full E1 acceptance |
| Cargo lockfile bootstrap | [40092715680](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715680) | PASS |
| Linux/Windows candidate artifact integrity | [40092715698](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715698) | PASS — bundle digests match GitHub artifact metadata; embedded source SHA/toolchain/CLI metadata and ELF64 EM_X86_64 / PE32+ x86-64 headers validated |
| Android AArch64 runtime | [40092942784](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092942784) | IN PROGRESS — API 35 arm64 emulator boot; no ELF execution evidence yet |
| Fixed-weight ledger gate | [40092715712](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715712) | NOT PASSED at time of evaluation: current-SHA cross-platform/artifact runs were still in progress; protected canonical release evidence remains inaccessible because `CANONICAL_READ_TOKEN` lacks Actions:read on the private source repository; nine Definition of Done items remain unchecked |

Artifact metadata observed in the successful integrity run:
- Linux candidate ZIP artifact ID `12559338923`, SHA-256 `f2d00fa3ce1bf6489a29006b29df5e31a84a53c1c920ce9d481418374be38979`.
- Windows candidate ZIP artifact ID `12559339113`, SHA-256 `d19fbda9d8df0a2aca82f433e28d745d34c5ba131eef3117595b83a062b0bf0e`.
- Embedded Linux binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`.
- Embedded Windows binary SHA-256 `30efd82327c058f49c45fb30a0be9d298efac6e3c259928097061af52b5804b6`.

The canonical repository hosted workflow remains an independent gate: its recent failure had no executable job steps/logs, so independent mirror passes do not convert canonical CI to PASS. Protected release dispatch, trusted-publisher configuration, full E1, Android ELF execution, complete E4 security acceptance, and E6 forensic closeout remain open. Do not merge PR #80 or claim GREEN LOCKED until those are accepted on the final frozen source SHA.


## Canonical hosted-CI retry result for source SHA `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`

I retried the canonical failed workflow jobs instead of treating the first failure as final: [One CI run 40092705031, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705031), [Linux distribution run 40092705049, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705049), and [focused stdlib run 40092705091, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705091). All three retries still ended in failure with **zero executable steps** in every job. This is recorded as a hosted-runner/infrastructure failure, not a source test failure and not a PASS. Independent exact-SHA mirror results remain separate evidence and do not replace canonical hosted CI.


## Ledger-gate permission diagnosis

The verifier now retries a public unauthenticated read after HTTP 403, but the canonical repository is private, so that fallback correctly returns 404. To finish the live protected-release evidence check, the repository administrator must update the verification repository secret `CANONICAL_READ_TOKEN` to a token with read access to Actions on `panglimanetizen01/one`. The gate remains fail-closed until that permission exists and an exact-SHA protected release workflow succeeds.


## E2 acceptance boundary — latest checkpoint

- Prior code SHA `a75362fcb9dd7514c1253f661443252122053aa9`: focused package-signature/trusted-publisher tests and lockfile bootstrap passed in [40107005038](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40107005038) and [40106909806](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40106909806). These are historical for the new documentation commit `dca9a22c242905b97275161d9fdda933b986ec0d`.
- Current candidate `dca9a22c242905b97275161d9fdda933b986ec0d` changes only ledger/checkpoint documentation. The exact-SHA matrix is pending and will be rerun.
- E2 stays **0/8 verified / NOT ACCEPTED** until a real protected `one-release` run proves environment protection, securely configured signing seed, independently provisioned trusted publisher store, successful V2 source-bound signature verification, and retained artifacts. Synthetic fixture keys do not satisfy this criterion.


## Prompt 2/4 — E2 evidence checkpoint (2026-10-24)

- Canonical source SHA pinned for this matrix: `dca9a22c242905b97275161d9fdda933b986ec0d`. Completed exact-SHA runs: focused package signature/trusted-publisher tests [40108646700](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646700) PASS; lockfile bootstrap [40108646762](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646762) PASS; Ubuntu 24.04 + Debian 12 [40108646764](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646764) PASS; Ubuntu + Windows Server 2025 [40108646717](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646717) PASS; artifact integrity [40108646691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646691) PASS.
- Android AArch64 run [40108646751](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646751) is still in progress at emulator boot; no native ELF execution result yet.
- The fixed-weight gate [40108651511](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108651511) is **NOT PASSED**. It reports 9 unchecked DoD items, full-row acceptance absent for E1/E2/E3/E4/E6, Android pending at evaluation time, and inability to query canonical release evidence due to the missing Actions:read permission for the canonical repository.
- E2 remains **0/8 verified / NOT ACCEPTED**. Focused tests verify cryptographic signing and rejection of tampering/untrusted keys with synthetic fixture keys, not a real independently authenticated publisher key. The protected `one-release` workflow has not run; environment protection and secret/trust-store configuration are unverified. No release was published.
