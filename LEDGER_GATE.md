# ONE Fixed-Weight Ledger Gate

This repository now has a dedicated GitHub Actions gate that checks the ONE completion ledger against the exact source SHA pinned in `CANONICAL_COMMIT.txt`.

- Workflow: [ONE Fixed-Weight Ledger Gate](https://github.com/panglimanetizen01/one-windows-verification/actions/workflows/ledger-gate.yml)
- Workflow source: `.github/workflows/ledger-gate.yml`
- Verifier: `tools/verify_completion_ledger.py`
- Unit tests: `tests/test_verify_completion_ledger.py`
- Source ledger: `panglimanetizen01/one/docs/verification/one-completion-ledger.md`
- Definition of Done: `panglimanetizen01/one/docs/verification/DEFINITION_OF_DONE.md`

## What the gate enforces

1. Exactly the fixed F1–F6, C1–C6, and E1–E6 ledger rows are present.
2. Fixed row weights total 100; row denominators match those weights; implementation/verified totals agree with the ledger's TOTAL row.
3. Verified points cannot exceed implementation points or the row's fixed weight.
4. The independent evidence index names the exact pinned source SHA.
5. Every Definition-of-Done checkbox is checked before final acceptance.
6. Every non-zero-weight row must have all its verified points and a VERIFIED status before the gate can report `PASS GREEN LOCKED — FINAL RELEASE`.

The gate queries the current independent workflow runs and resolves the pinned source SHA at each run's mirror commit. It requires successful cross-platform, distro, focused, lockfile, artifact-integrity, and Android runtime jobs for the exact source SHA, plus a successful protected source-bound release run. The gate does not award points automatically and does not treat the existence of a workflow, a green unrelated job, a checksum-only artifact, or evidence from an older source SHA as acceptance. It exits non-zero when required acceptance is missing, so a failed gate is an explicit **NOT PASSED**, not an infrastructure success.

## First live audit

- Latest full live audit: [40090572460](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40090572460)
- Pinned source SHA: `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`
- Unit tests for the verifier: **PASS** (4 tests).
- Ledger arithmetic: **100 total fixed-weight points; 91/100 implementation; 60/100 verified**. The row sum agrees with the ledger TOTAL row.
- Acceptance gate: **NOT PASSED**, correctly. The Definition of Done has 10 unchecked items; E1–E6 currently contribute 0 verified points. The gate logs identify the unaccepted rows rather than allowing a manual percentage edit to manufacture 100%. Live checks also report the Android run still in progress and the canonical release-run API returning HTTP 403 to the current read token; neither is treated as a pass.

## How to rerun

Push a change to the `verification` branch or open the workflow and select **Run workflow**. The workflow checks out the exact SHA from `CANONICAL_COMMIT.txt`, runs its unit tests, then evaluates the source ledger and Definition of Done. To turn the gate green, close the actual E1–E6 acceptance items and provide exact-SHA evidence; do not change fixed weights or mark rows verified without that evidence.


## Live gate diagnosis — 2026-11-18

The gate is currently **NOT PASSED / BLOCKED BY INPUT INTEGRITY**, not green:

- Run `44240745287`: one unit test was stale; it expected `CANONICAL_COMMIT.txt` in the Windows native workflow although that workflow intentionally reads `WINDOWS_SOURCE_COMMIT.txt`. Fixed in verifier commit `66af5cbc9805f95b5d13c192ce5989bfe8d2336c`.
- Run `44241595784`: all 15 unit tests passed after the correction, then the live gate stopped because the pinned ONE source SHA `e50748a1b25922d9090eba1f5fb90548d7c7d003` does not contain the configured ledger path `docs/verification/one-completion-ledger.md`; the configured DoD path is absent too.
- Current PR #110 source HEAD `871a39967db315c695a642f527c41c7172922201` also lacks those two fixed-weight gate inputs. The similarly named `one-v0.1-evidence-matrix.md` and `one-v0.1-implementation-status.md` are not format-equivalent and must not be substituted.
- Historical copies exist at `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`, but using them silently would bind a current acceptance decision to stale source documentation. No such fallback is permitted.

Required repair: restore/re-author the fixed-weight ledger and Definition of Done in a current, explicitly versioned ONE candidate; keep the E4 security pin separate from the ledger-documentation pin so repairing the ledger does not prematurely trigger security verification against an incomplete implementation. Until that separation and source docs exist, this workflow must remain non-green and no completion score is promoted.


## Ledger document pin separation — 2026-11-18

The fixed-weight ledger and Definition of Done are maintained on ONE PR #103's documentation branch, while `CANONICAL_COMMIT.txt` is the independent E4/security candidate pin. These are intentionally different source revisions. `LEDGER_SOURCE_COMMIT.txt` now pins the exact PR #103 documentation SHA `fde2b81b2f63743b990e9fbbade47ec8076e2151`; `ledger-gate.yml` checks out that revision into `ledger-source/` and reads the two canonical ledger documents there. The candidate code SHA remains read from `CANONICAL_COMMIT.txt` and continues to drive live exact-SHA workflow/release evidence checks. This resolves the missing-file precondition without moving the E4 pin or weakening any acceptance rule. The gate is still expected to remain NOT PASSED while DoD has 10 unchecked items and the ledger has 0/100 verified points.


### Pin-format correction — 2026-11-18

Run `44242265068` stopped at the new 40-character SHA validation because the initial ledger pin omitted one character. `LEDGER_SOURCE_COMMIT.txt` is corrected to `fde2b81b2f63743b990e9fbbade47ec8076e2151`; the E4 `CANONICAL_COMMIT.txt` remains untouched. This run did not reach checkout or acceptance evaluation.


## Ledger checkout ref interpolation correction — 2026-11-18

- Verifier run `44242448522` reached the dedicated ledger checkout, but the checkout step passed a literal leading backslash before the GitHub Actions expression (`\${{ steps.ledger.outputs.sha }}`). Git interpreted the resulting `\fde2...` as an invalid refspec and checkout failed before tests.
- Root cause: the workflow and its source assertion were generated from a raw template string that preserved the escape character. Remove the literal backslash so Actions evaluates the `ref` and `token` expressions normally.
- The exact ledger-document pin is valid and remains `fde2b81b2f63743b990e9fbbade47ec8076e2151` (40 lowercase hex characters). The shared E4/security pin remains `e50748a1b25922d9090eba1f5fb90548d7c7d003`.
- No source implementation, ledger points, DoD checkboxes, or acceptance criteria changed. This is a workflow expression syntax fix only.


## Current ledger/DoD document source refresh — 2026-11-18

- ONE PR #103 documentation branch advanced to exact HEAD `d6c382a245c49a028bc60809f22ca956c7f894cc` with a fresh live-state checkpoint in both `docs/verification/one-completion-ledger.md` and `docs/verification/DEFINITION_OF_DONE.md`.
- `LEDGER_SOURCE_COMMIT.txt` is updated to this exact 40-character documentation SHA. The shared `CANONICAL_COMMIT.txt` remains unchanged at `e50748a1b25922d9090eba1f5fb90548d7c7d003` for the E4/security candidate.
- Previous verifier run `44242590734` evaluated ledger docs SHA `fde2b81b2f63743b990e9fbbade47ec8076e2151` and returned the expected NOT PASSED result: 16/16 unit tests passed, 92/100 provisional implementation, 0/100 verified, 10 unchecked DoD items, failed exact-SHA workflow evidence on the historical candidate, and no protected package-provenance release run.
- The new pin triggers a fresh exact-document checkout and ledger evaluation. This does not change weights, checkboxes, security implementation, or E4 source pin.


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
