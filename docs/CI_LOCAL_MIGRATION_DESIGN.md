# Standalone ci-local verifier migration design

**Status: design only — not implemented, not verified.**  
**Scope:** `panglimanetizen01/one-windows-verification`, branch `verification`.

This note records the safe migration boundary for replacing the verifier's direct dependency on ONE's legacy generic Local CI scripts. It does not change either pin, the workflow, the product verifier, or any legacy source file.

## Exact baseline inspected

- Verifier branch HEAD at inspection: `d13ea8ad90c7123eddc090e398552faa382bcb6f`.
- `.github/workflows/windows-verification.yml` blob: `1e3c1079ee5c6876caeabf1906f62edd031757eb`.
- `README.md` blob: `467824e121f02298b6af84ad7959594c9abc24da`.
- `LOCAL_CI_CANONICAL_COMMIT.txt` blob: `8b6557772c1341bbaa2a48c75d0cc052295d9d9f`; value remains the ONE source SHA `56ef8babfbc35808d82b930d8dd9baa92afb26af`.
- Standalone ci-local candidate branch: `fix/evidence-single-read-integrity-20261112`, inspected at `25cee22354e6eb04ab1ef8fc6bc3e2c044963056`. This is an unverified candidate, not an approved canonical pin.
- ci-local consumer contract blob inspected: `3f76b3cfa7a31c18f501192df572978b972cb110`.

The current workflow still invokes `source/tools/ci_unittest.py`, `source/tools/ci_local.py`, and `source/tools/ci_local_evidence.py`. The README still describes the old single pin as a ONE source target. This verifier has not yet been migrated.

## Required dual-pin model

Replace the ambiguous Local CI source pin with two explicit files in the same reviewed change:

- `ONE_SOURCE_CANONICAL_COMMIT.txt`: exact ONE source SHA.
- `CI_LOCAL_CANONICAL_COMMIT.txt`: exact standalone ci-local runner SHA.

Each file must contain exactly one lowercase 40-character commit SHA. The verifier workflow's own `github.sha` is a third, separate identity. Do not repurpose the existing pin file alone or change either pin before the workflow and documentation are migrated together.

Keep `CANONICAL_COMMIT.txt` and `.github/workflows/one-cross-platform-verification.yml` separate and unchanged; they belong to product cross-platform verification, not this generic runner migration.

## Target workflow sequence

1. Checkout the verifier repository and capture its exact workflow checkout SHA (`github.sha`).
2. Read and validate both pin files independently.
3. Checkout `panglimanetizen01/one` at the ONE pin into `source/`.
4. Checkout `panglimanetizen01/ci-local` at the ci-local pin into `ci-local/`.
5. Assert each checkout's `git rev-parse HEAD` equals its own pin, and assert the verifier checkout HEAD equals `github.sha`.
6. Provision the same pinned Python 3 version on Ubuntu and Windows. Assert `python --version` and `python -c "import sys; assert sys.version_info.major == 3"`. Do not assume `python3` exists on Windows.
7. Install the package from the pinned ci-local checkout using its exact build-backend pin (`setuptools==80.9.0` as inspected in the current candidate's `pyproject.toml`). Verify `ci_local.__file__` resolves to the intended pinned install, not a shadow import from ONE or another environment location.
8. Resolve the ONE-owned profile (target path `source/ci/ci-local-plan.json`) and assert it remains inside the pinned ONE checkout. Record its SHA-256.
9. Run `ci-local --plan <absolute-plan-path> --cwd <absolute-source-root> --report <absolute-external-report-path>`. Reports and manifests must be outside the ONE source worktree.
10. Create and verify evidence atomically with the matching standalone `ci-local-evidence` CLI. Supply the plan path and all three expected identities: ONE source SHA, verifier SHA, and ci-local runner SHA. Require manifest v2 and a matching runner SHA; a v1 manifest is not acceptable when runner identity is expected.
11. Upload the report, manifest, and provenance containing all three SHAs, profile SHA-256, Python version, OS/architecture, workflow/run/attempt/job IDs, and report/manifest digests.
12. Execute and validate Ubuntu and Windows independently. One platform's result cannot stand in for the other.

Use immutable action references and least-privilege private-repository checkout permissions. Credentials must not be passed through the plan or command line.

## Product checks that must remain

The generic 12-step plan is not a replacement for the complete ONE CI workflow. Preserve Android SDK/NDK setup, native toolchain provisioning and probes, user documentation validation, ONE-owned fail-closed discovery/config/path tests, trusted CLI build and hard-link invariant, product cross-platform checks, Android runtime/emulator checks, repository-health checks, and their separate evidence/artifacts. The migration change must include a before/after ownership inventory proving every check has exactly one owner.

## Atomic switch and validation gates

The old ONE runner report schema and standalone ci-local report schema are incompatible. In one workflow change, switch execution, evidence creation/verification, output paths, artifact paths, workflow tests, and docs together. Never validate a generic ci-local report using the legacy ONE evidence helper.

Do not implement or advance pins until the ci-local candidate has completed its own exact-SHA test, compile, install, console, smoke, evidence roundtrip, and artifact gates, plus hosted CircleCI Linux and independent hosted Linux/Windows verification. Then migrate this verifier on an isolated draft PR/branch and prove the exact dual-pin execution before changing the ONE consumer.

## Current disposition

- No verifier workflow or pin change is made by this design note.
- No ONE source, workflow, product pin, or legacy file is changed.
- ci-local candidate `25cee22354e6eb04ab1ef8fc6bc3e2c044963056` remains unverified.
- No CI result is inferred from empty status/workflow-run collections.
- No merge, release, pin advance, or legacy deletion is authorized by this note.
