# One — Cross-Platform Verification

Temporary public verification mirror for independent Linux and Windows verification of the One programming language.

The canonical source repository remains private: `panglimanetizen01/one`.

A draft extraction-validation branch, `migration/ci-local-dual-pin-20261113`, now carries separate candidate pins for ONE source (`fb58a7f7bd357b469452c19379b6b07ad133535b`) and standalone ci-local (`df592ae615f573e1b3ecec178a3daf0d1009b1ba`). The workflow checkout SHA is a third, independent identity. These are draft validation candidates only: the `verification` branch has not been advanced, no PR has been merged, and no parity PASS is claimed. The ONE candidate currently has a failing CircleCI status whose job logs are unavailable; the dual-platform verifier workflow is intended to expose the exact Linux/Windows result.

The separate `CANONICAL_COMMIT.txt` pin for PR #94 remains unchanged.

This repository exists only to execute the canonical source snapshot on GitHub-hosted runners without requiring a paid GitHub upgrade.

## Current candidate evidence

See [CANDIDATE_VERIFICATION.md](CANDIDATE_VERIFICATION.md) for the exact source SHA, current verification runs, runner diagnostics, and release-gate rules.

The 2026-10-28 refresh is recorded in [Exact-SHA revalidation note](docs/verification/EXACT_SHA_REVALIDATION_2026-10-28.md). It documents successful Linux/Windows cross-platform checks for the pinned source SHA, the still-pending Android runtime at last observation, and why the acceptance gate remains NOT PASSED.

## Continuous diagnostic and repair system

See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the proposed detector catalogue, evidence model, guarded repair lifecycle, safety tiers, and incremental implementation roadmap. The canonical source currently contains the scanner, detector regression tests, baseline triage, guarded Markdown repair, and reviewed quality-ledger code. The independent exact-SHA scanner workflow is defined in this repository; its execution artifacts and outcomes must be inspected before claiming acceptance.


## Draft standalone ci-local dual-pin migration — 2026-11-13

Implementation candidate branch: `migration/ci-local-dual-pin-20261113`, based on verifier branch `verification` at exact SHA `f364ba99b3ff8eeccd166bf6a1e8c57f3af0a288`.

