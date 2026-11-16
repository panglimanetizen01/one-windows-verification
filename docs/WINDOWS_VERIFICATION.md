# Project ONE independent Windows exact-SHA verification


## Current exact-SHA candidate — 2026-11-16

The verifier pin has been advanced to the current canonical Project ONE PR #95 head:

- Canonical source: `panglimanetizen01/one`.
- Canonical branch: `ci/circleci-migration-20261113`.
- Canonical PR: [#95](https://github.com/panglimanetizen01/one/pull/95).
- Exact source SHA: `e92d3a3003b68283d5f0fe1315dcb41dcc33bd62`.
- Pin file: `WINDOWS_SOURCE_COMMIT.txt`.

Earlier successful Windows runs on `f85375e279257dcbb7d4ded9632800fcd1b78cc9` remain valid only for that older source snapshot. They must not be carried forward as evidence for the current candidate. The current candidate is **PENDING** until a terminal Windows workflow SUCCESS is accompanied by a manifest that records this exact source SHA and the verifier SHA, and the native artifact evidence is inspected.


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
- Verifier commit used by run #12: `e765113b66eca514aa4759ddcc7215fc09254554`.
- Verifier PR branch head for run #15: `f0ad340e97f3b66319ba4331636a205747ba523e`; run #15's manifest records the GitHub pull-request merge ref `81f5d38a098614f77475951aec6454865238d11b` as the verifier SHA.

The canonical PR #95 branch subsequently advanced to `5d50f42d76a071800dd84ee5faa8b216335c1ced`. A GitHub compare of `f85375e...` to `5d50f42...` shows one documentation-only commit affecting eight documentation paths: `CHANGELOG.md`, `docs/CI.md`, and six files under `docs/verification/`. No product source, tests, or CI configuration changed. The successful Windows results remain bound to the exact `f85375e...` snapshot and are not represented as runs on `5d50f42...`.

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

## Latest successful exact-SHA evidence — run #17

Windows run [#17](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43665622971) completed terminal **SUCCESS**:

- Run ID: `43665622971`; attempt: `1`.
- Verifier branch HEAD at trigger: `e9bc77696b1d48902de7947c61eb532eb9287fe0`.
- Verifier SHA asserted and recorded in the manifest: `c07114c5ff1ea04fbce0767301650515c9d0fde8` (GitHub pull-request merge-ref checkout).
- Job ID: `132665370187`.
- Canonical source SHA: `f85375e279257dcbb7d4ded9632800fcd1b78cc9`.
- Host: Windows Server 2025 / AMD64 (`Microsoft Windows NT 10.0.26100.0`).
- All 28 substantive steps succeeded, including exact source/verifier identity checks, contract/document checks, workspace build, Clippy with warnings denied, complete workspace tests, deterministic artifacts, DNS/orchestration/database/HTTP, real-network/offline checks, Windows native build, PE32+ AMD64 inspection, execution, manifest creation, and artifact upload.
- Manifest: `job_status=success`, target `x86_64-pc-windows-gnu`, native exit code `0`, output `Budi`.
- Executable: `examples/one-windows-native.exe`, 52,918 bytes, SHA-256 `70f9a08505d456c24119e3e24379e960c49c704799bb8aebc33836e6ffa0c3e0`.
- Artifact ID: `14142430864`; ZIP size: 15,865 bytes; ZIP SHA-256: `5a44e5e857ae899977e8f80d6196cb15f4f1315dcf257a8cf6d1070c329fa944`.
- The artifact ZIP was downloaded. Its SHA-256 was independently recomputed and matched GitHub's digest. The embedded manifest was read back, the executable hash was independently recomputed and matched the manifest, and the executable was identified as PE32+ x86-64.

## Latest successful exact-SHA evidence — run #15

Windows run [#15](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43595298718) completed terminal **SUCCESS**:

- Run ID: `43595298718`; attempt: `1`.
- Verifier PR branch head: `f0ad340e97f3b66319ba4331636a205747ba523e`.
- Verifier SHA asserted and recorded in the manifest: `81f5d38a098614f77475951aec6454865238d11b` (GitHub pull-request merge ref).
- Job ID: `132449491722`.
- Canonical source SHA: `f85375e279257dcbb7d4ded9632800fcd1b78cc9`.
- Host: Windows Server 2025 / AMD64 (`Microsoft Windows NT 10.0.26100.0`).
- All substantive steps succeeded, including source/verifier identity checks, contract/document checks, workspace build, Clippy, complete workspace tests, deterministic artifacts, DNS/orchestration/database/HTTP, real-network/offline checks, Windows native build, PE32+ AMD64 inspection, execution, manifest creation, and artifact upload.
- Manifest: `job_status=success`, target `x86_64-pc-windows-gnu`, native exit code `0`, output `Budi`.
- Executable: `examples/one-windows-native.exe`, 52,918 bytes, SHA-256 `2af866c764c9effb9f4a8aca8c3e8eac4750e908eeddfebbbe3280ed126cb23f`.
- Artifact ID: `14114262180`; ZIP size: 15,870 bytes; ZIP SHA-256: `9d4d3f31f635a260ac4143351ee0b996cb81863fe1e5d8e0f47efb129e6459f1`.
- The artifact ZIP was downloaded. Its SHA-256 was independently recomputed and matched GitHub's digest. The embedded manifest was read back, the executable hash was independently recomputed, and the executable was identified as PE32+ x86-64.

## Earlier successful exact-SHA evidence — run #12

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


### Latest successful exact-SHA evidence — run #19

- Canonical source SHA: `f85375e279257dcbb7d4ded9632800fcd1b78cc9` (the exact pin in `WINDOWS_SOURCE_COMMIT.txt`).
- Verifier branch HEAD at trigger: `89700258033c16bf6bad7ef983b0f442703d5a4c`.
- Verifier SHA recorded in the run manifest: `40b7087bbd30dbf9c30cfec2c1d4af94e2796505` (GitHub pull-request merge-ref checkout).
- Windows run [#19](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43666673348): terminal **SUCCESS**; job `132668616929`; Windows Server 2025 / AMD64.
- All 28 substantive workflow steps succeeded, including exact source/verifier identity, toolchain setup (Rust 1.100.0, Clang 20.1.8, Android NDK r27c), contract/document checks, workspace build, Clippy with warnings denied, full workspace tests, deterministic artifacts, DNS/orchestration/database/HTTP, real-network/offline checks, Windows native build, PE32+ AMD64 inspection, native execution, manifest, and artifact upload.
- Manifest: `job_status=success`, target `x86_64-pc-windows-gnu`, native exit code `0`, output `Budi`; executable SHA-256 `ef996ba9a1229afca36fcf9767042a1eb0032fc44b279588dfb5de59d74e3d34`.
- Artifact ID `14142329450`; ZIP size 15,868 bytes; ZIP SHA-256 `1c51ca84a1396d25585d30a65295821ce5c8ac545cf8e29787e16bae64f53a0e`. The downloaded ZIP was independently hashed and matched GitHub's digest; the embedded manifest and executable were inspected, the executable hash independently recomputed and matched the manifest, and the binary was identified as PE32+ x86-64.
- This Windows PASS applies only to canonical source SHA `f85375e...`; it does not transfer to PR #95's later documentation-only HEAD `5d50f42...`.
- CircleCI `ci/circleci: one-linux` on current PR #95 HEAD `5d50f42...` remains **FAILURE** (workflow `d98d94fa-cb59-4487-84e9-582d889f6143`, job `b4427cc0-8253-4d95-8b5d-51f2f2778ca6`). Its first failing step/root cause is still unknown in this session. **No Linux PASS or overall cross-platform PASS is claimed.**
