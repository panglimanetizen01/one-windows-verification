# Candidate build matrix — non-acceptance evidence

`CANDIDATE_BUILD_COMMIT.txt` pins the current ONE PR #108 CircleCI migration candidate for a dedicated Linux/Windows `cargo test --locked -p one-core` matrix. This pin is intentionally independent from both `CANONICAL_COMMIT.txt` (E4 security acceptance) and `LEDGER_SOURCE_COMMIT.txt` (fixed-weight ledger/DoD documentation). The build matrix establishes a repeatable compile/test route and provides detailed logs; it does not award fixed-weight points, satisfy E1–E6, or authorize a release. Advance only this build pin when the PR #108 source candidate advances; do not change the E4 pin until the required security implementation and adversarial test inventory are committed.

## Rust toolchain identity

The source repository pins Rust `1.100.0` in `rust-toolchain.toml`. Both Linux and Windows matrix jobs explicitly install the same exact toolchain release. A toolchain or source-pin change requires a new exact-SHA matrix run; prior results are not transferable.

## Native backend toolchain prerequisites

The full `one-core` suite includes a contract test that builds a Windows GNU artifact from both Linux and Windows hosts. The Linux runner installs `clang`, `lld`, and `mingw-w64`, then sets `ONE_WINDOWS_CLANG=clang`. The Windows runner uses the pinned `msys2/setup-msys2` action and installs `mingw-w64-x86_64-clang` plus `mingw-w64-x86_64-lld`, then sets the same override. These are test-host prerequisites, not changes to ONE target semantics or security acceptance.

## 2026-11-18 candidate update

The candidate pin now follows PR #108's exact source SHA after the Rust 1.100.0 reproducibility change. This remains a non-acceptance build/test matrix; the E4 canonical acceptance pin is unchanged.
