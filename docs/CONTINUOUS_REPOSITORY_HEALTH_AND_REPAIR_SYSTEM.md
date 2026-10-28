# Continuous Repository Health & Repair System — Design and Evolution Plan

Status: **proposal / implementation plan**  
Created: 2026-10-28  
Canonical source under observation: `panglimanetizen01/one`  
Current candidate at time of writing: `b8a6888e68c4432c044282be998de468f7a9c31e`  
Independent verifier branch: `verification`

> This document defines a continuously extensible diagnostic and guarded-remediation system. It is not evidence that any proposed detector or repair automation is already implemented. It awards no acceptance-ledger points and does not authorize merge or release.

## 1. Goal

Evolve one-off diagnostic notes into a maintainable system that continuously discovers, explains, tracks, and—where safe—repairs repository anomalies across source code, tests, workflows, contracts, generated artifacts, package metadata, and documentation.

The system must distinguish:
- **Observed fact** — directly supported by a file, command result, workflow job, log, or API response.
- **Inference** — a likely explanation, with confidence and supporting evidence.
- **Recommendation** — a proposed next action, not yet executed.
- **Repair attempt** — a change made on an isolated branch or worktree.
- **Verified repair** — the repair passed its declared checks on the exact resulting commit.
- **Unresolved** — evidence is missing, contradictory, inaccessible, or inconclusive.

Missing logs, absent runner steps, stale workflow snapshots, and unavailable external services must never be silently reclassified as source-code failures or passes.

## 2. Coverage catalogue

The detector catalogue is modular. Each detector produces a stable finding ID, scope, evidence references, confidence, severity, remediation guidance, and regression check.

| Detector family | Examples to detect | Minimum evidence |
|---|---|---|
| Syntax and parsing | Rust/TOML/YAML/JSON/Markdown parse errors, malformed workflow expressions, broken front matter | Parser or linter output with file and location |
| Build and tests | compile failures, failing tests, warnings denied, flaky/reproducibility issues | Exact command, exit code, environment, commit SHA |
| Broken paths and references | missing files, invalid links, broken relative paths, stale workflow references | Resolved path/link result and source location |
| Contract drift | spec/API/schema/workflow/package manifest disagree; undocumented behavior; mismatched names or fields | Both sides of the contract and a normalized diff |
| Stale artifacts | evidence pinned to old SHA, old generated files, outdated lockfiles, old reports, stale snapshots | Declared source SHA/time versus current source SHA/time |
| Documentation hygiene | README claims that no longer match code, stale setup commands, outdated examples, inconsistent Markdown tables/headings | Rule/check plus the exact conflicting source |
| Workflow/CI anomalies | workflow never starts, runner ID absent/zero, no steps/logs, invalid permissions, missing artifacts, duplicate triggers | Run/job metadata and log availability; distinguish service uncertainty |
| Overlapping or dead paths | duplicate workflows, shadowed routes, competing configuration, redundant scripts, dead feature flags | Dependency/call/config graph plus reachability evidence |
| Security and release provenance | untrusted publisher, broad trigger on release workflow, missing permissions/attestations, synthetic trust mistaken for production | Workflow policy, protected environment evidence, signature/identity verification |
| Dependency and supply-chain drift | inconsistent dependency versions, unreviewed lockfile changes, vulnerable/outdated packages | Lockfile/manifests and authoritative scanner output |
| Artifact integrity | checksum mismatch, missing bundle members, non-deterministic outputs, metadata disagreement | Reproducible digest/manifest comparison |
| Evidence and acceptance ledger | stale pin, unlinked evidence, score/DoD inconsistency, unscoped PASS, old result credited to new SHA | Ledger schema validation and exact-SHA provenance checks |
| Maintenance anomalies | TODO/FIXME accumulation, orphaned files, duplicate docs, expired suppressions, unowned checks | Inventory and explicit age/ownership policy |

New detector families should be added through the same detector contract; no detector should need to rewrite the entire engine.

## 3. Finding record contract

Each finding must be machine-readable and retain a human-readable explanation. Recommended fields:

- `finding_id`: stable identifier derived from detector + normalized location/rule (not from mutable prose).
- `detector_id`, `detector_version`, `schema_version`.
- `status`: `open`, `triaged`, `repair_proposed`, `repairing`, `verification_pending`, `resolved`, `accepted_risk`, `blocked`, or `reopened`.
- `severity`: `critical`, `high`, `medium`, `low`, `info`.
- `confidence`: numeric or bounded enum, with the evidence basis stated.
- `category`, `summary`, `impact`, `affected_paths`, `first_seen`, `last_seen`.
- `candidate_sha`, `base_sha`, `workflow_run_ids`, `job_ids`, `artifact_refs`, and log links where available.
- `observations[]`, `inferences[]`, `recommended_actions[]`, `repair_attempts[]`.
- `verification_plan`: exact checks required to prove resolution.
- `owner`, `expiry` for accepted-risk suppressions, and links to follow-up issues/PRs.

