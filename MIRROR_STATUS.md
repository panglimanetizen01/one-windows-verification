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


## ONE PR #113 platform metadata candidate — exact-SHA evidence — 2026-11-20

- Branch-local `CANONICAL_COMMIT.txt` pins ONE source `c7f460a4e38be61de635ad5af9f7ff987a941f01`; verifier PR #51 is a diagnostic OPEN / DRAFT / UNMERGED PR. Protected `verification` branch remains `b14abf0020472dc45842be30854e0a09317d6cb4` with protected canonical pin `722d662e7a81711ba3607d26571f4048a292b3ed` unchanged.
- E4 run #44585270928 SUCCESS on the exact candidate: Unix no-follow/resource-bound and Windows reparse/handle jobs passed; Windows native `NtCreateFile + OBJ_DONT_REPARSE` probe passed on Windows Server 2025 build 26100. The added test `filesystem_adapters_advertise_only_platforms_with_native_backends` explicitly passed on Linux and Windows (1 passed / 0 failed each).
- Linux distro run #44585282690 SUCCESS on Ubuntu 24.04 and Debian 12, including workspace tests and corrected filesystem vertical-slice CLI integration. E1 Windows acceptance run #44585282432 SUCCESS.
- Remaining aggregate cross-platform, Windows native runtime, Android runtime, SEC-05, E1 milestone and artifact-integrity workflows were IN_PROGRESS/PENDING at this checkpoint. CircleCI on source `c7f460a...` was PENDING; provider step logs unavailable.
- The prior source `7581a1b...` exposed a CLI integration mismatch because the interpreter passed `PlatformKind::Any`; candidate `c7f460a...` fixes this by using `PlatformKind::current_host()` and updates the integration test to use the actual host platform.
- Filesystem adapter metadata is now Linux-only on Linux, Windows-only on Windows, and empty on Android/macOS/other unsupported targets. This does not add Android/macOS filesystem support. Issue #104 remains OPEN / NOT ACCEPTED; no protected pin or ledger weight is promoted.
