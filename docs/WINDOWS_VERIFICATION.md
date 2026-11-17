# Project ONE independent Windows exact-SHA verification


## Current exact-SHA Windows verification — PASS — 2026-11-17

**PASS** Exact source checkout, Windows native build, PE inspection, runtime execution, and evidence upload all succeeded.

- Canonical ONE source SHA: `a10a69afdf8675e703f38f1620abc935d8361897` (PR #102 lockfile candidate).
- Verifier workflow run #32: [Windows native runtime — Windows Server 2025](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43999096244).
- Verifier commit: `566a2edf7a30638d99a146e283c294b6bf707f2e`; job ID: `133758391930`.
- Exact source SHA assertion passed; Rust toolchain and MinGW clang/linker setup passed.
- Native Windows artifact built successfully and inspected as PE32+ AMD64.
- Runtime exit code: `0`; output: `Budi`.
- Executable SHA-256: `6ee176da3d9989a58c7dc1cb6280ee65c6973c858d266e298bbb42e87e9961be`.
- Uploaded artifact ID: `14290758793`; artifact ZIP SHA-256: `2fdc0f4ca7f76946cf71025608350f5cd7c38f02ccf97facd25d7f88fae83bc6`; size: 15,775 bytes.
- The artifact is retained by GitHub Actions until 2027-02-15.

The earlier run #31 on source SHA `e50748a...` remains a blocked attempt caused by the absent Cargo.lock. It is not relabeled; run #32 is the successful follow-up on the lockfile-bearing source SHA `a10a69...`.

Verifier PR #42 remains OPEN / DRAFT / UNMERGED. No merge or release is authorized.

