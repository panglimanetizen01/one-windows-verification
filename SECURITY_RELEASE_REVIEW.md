# ONE v0.1 — Focused Security Release Review

**Reviewed code SHA:** `11d53e8558a948b9607b5d70ab84d1ddcc0e29cd`  
**Current candidate SHA:** `9d5d319b88cbee17b18554cfe7641ec1008ba62a` (ledger/checkpoint arithmetic reconciliation; code under review unchanged)  
**Review date:** 2026-10-24  
**Status:** Findings documented; security acceptance remains OPEN  
**Normative context:** [SECURITY.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/SECURITY.md), [effect/capability contract](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/spec/one-v0.1-effect-capability.md), [Definition of Done](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/DEFINITION_OF_DONE.md)

This is a focused source review, not a claim of a complete sandbox or a third-party penetration test. It records both implemented controls and residual risks that affect release acceptance.

## Scope inspected

- `crates/one-core/src/governance.rs`: capability grants, denials, approval, target/root/resource scope decisions.
- `crates/one-core/src/adapter.rs`: Unix descriptor-relative `openat`/no-follow reads and writes; Windows canonical path, reparse-point, and final-handle checks; fallback behavior on other targets.
- `crates/one-core/src/database.rs`: read-only SQLite connection flags, `query_only`, SQL/parameter/result bounds, SQLite VM limit, deadline, and output serialization.
- `crates/one-core/src/interop.rs` and `network_runtime.rs`: process/network host-effect boundaries and explicit target handling.
- `docs/SECURITY.md` and `docs/spec/one-v0.1-effect-capability.md`: declared threat model and stated limitations.

## Controls confirmed in source

- Default policy starts without ambient capabilities; grants require matching capability and an allowed typed scope.
- Unix filesystem adapter opens each path component relative to an open directory descriptor with `O_NOFOLLOW`; final read/write targets must be regular files. Read/write payloads are capped at 16 MiB.
- Windows file paths are compared against canonical paths, reparse points are rejected, and the final opened handle path is checked. Creation that fails final-handle validation attempts handle-based deletion.
- SQLite file-backed access uses read-only flags plus `query_only`; query, parameter, column, row, output, SQLite VM-opcode, and execution-time budgets are applied.
- The candidate adds `SQLITE_OPEN_NOFOLLOW` and the focused Unix regression `sqlite_read_only_open_rejects_symlink_even_if_precheck_races), which passed in [focused exact-SHA run 40083996493](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083996493).
- The source explicitly documents that these controls do not constitute a complete OS sandbox.

## Findings and acceptance disposition

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| SEC-01 | High if hostile concurrent local filesystem mutation is in scope | SQLite still validates parent path components before asking SQLite to open the path. `SQLITE_OPEN_NOFOLLOW` blocks a final-component symlink but does not anchor all parent components to a trusted directory descriptor; a parent-component swap/mount scenario is not proven race-resistant. | **Open.** Either implement platform-appropriate anchored opening/VFS semantics and regression tests, or formally narrow the v0.1 threat model and keep root-confinement claims disabled. |
| SEC-02 | High if `--root` is expected to be a hard sandbox | `ScopeRule::Root` enforces lexical path-component containment. Adapter no-follow checks reject symlinks/reparse points, but mount/bind-mount semantics and a configured root-relative descriptor boundary are not fully enforced. | **Open.** Do not describe `--root` as a complete sandbox. Acceptance requires explicit threat-model disposition plus platform-specific tests or a stronger root-anchored implementation. |
| SEC-03 | Medium | Targets on platforms outside Unix and Windows use standard-library filesystem fallback paths without the same no-follow/open-handle guarantees. | **Open.** Treat those platforms as conditional/unsupported for security-sensitive filesystem effects until equivalent tests and guarantees exist. |
| SEC-04 | Medium | Current resource limits are adapter-specific; there is no demonstrated runtime-wide memory, open-resource, process-output, or aggregate concurrency quota contract. | **Open.** Scope the v0.1 guarantee narrowly or implement/test runtime-wide quotas before claiming complete failure/resource recovery. |
| SEC-05 | Medium | Hosted canonical CI has repeatedly failed with `runner_id: 0` and no executable steps. Independent exact-SHA jobs provide executable evidence, but do not repair the canonical hosted-CI infrastructure itself. | **Open infrastructure item.** Keep the distinction explicit; never relabel those canonical runs as passing tests. |

## Verification evidence

- Focused SQLite/stdlib/provenance regression and Clippy: [40084595238](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595238) — PASS on prior code SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; final-candidate rerun is pending.
- Cross-platform Ubuntu/Windows verification: [40083875189](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083875189) — **PASS** on the reviewed source SHA; both jobs passed and produced inspected bundles.
- Ubuntu/Debian distribution verification: [40083875252](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40083875252) — **PASS** on the reviewed source SHA.
- Android AArch64 ELF runtime: [40085406752](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406752) — queued on current candidate with a QEMU wrapper that strips injected `-enable-hvf`; not yet accepted.

## Decision

**Security release acceptance: NOT PASSED.** The final-symlink SQLite hardening is a verified improvement, but it does not close parent-component TOCTOU, mount/root confinement, unsupported-platform fallback, or runtime-wide quota gaps. E4 must remain unverified until these are resolved or formally accepted within an explicitly narrower v0.1 threat model. Do not claim complete sandboxing.


## Exact-SHA continuation evidence — 2026-10-24

The current candidate source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a` passed the independent cross-platform suite [40086990528](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528), Ubuntu/Debian suite [40086990470](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990470), and focused stdlib/SQLite/provenance suite [40086990463](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990463). These runs provide fresh executable evidence for existing security regression tests; they do not resolve SEC-01 through SEC-04. Android [40086990457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990457) remains in emulator boot and has no runtime acceptance yet. Canonical CI remains infrastructure-failed with zero steps; see index for exact run links.

Security acceptance remains **OPEN**. This review does not waive the residual risks or mark E4 verified.
