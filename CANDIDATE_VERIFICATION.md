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
| Full cross-platform verification (Ubuntu and Windows 2025) | [40081549604](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081549604) | Ubuntu job **PASS**; Windows 2025 still running, so matrix not yet counted |
| Android AArch64 native ELF runtime execution | [40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013) | Running; do not count yet |

## Android runner diagnosis and remediation

The prior Android attempt [40080133616](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40080133616) failed before the native test ran: the Android emulator process exited with `HVF error: HV_UNSUPPORTED` / `failed to initialize HVF`, and ADB never saw `emulator-5554`. The verification workflow now adds `-accel off` so QEMU uses software emulation instead of the unsupported HVF path. This change is an infrastructure remediation, not proof that Android runtime acceptance passed; only the actual ELF build, AArch64 header checks, ADB push, and successful execution output can close that gate.

## Canonical CI runner issue

The canonical repository's candidate runs [40077268116](https://github.com/panglimanetizen01/one/actions/runs/40077268116), [40077268118](https://github.com/panglimanetizen01/one/actions/runs/40077268118), and [40077268122](https://github.com/panglimanetizen01/one/actions/runs/40077268122) have jobs reporting `runner_id: 0` and empty `steps: []`. These runs produced no source build/test evidence. They are neither a source-code failure diagnosis nor a passing result. Independent mirror runs are being used as exact-SHA evidence; the canonical runner issue remains documented separately.

## Release gate rules

- Do not credit tests run against a different source SHA.
- Do not count a running, skipped, infrastructure-failed, or logless job as PASS.
- Do not infer Android runtime success from a cross-compiled ELF alone.
- Do not mark the overall milestone GREEN LOCKED until all weighted ledger rows and required release gates have acceptance evidence, the completion ledger is reconciled, and the final forensic audit is complete.
- The focused workflow PASS is a narrow pass only; it does not by itself establish the full release gate.
