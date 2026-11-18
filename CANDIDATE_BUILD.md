# Candidate build matrix — non-acceptance evidence

`CANDIDATE_BUILD_COMMIT.txt` pins the current ONE PR #108 CircleCI migration candidate for a dedicated Linux/Windows `cargo test --locked -p one-core` matrix. This pin is intentionally independent from both `CANONICAL_COMMIT.txt` (E4 security acceptance) and `LEDGER_SOURCE_COMMIT.txt` (fixed-weight ledger/DoD documentation). The build matrix establishes a repeatable compile/test route and provides detailed logs; it does not award fixed-weight points, satisfy E1–E6, or authorize a release. Advance only this build pin when the PR #108 source candidate advances; do not change the E4 pin until the required security implementation and adversarial test inventory are committed.

## Rust toolchain identity

The source repository pins Rust `1.100.0` in `rust-toolchain.toml`. Both Linux and Windows matrix jobs explicitly install the same exact toolchain release. A toolchain or source-pin change requires a new exact-SHA matrix run; prior results are not transferable.

## Native backend toolchain prerequisites

The full `one-core` suite includes a contract test that builds a Windows GNU artifact from both Linux and Windows hosts. The Linux runner installs `clang`, `lld`, and `mingw-w64`, then sets `ONE_WINDOWS_CLANG=clang`. The Windows runner uses the pinned `msys2/setup-msys2` action and installs `mingw-w64-x86_64-clang` plus `mingw-w64-x86_64-lld`, then sets the same override. These are test-host prerequisites, not changes to ONE target semantics or security acceptance.

## 2026-11-18 candidate update

The candidate pin now follows PR #108's exact source SHA after the Rust 1.100.0 reproducibility change. This remains a non-acceptance build/test matrix; the E4 canonical acceptance pin is unchanged.


## Exact source pin correction — 2026-11-18

The candidate pin has been advanced from the initial toolchain commit to its immediate fix-up SHA `a20676be53e5f78c465832379d86c3675a2ed7c8`. The fix-up corrects static CircleCI toolchain parsing before acceptance. This new SHA receives its own Linux/Windows run; no result from the previous candidate pin is transferred.


## Reconciliation candidate — 2026-11-18

- Non-acceptance build pin advanced to exact ONE source SHA `e47b3b52eeb7e1b25fc24f741d5bb5cc1b01f24d` on reconciliation branch `reconciliation/pr-110-base-sync-20261118`.
- Verifier commit: `46ba6c5beb028db6c1bec036fcf7f189999a5c74`; the push to `verification` changes `CANDIDATE_BUILD_COMMIT.txt`, which is a configured trigger for `.github/workflows/candidate-build-matrix.yml`.
- Expected jobs: Ubuntu 24.04 and Windows Server 2025, each checking out the exact pinned ONE SHA and running `cargo test --locked -p one-core -- --nocapture`.
- This is baseline compile/test evidence only. It does not run or satisfy E4 adversarial acceptance, does not alter `CANONICAL_COMMIT.txt`, and does not alter the independent ledger source pin.
- At update time, the newly triggered workflow has not yet been observed to completion. Record each job's exact terminal result and logs before claiming parity.
