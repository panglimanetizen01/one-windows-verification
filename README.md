# Project ONE — Independent Verification Harness

This repository hosts isolated GitHub Actions workflows for independent verification of selected snapshots of the canonical Project ONE source repository.

- Canonical source: `panglimanetizen01/one` (private).
- Canonical product CI: CircleCI, Linux host only.
- Independent Windows host verification: this repository, on GitHub-hosted Windows Server 2025 AMD64.
- GitHub remains the source-control and review host; this repository does not replace the canonical source repository.

## Project ONE Windows host verification

The Windows verification workflow is `.github/workflows/windows-native-backend-runtime.yml`. Its source target is the full commit SHA in `WINDOWS_SOURCE_COMMIT.txt`; it does not follow a branch name.

The workflow:
1. Validates the 40-character source pin.
2. Checks out the private canonical repository at that exact SHA using the repository-scoped `CANONICAL_READ_TOKEN` secret.
3. Asserts both the canonical source SHA and the verifier checkout SHA before running product commands.
4. Runs source contract and user-document checks, Rust build, Clippy, the full workspace test suite, deterministic artifacts, DNS/orchestration/database/HTTP checks, real-network tests, and offline verification.
5. Builds the Windows native backend, inspects the PE32+ AMD64 artifact, executes it, and requires the expected `Budi` output.
6. Writes a manifest with source/verifier identities and the executable SHA-256, then uploads the manifest and binary.

### Demonstrated exact-SHA evidence — run #12

- Canonical source SHA: `f85375e279257dcbb7d4ded9632800fcd1b78cc9`.
- Verifier SHA used by the run: `e765113b66eca514aa4759ddcc7215fc09254554`.
- Windows run [#12](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43593490063): terminal **SUCCESS**; job `132442986608`; Windows Server 2025 / AMD64.
- Manifest: `job_status=success`, target `x86_64-pc-windows-gnu`, native exit code `0`, output `Budi`.
- Artifact ID `14113646474`; ZIP SHA-256 `551df64ac4ee00f1a2a7c9a65140b091cc956a2024d5ff23e12112cc3ade9201`; manifest SHA-256 `bfed07d536ce7d95a9b09140075c954877411922d5e85e12d79a69fd3f1dd638`; executable SHA-256 `ceaa2996f70a03cb69fb08b4b4d4edf63a2db453e5c13cfc7e356235fbb04e81`.
- The downloaded ZIP digest, embedded manifest and executable hashes, MZ/PE signatures, AMD64 machine `0x8664`, and PE32+ magic `0x20B` were independently checked.

The tested source SHA was the PR #95 head when run #12 started. PR #95 later advanced to `5d50f42d76a071800dd84ee5faa8b216335c1ced`; the single intervening commit changes only documentation/evidence files (no product source, tests, or CI configuration). The Windows PASS remains explicitly bound to `f85375e...`, not silently transferred to the later SHA.

CircleCI Linux is a separate result. The current PR #95 head `5d50f42...` reports `ci/circleci: one-linux` FAILURE (workflow `d98d94fa-cb59-4487-84e9-582d889f6143`, job `b4427cc0-8253-4d95-8b5d-51f2f2778ca6`, failure report `aebbf019-e2c7-4c61-b0ce-e63a6b373832`). The authenticated first-failure output is not available in the current execution session, so the failed step/root cause is unknown. **No Linux PASS or overall cross-platform PASS is claimed.**

PR #95 and the independent verifier PR #42 remain open, draft, and unmerged. The canonical `main` branch remains unchanged.

## Other verification workflows

This repository also contains separate Android, Linux, scanner, package, and other verification workflows. The Project ONE Windows workflow above is scoped to Windows-host verification of the pinned canonical source snapshot; it does not redefine or remove those unrelated workflows.

- See [Candidate verification](CANDIDATE_VERIFICATION.md) for the broader candidate and release-gate process.
- The 2026-10-28 refresh is recorded in [Exact-SHA revalidation](docs/verification/EXACT_SHA_REVALIDATION_2026-10-28.md).
- See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the scanner and guarded-repair design.

## Historical checkpoint handling

Older Local CI extraction notes previously embedded in this README are superseded by the canonical Project ONE Notion checkpoint. They are not instructions for the current Windows verifier and must not be used to change its source pin or workflow.
