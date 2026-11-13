# CI Local migration implementation — draft validation

## Scope

Replace the verifier's dependency on ONE's legacy generic Local CI scripts with the standalone `panglimanetizen01/ci-local` package. Keep ONE product verification independent from the runner implementation. The plan is verifier-owned so ONE contains no CI Local plan/configuration or operational dependency.

## Candidate identities

| Identity | Candidate |
| --- | --- |
| ONE source | `59f8a651b693d6fbdadc03ff398290486bee35e2` |
| ci-local package | `ddad4a290937735d261f3608f2448632b180b90a` |
| verifier workflow | `github.sha` captured from the verifier checkout |

These are draft validation pins only. They do not update the `verification` branch's production pin or establish PASS.

## Files changed on the isolated branch

- `ONE_SOURCE_CANONICAL_COMMIT.txt` — exact ONE source candidate.
- `CI_LOCAL_CANONICAL_COMMIT.txt` — exact standalone package candidate.
- `plans/one-product-checks.json` — ONE product-owned checks, stored in the verifier repository rather than ONE.
- `.github/workflows/windows-verification.yml` — dual checkout and three-identity evidence workflow.
- `LOCAL_CI_CANONICAL_COMMIT.txt` — removed from this draft branch because its single-pin meaning is ambiguous.
- `README.md` and `docs/CI_LOCAL_MIGRATION_DESIGN.md` — current draft state and ownership boundary.

The separate `CANONICAL_COMMIT.txt` and `.github/workflows/one-cross-platform-verification.yml` product-verification workflow are unchanged.

## Workflow contract

For both `ubuntu-latest` and `windows-2025`:

1. Checkout verifier and validate both candidate pins as lowercase 40-character SHAs.
2. Checkout ONE at the ONE pin and ci-local at the ci-local pin into separate directories.
3. Assert verifier `HEAD == github.sha`, ONE `HEAD == ONE_SOURCE_CANONICAL_COMMIT`, and ci-local `HEAD == CI_LOCAL_CANONICAL_COMMIT`.
4. Compile and run the standalone ci-local test suite from its source checkout.
5. Build/install the ci-local distribution and verify the import resolves to the installed package, not a checkout shadow.
6. Verify both console entry points and run the package smoke plan.
7. Execute `plans/one-product-checks.json` against the ONE checkout using the installed `ci-local` command. The plan preserves user documentation, contract, Cargo, product test, deterministic artifact, native toolchain, and trusted CLI checks.
8. Create and verify a manifest v2 bound to the exact ONE source SHA, verifier SHA, ci-local runner SHA, and plan digest.
9. Upload the smoke report, product report, manifest, and plan separately for each OS.

## Verification status

- Draft branch created from verifier `verification` at `f364ba99b3ff8eeccd166bf6a1e8c57f3af0a288`.
- Workflow and candidate pins committed on the isolated draft branch; PR has not yet been created at the time of this document.
- No Linux/Windows run has completed. No test, compile, install, smoke, report, manifest, or artifact PASS is claimed.
- ONE's CircleCI status for the candidate source SHA is FAILURE, with job logs unavailable through the current session. This workflow is intended to produce independent diagnostic evidence; it does not reclassify or hide that CircleCI result.

## Promotion rule

Do not merge the draft PR or update the `verification` branch until both OS jobs complete on the exact three identities and the report/manifest artifacts verify. Do not modify the separate product-verification workflow or pin. No release or unrelated ci-local backlog work is part of this task.


## Private repository checkout credential

The standalone ci-local repository is private. The verifier workflow checks the pinned commit API endpoint before checkout and uses the repository secret `CI_LOCAL_READ_TOKEN`, falling back to `CANONICAL_READ_TOKEN` for compatibility. The selected token must have Contents: read access to `panglimanetizen01/ci-local`. The diagnostic prints only the HTTP status, never the token. If the pinned commit endpoint is not HTTP 200, update the verifier repository secret; do not make ci-local public or weaken repository visibility.


## Exact current authored regression inventory

At ci-local candidate SHA `df592ae615f573e1b3ecec178a3daf0d1009b1ba`, static GitHub-readback counting found 96 methods across the five test modules (55 runner, 34 evidence, 3 CI/build, 2 discovery, 2 path-contract). This is not runtime evidence. The exact-SHA dual-pin workflow must execute the suite before preservation is accepted.


## ONE residual reference cleanup

The ONE PR #92 candidate was advanced to `fb58a7f7bd357b469452c19379b6b07ad133535b` to remove the retired working-branch name from `docs/verification/runtime-governance-audit-2026-11-12.md`. The source branch's known legacy CI Local paths remain absent. Re-run the dual-pin workflow on the new exact ONE SHA after the private ci-local checkout credential is available.


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


## Artifact publication guard — 2026-11-13

Run `43389915562` exposed that the unconditional upload step packaged only the verifier-owned product plan when private ci-local checkout failed; the artifact name implied that reports/evidence existed. The workflow now gives the ci-local checkout and install steps explicit IDs, runs artifact upload only after both succeed, and uploads only generated smoke/product reports and the manifest (not the always-present plan). The manifest step name now states that creation is conditional on a report. This prevents a plan-only ZIP from appearing as verification evidence. The source plan remains versioned in the verifier repository. No tests or evidence PASS is inferred from this workflow correction.
