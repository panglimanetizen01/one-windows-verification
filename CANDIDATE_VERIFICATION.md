# ONE Candidate Verification — Exact-SHA Evidence

**Canonical source repository:** https://github.com/panglimanetizen01/one  
**Candidate source SHA:** `1a48989f213cd000a1eb3143b97549415b733241`  
**Source branch:** `milestone/100-ecosystem-20261023`  
**Candidate PR:** https://github.com/panglimanetizen01/one/pull/80

This file is the evidence index for the candidate. The workflows check out the exact source SHA from `CANONICAL_COMMIT.txt`; a green result from a different SHA is historical context only and must not be credited to this candidate.

## Exact-SHA workflow evidence

| Gate | Run | Current evidence |
|---|---|---|
| Focused standard library, UTC parser/formatter, JSON bounds, SQLite limits, package signing and trusted-publisher verification, Clippy | [40081565281](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081565281) | **PASS** on the candidate SHA |
| Linux distro conformance (Ubuntu 24.04 and Debian 12) | [40081562357](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081562357) | **PASS** on the candidate SHA; both distro jobs green |
| Full cross-platform verification (Ubuntu and Windows 2025) | [40081549604](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604) | **PASS** on the candidate SHA; Ubuntu and Windows jobs green |
| Android AArch64 native ELF runtime execution | [40082714472](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40082714472) | Running with explicit TCG opt-in and a 30-minute boot window; do not count yet |

**Release bundle evidence:** the passing cross-platform run produced non-expired artifacts: [Linux bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604/artifacts/12556010150), SHA-256 `5a5a63fef110959c5880a020f0933084e691814e6a92f403f35bea3d396f1f80`; [Windows bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604/artifacts/12555024750), SHA-256 `c43d5811ac872af8a07c1f453e5f87ff7adc138d2a445b267e2655f9ab35f197`. Both artifacts are named with source SHA `1a48989f213cd000a1eb3143b97549415b733241`.

The downloaded ZIPs were independently inspected, and their locally computed SHA-256 digests match GitHub's reported artifact ZIP digests exactly. Linux bundle contains an x86-64 ELF executable and Windows bundle contains a PE32+ x86-64 executable. Both embedded `SHA256SUMS` files verified successfully. Embedded binary digests: Linux `6b6190ac0fe3c3954178e4f1e15601e959206015aaf06aee4fb157fc394ba676`; Windows `d7cb24e1833730566d6a62fbed71748a1295637ab0e82efd6f2700b60b1306da`. `BUILD-METADATA.txt` in both bundles pins source SHA `1a48989f213cd000a1eb3143b97549415b733241`, target triple, Rust/Cargo 1.99.0, and CLI version `one 0.1.0`.

## User workflow and documentation checks

The passing exact-SHA cross-platform run [40081549604](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604) also executed `tools/check_contract.py`, `tools/check_user_docs.py`, and `tools/check_user_docs_test.py`; the user-doc consistency check reported `OK: user documentation is consistent: docs/panduan-pengguna`. The CLI smoke sequence exercised project creation, source checking, running, building, testing, and packaging; both Linux and Windows offline verification ended with `OFFLINE VERIFICATION: PASS`. These are concrete workflow/doc checks, but they do not substitute for the remaining security review or final Definition-of-Done audit.

## Android runner diagnosis and remediation

Android attempt [40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013) proved that `-accel off` alone was insufficient: QEMU still appended `-enable-hvf` and failed with `HVF error: HV_UNSUPPORTED`. Android's official [emulator command-line documentation](https://developer.android.com/studio/run/emulator-commandline) requires `ANDROID_I_WANT_MY_TCG=yes` to opt in to software TCG mode. The workflow now sets that environment variable and extends the boot window to 1800 seconds (job timeout 60 minutes); the new exact-SHA attempt is [40082714472](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40082714472). This is a targeted remediation, not proof that Android runtime acceptance passed; only the actual ELF build, AArch64 header checks, ADB push, and successful execution output can close that gate.

## Canonical CI runner issue

The canonical repository's candidate runs [40077268116](https://github.com/panglimanetizen01/one/actions/runs/40077268116), [40077268118](https://github.com/panglimanetizen01/one/actions/runs/40077268118), and [40077268122](https://github.com/panglimanetizen01/one/actions/runs/40077268122) have jobs reporting `runner_id: 0` and empty `steps: []`. These runs produced no source build/test evidence. They are neither a source-code failure diagnosis nor a passing result. Independent mirror runs are being used as exact-SHA evidence; the canonical runner issue remains documented separately.

## Remaining fixed-ledger acceptance scope

The canonical fixed-weight [completion ledger](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md) currently records **90/100 implementation, 60/100 verified**. Do not change the weights or infer full row credit from a partial pass.

- **E1 — standard library (10 points):** only credit the full row after every scope-defined reusable API contract is implemented and covered by executable tests; focused regressions pass, but ledger acceptance has not been awarded.
- **E2 — packaging/provenance (8 points):** deterministic package and trusted-publisher tests pass; protected `one-release` environment dispatch and exact-source signed release acceptance still need direct evidence.
- **E3 — compatibility/platforms (8 points):** current Linux/Windows matrix and Ubuntu/Debian distro matrix pass; Android AArch64 runtime is still pending the emulator result.
- **E4 — security/recovery (6 points):** bounded I/O, SQLite limits, and symlink/reparse protections have tests; path-scoped capability root confinement and the full threat review remain open.
- **E5 — docs/tooling (4 points):** user-doc consistency/tests and CLI smoke workflows pass; final reviewed user-workflow acceptance still needs to be reconciled in the ledger.
- **E6 — forensic audit (4 points):** not complete until E1–E5 are accepted, all evidence references agree on the final source SHA, and all mandatory release gates pass.

## Release gate rules

- Do not credit tests run against a different source SHA.
- Do not count a running, skipped, infrastructure-failed, or logless job as PASS.
- Do not infer Android runtime success from a cross-compiled ELF alone.
- Do not mark the overall milestone GREEN LOCKED until all weighted ledger rows and required release gates have acceptance evidence, the completion ledger is reconciled, and the final forensic audit is complete.
- The focused workflow PASS is a narrow pass only; it does not by itself establish the full release gate.
