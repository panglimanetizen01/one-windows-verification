# ONE Prompt 3/4 — E3/E4 checkpoint

Updated: 2026-10-25
Canonical repository: https://github.com/panglimanetizen01/one
Canonical PR: https://github.com/panglimanetizen01/one/pull/80
Canonical branch: `milestone/100-ecosystem-20261023`
Exact canonical source SHA tested: `56606c7f8076bc9a67e321835077315d321b8b7a`
Verifier repository/branch: `panglimanetizen01/one-windows-verification` / `verification`
Verifier harness commit: `803b4e45d1979ba2105f777d4c22dfc89526ea2e`

## E3 — platform conformance

- Windows Server 2025: [run 40161268846](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268846) — PASS. Job logs show exact-source SHA verification, release/debug builds, AST contract regression, Clippy, Windows tests, CLI smoke (create/check/run/build/test/package), offline verification, and real network runtime tests succeeded. This proves the listed Windows job, not all Windows use cases.
- Ubuntu 24.04 and Debian 12: [run 40161268804](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268804) — PASS. Both jobs show exact-source SHA check, contract checks, build, Clippy, workspace tests and real network runtime tests succeeded.
- Android API 35 arm64-v8a: [run 40161268812](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268812) — NOT PASSED. SDK/NDK install and Android backend contract tests passed. The emulator boot step failed before ELF execution with `HVF error: HV_UNSUPPORTED` and `failed to initialize HVF: Invalid argument`; the required ELF build-and-execute step was skipped. Thus no successful runtime output/assertion exists. This is a hosted-runner virtualization capability failure; it is not evidence of an Android source-code failure and is not a pass. A supported hardware-virtualized runner or connected API 35 arm64-v8a device is required.
- Exact-SHA candidate artifact inspection: [run 40161268883](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268883) — PASS for archive digests, embedded manifests/metadata, and executable-format inspection; this is not Android runtime evidence.
- E3 acceptance: NOT ACCEPTED. The fixed-weight ledger currently records E3 as 8/8 implementation points but 0/8 verified points pending the required Android execution and full row acceptance.

## E4 — security/resource-bound review

Reviewed canonical source at the exact SHA, including `SECURITY.md`, `docs/SECURITY.md`, `crates/one-core/src/capability.rs`, `crates/one-core/src/adapter.rs`, and `crates/one-core/src/database.rs`.

- Capability model defaults to no granted capabilities and tests explicit denial/isolation for filesystem read/write, database query, network discovery, and network administration.
- Unix filesystem adapter uses descriptor-relative `openat`, `O_NOFOLLOW` on parent components and final target, `O_NONBLOCK` for reads/writes, and rejects non-regular targets. Adapter payloads are capped at 16 MiB.
- Windows adapter rejects reparse points, compares lexical/canonical paths, checks the opened handle, and deletes a newly created file through the handle if verification fails.
- SQLite adapter has read-only opens and query-only mode; limits SQL to 1 MiB, parameters to 256 (1 MiB each / 16 MiB aggregate), 100,000 rows, 16 MiB rendered output, 1 MiB text values, 32 columns, 100,000 VDBE ops, a 2-second progress-handler deadline and 250 ms lock timeout. The exact-SHA focused run [40161268885](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268885) reports success for SQLite SQL/parameter/row/size-bound regression steps and final-symlink rejection.
- Broader regression/security tests and source contracts exist, but this session did not execute a dedicated exhaustive adversarial race/mount-boundary suite on every OS. No claim of a complete sandbox is made.
- Explicit residual risks: no runtime-wide memory/open-resource quota policy; adapter capability scope is not automatically a project-root sandbox; non-Unix/non-Windows targets use standard-library fallback; project-root confinement is only a capability-policy boundary where configured and does not control host mounts; Windows TOCTOU and Unix race resistance need adversarial coverage across all required targets.
- E4 acceptance: NOT ACCEPTED. The fixed-weight ledger records 5/6 implementation points and 0/6 verified points pending full threat-review/regression evidence and disposition of the residual risks against mandatory release criteria.

## Current fixed-weight gate and Git state

- [Ledger gate run 40161268817](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40161268817) — NOT PASSED. Its log reports 91/100 provisional implementation, 64/100 verified, nine unchecked Definition-of-Done items, and E1/E2/E3/E4/E6 rows not fully accepted. It also observed some exact-SHA jobs still running at gate evaluation time; later results above are separately linked and do not retroactively change that run.
- Canonical PR #80 remains open, draft and unmerged. Canonical source SHA remains `56606c7f8076bc9a67e321835077315d321b8b7a`. No merge or release was performed.
- No canonical source code was changed in this Prompt 3 session; no percentage or ledger weights were promoted.
- Next for Prompt 4: obtain a runner/device that can actually boot Android API 35 arm64-v8a and execute the produced ELF; run the full adversarial security/resource-bound matrix across supported OS targets; fix any demonstrated source defects; then rerun exact-SHA CI and update the canonical ledger/checkpoint only after evidence supports the result.

## Gate

**NOT PASSED — Prompt 3/4 is not complete.** Linux and Windows job matrices pass for the exact source SHA, but required Android ELF runtime evidence is missing and E4's full acceptance criteria have not been proven. This checkpoint intentionally does not claim milestone completion.


## E3/E4 continuation update — 2026-10-26, source SHA 68883f000caa7143ee93886753b9a7bf3ce9a448

- Canonical candidate pin is `68883f000caa7143ee93886753b9a7bf3ce9a448`; the source branch HEAD matched this pin when checked.
- Linux distro run [40261837590](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837590) passed Ubuntu 24.04 and Debian 12; cross-platform run [40261837558](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837558) passed Ubuntu and Windows Server 2025; E4 adversarial run [40261837581](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837581) and SEC-05 run [40261837493](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837493) passed on the prior source pin `c1eff93d2c675dfeaca0c69a60feee82c912b2f6`, so they are **not final-source evidence**.
- API 35 QEMU TCG run [40262251273](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262251273) failed before guest boot. The uploaded emulator log explicitly says: `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host. System image must match the host architecture.` This is an environment/runner architecture incompatibility, not evidence that the candidate binary passes runtime. The test's native ELF execution assertion did not run.
- An ARM64-host workflow already exists at `.github/workflows/android-aarch64-arm-host.yml`, using `ubuntu-24.04-arm` and the API 35 `arm64-v8a` image. Its push trigger is being corrected to run whenever `CANONICAL_COMMIT.txt` changes, so the exact candidate SHA can be tested on a compatible host rather than retrying the same impossible x86_64-host/arm64-guest configuration.
- Fixed-weight ledger gate [40261837548](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837548) failed because `CANONICAL_READ_TOKEN` does not have Actions: read access to the private canonical repository; the API fallback returned 404. Keep the gate fail-closed. This permission cannot be safely repaired by changing acceptance assertions or claiming the protected release workflow passed.
- The exact-SHA artifact inspection run [40261837655](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837655) and the older-source TCG retry [40261837570](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40261837570) were still running at the last poll; their conclusions must be checked before crediting anything.
- No E3/E4 final acceptance is claimed. The pin update must trigger a fresh Linux/Windows/E4/SEC-05/artifact matrix. API 35 runtime is still open until a real ARM64 execution records SDK 35, ABI `arm64-v8a`, the actual ELF invocation, exit code 0, and `ONE_NATIVE_BACKEND_OK`.