Never store secrets, tokens, signing keys, private environment values, or sensitive runner data in the finding record. Redact secrets from captured logs before persistence.

## 4. End-to-end lifecycle

1. **Inventory** — discover source files, workflows, contracts, docs, generated outputs, manifests, and evidence indexes.
2. **Collect** — run deterministic local checks and query workflow/job/artifact metadata. Record the exact candidate SHA and tool versions.
3. **Normalize** — convert raw outputs into the finding contract and deduplicate equivalent findings without discarding distinct evidence.
4. **Correlate** — connect symptoms across files and runs (for example, a missing artifact plus a workflow that never started).
5. **Classify** — separate source defect, test defect, configuration defect, infrastructure/service issue, stale evidence, policy block, and unknown.
6. **Prioritize** — rank by impact, confidence, blast radius, recurrence, and whether the issue blocks acceptance.
7. **Plan** — generate a minimal patch proposal and a verification plan. Explain why the change addresses the observed evidence.
8. **Repair safely** — use an isolated branch/worktree; preserve unrelated changes; never write to protected branches directly.
9. **Verify** — rerun detector-specific checks, relevant regression tests, and required exact-SHA matrix. A changed SHA invalidates evidence scoped to the previous SHA unless a rule explicitly establishes otherwise.
10. **Review** — present diff, findings closed/opened, risks, test results, and unresolved items for human review.
11. **Record and learn** — append outcome and recurrence data; update the detector catalogue only through reviewed changes.
12. **Reconcile** — update docs, evidence index, issue/PR links, and acceptance ledger only when supported by fresh evidence.

## 5. Remediation autonomy and safety tiers

### Tier 0 — Observe only
Examples: collect run metadata, enumerate files, detect broken links, report stale pins. No repository mutation.

### Tier 1 — Safe proposal
Examples: draft a Markdown correction, suggest a missing test, prepare a patch diff. Human approval required before writing.

### Tier 2 — Isolated low-risk repair
Examples: fix an unambiguous broken relative link, normalize Markdown formatting, regenerate a clearly generated index. Only on a dedicated branch; must include tests/checks and a reviewable diff.

### Tier 3 — High-impact repair
Examples: modify workflow triggers/permissions, package manifests, public contracts, security controls, signing/provenance configuration, release automation, or acceptance weights. Require explicit human review and focused evidence. Do not self-approve.

### Tier 4 — Protected action
Examples: merge, deploy, sign, publish, change protected environment settings, or use production credentials. The diagnostic system must not autonomously execute these actions. It may assemble a readiness report; existing branch protections, required reviewers, environment approvals, and exact-SHA acceptance gates remain authoritative.

**Fail closed:** if a repair changes code, workflow behavior, contracts, trust configuration, or acceptance criteria, no prior test result is automatically credited to the new SHA. Never weaken a gate, suppress a detector, alter weights, or mark a checklist complete merely to make the system green.

## 6. Distinguishing CI infrastructure failures from source defects

For every workflow failure, collect (where available):
- workflow/run ID, attempt number, event, ref and checked-out SHA;
- job conclusion, runner ID/name/labels, start/end time, step list;
- annotations, log availability and artifact availability;
- whether any command actually executed;
- retry history and comparison with a known healthy run.

Classify as:
- `source_test_failure` only when a source/build/test command ran and its output supports that diagnosis;
- `job_start_or_runner_failure` when evidence shows the job did not reach executable steps;
- `log_or_artifact_unavailable` when the result cannot be inspected;
- `workflow_configuration_failure` when configuration evidence establishes a defect;
- `external_service_failure` only with evidence supporting the service diagnosis;
- `unknown` otherwise.

A `BlobNotFound` response establishes that the requested log blob was unavailable; by itself it does not establish why the job failed. Retrying is an experiment, not a diagnosis. Repeated failure without new evidence should trigger a different diagnostic path (inspect job metadata, workflow YAML, repository Actions policy, runner availability, or request an authorized administrator review), not endless identical retries.

## 7. Staleness and contract checks

Every generated report/evidence record should declare its inputs and freshness rule. At minimum:
- Source-bound evidence must record the exact source SHA and the checked-out SHA must match.
- Workflow names, paths, artifacts, test commands, and output filenames should be checked against actual repository files.
- Documentation claims about CLI flags, API names, supported platforms, environment variables, package formats, and release behavior should be cross-checked against the implementation or normative contract.
- Generated files should identify their generator and reproducible command where feasible.
- Historical evidence remains preserved but clearly marked historical; never silently delete it or present it as current.
- A suppression must include rationale, owner, creation date, and expiry/review date.
- Link checking should distinguish private/inaccessible URLs from confirmed 404s; network errors are not automatically broken links.
- Markdown checks should cover parse/lint, relative links, heading/table structure, fenced code blocks, and example consistency.
- Duplicate/overlap checks must show evidence of collision or shadowing; similarity alone is not proof of a bug.

