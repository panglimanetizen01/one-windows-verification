# One — Cross-Platform Verification

Temporary public verification mirror for independent Linux and Windows verification of the One programming language.

The canonical source repository remains private: `panglimanetizen01/one`.

Current PR #92 Local CI verifier target: `56ef8babfbc35808d82b930d8dd9baa92afb26af` (PR #92, branch `tooling/python-local-ci`). The pin file `LOCAL_CI_CANONICAL_COMMIT.txt` is authoritative for the actual workflow checkout. The pin is a target pointer, not execution evidence. Linux/Windows results must complete on this exact SHA before parity is claimed. This is the last source SHA recorded as independently verified; newer PR #92 commits must not inherit that evidence.

The separate `CANONICAL_COMMIT.txt` pin for PR #94 remains unchanged.

This repository exists only to execute the canonical source snapshot on GitHub-hosted runners without requiring a paid GitHub upgrade.

## Current candidate evidence

See [CANDIDATE_VERIFICATION.md](CANDIDATE_VERIFICATION.md) for the exact source SHA, current verification runs, runner diagnostics, and release-gate rules.

The 2026-10-28 refresh is recorded in [Exact-SHA revalidation note](docs/verification/EXACT_SHA_REVALIDATION_2026-10-28.md). It documents successful Linux/Windows cross-platform checks for the pinned source SHA, the still-pending Android runtime at last observation, and why the acceptance gate remains NOT PASSED.

## Continuous diagnostic and repair system

See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the proposed detector catalogue, evidence model, guarded repair lifecycle, safety tiers, and incremental implementation roadmap. The canonical source currently contains the scanner, detector regression tests, baseline triage, guarded Markdown repair, and reviewed quality-ledger code. The independent exact-SHA scanner workflow is defined in this repository; its execution artifacts and outcomes must be inspected before claiming acceptance.


## Standalone ci-local migration checkpoint — 2026-11-13

The migration design is recorded in [CI_LOCAL_MIGRATION_DESIGN.md](docs/CI_LOCAL_MIGRATION_DESIGN.md). **It remains design-only and the verifier workflow has not been migrated.**

- PR #92 current ONE source candidate: `66a94d4ffc69240b5303745eaab02fcb5b31aa47` on `tooling/python-local-ci`; its exact-SHA verification is pending. The existing `LOCAL_CI_CANONICAL_COMMIT.txt` still points to the older last-verified baseline `56ef8babfbc35808d82b930d8dd9baa92afb26af`. Do not treat that old pin as validation of the newer candidate.
- Standalone runner candidate: `panglimanetizen01/ci-local`, branch `fix/evidence-single-read-integrity-20261112`, exact source/test checkpoint `188ce087391ae1ef37c4baa107c7cecd77b9751c`; current docs-only branch HEAD `2049fcd52f5861b967c019f30fefbc0cbf0c7a42`. PR #2 is OPEN / DRAFT / UNMERGED.
- The standalone candidate has 90 authored test methods (54 runner + 34 evidence + 2 CI/build contract). This is an inventory only; no execution PASS is claimed. Exact latest HEAD has no GitHub check-runs or Actions runs at the checkpoint.
- Finding #61 hardens Windows `taskkill` nonzero-exit fallback and adds a mocked regression test. Hosted Windows process-tree validation remains pending.
- The current verifier workflow still checks out only ONE and invokes `source/tools/ci_unittest.py`, `source/tools/ci_local.py`, and `source/tools/ci_local_evidence.py`. It still has one legacy ONE-source pin, not the required separate ONE and ci-local pins.
- Keep both current pins and workflow unchanged until ci-local completes its own exact-SHA tests, compile/install/console/smoke/evidence/artifact gates and hosted Linux/Windows verification. Then implement the dual-pin verifier workflow on an isolated draft branch and prove it before changing ONE's consumer.
- No verifier workflow, pin, product verifier, or legacy implementation has been changed. No merge, release, or deletion.


## Standalone ci-local migration reconciliation — 2026-11-13

This addendum supersedes earlier candidate/test-inventory values above; it does not authorize pin or workflow changes.

