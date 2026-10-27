# Current exact-SHA acceptance evidence

Canonical ONE source SHA under verification: `0d0202a1405ae12aaaadf05c6916bacc70316126`.

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

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841) — one platform passed; the other was still running at last check.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726) — still running at last check.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072667) — still running at last check.
- [Android API 35 AArch64 runtime, community fallback](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072659) and [native ARM64 host](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072760) — runtime acceptance not yet concluded.
- [Protected ONE package provenance release](https://github.com/panglimanetizen01/one/actions/runs/40467992667) — failed before runner allocation (runner ID 0, no steps); a rerun was requested but again failed before any steps. This is an infrastructure/runner failure, not a proven source test failure, and production trusted-publisher acceptance remains unproven.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072703) — failed closed; implementation 92/100, verified 78/100; E1 0/10, E2 0/8, E6 0/4; seven Definition of Done items remain unchecked.

The previous cumulative evidence notes are preserved in `CANDIDATE_VERIFICATION_ARCHIVE_20261027.md`. No score, fixed weight, or Definition of Done checkbox is altered by this index update.
