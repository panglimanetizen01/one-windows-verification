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


## Android API 35 AArch64 runtime artifact — 2026-11-20

- Workflow #44585282482 SUCCESS on exact ONE source `c7f460a4e38be61de635ad5af9f7ff987a941f01`; ARM64-native runtime job #135777110380 exited 0 with `ONE_NATIVE_BACKEND_OK`.
- Artifact ID `14562860220`, 12,953 bytes; GitHub archive digest and independently downloaded ZIP SHA-256 both `75a73869f4d5351b3d3a9ba311266602a89221bad81b040d0433432c2aa41741`.
- Embedded source marker matches `c7f460a...`; ELF is AArch64 PIE with `/system/bin/linker64`; embedded ELF SHA-256 `5b05504a0167beeae1d15e267c2e7af1f1a7c62b163d459289be1d663c380a0c` matches the included sidecar.
- This is native backend runtime evidence only. It does not establish Android filesystem adapter support or promote the protected E3 source pin/ledger.

## Exact-source hard-link verification checkpoint — 2026-11-20

The current branch-local source pin is `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`. The verifier workflows were executed from verifier HEAD `27207b85ed205d2cf12e6fd66b918193a215d8fd`; this documentation commit does not change the protected `verification` branch or its source pin.

- E4 run #44651796986 SUCCESS: Unix and Windows adversarial filesystem jobs passed, including `filesystem::hardlink_tests::authority_rejects_hard_linked_targets_without_side_effects`.
- Windows E4 job #136008224371 explicitly passed the seven named Windows filesystem regressions, atomic-replacement failure-preservation, hard-link, and platform-metadata tests (9 selected tests, 0 failures).
- Unix E4 job #136008224711 passed the no-follow, mount-boundary, traversal, race, write-boundary, hard-link, platform-metadata, and policy regression filters.
- Linux distro run #44651796952 SUCCESS on Ubuntu 24.04 and Debian 12.
- Windows native backend runtime #44651796852, E1 Windows #44651797000, focused stdlib/database #44651796941, SEC-05 #44651796634, E4 resource guard #44651796650, and artifact integrity #44651796712 all SUCCESS.
- Artifact integrity #44651796712 verified Linux artifact #14563276002 (`sha256:59aa04887ffa5c2cb66d65e4ef7936622c6e0a4f6164ea8ea458457d10b8a940`) and Windows artifact #14561664789 (`sha256:7d3c51123f73c398032ef0c636c018c12ea501340b822b8e3b4edc9777645a3a`); embedded source manifests match `fb5c8bc...`, and ELF64/PE32+ format checks pass.
- ONE CircleCI `ci/circleci: one-linux` on exact source `fb5c8bc...` is SUCCESS (workflow `3a9c0613-a1bc-43ae-b2d6-319841061048`, job `c4faf162-80e9-4f17-a83a-a72634bb592f`); provider step logs were not inspected.
- Android build artifact #44651796635 is SUCCESS; Android API 35 runtime #44651796976 remained IN PROGRESS. Cross-platform aggregate #44651796654 remained PENDING and E1 Milestone 1 #44651796950 remained IN PROGRESS at last read.

The previous artifact-integrity failure #44589012615 is preserved as historical evidence. Its follow-up #44651796712 is a separate successful exact-source verification, not a replacement of the historical failure.

Evidence details and exact artifact digests: [evidence/ISSUE_104_HARDLINK_EXACT_SHA_2026-11-20.md](evidence/ISSUE_104_HARDLINK_EXACT_SHA_2026-11-20.md).

Issue #104 remains OPEN / NOT ACCEPTED. Linux nested writes and unsupported Android/macOS filesystem adapters remain fail-closed/unavailable. No protected pin, ledger weight, DoD checkbox, release status, or merge state is changed.


## Current Project ONE Issue #104 verifier checkpoint — 2026-11-20

- Verifier PR #51: OPEN / DRAFT / UNMERGED; branch `probe/issue-104-platform-metadata-20261120`; HEAD at readback `e5632e75c473546527c7e9a404262631d827f429`.
- Branch-local `CANONICAL_COMMIT.txt`: exact ONE source `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`.
- Fresh E4 #44656893733, Linux distro #44656893931, Windows native runtime #44656893882, SEC-05 #44656893697, E4 resource guard #44656893627, artifact integrity #44656893650, E1 Windows #44656893639, focused stdlib/database #44656893788, and cross-platform aggregate #44656893832: SUCCESS.
- Android AArch64 build #44656893715: SUCCESS. Fresh Android API 35 ARM64 runtime #44656893597 remains IN PROGRESS (runtime job #136025758614).
- E1 Milestone 1 #44656893655 remains IN PROGRESS (Windows passed; Ubuntu job #136025210968 still running).
- Earlier Android API 35 runtime #44652693606 completed SUCCESS for the same ONE source on verifier HEAD `226360d...`; that historical exact-source proof is preserved, but it does not make the fresh run on HEAD `e5632e...` terminal.
- Issue #104 remains OPEN / NOT ACCEPTED. Linux nested writes and unsupported Android/macOS filesystem adapters remain fail-closed/unavailable. No source pin, ledger weight, DoD item, merge, or release state is changed.
- GitHub branch metadata reports `protected=false` for branch `verification`; the repository rulesets endpoint returned an empty list. The classic branch-protection endpoint returned 403 to this integration, so actual protection configuration is NOT VERIFIED. Do not assume GitHub-side protection is enabled or change branch settings without explicit authorization.

The PR #92 Local CI migration notes above are historical and separate from this current product-verification candidate. The branch-local source pin remains the authoritative checkout target for the workflows in this PR.

## Independent verifier source-pin refresh — 2026-11-26

The branch-local source pin has been refreshed from the stale ONE PR #123 candidate `ffc6f417...` to current-main test-only candidate PR #133 exact SHA `cd4651d947d309a5087f9b9eae42580a669f543f`. The Windows/local-CI parity pin remains separate and unchanged. Historical evidence for prior source pins is retained and must not be attributed to the new SHA. New verifier runs must reach terminal SUCCESS and their exact source/artifact identities must be checked before the PR can be considered. Issue #104 remains OPEN / NOT ACCEPTED.