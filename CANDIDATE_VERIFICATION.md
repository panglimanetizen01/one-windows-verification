# ONE Candidate Verification — Exact-SHA Evidence

**Canonical source repository:** https://github.com/panglimanetizen01/one  
**Candidate source SHA:** `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`  
**Source branch:** `milestone/100-ecosystem-20261023`  
**Candidate PR:** https://github.com/panglimanetizen01/one/pull/80

This file is the evidence index for the candidate. The workflows check out the exact source SHA from `CANONICAL_COMMIT.txt`; a green result from a different SHA is historical context only and must not be credited to this candidate.

## Exact-SHA workflow evidence

| Gate | Run | Current evidence |
|---|---|---|
| Focused standard library, UTC parser/formatter, JSON bounds, SQLite limits, package signing and trusted-publisher verification, Clippy | [40084595238](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595238) | **PASS** on exact source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; UTC/JSON/SQLite/provenance tests, Clippy, and SQLite NOFOLLOW regression passed |
| Linux distro conformance (Ubuntu 24.04 and Debian 12) | [40084595259](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595259) | **PASS** on exact source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; Ubuntu 24.04 and Debian 12 passed |
| Full cross-platform verification (Ubuntu and Windows 2025) | [40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236) | Running on final source SHA; do not count yet |
| Android AArch64 native ELF runtime execution | [40084822122](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084822122) | Running on macOS ARM64; wrapper strips injected `-enable-hvf` to force TCG; runtime acceptance not yet counted |

**Historical release bundle evidence (prior source SHA `1a48989f213cd000a1eb3143b97549415b733241`; not final-SHA acceptance):** the earlier passing cross-platform run produced non-expired artifacts: [Linux bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604/artifacts/12556010150), SHA-256 `5a5a63fef110959c5880a020f0933084e691814e6a92f403f35bea3d396f1f80`; [Windows bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604/artifacts/12555024750), SHA-256 `c43d5811ac872af8a07c1f453e5f87ff7adc138d2a445b267e2655f9ab35f197`. Both artifacts are named with source SHA `1a48989f213cd000a1eb3143b97549415b733241`. The current candidate SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` requires fresh bundles and checksum inspection.

The downloaded ZIPs were independently inspected, and their locally computed SHA-256 digests match GitHub's reported artifact ZIP digests exactly. Linux bundle contains an x86-64 ELF executable and Windows bundle contains a PE32+ x86-64 executable. Both embedded `SHA256SUMS` files verified successfully. Embedded binary digests: Linux `6b6190ac0fe3c3954178e4f1e15601e959206015aaf06aee4fb157fc394ba676`; Windows `d7cb24e1833730566d6a62fbed71748a1295637ab0e82efd6f2700b60b1306da`. `BUILD-METADATA.txt` in both bundles pins source SHA `1a48989f213cd000a1eb3143b97549415b733241`, target triple, Rust/Cargo 1.99.0, and CLI version `one 0.1.0`.

**Historical standard-library test detail (prior source SHA `1a48989f213cd000a1eb3143b97549415b733241`; final-SHA rerun pending):** on both Linux and Windows, `crates/one-core/src/stdlib.rs` unit tests reported **228 passed, 0 failed**, and `crates/one-core/tests/stdlib_builtins.rs` reported **18 passed, 0 failed**. The latter includes the JSON round-trip and strict UTC timestamp source-pipeline regressions. These passing suites establish test results for the implemented API subset, not completion of the broader E1 public-library stability/backend-conformance criteria.

## User workflow and documentation checks

The earlier passing cross-platform run [40081549604](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604) on prior source SHA `1a48989f213cd000a1eb3143b97549415b733241` also executed `tools/check_contract.py`, `tools/check_user_docs.py`, and `tools/check_user_docs_test.py`; the user-doc consistency check reported `OK: user documentation is consistent: docs/panduan-pengguna`. The CLI smoke sequence exercised project creation, source checking, running, building, testing, and packaging; both Linux and Windows offline verification ended with `OFFLINE VERIFICATION: PASS`. These are concrete workflow/doc checks, but they do not substitute for the remaining security review or final Definition-of-Done audit.

## Android runner diagnosis and remediation

Android attempt [40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013) proved that `-accel off` alone was insufficient: QEMU still appended `-enable-hvf` and failed with `HVF error: HV_UNSUPPORTED`. The TCG-enabled wrapper attempt [40082714472](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40082714472) remained stuck in the opaque boot action and was cancelled by the next attempt. To avoid repeating that opaque failure mode, workflow run [40083495815](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083495815) replaces the action wrapper with direct emulator launch, host architecture output, 15-second boot polling, and emulator-log tails on failure. The latest final-SHA run is [40083555754](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083555754). This is a diagnostic remediation, not proof that Android runtime acceptance passed.

## Canonical CI runner issue

The canonical repository's current-candidate runs [One CI 40084579487](https://github.com/panglimanetizen01/one/actions/runs/40084579487), [Linux distro 40084579475](https://github.com/panglimanetizen01/one/actions/runs/40084579475), and [focused stdlib 40084579490](https://github.com/panglimanetizen01/one/actions/runs/40084579490) have jobs with empty `steps: []` and failed before executable steps. These runs produced no source build/test evidence; they are neither a source-code failure diagnosis nor a passing result. Independent mirror runs are being used as exact-SHA evidence; the canonical runner issue remains documented separately.

**Focused security review:** [SECURITY_RELEASE_REVIEW.md](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/SECURITY_RELEASE_REVIEW.md) records the inspected boundaries and residual risks; reviewed code is unchanged from `11d53e8558a948b9607b5d70ab84d1ddcc0e29cd`, and current source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` only adds the Definition of Done wording correction. It explicitly keeps E4 open for SQLite parent-component races, root/mount confinement, fallback platforms, and runtime-wide quotas; the review is not a claim of complete sandboxing.

