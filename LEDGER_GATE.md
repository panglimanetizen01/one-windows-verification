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


## ONE PR #113 platform metadata candidate — exact-SHA evidence — 2026-11-20

- Branch-local `CANONICAL_COMMIT.txt` pins ONE source `c7f460a4e38be61de635ad5af9f7ff987a941f01`; verifier PR #51 is a diagnostic OPEN / DRAFT / UNMERGED PR. Protected `verification` branch remains `b14abf0020472dc45842be30854e0a09317d6cb4` with protected canonical pin `722d662e7a81711ba3607d26571f4048a292b3ed` unchanged.
- E4 run #44585270928 SUCCESS on the exact candidate: Unix no-follow/resource-bound and Windows reparse/handle jobs passed; Windows native `NtCreateFile + OBJ_DONT_REPARSE` probe passed on Windows Server 2025 build 26100. The added test `filesystem_adapters_advertise_only_platforms_with_native_backends` explicitly passed on Linux and Windows (1 passed / 0 failed each).
- Linux distro run #44585282690 SUCCESS on Ubuntu 24.04 and Debian 12, including workspace tests and corrected filesystem vertical-slice CLI integration. E1 Windows acceptance run #44585282432 SUCCESS.
- Remaining aggregate cross-platform, Windows native runtime, Android runtime, SEC-05, E1 milestone and artifact-integrity workflows were IN_PROGRESS/PENDING at this checkpoint. CircleCI on source `c7f460a...` was PENDING; provider step logs unavailable.
- The prior source `7581a1b...` exposed a CLI integration mismatch because the interpreter passed `PlatformKind::Any`; candidate `c7f460a...` fixes this by using `PlatformKind::current_host()` and updates the integration test to use the actual host platform.
- Filesystem adapter metadata is now Linux-only on Linux, Windows-only on Windows, and empty on Android/macOS/other unsupported targets. This does not add Android/macOS filesystem support. Issue #104 remains OPEN / NOT ACCEPTED; no protected pin or ledger weight is promoted.
