# Prompt 3 E3/E4 evidence index

- Canonical source repository: https://github.com/panglimanetizen01/one
- Candidate branch: `milestone/100-ecosystem-20261023`
- Exact code-bearing source SHA: `85ded41bea3d7e2f64f0758e1bfacb376f0cb2cd`
- Independent lab pin at test time: `CANONICAL_COMMIT.txt` = the exact SHA above.
- PR #80 remains open/draft/unmerged. No merge or release is authorized.
- This index is a lab record; it does not alter source code or change acceptance status.

## Exact-SHA matrix results

| Gate | Run | Result | Evidence boundary |
|---|---|---|---|
| Linux distributions | [40217709918](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709918) | PASS | Ubuntu 24.04 and Debian 12 completed build, Clippy, workspace/contract tests, and real-network checks on the pinned source. |
| Linux + Windows cross-platform | [40217709951](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709951) | PASS | Ubuntu 24.04 and Windows Server 2025 jobs completed build, strict Clippy, workspace tests, real-network tests, offline verification, and release-bundle checks. Exact-SHA assertions passed. |
| SEC-05 bounded subprocess | [40217709933](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709933) | PASS | Linux and Windows subprocess contract/static guards completed; Windows suite covers bounded output, timeout, command-line quoting, Unicode/working directory and descendant Job Object containment. |
| E4 filesystem / SQLite / policy adversarial tests | [40217709863](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709863) | PASS for tested cases | Unix descriptor-relative no-follow tests, SQLite resource/query-limit tests, Windows reparse/junction escape regression, and capability-denial policy tests passed. The orchestrator denial regression confirms denied requests do not invoke adapters. This is not proof of full sandboxing. |
| E4 subprocess resource guard | [40217709957](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709957) | PASS | Static guard confirms bounded subprocess implementation exists; this is supplemental to runtime tests. |
| Android AArch64 ELF build/header | [40217710176](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217710176) | PASS — build/header only | Artifact ID `12607904032`. ELF64, little-endian, ET_DYN PIE, EM_AARCH64, interpreter `/system/bin/linker64`. Binary SHA-256: `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`. Artifact `SOURCE.txt` pins source SHA `85ded41bea3d7e2f64f0758e1bfacb376f0cb2cd`. No runtime claim. |
| Android API 35 runtime — macOS ARM64 host | [40217819570](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217819570) | FAIL | Emulator reported `HV_UNSUPPORTED`; software fallback still failed to boot. ELF execution step was skipped. |
| Android API 35 runtime — Linux ARM64 host | [40217709923](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709923) | FAIL before runtime | SDK manager could not find/install the Android emulator package for the ARM64 host. No guest boot or ELF execution. |
| Android API 35 runtime — Linux x86_64 / QEMU TCG | [40219720567](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40219720567) | FAIL — host architecture limitation | API 35 AArch64 AVD was created and discovered; emulator exited with `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host. System image must match the host architecture.` No guest boot or ELF execution. |

| Android API 35 runtime — macOS ARM64 host, documented TCG opt-in | [40221042296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40221042296) | IN PROGRESS at index update | Previous retries established that macOS hosted HVF is unavailable in this environment and the emulator ignores `-accel off` without the documented `ANDROID_I_WANT_MY_TCG=yes` opt-in. Current workflow removes the QEMU wrapper experiment and sets that documented environment variable. At index update, SDK/NDK installation is still running; no guest boot or ELF runtime result yet. |\n\n## E4 disposition and residual risks

The candidate has tested no-follow descriptor-relative Unix file operations, Windows reparse/junction checks, SQLite query/resource bounds, capability policy denial, and bounded subprocess lifecycle/output. However, these do not close all mandatory E4 criteria.

Open security design gaps:
1. Explicit project-root descriptor anchoring/confinement is not consistently implemented across supported platforms.
2. Mount-boundary enforcement has not been proven by implementation and adversarial tests.
3. Runtime-wide quotas across concurrent operations are not implemented/proven; per-invocation timeout and output caps are not equivalent.
4. Non-Unix/non-Windows fallback filesystem paths do not provide equivalent no-follow guarantees.
5. The complete threat review and end-to-end failure/recovery matrix remain incomplete.

These are release-gate blockers, not documentation-only findings. Do not claim a complete OS sandbox. Keep E4 unaccepted until implementation and regression evidence close these requirements or the approved contract explicitly changes them.

## Status

- E3: **NOT ACCEPTED** pending actual Android API 35 `arm64-v8a` ELF execution and asserted output.
- E4: **NOT ACCEPTED** pending the open root/mount/quota/fallback security requirements above.
- Overall Prompt 3: **NOT PASSED**. No `PASS GREEN LOCKED` claim.
- Implementation subtotal remains 91/100 provisional; weighted verified total remains 64/100 as in the fixed-weight ledger. E3 stays 0/8 verified and E4 stays 0/6 verified. No weights were changed.
- Do not merge PR #80 or PR #83, publish a release, or start Prompt 4 without the required authorization and evidence closure.
