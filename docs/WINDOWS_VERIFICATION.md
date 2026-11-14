# Independent Windows exact-SHA verification

## Canonical source identity

- Source repository: `panglimanetizen01/one` (private).
- Source pin file: `WINDOWS_SOURCE_COMMIT.txt`.
- Current candidate: `195755054bb733f44ff30acf8d3281b4efc820bf`.
- Source branch context: Project ONE PR #95, `ci/circleci-migration-20261113`.
- Verifier workflow: `.github/workflows/windows-native-backend-runtime.yml`.
- Host: GitHub-hosted Windows Server 2025, AMD64.

The workflow reads a full 40-character hexadecimal commit from the pin file, checks out that exact commit from the private canonical repository with the repository-scoped `CANONICAL_READ_TOKEN` secret, and compares the checked-out `git rev-parse HEAD` with the pin before running any product command. The workflow separately records its own verifier SHA. The verifier pin is not itself execution evidence.

## Required Windows checks

1. Validate canonical contract artifacts and user documentation.
2. Provision stable Rust, MinGW-w64 Clang/linker, and Android NDK r27c.
3. Build all workspace targets.
4. Run Clippy with warnings denied.
5. Run the complete workspace test suite.
6. Run deterministic `.oneir`/`.onepkg`, DNS, orchestration, database, HTTP GET, and HTTP GET CLI checks.
7. Run real-network tests and the Windows offline verification script.
8. Build the Windows GNU native artifact from `examples/hello.one`.
9. Inspect MZ header, PE signature, AMD64 machine value `0x8664`, and PE32+ optional-header magic `0x20B`.
10. Execute the produced Windows artifact and require the expected `Budi` output.
11. Confirm the source checkout is still at the pinned SHA and tracked source files remain unchanged.

The current source tree does not commit `Cargo.lock`; therefore this workflow intentionally does not use Cargo's `--locked` flag. It uses the same stable toolchain channel declared by the source repository's `rust-toolchain.toml`.

## Evidence artifact

The workflow uploads:

- `one-windows-native.exe`
- `one-windows-native-runtime-manifest.txt`

The manifest records the canonical source SHA, verifier SHA, workflow run ID/attempt, job status, Windows host/architecture, Rust/Cargo/Clang versions, target triple, binary SHA-256, and native runtime result.

A candidate may be called Windows-verified only when:
- the workflow run is terminal SUCCESS on the exact source SHA;
- the native build, PE32+ inspection, and execution steps succeeded;
- the manifest records the same source SHA and verifier SHA as the workflow;
- the downloaded artifact hash matches the manifest.

A configured workflow, a queued run, a successful Linux job, or an older source SHA is not a Windows PASS.

## Current candidate state — 2026-11-14

The workflow branch is `verify/windows-pr95-20261114`. The source pin currently points to `195755054bb733f44ff30acf8d3281b4efc820bf`. The PR and workflow execution are pending; no Windows PASS is claimed yet. The shared `CANONICAL_COMMIT.txt` used by older independent verification workflows is deliberately left unchanged.
