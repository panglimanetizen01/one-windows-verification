# One — Cross-Platform Verification

## LIVE CHECKPOINT — 2026-11-14 (iteration 13: exact-pin cross-platform verification PASS)

- Independent verifier run #758: `43489905888`, terminal SUCCESS on Ubuntu and Windows Server 2025. Both jobs passed the standalone ci-local compile/test suite, build/install, installed import-origin and console entry-point checks, smoke plan, all 15 ONE product-plan checks, manifest v2 validation, and artifact upload.
- Exact identities: ONE source `fb58a7f7bd357b469452c19379b6b07ad133535b`; ci-local runner `5e09517b80d77ce417c3f752c75e37ce24638943`; verifier workflow merge identity `491afefcba6d99dd58765fbe11df90cfa80515d2`. Verifier PR head tested: `fcd0d972d0da5d7f96d5c6d97e8ba2ed984a69b3`.
- Both evidence ZIPs were downloaded and inspected. Each contains only the smoke report, ONE product report, and manifest. Both reports are PASS; each product report has 15/15 steps PASS and exit code 0. Both manifest v2 validations PASS with empty errors; report SHA-256 values were independently recomputed and matched. ZIP hashes also match GitHub artifact metadata.
- The run #757 Windows manifest mismatch was fixed in the verifier-owned plan by renaming the local Python variable `root` to `workspace`; behavior and strict evidence validation were preserved.
- ci-local PR #5 and verifier PR #41 remain OPEN / DRAFT / UNMERGED. Production verifier branch/pin remains unchanged. This is successful exact-pin draft validation, not authorization to merge, release, or promote production pins. Standalone CircleCI pipeline status is a separate check and is not inferred from this GitHub Actions run.

Historical checkpoint entries below are retained as chronology and are superseded where they conflict with this live state.

---


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


## Standalone ci-local extraction verifier — live checkpoint 2026-11-13

### Exact candidate identities

- ONE PR #92 source: `fb58a7f7bd357b469452c19379b6b07ad133535b`.
- ci-local PR #2 package: `df592ae615f573e1b3ecec178a3daf0d1009b1ba`.
- Verifier branch: `migration/ci-local-dual-pin-20261113`; use live PR #41 metadata for its current HEAD. The workflow binds the verifier identity to `github.sha`.
- PR #41 remains OPEN / DRAFT / UNMERGED. The production `verification` branch and separate product-verification pin/workflow remain unchanged.

### Extraction boundary and static inventory

- ONE's eight known legacy runner/config/guide/test paths are absent at its candidate SHA. The ONE product plan is held in this verifier repository, not in ONE.
- The ci-local candidate has 96 authored regression methods: 55 runner, 34 evidence, 3 CI/build contract, 2 discovery, 2 path-contract. This is static inventory only; no runtime PASS is claimed.
- ONE PR #94's separate CircleCI workflow is product-owned and has no CI Local runner/evidence/import/path markers. It remains outside this extraction.
- PR #92's remaining product code/test/docs diff is not an extraction deliverable and is explicitly separated in that PR's description.

### Latest exact-head run and blocker

- Workflow run `43390289272` ran on verifier commit `dd353b68cf0bf7cd8ced10d1a7fd91bd5fc26f07`, with ONE `fb58a7f7bd357b469452c19379b6b07ad133535b` and ci-local `df592ae615f573e1b3ecec178a3daf0d1009b1ba`.
- Ubuntu job `131768291523` and Windows job `131768291055` both failed at the private ci-local access diagnostic. The existing `CI_LOCAL_READ_TOKEN` secret is present but returns HTTP 404 for the pinned private commit endpoint. It lacks effective access to `panglimanetizen01/ci-local` or is otherwise not authorized for that repository.
- Both repository checkouts and all package tests, compile/install, smoke, ONE product-plan, and manifest verification steps were skipped. No runtime preservation or parity PASS is claimed.
- Corrective action: replace/update the existing verifier Actions secret `CI_LOCAL_READ_TOKEN` with a token explicitly authorized for the private ci-local repository and Contents: read. Do not paste it into chat or make the repository public.

### Artifact publication correction

Run `43389915562` produced misleading plan-only ZIPs because the upload path included the verifier-owned plan even when runner checkout was blocked. Both ZIPs were inspected and contained only `plans/one-product-checks.json`, not reports or manifests. The workflow was corrected in commit `5875d1b7f5b57512ca17934145ce010b8a3e4339`: report upload now requires successful ci-local checkout and install, and only generated reports/manifests are uploaded. On run `43390289272`, the upload step was correctly SKIPPED and no artifacts were produced. The plan remains versioned in this repository and is not treated as evidence.

### Promotion rule

Do not merge PR #41, advance the `verification` branch, or claim migration preservation until the token has effective private-repository read access and both Linux/Windows jobs complete on the exact three identities with package/product reports and a verified manifest. No unrelated ci-local roadmap/backlog work is required.
