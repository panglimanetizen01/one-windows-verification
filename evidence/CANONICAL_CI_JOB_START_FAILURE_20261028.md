# Canonical CI retry diagnostics — 2026-10-28

## Candidate identity

- Canonical source repository: https://github.com/panglimanetizen01/one
- Candidate branch: `milestone/100-ecosystem-20261023`
- Exact source SHA: `b8a6888e68c4432c044282be998de468f7a9c31e`
- Pull request: https://github.com/panglimanetizen01/one/pull/80

## Retry results

The failed jobs were explicitly retried. The GitHub workflow-run API still reports failure for these canonical-repository runs:

| Workflow | Run | Result / log retrieval |
|---|---:|---|
| One CI | [40685999512](https://github.com/panglimanetizen01/one/actions/runs/40685999512) | Failure; job log download returned `BlobNotFound` |
| E1 Standard Library Test Lab | [40685999518](https://github.com/panglimanetizen01/one/actions/runs/40685999518) | Failure; job log download returned `BlobNotFound` |
| E2 Package and Provenance Test Lab | [40685999558](https://github.com/panglimanetizen01/one/actions/runs/40685999558) | Failure; job log download returned `BlobNotFound` |
| Linux Distribution Conformance | [40685999650](https://github.com/panglimanetizen01/one/actions/runs/40685999650) | Failure; job log download returned `BlobNotFound` |
| Focused Standard Library Verification | [40685999511](https://github.com/panglimanetizen01/one/actions/runs/40685999511) | Re-run requested; API showed queued at first post-retry inspection |

The job-log API returned an Azure storage error similar to:

```text
BlobNotFound — The specified blob does not exist.
```

This means there is no retrievable job log from which to diagnose a test failure. It does **not** prove a source test failed, and it does **not** count as a pass. Treat these as unresolved runner/job-log infrastructure failures until GitHub Actions exposes a completed job with usable diagnostics.

## Recovery procedure

1. In the canonical repository's Actions UI, open each linked run and inspect its attempt history, job initialization, runner assignment, and annotations.
2. Verify repository Actions policy, runner availability/usage limits, permissions, and any service incident affecting job startup or log persistence.
3. If a hosted job never starts or logs are still absent, resolve that runner/service problem first; changing application code cannot be justified from a missing log.
4. Re-run the canonical workflows on the same exact source SHA once the infrastructure is healthy. If any source changes are needed, freeze the new SHA and rerun the entire required matrix against that new SHA.
5. Keep the independent verification repository's results labeled as independent evidence; do not relabel them as canonical CI.
6. Keep E2 open until the source-bound provenance signature is checked against independently configured trusted-publisher trust and the protected production release path is exercised. A synthetic/disposable trust test is only a test-harness result.
7. Do not merge PR #80 or publish a release until the fixed-weight acceptance gate reports PASS for the final exact SHA and the protected production provenance evidence exists.

## Current disposition

The independent matrix has passed its documented scopes, but the fixed-weight ledger gate remains **NOT PASSED**. E1, E2, and E6 remain open; seven Definition-of-Done items were reported unchecked in the latest gate snapshot. This document is diagnostic evidence only and awards no ledger points.
