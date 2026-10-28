# Exact-SHA revalidation note — 2026-10-28

## Scope and identity

- Canonical Project ONE source SHA tested by the verifier workflow: `f21e8d178f72c6f9c76b4027d5ff85742dbe672e`.
- Temporary verifier PR: [#38](https://github.com/panglimanetizen01/one-windows-verification/pull/38).
- Verifier PR head SHA: `376083d7b343dc81c5db49ef3f70050d558fcc03`. This is **not** the source SHA. The workflow reads `CANONICAL_COMMIT.txt`, checks out the canonical source separately, and its source-SHA verification step passed on both OS jobs.
- The PR changes only trailing whitespace in the verifier's canonical pin file. No Project ONE source code was changed.
- This note records workflow-scoped evidence only; it does not itself close any E1–E6 acceptance row or authorize merge/release.

## Completed exact-source workflow evidence

### Cross-platform verification

[Run 40736440093](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736440093) — **SUCCESS**.

Both jobs passed:
- Ubuntu: canonical SHA check, contract checks, scanner tests, CI collector tests, quality-ledger tests, debug and release builds, normative source scan, AST contract tests, Clippy, workspace tests, real-network tests, offline verification, and Linux candidate bundle checksum/provenance checks.
- Windows 2025: canonical SHA check, contract checks, scanner tests, CI collector tests, quality-ledger tests, debug and release builds, normative source scan, AST contract tests, Clippy, Windows workspace tests, real-network tests, offline verification, and Windows candidate bundle checksum/provenance checks.

Artifacts reported for this run:
- Linux health report, artifact ID `12838140706`, SHA-256 `c8e1187874e977d8a0450e40f1c201238bf25e087d30d87ccefe73d503fe95f0`.
- Windows health report, artifact ID `12838305654`, SHA-256 `999ec7eaf7d27ca0009f12720c2d1cbb4c86aabb30ebea0593e475af532860b8`.
- Linux release-candidate bundle, artifact ID `12838260655`, SHA-256 `fa305b82946142d00aab5d29f4cf33fe79f7c22b9216fc360fdc51b1f7d10844`.
- Windows release-candidate bundle, artifact ID `12838191080`, SHA-256 `0fd6c36797d79f86ddd2ad8b540e015eee85562b5d3c6085be45a71b0ff43439`.

These are unsigned verification artifacts, not a protected production provenance release.

### Additional completed workflow scopes

- [Linux distro verification — run 40736439935](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736439935): **SUCCESS** for Ubuntu 24.04 and Debian 12 jobs; contract checks, build, Clippy, workspace tests, and real-network tests passed.
- [E4 subprocess resource guard — run 40736439985](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736439985): **SUCCESS** for its defined scope.
- [E4 adversarial filesystem/resource regression — run 40736440154](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736440154): **SUCCESS** for its defined scope.
- [E4 SEC-05 subprocess timeout/output-limit — run 40736439955](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736439955): **SUCCESS** for its defined scope.
- [Android AArch64 runtime — run 40736440037](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736440037): at last observation, the exact-source ELF build and Android backend contract tests passed, but boot/runtime execution was still **IN PROGRESS**. Do not claim runtime acceptance until the run concludes successfully and evidence is uploaded.

## Gate remains NOT PASSED

The [fixed-weight ledger gate — run 40735752869](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40735752869) failed. Its captured log reported 10 unchecked Definition-of-Done items, full-row acceptance still unrecorded for E1–E6, several required runs still pending at the time of evaluation, and no protected `ONE Package Provenance Release` for this exact source SHA. The gate result is a real acceptance failure, not a runner-start failure.

The newly completed PR-triggered runs above improve exact-SHA evidence for their tested scopes, but do not automatically reconcile the fixed-weight ledger, check Definition-of-Done items, close whole E1–E6 rows, or satisfy E2 protected production provenance. A new gate evaluation should occur only after the ledger and DoD are reconciled against verified evidence. No merge, release, protection bypass, or protected E2 dispatch is authorized by this note.


## Follow-up check — 2026-10-29

- [ONE E1 Standard Library Windows Acceptance — run 40735752836](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40735752836): **SUCCESS** for its defined Windows acceptance scope.
- [ONE Milestone 1 E1 Cross-Platform Acceptance Lab — run 40735752814](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40735752814): **SUCCESS** for its defined cross-platform lab scope.
- [Fixed-weight ledger gate — run 40735752869](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40735752869), attempt 3: **FAILURE**. Its latest captured evaluation still found 10 unchecked DoD items and no protected production provenance release for the exact source SHA. It is not a passing acceptance gate.
- [Android AArch64 runtime — run 40736440037](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40736440037): still **IN PROGRESS** at the latest check; exact-source ELF build passed, but API 35 ARM64 boot/runtime step had not concluded. No runtime pass is claimed.

These E1 workflow successes are evidence for their defined scopes only. They do not justify checking an entire fixed-weight row without matching row-level criteria, and they do not change the E2 provenance requirement. Keep the overall gate **NOT PASSED** until each DoD item and ledger row is reconciled with exact-SHA evidence.
