# Issue #104 — exact-source hard-link and platform verification evidence

Date: 2026-11-20 (UTC)

## Identity

- ONE repository: `panglimanetizen01/one`
- ONE PR: #113, OPEN / DRAFT / UNMERGED
- Exact tested ONE source SHA: `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`
- ONE main: `d35db95153f6ddd79885494c72f5aee16c899751` (unchanged)
- Independent verifier PR: #51, OPEN / DRAFT / UNMERGED
- Verifier HEAD for the listed workflows: `27207b85ed205d2cf12e6fd66b918193a215d8fd`
- Branch-local `CANONICAL_COMMIT.txt`: `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`
- Protected verifier branch/pin: unchanged; canonical protected source remains `722d662e7a81711ba3607d26571f4048a292b3ed`.

## Hard-link regression

Test: `filesystem::hardlink_tests::authority_rejects_hard_linked_targets_without_side_effects`.

The fixture creates an in-root file and a hard-link name outside the project root. The test requires read and write to fail with the hard-link rejection and verifies that both names retain their original bytes. The Windows fixture releases the retained root handle before cleanup.

- E4 run [#44651796986](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796986): SUCCESS.
- Windows job #136008224371: the hard-link test passed; 9 selected Windows filesystem/platform regression tests passed with 0 failures. The same log explicitly shows the junction escape, absolute in-root read, outside-root no-side-effect rejection, text write, oversized write rejection, atomic-replacement failure preservation, and parent traversal tests passing.
- Unix job #136008224711: the hard-link test passed. The log also shows the no-follow, mount-boundary, parent traversal, outside-target write, nested-write fail-closed, oversized write, symlink-target, atomic replacement, parent-swap race, and policy tests passing.

## Exact-source workflows

| Scope | Run | Result |
|---|---:|---|
| E4 Unix + Windows adversarial filesystem | [44651796986](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796986) | SUCCESS |
| Linux distro: Ubuntu 24.04 + Debian 12 | [44651796952](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796952) | SUCCESS |
| Windows native backend runtime | [44651796852](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796852) | SUCCESS |
| E1 Standard Library Windows | [44651797000](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651797000) | SUCCESS |
| Focused standard-library/database | [44651796941](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796941) | SUCCESS |
| SEC-05 subprocess timeout/output | [44651796634](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796634) | SUCCESS |
| E4 subprocess resource guard | [44651796650](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796650) | SUCCESS |
| Candidate artifact integrity | [44651796712](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796712) | SUCCESS |
| Android AArch64 build artifact | [44651796635](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796635) | SUCCESS |
| Android API 35 ARM64 runtime | [44651796976](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796976) | IN PROGRESS at last read |
| Cross-platform aggregate | [44651796654](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796654) | PENDING at last read |
| E1 Milestone 1 aggregate | [44651796950](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796950) | IN PROGRESS at last read |

Linux distro run #44651796952 has successful contract checks, build, Clippy, workspace tests, and real-network tests on both Ubuntu 24.04 and Debian 12.

## Artifact integrity

Run [#44651796712](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44651796712) successfully verified both release candidate archives:

- Linux artifact #14563276002: `sha256:59aa04887ffa5c2cb66d65e4ef7936622c6e0a4f6164ea8ea458457d10b8a940`
- Windows artifact #14561664789: `sha256:7d3c51123f73c398032ef0c636c018c12ea501340b822b8e3b4edc9777645a3a`

Both embedded `BUILD-METADATA.txt` files identify the exact source SHA, Rust/Cargo 1.100.0, and CLI 0.1.0. ELF64 little-endian EM_X86_64 and PE32+ x86-64 checks passed.

Historical artifact-integrity run #44589012615 remains FAILURE. Its log reported that it did not discover a successful cross-platform run for the exact source within 45 minutes. A later, separate exact-source run #44651796712 completed all digest, manifest, metadata, and executable-format checks successfully. Preserve both outcomes; do not delete or relabel the historical failure.

## CircleCI

ONE source SHA `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20` has CircleCI context `ci/circleci: one-linux` = SUCCESS. Workflow `3a9c0613-a1bc-43ae-b2d6-319841061048`; job `c4faf162-80e9-4f17-a83a-a72634bb592f`. Provider step logs were not inspected, so no individual CircleCI step or test-count claim is made.

## Status boundary

- Hard-link rejection: IMPLEMENTED / TESTED / VERIFIED on Linux and Windows for the exact source above.
- The listed E4 adversarial controls: VERIFIED within the tested runner/platform scopes.
- Linux nested writes: still fail-closed; not supported.
- Filesystem adapters: Linux-only on Linux and Windows-only on Windows. Android/macOS filesystem adapters remain unavailable.
- Android native runtime is separate evidence and does not establish Android filesystem adapter support.
- Issue #104 remains OPEN / NOT ACCEPTED. Do not promote the protected canonical pin, fixed-weight ledger, or DoD; do not merge PR #51 or PR #113; do not change ONE main or protected verifier branch.
