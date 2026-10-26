# ONE v0.1 — Candidate Verification Index

**Canonical repository:** [panglimanetizen01/one](https://github.com/panglimanetizen01/one)  
**PR:** [#80](https://github.com/panglimanetizen01/one/pull/80) — open, draft, unmerged  
**Current source SHA:** `78b9436c318032b1c19a4e5c110142fffc58b4d5`  
**Fixed-weight ledger:** [one-completion-ledger.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md)  
**Release gate:** **NOT PASSED** — fixed-weight ledger remains 91/100 provisional implementation and 64/100 verified in the last recorded scoring; this is not a final acceptance score. The current independent verification pin is `78b9436c318032b1c19a4e5c110142fffc58b4d5`. Exact-SHA Linux distro (Ubuntu 24.04 + Debian 12), Ubuntu/Windows Server 2025, E4 Unix/Windows adversarial tests, artifact integrity, Android AArch64 build, and Android cross-build/contract jobs have passed their scoped checks. **Android API 35 arm64-v8a runtime execution is not yet proven**: run [40264206706](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264206706) remains queued. The latest ledger gate [40265232307](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40265232307) failed closed (latest rerun; the previous run [40265144750](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40265144750) also failed). Do not award full E3/E4 rows or mark the overall release accepted from scoped passes; the protected canonical release evidence/permission gap also remains unresolved.

This file is the live exact-SHA evidence index. A workflow run counts only if its job logs assert the current source SHA and all required steps pass. Prior-SHA results are historical evidence, not current-candidate acceptance.


### SEC-05 subprocess guard — exact pinned source

Run [40264131009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264131009) completed successfully on Linux and Windows Server 2025, and both job logs explicitly check out source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`. Existing subprocess contract tests, the full `cargo test --locked -p one-core` suite, changed-file formatting, and the lab's static timeout/output-limit guard passed on both jobs. The Windows guard's checks also passed for the race-free process-creation markers (`CreateProcessW`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute`, `DeleteProcThreadAttributeList`, and `PROC_THREAD_ATTRIBUTE_JOB_LIST`) and reject `AssignProcessToJobObject` spawn-then-assign use. These are scoped CI results; they do not alone prove every descendant-process race, inherited-pipe, timeout, flood, and cleanup acceptance scenario. Keep SEC-05 and E4 unaccepted until the required dynamic adversarial assertions and ledger rows are evidenced.

### Latest ledger gate readback — 2026-10-26

Run [40265232307](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40265232307) checked out exact source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`. Verifier unit tests passed, but the fail-closed gate returned **NOT PASSED**: 9 unchecked Definition of Done items; E3 verified 0/8 and E4 verified 0/6 in the ledger; Android API 35 runtime run [40264206706](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264206706) remains queued; canonical release-workflow evidence cannot be read because `CANONICAL_READ_TOKEN` lacks required Actions read permission and anonymous fallback returns 404. Do not convert scoped CI passes into full row credit or weaken the gate to make it green.

## Current pinned candidate — `78b9436c318032b1c19a4e5c110142fffc58b4d5`

This is the canonical source SHA in `CANONICAL_COMMIT.txt` at the current `verification` branch head. The verifier branch SHA and source SHA are different identifiers.

| Gate | Run | Verified result |
|---|---|---|
| Linux distro matrix (Ubuntu 24.04 + Debian 12) | [40264090050](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264090050) | **PASS** — both job logs explicitly bind to source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5` |
| Cross-platform Ubuntu + Windows Server 2025 | [40264090066](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264090066) | **PASS** — both job logs explicitly bind to the pinned source SHA |
| E4 adversarial filesystem/resource-bound regression | [40264259048](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264259048) | **PASS for executed assertions only** — Unix and Windows jobs succeeded; logs bind to the pinned source SHA. This is not blanket proof of every filesystem/race acceptance criterion |
| Android AArch64 device artifact build | [40264171337](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264171337) | **PASS build only** — AArch64 ELF header validated; not Android runtime proof |
| Android API 35 AArch64 cross-build/contract fallback | [40264234301](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264234301) | **PASS for cross-build/contract only** — log explicitly says no Android ELF execution occurred |
| Android API 35 arm64-v8a ELF runtime | [40264206706](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264206706) | **QUEUED / NOT ACCEPTED** — rechecked 2026-10-26; job `121382904739` is still queued, with no guest boot, exit code 0, or `ONE_NATIVE_BACKEND_OK` evidence |

| SEC-05 subprocess timeout/output/cleanup tests | [40264131009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264131009) | **PASS for executed dynamic tests** — Linux job log pins exact SHA and records six passing interop tests including denied capability/no spawn, aggregate output cap, stdout/stderr flood bounds, and timeout with child reaped; full one-core suite also passed. Windows job succeeded and log explicitly cautions static launch-path markers do not replace dynamic descendant-race tests |
| E4 subprocess resource guard audit | [40264131027](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264131027) | **PASS for guard check only** — not a substitute for dynamic runtime evidence |
| Fixed-weight ledger gate | [40264648659](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264648659) | **FAILURE / NOT PASSED** — acceptance gate remains fail-closed; do not manufacture missing ledger or protected-release evidence |

The source pin and this evidence index are separate from the verifier branch head. Historical sections below document older source revisions and must not be counted as evidence for this current pin unless a run explicitly checked out this exact SHA.


## Newest candidate — `2ea52d4c39aac98be8678a2e1ac0b67997610c22`

The protected release workflow now enforces byte-identical package builds, validates signed source/artifact metadata, and emits a portable relative-path SHA-256 manifest that is checked before upload. The independent verification pin has been advanced to this exact source revision.

| Gate | Run | Result |
|---|---|---|
| E2 package/provenance synthetic-key lab | [40154415287](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415287) | **PASS** — exact source SHA `2ea52d4c39aac98be8678a2e1ac0b67997610c22`; provenance/CLI tests, stale-lock rejection, release build, two-build byte determinism, V2 signature/source verification, untrusted publisher rejection, modified artifact/metadata rejection, and artifact retention passed |
| Independent artifact checksum inspection | [artifact 12583637983](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415287/artifacts/12583637983) | **PASS** — downloaded archive digest `sha256:9c85b60d6806393236a681ec13201fa0138c002c9dccb4c5e1ab85d59cacea84`; independently ran `sha256sum --check SHA256SUMS` and both package and provenance sidecar verified. Package SHA-256 `fb1f5d28e8f95ba89332739c69f2602115c24701ab091334659366864fc126f5`; sidecar SHA-256 `b15307e79dd701613422b58d086192bb8de7e5bcb7ee87540a3e542fedae50e2` |
| Focused standard library/database | [40154415289](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415289) | **PASS** |
| Cargo lockfile bootstrap | [40154415296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415296) | **PASS** |
| Cross-platform, Linux distro, candidate artifact, Windows E1, Android | [matrix runs](https://github.com/panglimanetizen01/one-windows-verification/actions) | **IN PROGRESS** at index update; no credit until each required run completes on this exact source SHA |

**Acceptance status:** E2's independent synthetic-key acceptance suite passes on the current SHA, but the E2 ledger row remains **0/8 verified** until the protected `one-release` workflow runs with independently provisioned production trust material. The canonical repository's own E2 run and retry still fail before any job steps; logs/step data are absent, so this is an Actions infrastructure blocker, not a test pass. The available GitHub connection cannot configure repository secrets/environment protection or dispatch the protected workflow. The global release gate remains **NOT PASSED**.

## Latest candidate — `6478fe571b70f6ac088603ce955270fd47f9b0f2`

This source revision hardens the protected release workflow to build the package twice and fail if package bytes differ, validate the signed sidecar's source revision/digests/format/dependency model, and verify the generated SHA-256 manifest. The exact-SHA matrix was started after the source pin was updated. Do not treat in-progress jobs as passes.

| Gate | Run | Status at index update |
|---|---|---|
| E2 package/provenance synthetic-key lab | [40154316866](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316866) | **IN PROGRESS** — provenance/CLI tests and stale-lock rejection passed; package build and signature/tamper checks were still running |
| Cross-platform Ubuntu + Windows Server 2025 | [40154316968](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316968) | **IN PROGRESS** |
| Focused standard library/database | [40154316898](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316898) | **IN PROGRESS** |
| Linux Ubuntu/Debian conformance | [40154316877](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316877) | **IN PROGRESS** |
| Candidate artifact integrity | [40154317003](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154317003) | **IN PROGRESS** |
| Cargo lockfile bootstrap | [40154316809](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316809) | **PASS** |
| Fixed-weight ledger gate | [40154316876](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154316876) | **NOT PASSED** — this attempt identified the stale evidence index, unfinished matrix jobs, 9 unchecked Definition-of-Done items, unaccepted full E1/E2/E3/E4/E6 rows, and missing `Actions: read` access for the private canonical repository. No completion points are awarded. |

The protected canonical `one-release` workflow has not been exercised. The synthetic lab uses a disposable test key and cannot replace the protected production signing/trust-store gate. The candidate release gate remains **NOT PASSED**.


## Current canonical source revision — `dca9a22c242905b97275161d9fdda933b986ec0d`

This candidate contains documentation-only E2 ledger/checkpoint updates based on the preceding tested code snapshot. Exact-SHA verification has now been rerun against this canonical SHA; all completed matrix jobs below explicitly pin this SHA. Android runtime remains in progress.

| Gate | Run | Current exact-SHA status |
|---|---|---|
| Focused Standard Library/database + package provenance + package/lock regression | [40110118430](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40110118430) | **PASS** — exact-SHA checkout; UTC/database regressions, CLI signature/trust/tamper, full `package_provenance::tests`, deterministic artifact bytes, module-lock generation and stale-lock rejection, and unsupported-dependency fail-closed tests all passed |
| Package provenance end-to-end lab (synthetic fixture key only) | [40110376210](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40110376210) | **PASS** — built from exact source SHA; produced `.onepkg` + V2 sidecar + `SHA256SUMS`; trusted-store signature/source verification passed; untrusted publisher, altered artifact and altered signed metadata were rejected. Artifact ID `12565962511`, GitHub archive digest `sha256:7965d335824bed1bdb1463f214e5e89b2f6e251f73967a989a993ff43d4cbb59`. **Not** a production protected release; fixture key only. |
| Cargo lockfile bootstrap | [40108646762](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646762) | **PASS** — deterministic lockfile bootstrap on exact canonical SHA |
| Linux distro conformance | [40108646764](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646764) | **PASS** — Ubuntu 24.04 and Debian 12 jobs passed |
| Cross-platform Ubuntu + Windows Server 2025 | [40108646717](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646717) | **PASS** — Ubuntu and Windows Server 2025 jobs completed successfully |
| Candidate artifact integrity | [40108646691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646691) | **PASS** — exact-SHA Linux/Windows bundles discovered; archive digests, embedded manifests, metadata, executable formats validated |
| Android AArch64 ELF execution | [40108646751](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646751) | **IN PROGRESS** — API 35 arm64 emulator boot has not yet produced an ELF execution result |
| Fixed-weight ledger gate | [40109744699](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40109744699) | **NOT PASSED** — latest gate confirmed 9 unchecked DoD items, E1/E2/E3/E4/E6 full-row acceptance missing, Android runtime still in progress, and canonical protected-release evidence inaccessible with current token permissions |

### Retained package inspection — exact source SHA `dca9a22c242905b97275161d9fdda933b986ec0d`

- E2E lab run: [40110376210](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40110376210) — **PASS**.
- Retained artifact: [GitHub Actions artifact `one-provenance-lab-dca9a22c242905b97275161d9fdda933b986ec0d`](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40110376210/artifacts/12565962511); artifact ID `12565962511`; archive digest `sha256:7965d335824bed1bdb1463f214e5e89b2f6e251f73967a989a993ff43d4cbb59`.
- Package SHA-256: `fb1f5d28e8f95ba89332739c69f2602115c24701ab091334659366864fc126f5`.
- Provenance sidecar SHA-256: `6004148f252f84463e295be1d6a3beb1c8f32dc5d6a078945ad8d94bb83b9e21`.
- Sidecar records source revision `dca9a22c242905b97275161d9fdda933b986ec0d`, source-tree digest `7d71a70c10d87d1c8ebe25b564462070232cfba33a9b477b3843b65529349cc3`, artifact format `OneHumanCorePackageV1`, and dependency model `empty-v0.1`. Downloaded artifact ZIP was independently inspected; `sha256sum --check SHA256SUMS` passed for both retained files.
- Trust key is the documented disposable fixture key `lab-fixture-publisher`, not a production publisher identity or protected environment secret. This pass demonstrates the package/signature/verifier path and negative cases, but **does not** satisfy the production protected `one-release` requirement. E2 remains unaccepted.

## Previous exact-SHA candidate — `15e6ac358742b89076f21e079e16aa6ca5a2124a`

The canonical source SHA for this historical matrix was pinned in `CANONICAL_COMMIT.txt`. These results remain valid only for this exact source SHA; verifier-repository commits are not source commits.

| Gate | Run | Previous exact-SHA result |
|---|---|---|
| Focused Standard Library/database + source-bound package signature | [40105784848](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784848) | **PASS** — all 26 focused steps succeeded, including E1 boundary regressions, SQLite resource/symlink tests, and CLI package-signature/trusted-publisher/tampering test |
| Cargo lockfile bootstrap | [40105784758](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784758) | **PASS** — deterministic lockfile generation succeeded |
| Linux distro conformance | [40105784831](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784831) | **PASS** — Ubuntu 24.04 and Debian 12 jobs completed successfully, including contract checks, workspace build/tests, Clippy, and real-network tests |
| Cross-platform Ubuntu + Windows Server 2025 | [40105784872](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784872) | **PASS** — Ubuntu and Windows Server 2025 jobs completed successfully; workspace, Clippy, tests, real-network, and offline verification steps passed |
| Candidate artifact integrity | [40105784844](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784844) | **PASS** — exact-SHA Linux/Windows bundles were found; archive digests, embedded manifests, metadata, and executable formats passed |
| Android AArch64 ELF execution | [40105784785](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784785) | In progress at API 30 arm64 emulator boot; no ELF execution result yet |
| Fixed-weight ledger gate | [40105784763](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40105784763) | **NOT PASSED** — gate evaluated before matrix completion; index was stale, nine DoD items unchecked, E1/E2/E3/E4/E6 unaccepted, and canonical release-workflow evidence could not be queried because the mirror token lacks Actions:read on the private canonical repository |

The focused pass proves only the API/resource-bound tests listed in its executed steps; it does not award the complete E1 row while the broader reusable-standard-library scope remains incomplete. The synthetic-key CLI test verifies signing, trusted-publisher matching, package tampering detection, and source-tree mismatch rejection, but does not prove that the protected `one-release` environment or its secrets are configured. Do not convert these scoped passes into full E1/E2 credit. Rerun the fixed-weight gate after all matrix jobs finish; the gate must remain fail-closed for unaccepted requirements.

## Historical exact-SHA matrix — source `25b9b2385281c01280b46589c3bf9346bfdc2ea4` (2026-10-24 14:22 UTC)

**Canonical source SHA:** `25b9b2385281c01280b46589c3bf9346bfdc2ea4` (branch `milestone/100-ecosystem-20261023`; PR #80 remains open/draft/unmerged). All runs below checked out this exact source SHA; the verifier repository's own head SHA is not the canonical source SHA.

| Gate | Run | Exact-SHA result |
|---|---|---|
| Focused Standard Library/database | [40102204980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204980) | PASS — focused E1 regression target and `cargo --locked clippy -p one-core --all-targets -- -D warnings` succeeded |
| Linux distro conformance | [40102204891](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204891) | PASS — Ubuntu 24.04 and Debian 12; contract checker, workspace build/tests and Clippy passed |
| Cargo lockfile bootstrap | [40102204901](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204901) | PASS — deterministic lockfile bootstrap on the exact source SHA |
| Cross-platform Ubuntu + Windows Server 2025 | [40102204904](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204904) | PASS — both jobs succeeded, workspace tests and offline checks passed |
| Candidate artifact integrity | [40102204878](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204878) | PASS — exact-SHA Linux/Windows bundles downloaded; archive digests, embedded checksums, build metadata and ELF64/PE32+ headers validated |
| Android AArch64 ELF execution | [40103088590](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103088590) | IN PROGRESS — switched verifier workflow from API 35 to smaller API 30 arm64 image after the previous emulator boot stalled. No ELF execution result yet |
| Fixed-weight ledger gate | [40102204973](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40102204973) | NOT PASSED — evaluated before the current-SHA matrix finished; evidence index was stale, 9 DoD items unchecked, E1/E2/E3/E4/E6 not accepted, and canonical protected-release workflow evidence returned 404/403 due token access |

The focused and cross-platform test matrix verifies the documented source-level built-ins (text, collections, integer arithmetic, mappings, JSON, UTC) on the pinned source SHA. It does **not** by itself award full E1 credit while the ledger's broader reusable-standard-library requirement remains marked incomplete. Android is not accepted until the workflow demonstrates actual AArch64 ELF execution and output. The canonical repository's own hosted CI still has the separately documented runner-infrastructure failure; independent mirror evidence is not relabelled as canonical CI.

### Current exact-SHA results — `a4a146ae22c6629fe606185481055b667321d203`

| Gate | Run | Result |
|---|---|---|
| Focused Standard Library/database | [40103543035](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543035) | PASS — 30 workflow steps completed; focused stdlib/database regressions and core Clippy succeeded |
| Linux distro conformance | [40103543045](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543045) | PASS — Ubuntu 24.04 and Debian 12; workspace tests, Clippy and contract checks passed |
| Cargo lockfile bootstrap | [40103542984](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542984) | PASS |
| Cross-platform Ubuntu + Windows Server 2025 | [40103543039](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103543039) | PASS — both jobs succeeded; Ubuntu 22 steps, Windows 21 steps |
| Candidate artifact integrity | [40103542987](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542987) | PASS — exact source SHA, ZIP digests, embedded manifests, metadata, ELF64 and PE32+ formats validated |
| Android AArch64 ELF execution | [40103542978](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542978) | IN PROGRESS at API 30 arm64 emulator boot; no ELF execution result yet |
| Fixed-weight ledger gate | [40103542993](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40103542993) | FAILED before the matrix completed; stale evidence and pending jobs caused a fail-closed result. Rerun after Android completes; other E1/E2/E4/E6, DoD and canonical release-token gaps still prevent global release acceptance |



## Final candidate after ledger/DoD reconciliation

Current canonical source SHA: `54f3de667e05075805fcc5cd5dc621b653075667`. The completion ledger and Definition of Done E5 references were reconciled to the passing matrix on the prior candidate. That documentation-only reconciliation creates source SHA `54f3de667e05075805fcc5cd5dc621b653075667`; a fresh exact-SHA matrix is mandatory, and the prior candidate's results below remain historical until the rerun completes:

| Gate | Exact-SHA evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40095539284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539284) | PASS — both jobs succeeded; Windows test log includes all 23 `stdlib_builtins.rs` tests passing, including the new edge-contract tests |
| Linux distro conformance | [40095539287](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539287) | PASS — Ubuntu 24.04 and Debian 12 succeeded |
| Focused stdlib/database | [40095539311](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539311) | PASS |
| Cargo lockfile bootstrap | [40095539351](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539351) | PASS |
| Linux/Windows artifact integrity | [40095539261](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539261) | PASS — both bundle digests matched GitHub metadata; embedded source SHA, toolchain metadata, checksum manifests, and ELF64/PE32+ headers validated |
| Android AArch64 ELF runtime | [40095539358](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095539358) | IN PROGRESS at emulator boot; ELF execution/output not yet observed |
| Fixed-weight ledger gate | [40095563933](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40095563933) | NOT PASSED — evaluated before all matrix jobs completed; E1/E2/E3/E4/E6 remain unaccepted and canonical release evidence token permission is still missing |

The previous candidate `6d1577e078dfcf23295afdaf41568b85d3ba07bb` passed the same cross-platform, distro, focused, lockfile, and artifact checks; it is historical. Current ledger remains 91/100 implementation and 64/100 verified. E5's row now points to the last passing matrix on `533744e33e8e95ab83e239c2751846701b2604ea`; rerun this candidate before treating that evidence as current. Do not award E1 full credit: its implementation score remains 7/10 because the broader reusable standard-library scope is incomplete. The canonical hosted CI retries for this final SHA failed before executing any steps; this is an infrastructure failure, not source-test evidence. Protected release evidence remains inaccessible because `CANONICAL_READ_TOKEN` needs Actions:read on the private canonical repository.

## Latest candidate rerun — E1 boundary contracts

Current canonical source SHA `6d1577e078dfcf23295afdaf41568b85d3ba07bb` adds three regression tests for invalid text conversion/replacement/splitting inputs, strict UTC parser forms and full year-range boundaries, checked numeric overflow, and invalid collection inputs. Initial test attempts caught two fixture issues before acceptance: One source has no leading negative numeric literal, and Rust fixture newlines must be single escaped `\\n` sequences. Both were corrected using supported subtraction syntax and valid Rust string escapes. Fresh exact-SHA verification was triggered by pinning this source; no result is accepted until each job completes:

| Gate | Result |
|---|---|
| Cross-platform Ubuntu + Windows | Awaiting fresh run for `6d1577e078dfcf23295afdaf41568b85d3ba07bb` |
| Linux distro | Awaiting fresh run |
| Focused stdlib/database | Awaiting fresh run; includes the new E1 tests through the workspace test suite only if configured to run that integration target |
| Cargo lockfile | Awaiting fresh run |
| Candidate artifact integrity | Awaiting fresh run |
| Android AArch64 ELF runtime | Awaiting fresh run; execution remains unproven |
| Fixed-weight ledger gate | NOT PASSED until current-SHA evidence is complete; E1/E2/E3/E4/E6 acceptance is not yet recorded |

The previous `82e249879131323d015a1c93aea4fd986db1b271` candidate's cross-platform, Linux distro, focused, and lockfile runs passed, but those results are historical after the E1 test commit and do not certify this source SHA.

## Current exact-SHA verification

| Gate | Evidence | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [Run 40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; both Ubuntu and Windows Server 2025 jobs completed successfully, including workspace tests, real-network tests, offline verification, CLI smoke tests, documentation consistency checks, and candidate bundle generation. |
| Linux distro conformance | [Run 40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; Ubuntu 24.04 and Debian 12 jobs completed successfully. |
| Focused stdlib / SQLite / provenance | [Run 40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099) | **PASS** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; UTC/calendar, JSON byte budget, source-level text/integer integrations, SQLite bounds and final-symlink NOFOLLOW, trusted-publisher signature/tampering tests, and Clippy completed successfully. This is still a subset, not full E1 acceptance. |
| Deterministic Cargo lockfile bootstrap | [Run 40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148) | **PASS**; generated the lockfile from canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`. Lockfile SHA-256 is present in workflow output; do not infer that it is a release signature. |
| Android AArch64 native ELF runtime | [Run 40090809569](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40090809569) | **IN PROGRESS — NOT ACCEPTED**. Exact source checkout passed; emulator workflow now uses a smaller API 30 arm64 image to address the previous 30-minute API 35 TCG boot timeout. ELF execution/output has not yet been observed. |
| Current canonical hosted CI | [One CI 40088066589](https://github.com/panglimanetizen01/one/actions/runs/40088066589); [Linux distro 40088066594](https://github.com/panglimanetizen01/one/actions/runs/40088066594); [focused stdlib 40088066614](https://github.com/panglimanetizen01/one/actions/runs/40088066614) | **INFRASTRUCTURE FAILURE** on canonical source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`: retries again failed with no executable steps or logs. Canonical CI for the new `e8156e7d6c0a0f999f24ad00bf670e46f21dc128` candidate has not yet produced an executable run. They are not source-test results. Independent mirror runs do not convert canonical CI to PASS. |

## Current candidate bundles

The following bundles are **historical**, produced on prior source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8` by run [40084595236](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236). They were downloaded and inspected; embedded checksums pass, but they are not current-candidate acceptance. Fresh bundles for source SHA `e8156e7d6c0a0f999f24ad00bf670e46f21dc128` were uploaded by run 40091247192 and independently downloaded/extracted by [artifact integrity workflow 40091607139](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40091607139). Both ZIP hashes matched GitHub artifact metadata; embedded `SHA256SUMS`, build metadata, source SHA, toolchain versions, CLI version, and binary formats passed. Exact binary hashes and metadata are recorded in the dedicated section below.

- **Linux:** [artifact 12556841440](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236/artifacts/12556841440)  
  ZIP SHA-256: `e7266614dc9a5feb5e3673a63c409542b16d86c6d36fbea6a17be498b6fa3797`  
  Binary: ELF 64-bit LSB PIE, x86-64. Embedded binary SHA-256: `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`.
- **Windows:** [artifact 12556821645](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595236/artifacts/12556821645)  
  ZIP SHA-256: `7bd88e7197ae6d7a12fd946e6c2cb226c2be9c216379342fa229425ad4c60c95`  
  Binary: PE32+ console executable, x86-64. Embedded binary SHA-256: `0d4245cc51336f393a902370b1cb5095dd9169ea87132820cefa3a366024468f`.

Both `BUILD-METADATA.txt` files pin source SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, target triple, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. The current candidate `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` requires fresh bundles. All bundles are unsigned candidates, not a signed final release.

## Standard-library evidence

On the prior candidate SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`, both cross-platform logs asserted the exact commit and reported the stdlib integration suite passing (18 tests) and `one-core` library tests passing (228 tests). Focused tests also passed UTC/JSON/SQLite/provenance regressions and the SQLite final-symlink test. These are historical for the new candidate `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`; its exact-SHA reruns are pending. This verifies only the implemented API subset, not every broader E1 requirement.

## Canonical CI infrastructure

The canonical repo's current-candidate runs on source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a` again failed before executing any steps:

- [One CI 40086935480](https://github.com/panglimanetizen01/one/actions/runs/40086935480)
- [Linux distro 40086935432](https://github.com/panglimanetizen01/one/actions/runs/40086935432)
- [Focused stdlib 40086935441](https://github.com/panglimanetizen01/one/actions/runs/40086935441)

Every job has empty `steps: []`; they provide no source build/test evidence. Independent mirror workflows provide executable exact-SHA evidence, but the canonical runner/infrastructure issue remains an open release limitation.

## Android investigation history

- [Run 40081481013](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40081481013): macOS nested HVF failed with `HV_UNSUPPORTED`; Android Emulator injected `-enable-hvf` even with `-accel off`.
- [Run 40084595188](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40084595188): Ubuntu x86_64 rejected an ARM64 AVD because the emulator requires a system image matching the host architecture.
- Current [run 40086990457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990457) returns to macOS ARM64 and wraps the emulator's QEMU binary to remove only the injected `-enable-hvf` argument. As last checked, the emulator boot step remained in progress; API 35 / arm64-v8a, ADB push, ELF header, and execution output remain unproven.

## Security review and remaining fixed-ledger gates

The focused [security release review](https://github.com/panglimanetizen01/one-windows-verification/blob/verification/SECURITY_RELEASE_REVIEW.md) records the final-component SQLite symlink hardening and remaining risks. It does not claim complete sandboxing.

- **E1 — Standard library (10 points):** complete required API acceptance is not proven; broader domains such as concurrency, logging/configuration, and complete persistence APIs remain outside the currently implemented stable subset.
- **E2 — Packaging/provenance (8 points):** package-signature/trusted-publisher tests pass, but protected `one-release` environment dispatch and source-bound signed release acceptance have not been exercised.
- **E3 — Cross-platform (8 points):** Linux/Windows/distro matrix passed on prior SHA `1dec26abcc90ac27d892cf3ff0a83dedb8b90fd8`; the current candidate's cross-platform and distro reruns are in progress, and Android runtime remains open.
- **E4 — Security/recovery (6 points):** open parent-component TOCTOU, root/mount confinement, non-Unix/non-Windows fallback guarantees, and runtime-wide quota/threat review.
- **E5 — Docs/tooling (4 points):** implementation 4/4 after manual user-workflow review; exact-SHA cross-platform CLI smoke and documentation consistency tests now pass in run 40086990528. Verified credit remains unawarded pending full release-gate reconciliation.
- **E6 — Forensic audit (4 points):** open until E1–E5 are accepted and all release evidence, source SHA, ledger, and provenance are reconciled.

The canonical PR now includes the [Definition of Done](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/DEFINITION_OF_DONE.md). Do not change the fixed weights to manufacture a passing score. Do not claim **PASS GREEN LOCKED — FINAL RELEASE** while any gate above remains open.

**Final-SHA candidate bundles (source `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`):** [Linux artifact 12556803021](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12556803021), ZIP SHA-256 `8b7685c892fd335b1f39231a9224ab46580020d2f0823d8089867c5502b46507`; [Windows artifact 12557131610](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40085406746/artifacts/12557131610), ZIP SHA-256 `ecc0c0aadec6a04a8fb0f4b49ed40acc548f1e00fb50bf285ac3d412a8c6f8ba`. Both were downloaded and independently inspected. Embedded checksums pass; Linux payload is ELF x86-64 with binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; Windows payload is PE32+ x86-64 with binary SHA-256 `8c5558996d4e643243cbe0165b7a841d881e5c664617bd7e3217a7de55ebcf53`. Build metadata pins source SHA `f46b95ebdd0e26c5ba17f6acb953538f32401aeb`, Rust/Cargo 1.99.0, and CLI `one 0.1.0`. These remain unsigned candidate bundles, not a signed final release.


## New exact-SHA candidate — 2026-10-24 ledger/checkpoint reconciliation

- **Pinned source SHA:** `9d5d319b88cbee17b18554cfe7641ec1008ba62a`.
- This candidate contains documentation-only corrections reconciling the fixed-weight ledger total with its row values and adding the checkpoint evidence summary. The prior four passing mirror runs listed above are tied to `f46b95ebdd0e26c5ba17f6acb953538f32401aeb` and are **historical for this new SHA**.
- Required current-SHA runs: cross-platform Ubuntu/Windows, Linux distro, focused standard-library/SQLite/provenance, Cargo lockfile bootstrap, artifact integrity, and Android AArch64 ELF build-and-execute. The first five now pass against source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`; Android remains in progress and unaccepted.
- Android run `40085406752` was still booting the emulator on the prior SHA at the last check; it does not prove ELF execution on this candidate.
- Fixed weights unchanged. Implementation: **91/100 provisional**; verified: **60/100**; gate **NOT PASSED**. E1–E6 acceptance remains open, including full stdlib scope, protected release dispatch/signature, Android execution, security disposition, and final forensic audit.


## Exact-SHA bundle metadata — source `9d5d319b88cbee17b18554cfe7641ec1008ba62a`

Run [40086990528](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528) uploaded:
- Linux candidate artifact [12557347980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557347980), ZIP digest from GitHub artifact metadata: `sha256:33cc3445cbccc3780bb776a6d9b2ec846d1687e8d45a8526adf27aa120cf237f`, size 1,738,836 bytes.
- Windows candidate artifact [12557247338](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557247338), ZIP digest from GitHub artifact metadata: `sha256:564f7105d3f12face750d68431699d3f2491c28ff526c75e7951d766f21d8c0a`, size 1,488,731 bytes.

Both names embed the canonical source SHA. Independent download, extraction, ZIP digest comparison, embedded checksum validation, metadata review, and executable-header inspection have now been completed by [artifact integrity run 40087385932](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40087385932). See the PASS section below. These remain unsigned candidate bundles, not final release artifacts.


## Candidate artifact integrity — PASS for source `9d5d319b88cbee17b18554cfe7641ec1008ba62a`

Independent workflow [40087385932](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40087385932) passed. It downloaded both artifact archives by ID, compared ZIP SHA-256 against GitHub artifact metadata, extracted them, verified each embedded `SHA256SUMS`, checked metadata fields, and inspected executable headers.

- Linux artifact [12557347980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557347980): ZIP SHA-256 `33cc3445cbccc3780bb776a6d9b2ec846d1687e8d45a8526adf27aa120cf237f`; embedded binary `one` SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; ELF64 little-endian `EM_X86_64`; target `x86_64-unknown-linux-gnu`.
- Windows artifact [12557247338](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40086990528/artifacts/12557247338): ZIP SHA-256 `564f7105d3f12face750d68431699d3f2491c28ff526c75e7951d766f21d8c0a`; embedded binary `one.exe` SHA-256 `f5749302ef052c6f192939a9d0c96b54edc2c12cba606551383c3e194d7890a9`; PE32+ x86-64; target `x86_64-pc-windows-msvc`.
- Both metadata files assert source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`, Rust/Cargo 1.99.0, and CLI `one 0.1.0`.
- These are checksum-verified **unsigned candidate bundles**, not signed final release artifacts. This does not close E2.


## Supplemental Linux bundle execution — manual, not hosted CI

The Linux candidate ZIP from artifact `12557347980` was downloaded and its embedded `SHA256SUMS` checked in the current ChatGPT execution container. The binary's `BUILD-METADATA.txt` pins source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`. Manual smoke commands executed successfully: `one version` reported `one 0.1.0`; `one help` displayed the documented CLI commands; `one buat` created a temporary project; `one periksa`, `one jalankan`, `one bangun`, `one test` (1 fixture), and `one package` all succeeded on the generated example. The temporary project was removed after the test. This is supplemental direct artifact execution, **not GitHub-hosted CI**, and does not replace the required Windows/Android or release-provenance gates.


## 2026-10-24 — exact-SHA matrix refresh for PR #80 HEAD

The canonical source pin was refreshed from the stale prior target to the current PR head **`2ead9dba45db4ce4105deaa81720aacc8fcadd6c`**. The pin update commit is `5560edbb625e740f3c2c1a67bfedafda225ea104`; that is the verification-mirror commit, not the ONE source SHA.

Fresh workflows were triggered against the pinned source:
- Cross-platform Ubuntu + Windows Server 2025: [40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) — **both jobs PASS**, including full workspace, Clippy, real-network, offline checks and release candidate bundle generation.
- Ubuntu 24.04 + Debian 12: [40088230098](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230098) — **both jobs PASS**.
- Focused standard-library / SQLite / package-signature regressions: [40088230099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230099) — **PASS**.
- Cargo lockfile bootstrap: [40088230148](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230148) — **PASS**.
- Android AArch64 ELF build-and-execute: [40088230097](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230097) — still running at Android emulator boot; **not yet runtime evidence**.

All previous workflow results tied to source SHAs other than `2ead9dba45db4ce4105deaa81720aacc8fcadd6c` are historical and do not satisfy final-SHA acceptance. The artifact-inspection workflow still has hard-coded artifact IDs and source SHA `9d5d319b88cbee17b18554cfe7641ec1008ba62a`; it must be refreshed after the new cross-platform run publishes candidate artifacts. Until then, no artifact-integrity claim is made for the new candidate.

Fixed-weight score remains implementation **91/100 provisional** by row arithmetic, verified **60/100**, release gate **NOT PASSED**. Open acceptance includes the full E1 API scope, protected release-environment signing/trust-store exercise (E2), actual Android AArch64 ELF execution (E3), complete security/threat review and runtime-wide bounds (E4), final exact-SHA doc/tooling acceptance (E5), and the final forensic reconciliation (E6).

### Candidate Linux bundle published for source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Cross-platform run [40088230116](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116) has uploaded Linux candidate artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853), ZIP digest from GitHub artifact metadata `sha256:1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`, size 1,738,835 bytes. Its artifact name embeds the exact source SHA. The Windows candidate bundle has now appeared; paired artifact-integrity workflow [40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284) is queued to validate both bundles.

- Windows candidate artifact [12558350265](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12558350265): ZIP digest from GitHub artifact metadata `sha256:0686d79036c5ce4f4f95bf861c3e82ce8bd9813dbf5dcbe748053ed9c749ee9e`, size 1,488,730 bytes.
- Linux candidate artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853): ZIP digest `sha256:1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`, size 1,738,835 bytes.


### Candidate artifact integrity PASS — source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Independent inspection [40088506284](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088506284) passed against both exact-SHA bundles. The job downloaded artifacts by ID, compared archive digests with GitHub artifact metadata, checked embedded `SHA256SUMS`, source/build metadata, Rust/Cargo/CLI versions, and executable headers.
- Linux artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853): ZIP SHA-256 `1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`; binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`; ELF64 little-endian EM_X86_64; target `x86_64-unknown-linux-gnu`.
- Windows artifact [12558350265](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12558350265): ZIP SHA-256 `0686d79036c5ce4f4f95bf861c3e82ce8bd9813dbf5dcbe748053ed9c749ee9e`; binary SHA-256 `0abae22d28b34ffe266090679786132323dd7508f0f38b8a79c8229aa6cff279`; PE32+ x86-64; target `x86_64-pc-windows-msvc`.
- Both metadata files pin source SHA `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`, Rust/Cargo 1.99.0 and CLI `one 0.1.0`.
- This is artifact-integrity evidence, not signed package provenance or final release authorization; E2 remains open.


### Canonical repository CI retry classification — source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`

Canonical runs [40088066589](https://github.com/panglimanetizen01/one/actions/runs/40088066589) (main CI), [40088066594](https://github.com/panglimanetizen01/one/actions/runs/40088066594) (Linux distro), and [40088066614](https://github.com/panglimanetizen01/one/actions/runs/40088066614) (focused stdlib) failed. I invoked the supported rerun-failed-jobs action for all three. The retry attempts again returned completed-failure jobs with `steps: null` and `logs_url: null`; no executable test step or source failure diagnostic is available. These are **unusable runner/infrastructure attempts**, not evidence of a source test failure and certainly not PASS. The independent exact-SHA mirror remains the executable evidence path; canonical hosted CI infrastructure remains an open item.


### Supplemental current-SHA Linux bundle execution — manual, not hosted CI

Downloaded Linux artifact [12557424853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40088230116/artifacts/12557424853) into the current execution container. Its archive SHA-256 matched GitHub metadata: `1a9b889b980b309fb3807471399c5556b83631145d148a8e9cefb2afe135bd09`. The embedded `SHA256SUMS` passed; metadata pins source `2ead9dba45db4ce4105deaa81720aacc8fcadd6c`; CLI reports `one 0.1.0`. Manual smoke succeeded for `one version`, `one help`, `one buat`, `one periksa`, `one jalankan`, `one bangun`, `one test` (1 fixture), and `one package`. The temporary project was removed after the run. This is supplemental direct Linux artifact execution, **not GitHub-hosted CI**, and does not close Windows runtime, Android, signed-provenance, full E1, E4 or E6 gates.


## Current candidate — ledger/DoD reconciliation source SHA `f9a320e67145f7806f55123dbe72e578679d3f2e`

The current source candidate is `f9a320e67145f7806f55123dbe72e578679d3f2e`. The fixed-weight ledger TOTAL row has been corrected to `91/100 implementation, 64/100 verified`; E5 is the only newly credited verified row. This is not a final release gate pass.

Exact-SHA matrix triggered by verification pin commit [`07f2f4dcd3689b2903f6e5f17fd487ea1de61a58`](https://github.com/panglimanetizen01/one-windows-verification/commit/07f2f4dcd3689b2903f6e5f17fd487ea1de61a58), pinning the canonical source above:

| Required workflow | Run | State |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40092009937](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009937) | PASS; Ubuntu and Windows Server 2025 jobs both completed successfully, including build, tests, Clippy, CLI/docs checks, and candidate bundle generation |
| Linux distro conformance | [40092009933](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009933) | PASS; Ubuntu 24.04 and Debian 12 completed successfully |
| Focused standard library / SQLite / provenance | [40092009976](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009976) | PASS; subset only, not full E1 acceptance |
| Cargo lockfile bootstrap | [40092009942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009942) | PASS |
| Android AArch64 native ELF runtime | [40092009961](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009961) | In progress at API 30 emulator boot; no ELF execution evidence yet |
| Candidate artifact integrity | [40092478797](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092478797) | PASS; workflow dynamically selected exact-SHA bundles, matched ZIP SHA-256 against GitHub artifact metadata, and verified embedded checksums, source/build metadata, ELF64 x86-64 and PE32+ x86-64 |
| Fixed-weight ledger gate | [40092009911](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092009911) | NOT PASSED: matrix was still running when evaluated; canonical release evidence API returned HTTP 403; E1–E4 and E6 are not fully verified |

The prior bundle integrity and manual Linux bundle execution evidence refer to older source SHAs and are historical only. They do not satisfy current-source artifact integrity or Android execution. The canonical repository's hosted CI has repeatedly failed before executable steps (`runner_id: 0`, `steps: []`); independent verification does not relabel those canonical CI runs as PASS.

The release gate remains **NOT PASSED**. E1 requires the full public API contract suite; E2 requires independently configured trusted publisher and protected release-path evidence; E3 requires actual Android AArch64 ELF execution; E4 requires the complete security/root-confinement and resource-bound review; E6 requires a final forensic reconciliation after E1–E5 acceptance. Do not merge PR #80 or publish a release under this state.


## Exact-SHA candidate evidence — source `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`

The current canonical candidate source is `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`. This is the source SHA selected by `CANONICAL_COMMIT.txt` and the open PR #80 head. The fixed-weight ledger is `91/100 implementation, 64/100 verified`; weights were not changed. E5 is the only ecosystem row currently credited as verified.

| Required workflow | Exact-SHA run | Result |
|---|---|---|
| Cross-platform Ubuntu + Windows Server 2025 | [40092715740](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715740) | PASS — both jobs completed successfully |
| Linux distro conformance, Ubuntu 24.04 + Debian 12 | [40092715691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715691) | PASS — both jobs completed successfully |
| Focused UTC/database resource-bound regressions | [40092715735](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715735) | PASS — focused subset only; not full E1 acceptance |
| Cargo lockfile bootstrap | [40092715680](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715680) | PASS |
| Linux/Windows candidate artifact integrity | [40092715698](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715698) | PASS — bundle digests match GitHub artifact metadata; embedded source SHA/toolchain/CLI metadata and ELF64 EM_X86_64 / PE32+ x86-64 headers validated |
| Android AArch64 runtime | [40092942784](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092942784) | IN PROGRESS — API 35 arm64 emulator boot; no ELF execution evidence yet |
| Fixed-weight ledger gate | [40092715712](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40092715712) | NOT PASSED at time of evaluation: current-SHA cross-platform/artifact runs were still in progress; protected canonical release evidence remains inaccessible because `CANONICAL_READ_TOKEN` lacks Actions:read on the private source repository; nine Definition of Done items remain unchecked |

Artifact metadata observed in the successful integrity run:
- Linux candidate ZIP artifact ID `12559338923`, SHA-256 `f2d00fa3ce1bf6489a29006b29df5e31a84a53c1c920ce9d481418374be38979`.
- Windows candidate ZIP artifact ID `12559339113`, SHA-256 `d19fbda9d8df0a2aca82f433e28d745d34c5ba131eef3117595b83a062b0bf0e`.
- Embedded Linux binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`.
- Embedded Windows binary SHA-256 `30efd82327c058f49c45fb30a0be9d298efac6e3c259928097061af52b5804b6`.

The canonical repository hosted workflow remains an independent gate: its recent failure had no executable job steps/logs, so independent mirror passes do not convert canonical CI to PASS. Protected release dispatch, trusted-publisher configuration, full E1, Android ELF execution, complete E4 security acceptance, and E6 forensic closeout remain open. Do not merge PR #80 or claim GREEN LOCKED until those are accepted on the final frozen source SHA.


## Canonical hosted-CI retry result for source SHA `9f24014cd1ebde1f0a72ef598e44e29fa779ac3f`

I retried the canonical failed workflow jobs instead of treating the first failure as final: [One CI run 40092705031, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705031), [Linux distribution run 40092705049, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705049), and [focused stdlib run 40092705091, attempt 2](https://github.com/panglimanetizen01/one/actions/runs/40092705091). All three retries still ended in failure with **zero executable steps** in every job. This is recorded as a hosted-runner/infrastructure failure, not a source test failure and not a PASS. Independent exact-SHA mirror results remain separate evidence and do not replace canonical hosted CI.


## Ledger-gate permission diagnosis

The verifier now retries a public unauthenticated read after HTTP 403, but the canonical repository is private, so that fallback correctly returns 404. To finish the live protected-release evidence check, the repository administrator must update the verification repository secret `CANONICAL_READ_TOKEN` to a token with read access to Actions on `panglimanetizen01/one`. The gate remains fail-closed until that permission exists and an exact-SHA protected release workflow succeeds.


## E2 acceptance boundary — latest checkpoint

- Prior code SHA `a75362fcb9dd7514c1253f661443252122053aa9`: focused package-signature/trusted-publisher tests and lockfile bootstrap passed in [40107005038](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40107005038) and [40106909806](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40106909806). These are historical for the new documentation commit `dca9a22c242905b97275161d9fdda933b986ec0d`.
- Current candidate `dca9a22c242905b97275161d9fdda933b986ec0d` changes only ledger/checkpoint documentation. The exact-SHA matrix is pending and will be rerun.
- E2 stays **0/8 verified / NOT ACCEPTED** until a real protected `one-release` run proves environment protection, securely configured signing seed, independently provisioned trusted publisher store, successful V2 source-bound signature verification, and retained artifacts. Synthetic fixture keys do not satisfy this criterion.


## Prompt 2/4 — E2 evidence checkpoint (2026-10-24)

- Canonical source SHA pinned for this matrix: `dca9a22c242905b97275161d9fdda933b986ec0d`. Completed exact-SHA runs: focused package signature/trusted-publisher tests [40108646700](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646700) PASS; lockfile bootstrap [40108646762](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646762) PASS; Ubuntu 24.04 + Debian 12 [40108646764](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646764) PASS; Ubuntu + Windows Server 2025 [40108646717](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646717) PASS; artifact integrity [40108646691](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646691) PASS.
- Android AArch64 run [40108646751](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108646751) is still in progress at emulator boot; no native ELF execution result yet.
- The fixed-weight gate [40108651511](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40108651511) is **NOT PASSED**. It reports 9 unchecked DoD items, full-row acceptance absent for E1/E2/E3/E4/E6, Android pending at evaluation time, and inability to query canonical release evidence due to the missing Actions:read permission for the canonical repository.
- E2 remains **0/8 verified / NOT ACCEPTED**. Focused tests verify cryptographic signing and rejection of tampering/untrusted keys with synthetic fixture keys, not a real independently authenticated publisher key. The protected `one-release` workflow has not run; environment protection and secret/trust-store configuration are unverified. No release was published.


## E2 checkpoint refresh (2026-10-25)

Candidate source SHA: `2ea52d4c39aac98be8678a2e1ac0b67997610c22`.

Exact-SHA lab results: E2 synthetic package/provenance tests PASS [40154415287](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415287); checksum/artifact inspection PASS [40154415291](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415291); focused stdlib/database PASS [40154415289](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415289); lockfile bootstrap PASS [40154415296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415296); Linux distro jobs PASS [40154415350](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415350).

Cross-platform run [40154415306](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415306) concludes success but skips verification steps in both jobs, so it is not counted as platform-test evidence. Android/macOS HVF capability probe [40154415292](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154415292) failed; Android native runtime remains open.

Canonical repo workflows on this SHA (including E2 [40154410737](https://github.com/panglimanetizen01/one/actions/runs/40154410737)) failed with zero executable steps. Treat as hosted execution failure, not source test failure and not PASS. Latest fixed-weight gate [40154565531](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40154565531) remains failed.

Acceptance: E2 is NOT GREEN LOCKED. Synthetic-key lab evidence does not replace a protected canonical `one-release` run using production signing and independently trusted publisher keys. The canonical Actions read token permission remains unresolved; no production release was published.

## New candidate checkpoint — 2026-10-25

Canonical source candidate: `56606c7f8076bc9a67e321835077315d321b8b7a`. The E2 release workflow YAML was found malformed in the provenance-validation block: three incomplete `grep -Eq` expressions had been interrupted by repeated artifact-upload steps. The workflow was reconstructed with complete anchored metadata checks, digest comparison, a portable SHA-256 manifest check, and one final artifact upload. Fix commit: [56606c7](https://github.com/panglimanetizen01/one/commit/56606c7f8076bc9a67e321835077315d321b8b7a).

The verification harness pin was advanced to this SHA in [commit 6e3e8b8](https://github.com/panglimanetizen01/one-windows-verification/commit/6e3e8b86c546b3e3766f6c3c0a6e7b82cbd96a8d). Exact-SHA lab runs were queued at checkpoint time, including [E2 lab #40155108865](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108865). Canonical hosted workflows again failed with no executable steps, including [E2 #40155103608](https://github.com/panglimanetizen01/one/actions/runs/40155103608); this is not PASS evidence. Production protected release has not run. E2 remains NOT GREEN LOCKED until exact-SHA lab checks complete and a protected canonical release verifies using configured production signing material and trusted publisher keys.

## E2 exact-SHA rerun result — candidate `56606c7f8076bc9a67e321835077315d321b8b7a` (2026-10-25)

The repaired canonical workflow source is pinned in `CANONICAL_COMMIT.txt` and the independent harness checked out and asserted this exact source SHA.

- **E2 synthetic end-to-end package/provenance lab: PASS** — [run 40155108865](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108865). All executed steps succeeded: exact-SHA checkout/assertion, provenance/CLI tests, stale Cargo lock rejection, release CLI build, deterministic two-build package bytes, V2 source-bound signature, signature/source/metadata verification, untrusted publisher rejection, modified artifact and metadata rejection, checksum/provenance retention. Uses a disposable synthetic fixture key only; it is not production signing/trust evidence.
- **Focused stdlib/database regressions: PASS** — [run 40155108898](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108898), including package signing/trusted-publisher verification, V2 provenance, deterministic packaging, dependency fail-closed checks, and E1 focused regression suites.
- **Cargo lockfile bootstrap: PASS** — [run 40155108989](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108989).
- **Linux distro conformance: Ubuntu 24.04 PASS; Debian 12 running at last poll** — [run 40155108895](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108895).
- **Cross-platform matrix: running** — [run 40155108886](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108886). Ubuntu release-mode build and Windows contract checks were in progress at last poll; no full matrix credit yet.
- **Candidate artifact integrity: running** — [run 40155109003](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155109003); archive and embedded-manifest checks are not yet complete.
- **Fixed-weight ledger gate: NOT PASSED** — [run 40155108839](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108839). The gate fails closed because full acceptance requirements, including protected production release evidence and complete Definition-of-Done evidence, are still unmet.
- **Android AArch64 runtime: NOT PASSED** — [run 40155108942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108942). The Android emulator boot/capability probe failed; ELF execution was skipped. This is not E2 package-provenance evidence, but remains a global platform gate.

The canonical repository's own workflow runs still report no executable steps, so they are not counted as passing tests. The production protected `one-release` workflow has not run. Therefore the synthetic E2 path is now verified on the repaired exact SHA, but **E2 is not GREEN LOCKED / not fully accepted** until the protected production release path succeeds with independently provisioned signing and trusted-publisher material and retained output artifacts.


## E2 matrix update — exact candidate SHA `56606c7f8076bc9a67e321835077315d321b8b7a`

Updated 2026-10-25 after the previously running jobs completed:

- **Cross-platform matrix: PASS on both Ubuntu and Windows** — [run 40155108886](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108886). Ubuntu and Windows jobs completed successfully, including release-mode build, CLI smoke tests, package creation twice, and offline verification. Windows log includes 34 stdlib tests and 10 target-backend foundation tests plus CLI smoke/offline checks.
- **Linux distro matrix: PASS on Ubuntu 24.04 and Debian 12** — [run 40155108895](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108895).
- Cross-platform candidate artifacts (both unexpired) are available from run 40155108886:
  - Linux bundle ID `12584162788`, GitHub archive digest `sha256:7c7718750048ea52e546fd0f163e81e8e924aad657923e78faa6700691cdc398`.
  - Windows bundle ID `12584252835`, GitHub archive digest `sha256:dfe7afcd9f727042bc5200869a440ac7f7803f298548716c29a529820c081a22`.
- **Artifact content inspection remains in progress** — [run 40155109003](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155109003). The independent archive-digest and embedded metadata/binary-format assertions are not credited until that run completes successfully.
- **Fixed-weight ledger gate remains NOT PASSED** — [run 40155108839](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108839). It was evaluated before this matrix completed and before this index update; it also reported 9 unchecked Definition of Done items, missing complete E1/E2/E3/E4/E6 row evidence, and missing canonical Actions read permission for protected release evidence. Updating this index does not itself satisfy those acceptance requirements.
- **Android native runtime remains NOT PASSED** — [run 40155108942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155108942); the emulator/ELF execution probe failed.

The synthetic E2 package/provenance test, focused tests, lockfile bootstrap, Linux distro matrix, and now the full Ubuntu/Windows cross-platform matrix have passed for the exact source SHA. This is substantial test evidence but **does not constitute production release acceptance**: the protected `one-release` workflow with independently trusted production signing material has not run, and artifact inspection plus the complete ledger/DoD gate are not green.


## Artifact inspection completion — 2026-10-25

**Candidate artifact integrity: PASS** — [run 40155109003](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40155109003) completed successfully for source SHA `56606c7f8076bc9a67e321835077315d321b8b7a`.

The inspection verified GitHub archive SHA-256 digests, embedded `BUILD-METADATA.txt` source SHA and target/toolchain/version fields, binary hashes against embedded `SHA256SUMS`, and executable formats:
- Linux bundle: `x86_64-unknown-linux-gnu`, ELF64 little-endian EM_X86_64, binary SHA-256 `36aaf109b3689e61d879f2bc2f9ebe685976f703035eb06c08935a8a7c7b2c79`.
- Windows bundle: `x86_64-pc-windows-msvc`, PE32+ x86-64, binary SHA-256 `a515f22091d729131e352107f9b282ddb128c795402e06527938c72461d3ef2f`.
- Both report source SHA `56606c7f8076bc9a67e321835077315d321b8b7a`, Rust/Cargo 1.99.0, and CLI version 0.1.0.
- GitHub archive digests are recorded above in the matrix update; both archives were downloaded and checked against their API-provided digest.

This closes the synthetic candidate-bundle integrity checks for the current exact source SHA. It does not replace the protected production signing/trust workflow, which still has no successful run.


## Canonical Actions retry audit — 2026-10-25

- Re-ran failed jobs for canonical repository workflow run [40155103608](https://github.com/panglimanetizen01/one/actions/runs/40155103608) using GitHub's rerun-failed-jobs operation.
- Retry attempt 2 completed with **failure** on exact source SHA `56606c7f8076bc9a67e321835077315d321b8b7a`.
- The GitHub job API reports an empty executable step list (`steps: []`) for the canonical job. The job-log endpoint returns a missing-log/404 response. Therefore this retry produced no test evidence; it is neither a source-test failure nor a passing run.
- The independent lab's prior candidate bundle inspection remains PASS as documented above. This retry does not change or invalidate those scoped lab results, and does not satisfy the protected production release acceptance.
- Required external action remains: restore a functioning canonical Actions execution path and ensure `CANONICAL_READ_TOKEN` in the lab has Actions: read permission for the private canonical repository; then run the protected `one-release` workflow with independently provisioned production signing/trust material and re-run the fixed-weight ledger gate.


## Fixed-weight gate diagnostic — run 40157555318

- Gate run: [40157555318](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40157555318), evidence-index commit `6b045336e48cbdbcd0e950debc35eeb145867d40`, source pin `56606c7f8076bc9a67e321835077315d321b8b7a`.
- Ledger verifier unit tests: **4/4 PASS**. This confirms the gate checker behaves as intended; it is not project acceptance.
- Actual ledger summary: fixed weights `100/100`; implementation `91/100`; verified `64/100`; 18 weighted rows checked; 9 Definition of Done items unchecked.
- Acceptance failures reported by the gate:
  - E1 `0/10`, E2 `0/8`, E3 `0/8`, E4 `0/6`, E6 `0/4` lack full-row acceptance evidence.
  - No current-source-SHA run found for Android AArch64 native runtime verification.
  - Canonical release workflow evidence query fails because `CANONICAL_READ_TOKEN` lacks Actions: read access to the private canonical repository; anonymous fallback returns HTTP 404.
- Conclusion: gate failure is an acceptance/evidence result, not a failed ledger unit test. Do not change points or checkboxes to hide these blockers.


## Exact-source E3/E4 revalidation — 2026-10-26

Canonical candidate source SHA: `68883f000caa7143ee93886753b9a7bf3ce9a448`. The lab's `CANONICAL_COMMIT.txt` was checked against the candidate branch HEAD and matches this SHA. Evidence below is credited only where the workflow log checks out and prints this exact source SHA.

### Completed exact-source evidence

- Linux distro verification: **PASS**, Ubuntu 24.04 and Debian 12 — [run 40262677674](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262677674).
- Cross-platform verification (Ubuntu and Windows Server 2025): **PASS** — [run 40262677696](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262677696). Both OS jobs completed successfully; the workflow checks out and verifies the exact canonical source SHA.
- E4 adversarial filesystem/resource regression: **PASS** — [run 40262677927](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262677927). The Unix job checked out exact SHA `68883f000caa7143ee93886753b9a7bf3ce9a448` and executed passing assertions for final-component symlink denial, parent symlink denial, Linux `/proc` mount-boundary denial, concurrent parent-directory/symlink swap safety, SQLite query/value/parameter/row/output bounds, query timeout, capability scope, and adapter non-invocation on denial. The Windows job checked out the same source SHA and passed the directory-junction/reparse-point escape regression.
- SEC-05 subprocess timeout/output-bound verification: **PASS** — [run 40262718117](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262718117), Linux and Windows jobs completed successfully on the canonical pin.
- E4 subprocess resource guard: **static guard PASS** — [run 40262718153](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262718153). This job checks for bounded streaming/timeout implementation and absence of unbounded `Command::output()`; runtime behavior is credited only through the SEC-05 Linux/Windows test suite below.
- Exact-SHA candidate artifact integrity: **PASS** — [run 40262718176](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262718176).
- Android AArch64 device artifact build: **PASS for build only** — [run 40262754847](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262754847). This does not satisfy Android runtime acceptance.
- Focused standard-library/database verification: **PASS** — [run 40262536335](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262536335).
- Cargo lockfile bootstrap evidence: **PASS** — [run 40262536336](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262536336).

### Android API 35 runtime — still OPEN

- The Linux x86_64 TCG attempt [40262251273](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262251273) failed before guest boot because the emulator rejects an `arm64` AVD on an `x86_64` host. The native ELF execution assertion did not run.
- The ARM64 Linux-host attempt [40262536303](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262536303) failed during SDK setup because Google's SDK manager reported `Failed to find package 'emulator'` for that host. No guest boot or ELF execution occurred.
- Exact-source macOS TCG workaround run [40262902149](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262902149) was queued when this section was written. It must complete and show API 35, ABI `arm64-v8a`, actual ELF execution, exit code 0, and `ONE_NATIVE_BACKEND_OK` before runtime acceptance can be credited.

### Gate and residual status

- Fixed-weight ledger gate [40262754834](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262754834) failed closed. Besides evidence that was still running at evaluation time, it reported that `CANONICAL_READ_TOKEN` lacks Actions: read permission for the private canonical repository; the anonymous API fallback returned 404. This requires correcting the repository secret's permission outside a source-code assertion change. Do not weaken the gate or infer a protected release PASS.
- E3/E4 are **not declared PASS GREEN LOCKED**. The Windows cross-platform run and Android API 35 runtime must be confirmed, the exact-source evidence matrix must be refreshed after those results, and the protected canonical release evidence query must be accessible. Fixed ledger weights/scores remain unchanged until a valid gate evaluation supports a change.


### Android AArch64 ELF metadata inspection — 2026-10-26

- Exact-source build run [40262754847](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40262754847), artifact ID `12625815205`, artifact SHA-256 digest `sha256:0cc7ee554558cfa83bf46b67f2e8c87df037f59287749062295368b6472c31ef`.
- Downloaded and independently inspected the artifact ZIP. `SOURCE.txt` names source SHA `68883f000caa7143ee93886753b9a7bf3ce9a448`; binary SHA-256 is `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`, matching the archived `ELF-SHA256.txt`.
- `file` and `readelf -h` confirm ELF64, little-endian, PIE/DYN, machine AArch64. `readelf -l` confirms interpreter `/system/bin/linker64`. `readelf -d` shows dynamic dependencies `libdl.so` and `libc.so` only.
- This proves build artifact architecture, interpreter, and dependency metadata for the exact source SHA. It **does not** prove runtime execution on Android API 35; that remains gated on the queued emulator run.


## Candidate SHA advanced for E4 final-component mount-boundary side-effect fix — 2026-10-26

The ONE source branch advanced from `68883f000caa7143ee93886753b9a7bf3ce9a448` to `2da32ef96108579bac4752dc4ad75fa13c6f919e` after a source audit found that Unix write-open used `O_TRUNC` before validating the final opened file's mount identity. That ordering could truncate a final-component bind-mounted file before returning a mount-boundary denial.

The candidate now opens the final file without `O_TRUNC`, verifies the opened handle is on the same filesystem mount as its parent, and truncates only after the boundary check passes. A Linux regression creates a file on `/dev/shm`, invokes the same mount-identity guard against the project directory, and asserts the file contents remain unchanged on denial.

**All earlier E3/E4 runs and Android artifact metadata in this index are now preliminary evidence for the previous source SHA only.** The canonical pin is being advanced to `2da32ef96108579bac4752dc4ad75fa13c6f919e`; rerun Linux 24.04, Debian 12, Windows Server 2025, E4 adversarial, SEC-05, resource-budget tests, candidate artifact integrity, and Android API 35 `arm64-v8a` runtime on this exact SHA. Do not promote previous runs to final-source evidence.


## Strict Clippy correction — source SHA 78b9436c318032b1c19a4e5c110142fffc58b4d5

The first exact-source Linux distro run for the final-component mount fix, [40263804551](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40263804551), failed on both Ubuntu 24.04 and Debian 12 because the refactor left two unused `MetadataExt` imports in `open_read_target_in_project` and `open_write_target_in_project`. The imports are removed without changing the mount-boundary logic or regression assertions.

Candidate source HEAD is now `78b9436c318032b1c19a4e5c110142fffc58b4d5`; the canonical pin is being advanced to this SHA. Results on `2da32ef96108579bac4752dc4ad75fa13c6f919e` and all earlier SHAs are preliminary only. Re-run the exact-source matrix and verify the new Linux mount-boundary regression passes on both required distributions.


## Latest execution follow-up — canonical ONE source SHA 78b9436c318032b1c19a4e5c110142fffc58b4d5 — 2026-10-26

The live candidate branch HEAD and `CANONICAL_COMMIT.txt` were checked and both resolve to `78b9436c318032b1c19a4e5c110142fffc58b4d5`. The lab branch HEAD is a separate harness commit; it is not the candidate source SHA. Credit the source SHA only where the job log explicitly prints and verifies it.

### Results verified from job logs

- **E4 Unix adversarial/resource-bound job:** [run 40264259048](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264259048), job [121383062655](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264259048/job/121383062655), completed successfully. Log confirms the exact source SHA and executed descriptor-relative/no-follow regressions, final-component mount-boundary denial/no-truncation, SQLite tests, governance/capability tests, and denied-request adapter non-invocation. The captured output includes passing assertions for capability denial and root-scope traversal; use the complete job log for the full assertion list.
- **E4 Windows reparse-point regression:** same run [40264259048](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264259048), job [121383062857](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264259048/job/121383062857), completed successfully on the exact source SHA. The log explicitly prints `source_sha=78b9436c318032b1c19a4e5c110142fffc58b4d5` and records `filesystem_reader_rejects_directory_junction_escape ... ok` (1 passed).
- **Android API 35 AArch64 cross-build/contract:** [run 40264234301](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264234301), completed successfully, but its own log explicitly says this job does **not** execute the ELF on Android. This is not Android runtime acceptance.
- **Android device artifact build:** [run 40264171337](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264171337), successful build-only result. The log records exact source SHA, ELF64 little-endian PIE, AArch64 machine, and interpreter `/system/bin/linker64`; artifact ID `12626005596`, digest `sha256:99b3e024bd24f09008d5f44849c4fcf07d3c52ea0fe9517aef89cdcea3aff5b1`. It does not prove runtime execution.
- **Candidate artifact integrity:** [run 40264130879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264130879), successful. Its log resolves source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`, validates the Linux ELF64 x86-64 and Windows PE32+ x86-64 candidate bundles, and checks their artifact SHA-256 values.
- **Linux distro matrix:** [run 40264090050](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264090050), completed successfully for Debian 12 and Ubuntu 24.04. I re-read both job logs; both contain the canonical source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`, so the source-SHA binding is confirmed.
- **Cross-platform matrix:** [run 40264090066](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264090066), completed successfully for Ubuntu and Windows Server 2025. I re-read both job logs; both contain the canonical source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`. The Windows job includes a successful full `one-core` test suite, but its separate SEC-05/static markers explicitly state that static launch-path checks are not a substitute for dynamic race/adversarial testing.
- **SEC-05 subprocess guard:** [run 40264131009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264131009), both Linux and Windows jobs completed successfully. Treat its result as a guard/contract run, not proof of every Windows descendant-process race without the dynamic assertions and exact-source logs.

### Blocking items — not green

1. **Android API 35 runtime remains OPEN.** The AArch64 native-host run [40264050662](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264050662) failed before emulator setup completed: SDK manager reported `Failed to find package 'emulator'`. The macOS TCG workaround [40264206706](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264206706) was still queued at last poll. No verified log yet proves API 35 guest boot plus actual ELF execution, exit code 0, and `ONE_NATIVE_BACKEND_OK`.
2. **Fixed-weight ledger gate remains failed closed.** [run 40264171287](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264171287) passed its verifier unit tests but failed acceptance because E1/E2/E3/E4/E6 ledger rows and Definition of Done are not fully evidenced, Android runtime is pending, and `CANONICAL_READ_TOKEN` lacks Actions: read access to the private canonical repository's protected release workflow. The anonymous fallback returns 404. This requires authorized repository-secret/permission correction and a fresh gate run; do not weaken the gate or alter scores/checkboxes to hide it.
3. **Source-SHA freshness is per-job.** Runs with a different pinned source SHA are historical/preliminary and cannot be promoted to final acceptance after the source changes. Preserve the fixed ledger weights and keep the release gate `NOT PASSED` until all mandatory criteria and protected release evidence are actually verified.

No E3/E4 `PASS GREEN LOCKED` claim is made by this evidence update.
