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
