# Project ONE independent Windows exact-SHA verification


## Current exact-SHA Windows verification — PENDING — 2026-11-17

- Canonical ONE source pin: `a10a69afdf8675e703f38f1620abc935d8361897`, PR #102 branch `fix/commit-cargo-lockfile-20261117`.
- This source SHA includes the tracked generated `Cargo.lock` and the `.gitignore` change that stops ignoring it. GitHub Actions `One CI` reports Linux and Windows SUCCESS on this exact source SHA: run [#43998641019](https://github.com/panglimanetizen01/one/actions/runs/43998641019).
- The independent Windows native runtime gate is now isolated to the verifier's `WINDOWS_SOURCE_COMMIT.txt` pin and is running as workflow run [#32](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43999096244), verifier commit `566a2edf7a30638d99a146e283c294b6bf707f2e`.
- Do not claim Windows native artifact PASS until run #32 completes, the PE32+ artifact is inspected, runtime output is `Budi`, and the exact-SHA manifest/checksum is verified.
- Previous run #31 for source `e50748a...` was blocked before compilation by missing Cargo.lock; it remains historical failure evidence and is superseded by this new candidate, not relabeled.
- PR #42 remains OPEN / DRAFT / UNMERGED. No merge or release is authorized.

