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
