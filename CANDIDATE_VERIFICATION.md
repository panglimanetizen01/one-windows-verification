# ONE v0.1 — Candidate Verification Index

**Canonical repository:** [panglimanetizen01/one](https://github.com/panglimanetizen01/one)  
**PR:** [#80](https://github.com/panglimanetizen01/one/pull/80) — open, draft, unmerged  
**Current source SHA:** `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`  
**Fixed-weight ledger:** [one-completion-ledger.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md)  
**Release gate:** **NOT PASSED** — ledger records 91/100 implementation, 60/100 verified.

This file is the live exact-SHA evidence index. A workflow run counts only if its job logs assert the current source SHA and all required steps pass. Prior-SHA results are historical evidence, not current-candidate acceptance.

## Current exact-SHA verification

| Gate | Evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [Run 40085406746](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746) | **PASS** on exact source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`; Ubuntu + Windows Server 2025 workspace, real-network, offline, CLI smoke, docs consistency, and bundle generation passed |
| Linux distro conformance | [Run 40085406859](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406859) | **PASS** on exact source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`; Ubuntu 24.04 and Debian 12 passed |
| Focused stdlib / SQLite / provenance | [Run 40085406818](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406818) | **PASS** on exact source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`; UTC/JSON/SQLite/provenance, Clippy, and final-symlink NOFOLLOW regression passed |
| Deterministic Cargo lockfile bootstrap | [Run 40085406783](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406783) | **PASS** on exact source SHA; deterministic Cargo lockfile generated with SHA-256 `284f1186517314c88ac31412c86f09e6418114376e56cd4bb2ae5fd676495c90` |
| Android AArch64 native ELF runtime | [Run 40085406752](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406752) | Queued on current SHA; macOS ARM64, QEMU wrapper strips injected `-enable-hvf`; do not count until ELF executes |

## Current candidate bundles

The following bundles are **historical**, produced on prior source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` by run [40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236). They were downloaded and inspected; embedded checksums pass, but they are not current-candidate acceptance.

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

The canonical repo's current-candidate runs on source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` again failed before executing any steps:

- [One CI 40085390363](https://github.com/panglimanetizen01/one/actions/runs/40085390363)
- [Linux distro 40085390311](https://github.com/panglimanetizen01/one/actions/runs/40085390311)
- [Focused stdlib 40085390350](https://github.com/panglimanetizen01/one/actions/runs/40085390350)

Every job has empty `steps: []`; they provide no source build/test evidence. Independent mirror workflows provide executable exact-SHA evidence, but the canonical runner/infrastructure issue remains an open release limitation.

## Android investigation history

- [Run 40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013): macOS nested HVF failed with `HV_UNSUPPORTED`; Android Emulator injected `-enable-hvf` even with `-accel off`.
- [Run 40084595188](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595188): Ubuntu x86_64 rejected an ARM64 AVD because the emulator requires a system image matching the host architecture.
- Current [run 40085406752](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406752) returns to macOS ARM64 and wraps the emulator's QEMU binary to remove only the injected `-enable-hvf` argument. The run must prove actual boot, API 35 / arm64-v8a, ADB push, and execution output before E3 can be accepted.

## Security review and remaining fixed-ledger gates

The focused [security release review](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/SECURITY_RELEASE_REVIEW.md) records the final-component SQLite symlink hardening and remaining risks. It does not claim complete sandboxing.

- **E1 — Standard library (10 points):** complete required API acceptance is not proven; broader domains such as concurrency, logging/configuration, and complete persistence APIs remain outside the currently implemented stable subset.
- **E2 — Packaging/provenance (8 points):** package-signature/trusted-publisher tests pass, but protected `one-release` environment dispatch and source-bound signed release acceptance have not been exercised.
- **E3 — Cross-platform (8 points):** Linux/Windows/distro matrix passed on prior SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; the current candidate's cross-platform and distro reruns are in progress, and Android runtime remains open.
- **E4 — Security/recovery (6 points):** open parent-component TOCTOU, root/mount confinement, non-Unix/non-Windows fallback guarantees, and runtime-wide quota/threat review.
- **E5 — Docs/tooling (4 points):** implementation 4/4 after manual user-workflow review and documentation corrections; verified credit remains 0/4 until the current exact-SHA doc-consistency and CLI smoke tests pass.
- **E6 — Forensic audit (4 points):** open until E1–E5 are accepted and all release evidence, source SHA, ledger, and provenance are reconciled.

The canonical PR now includes the [Definition of Done](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/DEFINITION_OF_DONE.md). Do not change the fixed weights to manufacture a passing score. Do not claim **PASS GREEN LOCKED — FINAL RELEASE** while any gate above remains open.

**Final-SHA candidate bundles (source `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`):** [Linux artifact 12556803021](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12556803021), ZIP SHA-256 `8b7685c892fd335b1f39231a9224ab46580020d2f0823d8089867c5502b46507`; [Windows artifact 12557131610](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12557131610), ZIP SHA-256 `ecc0c0aadec6a04a8fb0f4b49ed40acc548f1e00fb50bf285ac3d412a8c6f8ba`. Both were downloaded and independently inspected. Embedded checksums pass; Linux payload is ELF x86-64 with binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; Windows payload is PE32+ x86-64 with binary SHA-256 `8c5558996d4e643243cbe0165b7a841d881e5c664617bd7e3217a7de55ebcf53`. Build metadata pins source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. These remain unsigned candidate bundles, not a signed final release.
