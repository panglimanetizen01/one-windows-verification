# ONE v0.1 — Candidate Verification Index

**Canonical repository:** [panglimanetizen01/one](https://github.com/panglimanetizen01/one)  
**PR:** [#80](https://github.com/panglimanetizen01/one/pull/80) — open, draft, unmerged  
**Current source SHA:** `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`  
**Fixed-weight ledger:** [one-completion-ledger.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md)  
**Release gate:** **NOT PASSED** — fixed-weight ledger arithmetic reconciled to 91/100 provisional implementation, 60/100 verified.

This file is the live exact-SHA evidence index. A workflow run counts only if its job logs assert the current source SHA and all required steps pass. Prior-SHA results are historical evidence, not current-candidate acceptance.

## Current exact-SHA verification

| Gate | Evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [Run 40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; both Ubuntu and Windows Server 2025 jobs completed successfully, including workspace tests, real-network tests, offline verification, CLI smoke tests, documentation consistency checks, and candidate bundle generation. |
| Linux distro conformance | [Run 40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; Ubuntu 24.04 and Debian 12 jobs completed successfully. |
| Focused stdlib / SQLite / provenance | [Run 40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; UTC/calendar, JSON byte budget, source-level text/integer integrations, SQLite bounds and final-symlink NOFOLLOW, trusted-publisher signature/tampering tests, and Clippy completed successfully. This is still a subset, not full E1 acceptance. |
| Deterministic Cargo lockfile bootstrap | [Run 40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148) | **PASS**; generated the lockfile from canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`. Lockfile SHA-256 is present in workflow output; do not infer that it is a release signature. |
| Android AArch64 native ELF runtime | [Run 40090809569](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40090809569) | **IN PROGRESS — NOT ACCEPTED**. Exact source checkout passed; emulator workflow now uses a smaller API 30 arm64 image to address the previous 30-minute API 35 TCG boot timeout. ELF execution/output has not yet been observed. |
| Current canonical hosted CI | [One CI 40088066589](https://github.com/panglimanetizen01/one/actions/runs/40088066589); [Linux distro 40088066594](https://github.com/panglimanetizen01/one/actions/runs/40088066594); [focused stdlib 40088066614](https://github.com/panglimanetizen01/one/actions/runs/40088066614) | **INFRASTRUCTURE FAILURE** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`: retries again failed with no executable steps or logs. They are not source-test results. Independent mirror runs do not convert canonical CI to PASS. |

## Current candidate bundles

The following bundles are **historical**, produced on prior source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` by run [40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236). They were downloaded and inspected; embedded checksums pass, but they are not current-candidate acceptance. Fresh bundles for source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c` were uploaded by run 40088230116 and independently downloaded/extracted by [artifact integrity workflow 40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284). Both ZIP hashes matched GitHub artifact metadata; embedded `SHA256SUMS`, build metadata, source SHA, toolchain versions, CLI version, and binary formats passed. Exact binary hashes and metadata are recorded in the dedicated section below.

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