- ONE PR #92 remains OPEN / DRAFT / UNMERGED. Candidate branch `tooling/python-local-ci`, exact HEAD `66a94d4ffc69240b5303745eaab02fcb5b31aa47`, base `main` SHA `d35db95153f6ddd79885494c72f5aee16c899751`.
- Standalone ci-local candidate branch `fix/evidence-single-read-integrity-20261112`, latest source/test SHA `b33f1a68f54e44fee24c275a5439c654689905fd`; latest documentation branch HEAD `c2b7b9b8388d9aad5727979dbeb76ae8fa111daf` at the time of this note. PR #2 remains OPEN / DRAFT / UNMERGED. Candidate is NOT VERIFIED: 92 authored test methods (55 runner, 34 evidence, 3 config/build) are inventory only. No full test, compile, package install, console, smoke, evidence roundtrip, or CircleCI Linux/Windows evidence is available for the candidate.
- Windows process-tree implementation now uses a suspended process assigned to a kill-on-close Windows Job Object before resume. Regressions cover parent-exits-first with inherited pipes and descendant cleanup on timeout; neither has hosted Windows execution evidence yet.
- The standalone CircleCI config now declares Linux `test` and Windows `test-windows` jobs. The supplementary GitHub Actions workflow was removed after runner allocation failures with no steps/logs; CircleCI remains the canonical standalone CI route. Actual CircleCI pipeline/log/artifact status is not readable in this session.
- The Local CI consumer workflow to migrate is `.github/workflows/windows-verification.yml`, not `.github/workflows/one-cross-platform-verification.yml`. The latter and its `CANONICAL_COMMIT.txt` pin are separate product cross-platform verification and must remain unchanged.
- Current legacy `LOCAL_CI_CANONICAL_COMMIT.txt` still contains ONE source SHA `56ef8babfbc35808d82b930d8dd9baa92afb26af`. Keep the required dual-pin model from this design: `ONE_SOURCE_CANONICAL_COMMIT.txt` for ONE, `CI_LOCAL_CANONICAL_COMMIT.txt` for standalone ci-local, plus verifier workflow SHA as third identity. No pin or workflow change until standalone Gate B passes.
- Preserve ONE-specific toolchain provisioning, contract/user-doc checks, Rust build/Clippy/tests, product checks, and evidence. The generic runner/evidence/test-discovery implementation moves to ci-local; ONE-specific checks become the ONE-owned plan at `source/ci/ci-local-plan.json` as already specified above.
- No ONE or verifier workflow/pin changes, no merge/release, no legacy deletion. Gate B incomplete; verifier migration and ONE consumer migration remain blocked.


## Latest standalone ci-local candidate refresh — 2026-11-13 12:20 WIB

- ci-local branch `fix/evidence-single-read-integrity-20261112` latest source commit: `a68960d8b1bf6ebe31793692bad81b77652541c0`; latest documentation branch HEAD at this refresh: `452fcb8d1f39cdb97c0480e95f97799c632f5dbd`. PR #2 remains OPEN / DRAFT / UNMERGED.
- The candidate now owns Windows process trees with suspended launch + kill-on-close Job Object assignment before resume. Cleanup explicitly calls `TerminateJobObject` then `CloseHandle`; delayed-marker regressions cover parent-exits-first inherited pipes and timeout descendant termination. Both are authored only, NOT EXECUTED on hosted Windows.
- Authored test inventory: 92 methods (55 runner, 34 evidence, 3 config/build). No full tests, compile, package build/install, console entry-point, smoke, evidence roundtrip, or CircleCI Linux/Windows artifacts have been verified for this candidate.
- Standalone CircleCI config declares Linux `test` and Windows `test-windows`; the redundant GitHub Actions Windows workflow was removed. No CircleCI API connector is exposed in this session, and no exact-SHA CircleCI run/log/artifact can be read back. Candidate remains NOT VERIFIED.
- The verifier migration target remains `.github/workflows/windows-verification.yml`; keep `.github/workflows/one-cross-platform-verification.yml` and `CANONICAL_COMMIT.txt` unchanged. Dual-pin design and ownership boundaries remain as specified in the previous addendum.
- Existing `LOCAL_CI_CANONICAL_COMMIT.txt` still contains ONE SHA `56ef8babfbc35808d82b930d8dd9baa92afb26af`; do not change it until a reviewed dual-pin workflow change is ready and ci-local Gate B passes.
- No verifier workflow/pin change, no ONE consumer change, no merge/release, and no legacy deletion.
