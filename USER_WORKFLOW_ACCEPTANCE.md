# ONE v0.1 — User Workflow Acceptance Review

**Reviewed documentation/code baseline:** source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`  
**Current source candidate:** `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` (documentation and ledger reconciliation since reviewed baseline; exact-SHA rerun pending)  
**Review status:** Manual review complete; final-SHA executable acceptance pending  
**Evidence:** [candidate verification index](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/CANDIDATE_VERIFICATION.md), [cross-platform run 40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236), [focused run 40084595238](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595238), [distro run 40084595259](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595259)

## User workflow reviewed

1. **Create → check → run:** documented CLI names and aliases match the CLI contract; beginner guide correctly states that source syntax is grammar-governed, not arbitrary natural-language execution.
2. **Test → build → package:** docs accurately distinguish local project/conformance testing, deterministic `.oneir` intermediate artifacts, and deterministic `.onepkg` packages from native executables or signed release packages.
3. **Filesystem read/write:** commands require explicit capability and exact target; write remains experimental and docs explicitly state that `--root` is not a complete sandbox.
4. **SQLite query:** documentation now states the tested boundary accurately: explicit `database.query`, resource-scoped target, parameterized read-only `SELECT`, normalized output, bounded resources, and no claim of complete persistence APIs.
5. **HTTP GET:** documentation now states the tested boundary accurately: explicit `network.connect`, exact `http://` URL, HTTP/1.1 GET, bounded/normalized response body; no claim of HTTPS or a general API client.
6. **Package provenance:** user docs correctly warn that `one package` does not sign automatically, that trust material must be provisioned independently, and that the protected release workflow must exist on the default branch before dispatch.
7. **Evidence vocabulary:** docs distinguish experimental, in-development, supported, and historical exact-SHA evidence; a later documentation commit must be retested before current-head claims.

## Corrections made

- Reconciled stale filesystem-write verification wording in `docs/panduan-pengguna/perintah-cli.md` with the exact-SHA Ubuntu/Windows evidence.
- Changed SQLite and HTTP user-facing status from “not executable-verified” to “experimental with exact-SHA cross-platform test evidence,” while preserving their narrow scope limits.
- Replaced stale claims that database/HTTP evidence existed only on Termux with explicit run links for `database_vertical_slice`, `database_orchestration`, `http_get_vertical_slice`, and `http_get_orchestration`.
- Corrected the verification-boundary paragraph to label run `40084595236` as evidence for SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, not the later documentation-only candidate.

## Test evidence and limits

At the reviewed baseline SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, the cross-platform workflow passed CLI smoke tests, contract and user-doc consistency checks, workspace tests, real-network tests, offline verification, and release-bundle generation on Ubuntu and Windows Server 2025. Focused stdlib/SQLite/provenance tests and Ubuntu/Debian distro tests also passed on that SHA.

The current source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` contains documentation and ledger reconciliation since that tested baseline, but exact-SHA policy still requires the cross-platform, focused, distro, and lockfile workflows to rerun before final acceptance.

## Decision

**Manual user-workflow review: PASS. E5 implementation is recorded as 4/4; final E5 verified credit remains 0/4 pending exact-SHA rerun and ledger acceptance.** This review does not close E1, E2, E3 Android runtime, E4 security/root confinement, or E6 forensic audit.