## 8. Prioritization and reporting

Recommended priority formula is configurable and versioned, not an acceptance score:

`priority = impact × confidence × recurrence_factor × acceptance_blocker_factor`

Use explicit bounded scales and show the inputs beside the result. Do not mix this operational priority with the project's fixed-weight verification ledger.

Every run should produce:
1. a short executive summary;
2. findings grouped by severity and subsystem;
3. newly detected, recurring, resolved, reopened, and suppressed findings;
4. exact evidence links and SHA;
5. safe repair candidates with expected blast radius;
6. verification commands and outcomes;
7. blockers requiring repository administrator or human approval;
8. a machine-readable JSON/SARIF-compatible report where practical.

A report must say **unknown** when it cannot establish the cause. It must never invent a root cause, test result, owner, or repair success.

## 9. Incremental implementation roadmap

### Phase A — Reliable evidence foundation
- [ ] Define and version the finding schema.
- [ ] Build a read-only repository inventory and evidence collector.
- [ ] Validate source SHA, checked-out SHA, workflow run metadata, job steps, logs, and artifacts.
- [ ] Add a stale-evidence detector and explicit historical/current labels.
- [ ] Add unit tests with fixtures for missing logs, absent steps, stale pins, and contradictory statuses.

### Phase B — Static integrity and contract checks
- [ ] Add syntax/lint checks for supported file types.
- [ ] Add broken path/link and Markdown structure checks.
- [ ] Compare workflow references, manifests, API/spec names, generated artifacts, and documentation claims.
- [ ] Detect duplicated workflow triggers, shadowed configuration, orphaned files, and expired suppressions.
- [ ] Provide stable finding IDs and deduplication tests.

### Phase C — Correlation and triage
- [ ] Correlate recurring errors across runs and files.
- [ ] Separate facts from hypotheses and expose confidence.
- [ ] Generate ranked repair plans with minimal reproduction steps.
- [ ] Track recurrence, false positives, time-to-diagnosis, and successful repair rate.

### Phase D — Guarded repair loop
- [ ] Implement dry-run patch proposals first.
- [ ] Apply only allowlisted Tier 2 repairs on isolated branches.
- [ ] Run targeted regression checks plus broader required checks.
- [ ] Require human review for Tier 3/4 changes.
- [ ] Preserve complete before/after diffs and failed repair attempts.

### Phase E — Continuous evolution
- [ ] Version detector rules and finding schema independently.
- [ ] Add regression fixtures for every confirmed incident.
- [ ] Retire or revise detectors only through reviewed changes with migration notes.
- [ ] Periodically audit false positives, blind spots, stale suppressions, and detector coverage.
- [ ] Publish a changelog and compatibility policy for reports and detector plugins.

## 10. Definition of done for the diagnostic system itself

The system is not considered production-ready until:
- [ ] Findings are reproducible from a recorded commit and toolchain.
- [ ] Missing evidence yields an explicit unknown/blocked state, not a pass.
- [ ] Each finding links to source locations and supporting evidence.
- [ ] Stale source-bound evidence is detected automatically.
- [ ] At least one fixture test exists for every detector family that ships.
- [ ] Repairs are isolated, diffed, and verified on the resulting SHA.
- [ ] Protected actions are technically excluded from autonomous repair execution.
- [ ] Reports preserve history and do not silently overwrite unresolved findings.
- [ ] Documentation describes current implemented behavior, not planned features.
- [ ] A maintainer can reproduce a report and understand why each finding was raised.

## 11. First implementation slice recommended

Start with a **read-only integrity scanner**, not automatic code rewriting. Its first release should:
1. verify candidate pin and checked-out SHA consistency;
2. inspect workflow/run/job state and distinguish absent steps/logs from test failures;
3. find stale evidence links and references to old SHAs;
4. check local links, required files, and Markdown structure;
5. validate the fixed-weight ledger schema without modifying scores;
6. emit a JSON report plus a concise Markdown summary;
7. test all classifications with fixture data.

This directly targets the current observed failure mode—repeated CI runs with no executable steps and unavailable logs—while laying a safe foundation for broader syntax, contract, overlap, documentation, and repair detectors.

## 12. Current blockers and boundaries

This is a design artifact only. It does not establish that the proposed scanner exists, that any new detector has run, or that any current finding has been repaired. The current candidate acceptance gate remains authoritative. The existing canonical CI job-start/log retrieval issue, incomplete E1/E2/E6 acceptance, and missing protected production provenance must continue to be tracked as separate blockers. No merge or production release is implied.
