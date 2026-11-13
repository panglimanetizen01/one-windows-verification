# One — Cross-Platform Verification

Temporary public verification mirror for independent Linux and Windows verification of the One programming language.

The canonical source repository remains private: `panglimanetizen01/one`.

A draft extraction-validation branch, `migration/ci-local-dual-pin-20261113`, now carries separate candidate pins for ONE source (`ebb11f8da5e8af7b0baf2e3785754e656b542777`) and standalone ci-local (`16fe520bdc8851526b64ccfb12a7c5a87f0c04d6`). The workflow checkout SHA is a third, independent identity. These are draft validation candidates only: the `verification` branch has not been advanced, no PR has been merged, and no parity PASS is claimed. The ONE candidate currently has a failing CircleCI status whose job logs are unavailable; the dual-platform verifier workflow is intended to expose the exact Linux/Windows result.

The separate `CANONICAL_COMMIT.txt` pin for PR #94 remains unchanged.

This repository exists only to execute the canonical source snapshot on GitHub-hosted runners without requiring a paid GitHub upgrade.

## Current candidate evidence

See [CANDIDATE_VERIFICATION.md](CANDIDATE_VERIFICATION.md) for the exact source SHA, current verification runs, runner diagnostics, and release-gate rules.

The 2026-10-28 refresh is recorded in [Exact-SHA revalidation note](docs/verification/EXACT_SHA_REVALIDATION_2026-10-28.md). It documents successful Linux/Windows cross-platform checks for the pinned source SHA, the still-pending Android runtime at last observation, and why the acceptance gate remains NOT PASSED.

## Continuous diagnostic and repair system

See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the proposed detector catalogue, evidence model, guarded repair lifecycle, safety tiers, and incremental implementation roadmap. The canonical source currently contains the scanner, detector regression tests, baseline triage, guarded Markdown repair, and reviewed quality-ledger code. The independent exact-SHA scanner workflow is defined in this repository; its execution artifacts and outcomes must be inspected before claiming acceptance.


## Draft standalone ci-local dual-pin migration — 2026-11-13

Implementation candidate branch: `migration/ci-local-dual-pin-20261113`, based on verifier branch `verification` at exact SHA `f364ba99b3ff8eeccd166bf6a1e8c57f3af0a288`.

- ONE source candidate: `47ac10686e6aac023941e72ec6fb3ad22d18f19b` (PR #92, `tooling/python-local-ci`). Its CircleCI context currently reports FAILURE; no root cause is inferred without job logs.
- Standalone runner candidate: `a34e07429ec686b91e74ef9c719cd499c7d2dd8a` (ci-local PR #2, `fix/evidence-single-read-integrity-20261112`). Its exact-SHA tests and CircleCI status are not verified yet.
- New `ONE_SOURCE_CANONICAL_COMMIT.txt` and `CI_LOCAL_CANONICAL_COMMIT.txt` pins are candidate-only and exist on this isolated branch. The old ambiguous `LOCAL_CI_CANONICAL_COMMIT.txt` is removed from this branch.
- `.github/workflows/windows-verification.yml` now checks out ONE and ci-local separately, asserts both source SHAs plus the verifier workflow SHA, runs the standalone package test/compile/install/console/smoke checks, executes the verifier-owned `plans/one-product-checks.json`, and creates/verifies a manifest bound to all three identities.
- The ONE product-check plan is owned by this verifier repository, not ONE. This respects the extraction boundary: ONE retains product-owned CircleCI commands and product contract tests, but no CI Local runner, package, or consumer plan.
- The separate `CANONICAL_COMMIT.txt` and `.github/workflows/one-cross-platform-verification.yml` product-verification route remain untouched.
- The workflow has not yet completed on this draft branch. Do not claim Linux/Windows parity, do not advance the `verification` branch, and do not merge this PR until exact-SHA jobs and artifacts are reviewed.

See [CI Local migration implementation](docs/CI_LOCAL_MIGRATION_IMPLEMENTATION.md) for the exact workflow and artifact contract.
