# Prompt 3 E3/E4 evidence index

- Canonical source repository: https://github.com/panglimanetizen01/one
- Candidate branch: `milestone/100-ecosystem-20261023`
- Exact code-bearing source SHA: `85ded41bea3d7e2f64f0758e1bfacb376f0cb2cd`
- Independent lab pin at test time: `CANONICAL_COMMIT.txt` = the exact SHA above.
- PR #80 remains open/draft/unmerged. No merge or release is authorized.
- This index is a lab record; it does not alter source code or change acceptance status.

## Exact-SHA matrix results

**Evidence boundary update (2026-10-26):** The results in the matrix below were executed against code-bearing SHA `85ded41bea3d7e2f64f0758e1bfacb376f0cb2cd`. The canonical branch then received documentation-only commits `a8e76ab6f3288c4391e059663e1815a361a54924` and `25dfbb6aa5bffd7049bf7228f0da190cb2520177` to correct the E3/E4 ledger and DoD. Results on earlier SHAs are historical until reruns against `25dfbb6aa5bffd7049bf7228f0da190cb2520177` complete. E3/E4 remain unaccepted.

| Gate | Run | Result | Evidence boundary |
|---|---|---|---|
| Linux distributions | [40252044796](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044796) | PASS | Exact source pin `25dfbb6aa5bffd7049bf7228f0da190cb2520177`; Ubuntu 24.04 and Debian 12 completed workspace build/tests, contract checks, Clippy, and real-network tests. |
| Linux + Windows cross-platform | [40252044688](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044688) | Ubuntu PASS; Windows in progress at index update | Exact source pin `25dfbb6aa5bffd7049bf7228f0da190cb2520177`; Ubuntu completed build/release build, AST regression, Clippy, workspace tests, real-network tests, and offline verification. Windows passed contract checks and debug build; release-mode build is still running. Overall matrix is not PASS until Windows completes. |
| SEC-05 bounded subprocess | [40252044630](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044630) | PASS | Exact source pin `25dfbb6aa5bffd7049bf7228f0da190cb2520177`; Linux and Windows subprocess contract tests and fail-closed guard passed, including the `PROC_THREAD_ATTRIBUTE_JOB_LIST` / `CreateProcessW` process-at-creation check. |
| E4 filesystem / SQLite / policy adversarial tests | [40252044602](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044602) | PASS for tested cases | Exact source pin `25dfbb6aa5bffd7049bf7228f0da190cb2520177`; Unix descriptor-relative no-follow and SQLite bounds passed; Windows reparse-point/handle regression passed. Does not prove project-root confinement, mount-boundary enforcement, runtime-wide quotas, or complete sandboxing. |
| E4 subprocess resource guard | [40252044911](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044911) | PASS | Static resource-enforcement guard passed on exact source pin `25dfbb6aa5bffd7049bf7228f0da190cb2520177`; supplemental to dynamic tests. |
| Android AArch64 ELF build/header | [40252250920](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252250920) | PASS — build/header only | Exact source SHA `25dfbb6aa5bffd7049bf7228f0da190cb2520177`. Artifact ID `12620868302`; archive digest `sha256:104dba65d2c1af3ea1d2148bea8eb281571cdc63eefa988249907081e47805a5`; ELF is ELF64 little-endian ET_DYN PIE, `EM_AARCH64`, interpreter `/system/bin/linker64`; binary SHA-256 `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`. No runtime claim. |
| Android API 35 runtime — macOS ARM64 host | [40217819570](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217819570) | FAIL | Emulator reported `HV_UNSUPPORTED`; software fallback still failed to boot. ELF execution step was skipped. |
| Android API 35 runtime — Linux ARM64 host | [40217709923](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40217709923) | FAIL before runtime | SDK manager could not find/install the Android emulator package for the ARM64 host. No guest boot or ELF execution. |
| Android API 35 runtime — Linux x86_64 / QEMU TCG | [40219720567](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40219720567) | FAIL — host architecture limitation | API 35 AArch64 AVD was created and discovered; emulator exited with `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host. System image must match the host architecture.` No guest boot or ELF execution. |

