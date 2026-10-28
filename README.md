# One — Cross-Platform Verification

Temporary public verification mirror for independent Linux and Windows verification of the One programming language.

The canonical source repository remains private: `panglimanetizen01/one`.

Current canonical verification target: `1c39b81cbc20706b67e54841e8aef92675a9a43a`.

This repository exists only to execute the canonical source snapshot on GitHub-hosted runners without requiring a paid GitHub upgrade.

## Current candidate evidence

See [CANDIDATE_VERIFICATION.md](CANDIDATE_VERIFICATION.md) for the exact source SHA, current verification runs, runner diagnostics, and release-gate rules.

## Continuous diagnostic and repair system

See [Continuous Repository Health & Repair System](docs/CONTINUOUS_REPOSITORY_HEALTH_AND_REPAIR_SYSTEM.md) for the proposed detector catalogue, evidence model, guarded repair lifecycle, safety tiers, and incremental implementation roadmap. The scanner is being implemented in the canonical source repository; this document remains the design plan, not evidence that every detector or repair tier is complete.
