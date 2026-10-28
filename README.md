# One — Cross-Platform Verification

Temporary public verification mirror for independent Linux and Windows verification of the One programming language.

The canonical source repository remains private: `panglimanetizen01/one`.

Current canonical verification target: `f21e8d178f72c6f9c76b4027d5ff85742dbe672e` (PR #80; matching pin is not execution evidence).

This repository exists only to execute the canonical source snapshot on GitHub-hosted runners without requiring a paid GitHub upgrade.

## Current candidate evidence

See [CANDIDATE_VERIFICATION.md](CANDIDATE_VERIFICATION.md) for the exact source SHA, current verification runs, runner diagnostics, and release-gate rules.

## Continuous diagnostic and repair system

See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the proposed detector catalogue, evidence model, guarded repair lifecycle, safety tiers, and incremental implementation roadmap. The canonical source currently contains the scanner, detector regression tests, baseline triage, guarded Markdown repair, and reviewed quality-ledger code. The independent exact-SHA scanner workflow is defined in this repository; its execution artifacts and outcomes must be inspected before claiming acceptance.
