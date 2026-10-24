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