## Final gate checklist

The canonical PR now includes [DEFINITION_OF_DONE.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/DEFINITION_OF_DONE.md), which defines exact-SHA evidence rules and the fixed-weight E1–E6 release acceptance criteria. Candidate SHA is now `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; previously passing cross-platform, distro, and focused runs were on the prior SHA and must not be counted as final-SHA acceptance until rerun.

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

The fixed-weight ledger was then reconciled in source commit `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; this is the current candidate SHA and the selector has been repinned. Runs started before this pin are historical and cannot close the current SHA gate. Wait for the new run set whose harness commit includes the pin update, then inspect every job's checked-out source SHA in its logs.

Current final-SHA workflow set is pinned to source `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`: cross-platform `40084595236`, Linux distro `40084595259`, focused standard-library/database/provenance `40084595238`, lockfile bootstrap `40084595303`, Android runtime `40084822122`. These IDs are the acceptance candidates; older run IDs above are historical and must not be used to claim final-SHA acceptance.

**Current final-SHA lockfile bootstrap:** [run 40084595303](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595303) passed after checking out exact source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; generated Cargo lockfile SHA-256 `284f1186517314c88ac31412c86f09e6418114376e56cd4bb2ae5fd676495c90`.

**Historical distro evidence detail:** [run 40083651500](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083651500) passed on source `9598e56ef4aaada5d37faae30110cf5f3ae6c4ac`. It is not final-SHA acceptance; the current source `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` is being reverified in run [40083875252](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083875252).

The final candidate source SHA adds a defense-in-depth SQLite fix: file-backed read-only opens include `SQLITE_OPEN_NOFOLLOW`, with a Unix regression for final symlinks. The focused run `40083996493` passed this regression on exact SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; full Linux/Windows and distro matrices also passed on that SHA. Parent-component/mount confinement remains open.

**Android emulator root cause and remediation:** run `40083651724` logs prove the hosted runner is `arm64`, but the Android emulator unconditionally injects `-enable-hvf` even with `-accel off` because the HVF feature remains enabled; nested virtualization on the hosted runner returns `HVF error: HV_UNSUPPORTED`. The latest workflow disables the emulator feature via `-feature -HVF` as well as selecting software TCG and emits the emulator command/logs, so the next attempt can confirm whether that override prevents HVF injection. This is still not Android runtime acceptance until the native test executes successfully.

**Historical release candidate bundles (prior source `11d53e8558a948b9607b5d70ab84d1ddcc0e29cd`; not final-SHA acceptance):** [Linux bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083875189/artifacts/12555899841), ZIP SHA-256 `0701866b270933c7207d6ba14c07a8799aaecd41e785342ee2f4cc7baafba73b`; [Windows bundle](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083875189/artifacts/12556332264), ZIP SHA-256 `e0c0f9f24794d292a4eaaac471ca0555ef0a1570630421c0fb83cfef43a25531`. Both bundles were downloaded and independently inspected: Linux payload is ELF 64-bit x86-64; Windows payload is PE32+ x86-64; both embedded `SHA256SUMS` manifests verify. Binary digests: Linux `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; Windows `dcd386d96d14712736b101f2a84a967189eb2c50cd3838072a4dc13453b69b04`. Both `BUILD-METADATA.txt` files pin source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, target triple, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. These are unsigned candidate build artifacts; they are not a signed source-bound release package.

The reusable Definition of Done received a final documentation correction in source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; the selector is repinned to this SHA. All runs that checked out `11d53e8558a948b9607b5d70ab84d1ddcc0e29cd` are historical evidence only for the new candidate. Re-run and inspect the new exact-SHA matrix before acceptance.

The current source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` is documentation-only relative to the reviewed code SHA; final-SHA matrix and fresh candidate bundles are still required.

**Final candidate focused/distro verification detail:** focused run `40084595238` passed on exact SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, including the SQLite final-symlink regression and trusted-publisher signature/tampering test. Linux distro run `40084595259` passed both Ubuntu 24.04 and Debian 12; both logs assert the exact source SHA.
