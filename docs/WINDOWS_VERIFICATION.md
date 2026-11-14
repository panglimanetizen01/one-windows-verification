# Project ONE independent Windows exact-SHA verification

## Ownership and provider boundary

- Canonical source repository: `panglimanetizen01/one` (private).
- Canonical product CI: CircleCI, Linux host only, configured by `.circleci/config.yml`.
- Independent Windows host verification: `panglimanetizen01/one-windows-verification`.
- Workflow: `.github/workflows/windows-native-backend-runtime.yml`.
- Host: GitHub-hosted Windows Server 2025 AMD64.
- Review PRs: Project ONE PR #95 and verifier PR #42; both remain open, draft, and unmerged.

The Windows workflow is not a CircleCI job. The canonical CircleCI configuration retains Linux product/release jobs only. Linux-host MinGW-w64 is retained for Windows-target cross-compilation regression coverage; it is not Windows-host evidence.

## Canonical source identity

The workflow reads `WINDOWS_SOURCE_COMMIT.txt`, requires exactly 40 lowercase hexadecimal characters, checks out the private canonical repository at that exact commit using the repository-scoped `CANONICAL_READ_TOKEN` secret, and asserts:

- `git -C source rev-parse HEAD` equals the explicit source pin;
- the verifier checkout's `git rev-parse HEAD` equals the workflow's own `github.sha`.

The manifest records `source_sha` and `verifier_sha` independently. The source pin is a target pointer, not execution evidence.

### Validated source snapshot

- Source repository: `panglimanetizen01/one`.
- Source branch at verification time: `ci/circleci-migration-20261113`.
- Exact source pin: `f85375e279257dcbb7d4ded9632800fcd1b78cc9`.
- Verifier commit used by the successful run: `e765113b66eca514aa4759ddcc7215fc09254554`.

The canonical PR #95 branch subsequently advanced to `5d50f42d76a071800dd84ee5faa8b216335c1ced`. A GitHub compare of `f85375e...` to `5d50f42...` shows one documentation-only commit affecting `CHANGELOG.md`, `docs/CI.md`, and `docs/verification/*`; no product source, tests, or CI configuration changed. The successful Windows result remains bound to the exact `f85375e...` snapshot and is not represented as a run on `5d50f42...`.

## Windows verification contract

The workflow performs the following checks on the exact pinned source:

1. Validate canonical source contracts and user documentation.
2. Provision stable Rust, MinGW-w64 Clang/linker, and pinned Android NDK r27c.
3. Build all workspace targets.
4. Run Clippy with warnings denied.
5. Run the complete workspace test suite.
6. Verify deterministic `.oneir`/`.onepkg` artifacts.
7. Run DNS, orchestration, database, HTTP GET, HTTP GET CLI, real-network, and offline verification checks.
8. Build the Windows GNU native artifact from `examples/hello.one`.
9. Inspect DOS MZ, PE signature, AMD64 machine field `0x8664`, and PE32+ optional-header magic `0x20B`.
10. Execute the Windows artifact and require successful exit plus the expected `Budi` output.
11. Confirm the source checkout remains at the pinned SHA and tracked source files/index remain unchanged.

The workflow intentionally does not use Cargo's `--locked` flag while the canonical repository does not commit `Cargo.lock`.

## Successful exact-SHA evidence — run #12

Windows run [#12](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43593490063) completed terminal **SUCCESS**:

- Run ID: `43593490063`.
- Verifier SHA: `e765113b66eca514aa4759ddcc7215fc09254554`.
- Job ID: `132442986608`.
- Canonical source SHA: `f85375e279257dcbb7d4ded9632800fcd1b78cc9`.
- Host: Windows Server 2025 / AMD64.
- Manifest: `job_status=success`, target `x86_64-pc-windows-gnu`, native exit code `0`, output `Budi`.
- Artifact ID: `14113646474`.
- ZIP size: `15866` bytes; ZIP SHA-256: `551df64ac4ee00f1a2a7c9a65140b091cc956a2024d5ff23e12112cc3ade9201`.
- Manifest SHA-256: `bfed07d536ce7d95a9b09140075c954877411922d5e85e12d79a69fd3f1dd638`.
- Executable SHA-256: `ceaa2996f70a03cb69fb08b4b4d4edf63a2db453e5c13cfc7e356235fbb04e81`.

The downloaded ZIP digest was independently recomputed and matched. The embedded manifest and executable hashes were independently checked. The 52,918-byte executable passed MZ, PE, AMD64 `0x8664`, and PE32+ `0x20B` inspection. The manifest records both exact source and verifier identities.

## Separate Linux CircleCI status — NOT PASS

CircleCI is not expected to run Windows after this split. For the exact Windows-tested source SHA `f85375e...`, CircleCI `ci/circleci: one-linux` reports FAILURE (workflow `1bc98a22-c403-4ba6-98dd-9143463a52b7`, job `588e3ce3-acc7-44cb-b453-c1d3787e03be`, failure report `53d7d9f0-a113-4728-8cf0-2a4729ae91dc`).

The current PR #95 head `5d50f42...` also reports `ci/circleci: one-linux` FAILURE (workflow `d98d94fa-cb59-4487-84e9-582d889f6143`, job `b4427cc0-8253-4d95-8b5d-51f2f2778ca6`, failure report `aebbf019-e2c7-4c61-b0ce-e63a6b373832`). The current execution session has no authenticated CircleCI connector/CLI/token access, so the first failed step and root cause cannot be retrieved here. Do not infer a product-code defect or claim Linux PASS.

Result: Windows is PASS for canonical source SHA `f85375e...` only. Overall cross-platform verification is **NOT PASS** while CircleCI Linux is failed.

## Acceptance and safety rules

A Windows PASS requires all of the following:

- terminal workflow SUCCESS for the exact canonical source SHA;
- successful source and verifier identity assertions;
- successful contract, build, Clippy, workspace tests, real-network/offline checks;
- successful Windows native build, PE32+ AMD64 inspection, and execution;
- manifest source/verifier identities matching the workflow;
- independently matching downloaded executable SHA-256.

A workflow definition, pin file, queued run, successful Linux CircleCI job, or older source SHA is not a Windows PASS. Evidence never transfers automatically between commits.

No merge, force-push, release, default-branch update, repository visibility change, or deletion of evidence is authorized by this verification record.
