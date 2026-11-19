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


## Protected verifier remediation integration — 2026-11-19 16:27Z

The user explicitly authorized continuing the proposed integration of verifier remediation PRs #45–#48 into protected `verification`. All four were converted from draft to ready-for-review and squash-merged with expected-head SHA guards:

| PR | Change | PR head tested | Protected merge commit |
|---|---|---|---|
| #45 | Candidate artifact integrity; Rust/Cargo metadata aligned to source pin | `9a72e04b7e2992d655f8e3fc4e478892e91b7ae5` | `42feff8bc11d9b17d04ac9cff4abea4e80a7a832` |
| #46 | SEC-05 bounded APT retries/timeouts/source diagnostics | `8a880ad00225ed8a78a3fd58adfbc329f0df5b11` | `d539a162aeed9d22988c7ffb0c7a893e8d33f571` |
| #47 | Windows native runtime uses canonical source pin and source-pinned Rust toolchain | `bd100d10c12c7b0849f01e9481111b0b0c859dd1` | `4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4` |
| #48 | E1/focused stdlib workflows aligned to normative v0.1 test targets | `06bf1d7cbd10adadb74c79d7296f951244ae9839` | `b14abf0020472dc45842be30854e0a09317d6cb4` |

Protected `verification` now points to `b14abf0020472dc45842be30854e0a09317d6cb4`. The canonical ONE source pin remains `722d662e7a81711ba3607d26571f4048a292b3ed`; neither canonical pin nor fixed-weight ledger/DoD values were changed.

### Protected post-merge exact-SHA execution (status at 2026-11-19 16:27Z)

| Workflow | Run | Exact protected commit | Status |
|---|---:|---|---|
| Candidate Artifact Integrity | [#44566172841](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566172841) | `42feff8bc11d9b17d04ac9cff4abea4e80a7a832` | SUCCESS |
| SEC-05 subprocess baseline | [#44566187162](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566187162) | `d539a162aeed9d22988c7ffb0c7a893e8d33f571` | IN PROGRESS (Linux + Windows) |
| Windows Native Backend Runtime | [#44566197814](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566197814) | `4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4` | IN PROGRESS (Windows Server 2025) |
| E1 cross-platform acceptance | [#44566212975](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212975) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS (Ubuntu + Windows) |
| Focused stdlib/database regressions | [#44566212982](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212982) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS |
| E1 Windows acceptance | [#44566212997](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44566212997) | `b14abf0020472dc45842be30854e0a09317d6cb4` | IN PROGRESS |

These are protected-branch push validations and are distinct from the earlier PR-branch PASS runs. Do not mark pending scopes PASS until all jobs complete and their logs establish non-zero tests. Existing protected E4 #44519577693 remains SUCCESS for its declared scope; it was not rerun because no E4 source/test input changed.

### Acceptance and safety boundary

The fixed-weight ledger gate #44519577312 remains FAILURE on its recorded run. Its inspected log reported 92/100 implementation, 0/100 verified, 18 rows checked, 10 unchecked DoD items, exact-SHA evidence timeout, failed protected SEC-05/artifact/E1/focused workflow attempts, no protected exact-source Windows Native Runtime run, and no protected ONE Package Provenance Release. The new post-merge runs must become terminal and be reconciled before any new gate evaluation. Do not alter fixed weights, award points without row evidence, check DoD items speculatively, or dispatch package provenance release. Full v0.1 provenance envelope remains outside implemented scope.

Issue #104 remains OPEN / NOT ACCEPTED. This verifier-only integration does not merge ONE PR #113 or change ONE `main`. ONE main remains `d35db95153f6ddd79885494c72f5aee16c899751`; ONE PR #113 remains OPEN / DRAFT / UNMERGED at HEAD `64c490e9045aa29506772f74e3697a63a66b9695`. CircleCI `ci/circleci: one-linux` on that exact ONE SHA was PENDING at 2026-11-19T16:24:23Z (workflow `b16121d3-51f0-4297-bb05-16e15b0434ea`, job `148c47ea-a1ac-4574-8a61-1980d6c5a55a`). No CircleCI connector/action is available in this session; no provider logs or terminal status are claimed.

Next: poll the six protected verifier runs above, inspect failed-step logs if any, and update this checkpoint only with terminal exact-SHA evidence. Do not repeat already-passing PR-branch checks or protected E4 without relevant input changes.

## Protected workflow terminal-result correction — 2026-11-19 16:32Z

The first protected-branch push workflows have now reached terminal results. This section supersedes the earlier IN PROGRESS labels above where the exact run is now terminal.

- Candidate artifact integrity #44566172841: SUCCESS on merge commit 42feff8bc11d9b17d04ac9cff4abea4e80a7a832; exact job log confirms Linux and Windows candidate metadata use Rust/Cargo 1.100.0.
- SEC-05 #44566187162: SUCCESS on merge commit d539a162aeed9d22988c7ffb0c7a893e8d33f571; Linux job 135708430394 and Windows job 135708430883 SUCCESS. Logs show bounded APT setup, Linux interop tests 12 passed, full one-core suite Linux 148 passed / Windows 133 passed, and SEC-05 static fail-closed guards completed.
- Windows Native Backend Runtime #44566197814: SUCCESS on merge commit 4ae84bad84ddacf169b9f25fa4c78581ab2b4bc4; Windows Server 2025 job 135708473420 verified exact source 722d662, Rust/Cargo 1.100.0, PE32+ AMD64, runtime exit 0, output Budi, exact-SHA manifest.
- Focused stdlib/database #44566212982: SUCCESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4; log shows stdlib 6/6, core pipeline 6/6, conformance 5/5, database unit 1/1, database vertical slice 9/9, one-core 148/148, Clippy PASS.
- E1 Windows #44566212997: SUCCESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4; log shows stdlib 6/6, core pipeline 6/6, conformance 5/5, one-core 133/133, Clippy PASS.
- E1 cross-platform #44566212975: still IN PROGRESS on final protected HEAD b14abf0020472dc45842be30854e0a09317d6cb4. Windows job 135708526901 SUCCESS; Ubuntu job 135708526288 has completed APT/toolchain setup and is executing full workspace tests. No overall E1 cross-platform PASS until Ubuntu completes and the workflow is terminal.

The earlier fixed-weight gate #44519577312 remains FAILURE; no new gate run was dispatched while E1 cross-platform is active. The gate additionally requires row-level verified evidence, checked DoD, and protected source-bound package provenance release. Do not change fixed weights, DoD checkboxes, canonical pin, or dispatch package release to force acceptance. The canonical source pin remains 722d662e7a81711ba3607d26571f4048a292b3ed.

ONE PR #113 HEAD d20036c0ad7b00caf6b68e4807102c6ee3b895a4 remains OPEN / DRAFT / UNMERGED. CircleCI ci/circleci: one-linux remains PENDING on that exact SHA at 2026-11-19T16:30:42Z (workflow fc7039a6-8cde-464b-8c06-387e291d6d67, job 1a030227-696e-490d-bb16-dd288947976d). The previous ONE SHA 64c490e... was SUCCESS, but evidence does not transfer. No CircleCI CLI/provider connection is exposed in this session. ONE main remains d35db95153f6ddd79885494c72f5aee16c899751; Issue #104 remains OPEN / NOT ACCEPTED.

No architecture diagram changes are required for this verifier-workflow-only change. PR #50 remains documentation-only and draft pending review.
