# Current exact-SHA acceptance evidence

Canonical ONE source SHA under verification: `0d0202a1405ae12aaaadf05c6916bacc70316126`.

## Latest status refresh — 2026-10-27

This status refresh records outcomes observed after the initial pending-state notes above. It does not change ledger weights or award points.

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841): Windows Server 2025 completed successfully, including the E1 regression suite, full workspace tests, Clippy, and repository contract checker. Ubuntu 24.04 was still running its native cross-compiler installation at the latest inspection; the full two-platform run is not complete.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726): **both Windows Server 2025 and Ubuntu completed successfully** for the exact pinned source SHA. Windows and Linux build/release-build, package-bundle integrity, AST contract regression, Clippy, workspace tests, real-network tests, and offline verification passed. This run is complete; it does not substitute for the separate E1, Android runtime, or protected-provenance gates.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072667): **completed successfully**. Exact-SHA Linux and Windows candidate bundle discovery, archive digest validation, embedded manifests/metadata, and executable-format checks passed.
- [Android API 35 community ARM64 runtime](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072659): exact-source AArch64 ELF build and metadata checks passed. The runtime job was still attempting to boot the API 35 arm64-v8a emulator; until it records exit code 0 and exact output `ONE_NATIVE_BACKEND_OK`, this is not runtime acceptance.
- [Android API 35 native ARM64-host attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072760): the ELF build passed, but the runtime job failed before executing the ELF. The emulator never reached `sys.boot_completed=1`; the log reported `Unable to spawn process ... No such file or directory`. This is an emulator/runtime-environment failure, not evidence that the ONE ELF passed or failed execution.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072703): the verifier's tests passed, then the gate correctly failed closed at 78/100 verified and 92/100 implemented. The recorded blockers include E1/E2/E6 incomplete acceptance, seven unchecked DoD items, unfinished exact-SHA jobs, and the failed protected release workflow. The gate result is not a source-test PASS.
- [Canonical repository CI for PR #85](https://github.com/panglimanetizen01/one/actions/runs/40471195625): the retry again failed both Ubuntu and Windows jobs with runner ID 0 and no steps. This is inconclusive infrastructure failure; the new documentation checks have not yet executed on hosted CI.


This index records exact-SHA evidence only. Scoped test success does not automatically award fixed-weight ledger points; E1, E2, and E6 remain open until their full row acceptance criteria and Definition of Done are satisfied.

## Completed PASS evidence for this SHA

- [E4 adversarial filesystem/resource-bound regression](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072725) — Unix and Windows jobs passed.
- [E4 SEC-05 subprocess timeout/output-limit verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072714) — Linux and Windows jobs passed.
- [Focused standard-library/database regression](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072805) — passed.
- [E1 Standard Library Windows Acceptance](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072646) — passed.
- [Cargo lockfile bootstrap](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072775) — passed.
- [Linux distribution verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072895) — Debian 12 and Ubuntu 24.04 passed.
- [Exact-SHA package, deterministic bytes, lock, signature and tamper checks](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072848) — passed using synthetic test trust only.

## Still pending or blocked

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841) — Windows passed; Ubuntu remains in progress at `Install Linux native cross-compilers` on the latest refresh.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726) — **completed PASS** on both Windows Server 2025 and Ubuntu.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072667) — **completed PASS** for exact-SHA Linux/Windows bundles.
- [Android API 35 AArch64 runtime, community fallback](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072659) — **runtime attempt failed at emulator boot before the ONE ELF ran**. The ARM64 hosted runner reports `ONE_KVM_AVAILABLE=false`, while QEMU reports `gic-version=host requires KVM`; the job exited 1 and uploaded diagnostic evidence (artifact `12719193755`). This is a host/emulator acceleration incompatibility, not a program runtime failure and not a PASS. The [native ARM64 host attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072760) remains a separate route to inspect.
- [Protected ONE package provenance release](https://github.com/panglimanetizen01/one/actions/runs/40467992667) — the initial attempt failed before runner allocation and exposed no job logs through the available connector. A fresh job retry was accepted by GitHub at 2026-10-27 and is currently **queued** (job ID `122086729327` at latest status refresh); it has not executed and cannot be counted as PASS. Production trusted-publisher acceptance remains unproven.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072703) — failed closed; implementation 92/100, verified 78/100; E1 0/10, E2 0/8, E6 0/4; seven Definition of Done items remain unchecked.

The previous cumulative evidence notes are preserved in `CANDIDATE_VERIFICATION_ARCHIVE_20261027.md`. No score, fixed weight, or Definition of Done checkbox is altered by this index update.
