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
