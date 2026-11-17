# Project ONE independent Windows exact-SHA verification


## Current exact-SHA Windows verification — BLOCKED BY MISSING LOCKFILE — 2026-11-17

- Canonical ONE source pin: `e50748a1b25922d9090eba1f5fb90548d7c7d003`, PR #95 branch `ci/circleci-migration-20261113`.
- CircleCI Linux on this exact source SHA reports SUCCESS; workflow `dc6f3660-328f-4016-8c01-72c3565d0321`, job `64a34e41-9759-4a5c-8e50-b77296730a54`.
- Windows native runtime run #31: [workflow run](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43998206222), verifier commit `9cf1bb3071c56497118ad9c9e532abfee3fd60ee`.
- Source checkout and exact SHA verification succeeded. Rust toolchain, MinGW install/compiler probe, and Windows Server 2025 host checks succeeded.
- Build failed before compilation because the source repository has no tracked `Cargo.lock`, while the verifier invokes Cargo with `--locked`: `cannot create the lock file .../Cargo.lock because --locked was passed to prevent this`.
- PE inspection, runtime execution, and manifest verification were skipped. This is **not a Windows product build PASS** and is not evidence of a compiler/runtime defect.
- ONE PR #102 proposes removing `Cargo.lock` from `.gitignore` and committing the generated lockfile (SHA-256 `c4f2c3c9607bb9b09bf6f7f0ea176972c2413fb226adee582d3e3150c5ca71b5`). After that change is merged/activated, advance the verifier pin to the resulting exact ONE SHA and rerun the Windows gate.
- Previous Windows run [#28](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43865524749) remains PASS for source SHA `07d8cbf7422b8340f8efda3c2f9d4425f85b7537` only; it is historical evidence, not a pass for `e50748a...`.
- Verifier PR #42 remains OPEN / DRAFT / UNMERGED. No merge or release is authorized.

