# Project ONE independent Windows exact-SHA verification


## Current exact-SHA Windows verification — PENDING — 2026-11-17

- Canonical ONE source pin: `e50748a1b25922d9090eba1f5fb90548d7c7d003`, PR #95 branch `ci/circleci-migration-20261113`.
- CircleCI Linux on the same exact source SHA reports SUCCESS; workflow `dc6f3660-328f-4016-8c01-72c3565d0321`, job `64a34e41-9759-4a5c-8e50-b77296730a54`.
- The source pin has been advanced from `07d8cbf...` to this SHA because PR #95 added current-evidence guards to `tools/check_contract.py` and refreshed the Windows/user-facing evidence checkpoints. The product source, product tests, and CircleCI configuration remain unchanged; the Windows verifier must nevertheless execute the new checker on this exact source SHA.
- Windows exact-SHA run for `e50748a...` has not yet been observed in the available GitHub run/status response. **Do not claim Windows PASS for this SHA until a terminal successful run and its artifact/manifest are inspected.**
- Previous Windows run [#28](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43865524749) remains PASS for source SHA `07d8cbf7422b8340f8efda3c2f9d4425f85b7537` only; it is historical evidence for that exact revision and is not relabeled as a run on `e50748a...`.
- Verifier PR #42 remains OPEN / DRAFT / UNMERGED. No merge or release is authorized.