- ONE source candidate: `fb58a7f7bd357b469452c19379b6b07ad133535b` (PR #92, `tooling/python-local-ci`). This includes the final targeted cleanup of a retired branch-name reference; no runtime PASS is claimed for this new SHA.
- Standalone runner candidate: `df592ae615f573e1b3ecec178a3daf0d1009b1ba` (ci-local PR #2, `fix/evidence-single-read-integrity-20261112`). Static readback counts 96 authored regression methods; none has been executed by this verifier yet.
- New `ONE_SOURCE_CANONICAL_COMMIT.txt` and `CI_LOCAL_CANONICAL_COMMIT.txt` pins are candidate-only and exist on this isolated branch. The old ambiguous `LOCAL_CI_CANONICAL_COMMIT.txt` is removed from this branch.
- `.github/workflows/windows-verification.yml` now checks out ONE and ci-local separately, asserts both source SHAs plus the verifier workflow SHA, runs the standalone package test/compile/install/console/smoke checks, executes the verifier-owned `plans/one-product-checks.json`, and creates/verifies a manifest bound to all three identities.
- The ONE product-check plan is owned by this verifier repository, not ONE. This respects the extraction boundary: ONE retains product-owned CircleCI commands and product contract tests, but no CI Local runner, package, or consumer plan.
- The separate `CANONICAL_COMMIT.txt` and `.github/workflows/one-cross-platform-verification.yml` product-verification route remain untouched.
- The workflow has not yet completed on this draft branch. Do not claim Linux/Windows parity, do not advance the `verification` branch, and do not merge this PR until exact-SHA jobs and artifacts are reviewed.

See [CI Local migration implementation](docs/CI_LOCAL_MIGRATION_IMPLEMENTATION.md) for the exact workflow and artifact contract.


The current pinned ci-local checkpoint includes the extraction inventory reconciliation: 96 authored test methods (55 runner, 34 evidence, 3 CI config/build, 2 discovery, 2 path-contract). This is static inventory, not a test PASS.

The current ONE candidate pin includes the final targeted cleanup of the retired branch-name reference in the runtime governance audit; the eight extracted runner/config/guide/test paths remain absent.


**Run-to-pin reconciliation:** workflow run `43387442873` tested an earlier candidate state (ONE `ebb11f8da5e8af7b0baf2e3785754e656b542777`, ci-local `99822c27730038659679099080ac839d11e03d4e`, verifier `508383a7668f696451be6c9a8e15e77555a1f1ab`) and failed at private ci-local access. It is not an execution of the current pins. Current pins are ONE `fb58a7f7bd357b469452c19379b6b07ad133535b` and ci-local `df592ae615f573e1b3ecec178a3daf0d1009b1ba`; no workflow run has executed on this exact candidate set.


## Latest exact-current-pin execution — 2026-11-13

- Workflow run: `43389690604`, on current verifier workflow commit `8c66b541549ab88446ed43cd0d832d3a3c9e6324`.
- Exact pins used: ONE `fb58a7f7bd357b469452c19379b6b07ad133535b`; ci-local `df592ae615f573e1b3ecec178a3daf0d1009b1ba`; verifier workflow SHA `8c66b541549ab88446ed43cd0d832d3a3c9e6324`.
- Ubuntu job `131766380963` and Windows job `131766381519` both failed at `Verify read access to pinned private ci-local repository`.
- Logs show `CI_LOCAL_READ_TOKEN` is present (redacted in logs), but the private commit API endpoint returns HTTP `404`. Therefore the secret exists but its token does not currently have effective read access to the private ci-local repository, or its repository authorization is otherwise insufficient.
- Both ONE/ci-local checkout steps and all package tests, compile/install, smoke, ONE product-plan, and evidence verification steps were skipped. The successful manifest step only emitted the explicit “skipped because runner/report not produced” notice; it is not evidence or a PASS.
- Required correction: replace/update the existing verifier Actions secret `CI_LOCAL_READ_TOKEN` with a token authorized for `panglimanetizen01/ci-local` and Contents: read. Do not paste the token into chat or make the repository public.
- This is an access blocker, not a package/test failure. No runtime preservation or parity PASS is claimed.


## Latest run on current source pins — verifier SHA superseded

- Workflow run: `43389690604`, workflow checkout/verifier SHA `8c66b541549ab88446ed43cd0d832d3a3c9e6324`.
- It used the current ONE source pin `fb58a7f7bd357b469452c19379b6b07ad133535b` and ci-local pin `df592ae615f573e1b3ecec178a3daf0d1009b1ba`.
- The verifier branch has since advanced through documentation-only commits to `479a12cc029a71b116890c8d9b3d332b159513f5`. Therefore run `43389690604` is **not** a run on the current exact three-identity set; its verifier identity is superseded.
- Ubuntu job `131766380963` and Windows job `131766381519` both failed at the private ci-local read-access diagnostic.
- Logs show `CI_LOCAL_READ_TOKEN` is present (redacted), but the private commit API endpoint returns HTTP `404`. The secret exists, but its token lacks effective read access to private ci-local or its repository authorization is otherwise insufficient.
- Both source checkout steps and all package tests, compile/install, smoke, ONE product-plan, and evidence verification steps were skipped. The green manifest step emitted an explicit skipped notice; it is not evidence or a PASS.
- Required correction: replace/update `CI_LOCAL_READ_TOKEN` with a token authorized for `panglimanetizen01/ci-local` and Contents: read. Do not paste the token into chat or make the repository public.
- No workflow run has executed on the current verifier HEAD `479a12cc029a71b116890c8d9b3d332b159513f5` with the current three identities. No runtime preservation or parity PASS is claimed.