| Android API 35 runtime — macOS ARM64 host, `ANDROID_I_WANT_MY_TCG=yes` retry | [40221042296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40221042296) | FAIL — hosted virtualization unavailable | SDK/NDK installation and backend contract tests passed, but boot failed with `HVF error: HV_UNSUPPORTED` and `qemu-system-aarch64-headless: failed to initialize HVF`. Despite `ANDROID_I_WANT_MY_TCG=yes` and `-accel off`, emulator still passed `-enable-hvf`; the ELF execution step was skipped. This is a runner/emulator capability blocker, not an Android runtime PASS. Need a supported virtualization host or physical API 35 arm64-v8a device. |\n\n## E4 disposition and residual risks

The candidate has tested no-follow descriptor-relative Unix file operations, project-root confinement, Windows reparse/junction checks, SQLite query/resource bounds, capability policy denial, and bounded subprocess lifecycle/output. However, these do not close all mandatory E4 criteria.

Open security design gaps (candidate source SHA `43c7987220d858f6f6a9be4222ead2db5311f29a`):
1. **Project-root confinement is now implemented in the candidate**: paths are constrained beneath the canonical current working directory; Unix opens walk from a pinned root descriptor using descriptor-relative `openat` + `O_NOFOLLOW`, and Windows verifies the opened handle's final path remains under the root. Outside-root read/write denial regression tests passed in the Unix E4 suite [run 40252707835](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252707835). Limitation: the root is the process current working directory at adapter invocation, not an explicit per-project root passed through the request API.
2. **Mount-boundary enforcement remains partial**: Unix traversal rejects a different `st_dev` from the root, but same-device bind mounts are not proven to be rejected. Do not claim full mount-ID confinement.
3. Runtime-wide quotas across concurrent operations are not implemented/proven; per-invocation timeout, output caps, and SQLite limits are not equivalent to a shared runtime-wide quota.
4. Non-Unix/non-Windows fallback filesystem operations now fail closed rather than following symlinks, but fallback-platform behavior still needs a dedicated compile/runtime regression and metadata contract review.
5. The complete threat review and end-to-end failure/recovery matrix remain incomplete.

These are release-gate blockers, not documentation-only findings. Do not claim a complete OS sandbox. Keep E4 unaccepted until implementation and regression evidence close these requirements or the approved contract explicitly changes them.

## Status

- Latest branch HEAD `25dfbb6aa5bffd7049bf7228f0da190cb2520177` requires a refreshed exact-SHA matrix; do not treat parent-SHA results as current release acceptance.

- E3: **NOT ACCEPTED** pending actual Android API 35 `arm64-v8a` ELF execution and asserted output.
- E4: **NOT ACCEPTED**. Root confinement is implemented and tested, but full mount-ID boundaries, runtime-wide quotas, fallback-platform acceptance, and complete threat review remain open.
- Overall Prompt 3: **NOT PASSED**. No `PASS GREEN LOCKED` claim.
- Implementation subtotal remains 91/100 provisional; weighted verified total remains 64/100 as in the fixed-weight ledger. E3 stays 0/8 verified and E4 stays 0/6 verified. No weights were changed.
- Do not merge PR #80 or PR #83, publish a release, or start Prompt 4 without the required authorization and evidence closure.


### Latest exact-SHA refresh — candidate `25dfbb6aa5bffd7049bf7228f0da190cb2520177`
- Android AArch64 cross-compile + contract tests: [run 40252261474](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252261474) completed successfully on the exact candidate SHA, including compilation/ELF inspection and backend contract regression tests. This is build/contract evidence only, not runtime acceptance.
- Independent Android artifact inspection: [run 40252250920](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252250920) still running at index update.
- API 35 runtime on macOS ARM64 with TCG retry: [run 40252056666](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252056666) failed at emulator boot with `HV_UNSUPPORTED`; no ELF execution.
- API 35 runtime on Linux x86_64 with TCG: [run 40252061955](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252061955) failed because Android Emulator does not support an `arm64` AVD on an x86_64 host; no ELF execution.
- API 35 macOS native capability probe: [run 40252044893](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044893) failed during boot; the ELF execution step was skipped.
- API 35 software-emulation fallback: [run 40252044795](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40252044795) failed at boot with `HV_UNSUPPORTED`; no ELF execution.