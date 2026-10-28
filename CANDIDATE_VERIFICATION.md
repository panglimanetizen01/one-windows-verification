# Current exact-SHA acceptance evidence

Canonical ONE source SHA under verification: `72c4d3d079a11d41e3410408898e6fe3ddcc9d05`.



## Historical candidate checkpoint — 2026-10-28T05:45Z (superseded; retained for audit trail)

- **Historical pinned canonical source SHA at this checkpoint:** `1119c450eda1437d79d75304a1daefb93e8a357f` ([source commit](https://github.com/panglimanetizen01/one/commit/1119c450eda1437d79d75304a1daefb93e8a357f)). This commit reconciles the E4 threat-review document with the current candidate-scoped evidence. No runtime code changed in this commit; nevertheless, exact-SHA policy requires rerunning the required matrix on this new SHA.
- **Threat review updated:** [E4 threat review](https://github.com/panglimanetizen01/one/blob/1119c450eda1437d79d75304a1daefb93e8a357f/docs/verification/E4-threat-review-2026-10-26.md) now records scoped current-candidate evidence links for runs 40634065806 (filesystem/resource regression), 40634065919 (SEC-05), 40634065925 (subprocess resource guard), 40634065845 (cross-platform), and 40634065997 (Linux distro). These runs checked out prior candidate SHA `1a84d522a2953044c250ebe43c22989d6ec07dfc`; they are historical after this documentation commit and are not falsely promoted as exact evidence for the new SHA.
- **Fixed-weight ledger remains unchanged:** implementation `92/100`; verified `72/100` provisional; 8 Definition-of-Done items unchecked. E1 `0/10`, E2 `0/8`, E4 `0/6`, E6 `0/4` remain open. No points are awarded by this documentation reconciliation.
- **E2 release provenance:** no protected production `ONE Package Provenance Release` run exists for this SHA. No release was dispatched or published; no release is authorized.
- **Required next gate:** the pin change triggers fresh exact-SHA verification workflows. Wait for and inspect those run results; pending/in-progress runs earn no points. The overall gate remains **NOT PASSED** until all acceptance criteria and protected provenance requirements pass.

## Exact-SHA matrix result refresh — 2026-10-28T05:46Z

Canonical ONE source SHA remains `1119c450eda1437d79d75304a1daefb93e8a357f`. These are scoped results from workflows whose jobs checked out the current pin:

- [E4 adversarial filesystem/resource-bound regression #40638898955](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898955) — success.
- [E4 SEC-05 subprocess timeout/output-limit #40638898978](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898978) — success.
- [Linux distro verification #40638899092](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899092) — success.
- [E1 Standard Library Windows Acceptance #40638899155](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899155) — success for its defined Windows acceptance suite; this does not by itself close the full E1 ledger row.
- [E1 cross-platform acceptance lab #40638899012](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899012) — success.
- [Cross-platform verification #40638898957](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898957) — success.
- [Candidate artifact integrity #40638898937](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898937) — success.
- [Focused standard-library/database #40638899182](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899182) — success.
- [E4 subprocess resource guard #40638899440](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899440) — success.
- [Android API 35 AArch64 runtime #40638899009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899009) — exact-source ELF build passed, but the native ARM64 guest-runtime job is still in progress at this checkpoint; no runtime PASS is claimed.

The fixed-weight ledger gate [#40638928894](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638928894), including its post-matrix retry, remains **NOT PASSED**: 8 Definition-of-Done items unchecked; E1 0/10, E2 0/8, E4 0/6, E6 0/4; Android runtime pending; and no protected production `ONE Package Provenance Release` run exists for this source SHA. Verifier unit tests passed 7/7. No points or checklist items are promoted by this refresh.

Canonical source Linux distro run [#40638875412](https://github.com/panglimanetizen01/one/actions/runs/40638875412) was retried; both jobs again failed before any steps were available (`steps: null`). Classify as an unresolved job-start/runner infrastructure failure, not as a source-test result. No root cause is established by available metadata. Canonical E1 standard-library lab [#40638875488](https://github.com/panglimanetizen01/one/actions/runs/40638875488) was also retried; both Ubuntu and Windows jobs again failed with `steps: null`. The same infrastructure classification applies; no source-test result or root cause is available.

## Pre-reconciliation candidate checkpoint — 2026-10-28T04:16Z (historical source SHA `53220eeb4bae9138b3a46b469004f8eac4a11420`)

- **Historical pinned canonical source SHA at this checkpoint:** `53220eeb4bae9138b3a46b469004f8eac4a11420` ([source commit](https://github.com/panglimanetizen01/one/commit/53220eeb4bae9138b3a46b469004f8eac4a11420)). The pin update itself is the only verifier-side action after this source SHA was frozen.
- **Ledger reconciliation:** E3/E4/E5 rows now conform to the six-column fixed-weight schema. Historical E3/E5 evidence is explicitly not credited to this candidate. Current recorded totals are **92/100 implementation** and **60/100 verified**; no weights changed.
- **Current required acceptance:** E1 0/10, E2 0/8, E3 0/8 pending exact-SHA matrix, E4 0/6 pending complete threat review/current-SHA evidence, E5 0/4 pending exact-SHA docs/tooling evidence, E6 0/4. The ledger gate remains NOT PASSED until direct acceptance evidence is complete.
- **Prior source-runner incidents:** E1 run [40630668456](https://github.com/panglimanetizen01/one/actions/runs/40630668456) and Linux distro run [40630668504](https://github.com/panglimanetizen01/one/actions/runs/40630668504) targeted previous source SHA `ea39f92b51f47f34d7edd5d283c68e9ca217cb64`; all four jobs reported runner ID `0`, empty runner name, and no steps. These are classified as infrastructure/job-start failures, not source-test results.
- **Protected release:** no release has been dispatched or published. Synthetic trust tests are not production provenance acceptance; E2 stays open and no release is authorized.
- **Fresh exact-SHA matrix:** pin change will trigger verification workflows. Until each required run reaches completed/success on this exact source SHA, pending/in-progress results earn no points.

Historical notes below are preserved as archive and must not override this current checkpoint.

## Latest status refresh — 2026-10-27

This status refresh records outcomes observed after the initial pending-state notes above. It does not change ledger weights or award points.

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841): **Ubuntu 24.04 and Windows Server 2025 both completed successfully** for the pinned source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`. Both jobs passed the E1 regression and library unit suites, full workspace tests, warnings-denied Clippy, and repository contract checker. This completes this workflow run's two-platform matrix; it does not alone award full E1 row credit because the fixed ledger has broader scope/DoD criteria.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726): **both Windows Server 2025 and Ubuntu completed successfully** for the exact pinned source SHA. Windows and Linux build/release-build, package-bundle integrity, AST contract regression, Clippy, workspace tests, real-network tests, and offline verification passed. This run is complete; it does not substitute for the separate E1, Android runtime, or protected-provenance gates.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072667): **completed successfully**. Exact-SHA Linux and Windows candidate bundle discovery, archive digest validation, embedded manifests/metadata, and executable-format checks passed.
- [Android API 35 community ARM64 runtime](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072659): exact-source AArch64 ELF build and metadata checks passed, but runtime failed before ELF execution. The hosted ARM64 runner has no usable KVM; QEMU reports `gic-version=host requires KVM`. Diagnostic artifact `12719193755` was uploaded. This is not runtime acceptance.
- [Android API 35 Linux TCG retry](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40475724178): exact candidate SHA and backend contract tests passed, but the emulator failed before guest boot with `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host`. The workflow incorrectly attempts to boot an ARM64 Android system image on an x86_64 runner; adding `-qemu -accel tcg` cannot overcome the emulator's unsupported host/guest architecture pairing. The AArch64 ELF execution step was skipped. This is a concrete workflow design failure, not runtime acceptance.
- [Android API 35 native ARM64-host attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072760): the ELF build passed, but the runtime job failed before executing the ELF. The emulator never reached `sys.boot_completed=1`; the log reported `Unable to spawn process ... No such file or directory`. This is an emulator/runtime-environment failure, not evidence that the ONE ELF passed or failed execution.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072703): the verifier's tests passed, then the gate correctly failed closed at 78/100 verified and 92/100 implemented. The recorded blockers include E1/E2/E6 incomplete acceptance, seven unchecked DoD items, unfinished exact-SHA jobs, and the failed protected release workflow. The gate result is not a source-test PASS.
- [Canonical repository CI for PR #85](https://github.com/panglimanetizen01/one/actions/runs/40471195625): the retry again failed both Ubuntu and Windows jobs with runner ID 0 and no steps. This is inconclusive infrastructure failure; the new documentation checks have not yet executed on hosted CI.


This index records exact-SHA evidence only. Scoped test success does not automatically award fixed-weight ledger points; E1, E2, and E6 remain open until their full row acceptance criteria and Definition of Done are satisfied.

## Execution delta — 2026-10-27 (latest inspected evidence)

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841): Ubuntu 24.04 and Windows Server 2025 jobs completed with conclusion `success` for canonical source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`. This confirms that matrix run only; it does not independently satisfy the full E1 row.
- [Exact-source platform and security evidence](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726): the Linux and Windows jobs checked out canonical ONE source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`; both passed build, release build, AST contract regressions, Clippy, platform tests, real-network tests, offline verification, and their platform bundle/provenance/checksum checks. The dedicated [E4 subprocess resource guard](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072707), [E4 filesystem/resource regression](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072725), [E4 SEC-05 cross-platform tests](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072714), and [Linux distro matrix](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072895) also completed successfully on the same canonical source pin. This is positive evidence for those scoped gates, not full E1/E2/E6 acceptance; Android API 35 guest ELF execution remains independently required.
- [Android x86_64 TCG attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40476757142): runtime failure is confirmed by the actual emulator log: `FATAL | Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host`. The guest ABI was incompatible with that host path, and no ELF was executed.
- [Android ARM64-host attempts](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477093827), [follow-up](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477231231), [checksum-pinned attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477432328), and [evidence-upload attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477658242): each exact-source ELF build completed successfully. Runs 40477231231 failed at emulator boot; run 40477432328 completed boot/runtime successfully; run 40477658242 completed the runtime and uploaded source-bound evidence. The latter run's log proves exit code 0 and exact output `ONE_NATIVE_BACKEND_OK`; see the Android API 35 runtime acceptance update below. Earlier in-progress observations are superseded by the completed run status.
- [Protected ONE package provenance release](https://github.com/panglimanetizen01/one/actions/runs/40467992667): attempt 6 (job `122101339491`) was retried after attempt 5 also failed before workflow steps. Attempt 6 again completed as failure with `runner_id: 0`, empty runner name, and zero steps. The retry did not reach workflow commands; it does not establish protected secret values, environment approval state, or production trusted-publisher acceptance. Do not classify it as code-level PASS or E2 acceptance.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40478102859): exact pinned source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`; verifier unit tests passed. The rerun after Android evidence became available still correctly failed closed: seven DoD items remain unchecked and E1/E2/E6 lack full-row evidence; the protected release workflow remains failed before starting. The Android runtime is now accepted by the live-evidence gate. Earlier ledger run [40477146203](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477146203) failed on the same broader acceptance gaps.

No ledger weights, acceptance criteria, scores, or Definition of Done checkboxes were changed by this evidence update.

## Completed PASS evidence for this SHA

- [E4 adversarial filesystem/resource-bound regression](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072725) — Unix and Windows jobs passed.
- [E4 SEC-05 subprocess timeout/output-limit verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072714) — Linux and Windows jobs passed.
- [Focused standard-library/database regression](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072805) — passed.
- [E1 Standard Library Windows Acceptance](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072646) — passed.
- [Cargo lockfile bootstrap](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072775) — passed.
- [Linux distribution verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072895) — Debian 12 and Ubuntu 24.04 passed.
- [Exact-SHA package, deterministic bytes, lock, signature and tamper checks](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072848) — passed using synthetic test trust only.

## Still pending or blocked

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072841) — **both Ubuntu 24.04 and Windows Server 2025 passed**; see the completed job steps above. Full E1 row credit remains governed by the fixed ledger's broader acceptance criteria.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072726) — **completed PASS** on both Windows Server 2025 and Ubuntu.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072667) — **completed PASS** for exact-SHA Linux/Windows bundles.
- [Android API 35 AArch64 runtime, community fallback](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072659) — **runtime attempt failed at emulator boot before the ONE ELF ran**. The ARM64 hosted runner reports `ONE_KVM_AVAILABLE=false`, while QEMU reports `gic-version=host requires KVM`; the job exited 1 and uploaded diagnostic evidence (artifact `12719193755`). This is a host/emulator acceleration incompatibility, not a program runtime failure and not a PASS. The [native ARM64 host attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072760) also failed before ELF execution: ADB detected `emulator-5554`, but `sys.boot_completed` never reached `1` before the bounded boot wait ended. Both logs are now inspected; neither proves Android runtime acceptance.
- [Android API 35 Linux TCG retry](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40475724178) — **failed before guest boot** because the stock QEMU2 emulator on `ubuntu-24.04` x86_64 rejects the `arm64` AVD architecture. The explicit TCG argument does not make this host/guest combination supported. The separate native ARM64-host attempt remains failed before ELF execution (`sys.boot_completed` never reached `1`). Android runtime acceptance remains unproven; next repair must use a supported native ARM64 runtime path, not repeat the x86-host ARM64 AVD attempt.
- [Protected ONE package provenance release](https://github.com/panglimanetizen01/one/actions/runs/40467992667) — the retry job `122086729327` is **completed failure**, not queued. GitHub's job listing contains no step summaries, log retrieval returns `BlobNotFound`, and the run has no artifacts; therefore the root cause is not established. This is not PASS. Production trusted-publisher acceptance remains unproven.
- [Fixed-weight ledger gate](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40468072703) — failed closed; implementation 92/100, verified 78/100; E1 0/10, E2 0/8, E6 0/4; seven Definition of Done items remain unchecked.

The previous cumulative evidence notes are preserved in `CANDIDATE_VERIFICATION_ARCHIVE_20261027.md`. No score, fixed weight, or Definition of Done checkbox is altered by this index update.


## Android API 35 runtime acceptance update — 2026-10-27

- [Native ARM64-host runtime workflow](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477658242) completed with **success** on the verification harness commit `598ca10c148e6c0c47c362d6cfaa73603433a3b6`, with the canonical ONE source pinned and checked out at `0d0202a1405ae12aaaadf05c6916bacc70316126`.
- Runtime job: [122100141841](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477658242/job/122100141841). The log confirms the runner architecture was `aarch64`, the guest API level was checked as 35 and ABI as `arm64-v8a`, the backend-generated ELF was pushed and executed, **exit code 0**, and the final output line was exactly `ONE_NATIVE_BACKEND_OK`.
- Evidence artifact: [one-api35-arm64-runtime-evidence-0d0202a1405ae12aaaadf05c6916bacc70316126](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40477658242) (artifact ID `12722651198`; SHA-256 of uploaded ZIP: `03c3a79a44ae6511d5550bb932398575ebfd686592b720e3153a3f0d6066f770`). Artifact includes the source SHA record, runtime result, ELF metadata/binary and emulator/QEMU diagnostics.
- This closes the previously open Android runtime execution fact for this exact candidate SHA only. It does **not** by itself award the E1/E2/E6 ledger rows, check Definition of Done items, establish production trusted-publisher acceptance, or make final release PASS.


## Protected release runner retry update — 2026-10-28

- [Protected ONE package provenance release](https://github.com/panglimanetizen01/one/actions/runs/40467992667) was retried again as job `122568205344` after the previous attempt failed before steps. The retry also completed as failure with an empty step list; log retrieval returned `BlobNotFound`. This is direct evidence that the job did not execute the source validation, signing, or trusted-publisher verification commands. It is an infrastructure/job-start failure, not a code-level provenance failure and not a PASS. The workflow was not bypassed, and no secret values were accessed or disclosed.
- The fixed-weight ledger was rerun after the Android runtime completed: [run 40478102859, latest attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40478102859). The live gate no longer lists Android runtime as an acceptance failure, but it remains NOT PASSED due to E1, E2, E6, seven unchecked DoD items, and the protected release workflow's failed conclusion.


## Historical candidate checkpoint — 2026-10-28T01:10Z (superseded; retained for audit trail)

- Canonical ONE milestone branch HEAD is now `89bd3297b53e21ec37180559ea20fe95ebb8f63e` (commit [89bd329](https://github.com/panglimanetizen01/one/commit/89bd3297b53e21ec37180559ea20fe95ebb8f63e)). This is a documentation reconciliation commit that corrects the stale claim that no Android runtime PASS existed. It does not change runtime implementation and does not carry previous SHA acceptance automatically.
- Independent verifier pin was updated to the exact new SHA in [verifier commit 7633aac](https://github.com/panglimanetizen01/one-windows-verification/commit/7633aac35978b12d6149e3bf79b18f70f2bbbcff). The push has launched the required exact-SHA matrix; at checkpoint capture:
  - [Cross-platform verification #40613334296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334296) — queued.
  - [Linux distro #40613334444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334444) — queued.
  - [Candidate artifact integrity #40613334473](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334473) — queued.
  - [E4 adversarial regression #40613334339](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334339) — queued.
  - [E4 SEC-05 subprocess #40613334345](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334345) — queued.
  - [Focused standard library/database #40613334381](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334381) — queued.
  - [E1 Windows acceptance #40613334441](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334441) — in progress.
  - [Cargo lockfile bootstrap #40613334258](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334258) — in progress.
  - [Android native ARM64-host runtime #40613334383](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334383) — in progress; no runtime claim until job output is checked.
  - [Fixed-weight ledger gate #40613334375](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334375) — in progress; no score claim until the gate completes.
  - [Android software-emulation fallback #40613334332](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334332) and [macOS HVF capability probe #40613334582](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334582) — queued; these are diagnostics/fallback paths and do not substitute for a successful runtime result.
- Canonical hosted CI on the new SHA also failed before executable steps were available. Runs [E1 lab #40613165664](https://github.com/panglimanetizen01/one/actions/runs/40613165664), [E2 lab #40613165725](https://github.com/panglimanetizen01/one/actions/runs/40613165725), [Linux distro #40613165667](https://github.com/panglimanetizen01/one/actions/runs/40613165667), and [focused stdlib #40613165662](https://github.com/panglimanetizen01/one/actions/runs/40613165662) all failed with job step lists empty and log retrieval returning `BlobNotFound`. Each workflow's failed jobs were retried once; the new attempt again returned completed failure with `steps: null` and no logs URL. This is a runner/job-start infrastructure blocker, not source-test evidence. Do not count these runs as PASS or as code-level test failures.
- The prior Android runtime PASS remains valid only for source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`; the new candidate's Android and full matrix evidence is pending the runs listed above.
- The fixed-weight gate remains NOT PASSED until the exact-SHA ledger run completes and E1/E2/E6 plus all DoD rows are independently accepted. No release is authorized.


## Exact-SHA verification results update — candidate `89bd3297b53e21ec37180559ea20fe95ebb8f63e`

Completed results confirmed from job logs and job conclusions:

- [E1 cross-platform acceptance lab #40613334404](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334404): Ubuntu 24.04 and Windows Server 2025 both **success**. Both jobs checked out the exact pinned source, ran the standard-library integration suite, library unit suite, full workspace tests, warnings-denied Clippy, and contract checker. Windows workspace test log includes 241 passed, 0 failed; both job conclusions are success.
- [Full cross-platform verification #40613334296](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334296): Ubuntu and Windows jobs both **success**. Logs include workspace tests, offline verification, native-target contract checks, and bundle build/package steps.
- [E1 Standard Library Acceptance #40613334441](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334441): **success**.
- [Focused standard-library/database verification #40613334381](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334381): **success**, including the test log summary `250 passed; 0 failed` and contract checker PASS.
- [Linux distribution verification #40613334444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334444): Ubuntu 24.04 and Debian 12 both **success**.
- [E4 adversarial filesystem/resource bounds #40613334339](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334339): Unix and Windows jobs both **success**.
- [E4 SEC-05 subprocess timeout/output-limit #40613334345](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334345): Linux and Windows jobs both **success**.
- [Cargo lockfile bootstrap #40613334258](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334258): **success**.
- [Package provenance end-to-end lab #40613334413](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334413): **success** for deterministic bytes, lock behavior, source-bound signature and tamper/invalid-publisher tests under disposable **synthetic** trust only. This is not production trusted-publisher acceptance. Artifact ID `12784445791`, uploaded ZIP SHA-256 `24523dacb8557f4d9e03ad934220ec04f72a6ce91f6cf6acd95f57c058e1dd4b`.
- Android AArch64 cross-builds [#40613334383](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334383) and [#40613334512](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334512): exact-source ELF build jobs **success**; runtime jobs are still in progress at this update.
- [Candidate artifact integrity #40613334473](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334473): **success** on exact source SHA `89bd3297b53e21ec37180559ea20fe95ebb8f63e`; Linux bundle metadata names target `x86_64-unknown-linux-gnu`, Rust/Cargo 1.99.0, CLI 0.1.0, embedded checksum matches binary SHA-256 `cb49c0a49da38bd147adf977889a379bd1631668cec511609e1bff983ce476e`, and ELF64 little-endian EM_X86_64 passes. Windows bundle metadata names target `x86_64-pc-windows-msvc`, Rust/Cargo 1.99.0, CLI 0.1.0, embedded checksum matches binary SHA-256 `dcc772b68bdfc6652456d3da146a42258909dcb5399fdd5bde205ed056b1dd30`, and PE32+ x86-64 passes.
- [Android Linux TCG #40613334253](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334253) and [Android software-emulation fallback #40613334452](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334452): failed before ELF execution with the explicit QEMU fatal message `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host. System image must match the host architecture.` These are incompatible host/guest attempts, not runtime acceptance and not a source-code failure. Their diagnostic artifacts were uploaded; the compatible ARM64-host runtime path remains in progress.
- [Fixed-weight ledger gate #40613334375](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40613334375) ran before the latest evidence-index update and correctly failed closed because the index did not yet name source SHA `89bd3297b53e21ec37180559ea20fe95ebb8f63e`, E1/E2/E6 were not accepted, seven DoD items remained unchecked, and mandatory exact-SHA runs were still pending. Rerun the ledger after all relevant current-SHA jobs complete; do not reuse this failed gate as a final result.

These results advance E1 and the E3/E4 evidence on the exact candidate SHA, but do not award E1/E3/E4 ledger points automatically. Candidate artifact integrity is now PASS for this SHA. E2 production trusted-publisher acceptance, E6 forensic reconciliation, the Android runtime result for this SHA, final DoD reconciliation, and the final ledger gate remain open.


## Canonical hosted-CI retry classification — 2026-10-28

- The canonical [One CI run #40613165686](https://github.com/panglimanetizen01/one/actions/runs/40613165686), pinned to candidate SHA `89bd3297b53e21ec37180559ea20fe95ebb8f63e`, was retried once after the earlier no-step failures. The retry jobs `122571500293` (Android), `122571500615` (Windows), and `122571500749` (Ubuntu) all completed as failure with empty step lists; each job-log download returned `BlobNotFound`. This reproduces the runner/job-start failure across the canonical matrix; it provides no source-test result and cannot be counted as PASS. Independent exact-SHA workflows are executing on the verification repository, but this does not silently replace the canonical hosted-CI requirement.
- The protected production provenance workflow's latest known run remains [#40467992667, attempt 7](https://github.com/panglimanetizen01/one/actions/runs/40467992667), pinned to older source SHA `0d0202a1405ae12aaaadf05c6916bacc70316126`; job `122568205344` had `runner_id=0`, empty runner name and `steps=[]`. There is no protected production release run for current SHA `89bd3297b53e21ec37180559ea20fe95ebb8f63e`. No workflow-dispatch was executed for the new SHA, and no source-path change was made solely to trigger the protected release workflow; production trusted-publisher acceptance remains open. No secret was read or disclosed, and no release was published.


## Historical candidate update — 2026-10-28 (superseded by the exact-SHA refreshes below)

- Canonical milestone branch advanced from `89bd3297b53e21ec37180559ea20fe95ebb8f63e` to source SHA `fbb8824fc48717aef7605f2dee8da25dbe2acdb7` in [commit `fbb8824`](https://github.com/panglimanetizen01/one/commit/fbb8824fc48717aef7605f2dee8da25dbe2acdb7). This is a code-bearing E1 change, not a documentation-only commit.
- Added the pure source-level built-in `hapus kunci pemetaan` through semantic registration/type checks and the canonical interpreter dispatch to `one_core::stdlib::map_remove`. The operation returns a new mapping, preserves its input, treats a missing key as a no-op, and rejects known receiver/key type mismatches with `E2043` (runtime invalid values remain `R3022`). Added end-to-end tests for deterministic JSON output, immutability, missing-key behavior, and invalid receiver/key types; updated the normative standard-library API contract.
- Canonical Actions on this exact source SHA did not execute any workflow steps: [One CI #40615117242](https://github.com/panglimanetizen01/one/actions/runs/40615117242), [E1 lab #40615117312](https://github.com/panglimanetizen01/one/actions/runs/40615117312), [focused stdlib #40615117272](https://github.com/panglimanetizen01/one/actions/runs/40615117272), [Linux distro #40615117241](https://github.com/panglimanetizen01/one/actions/runs/40615117241), [E2 lab #40615117302](https://github.com/panglimanetizen01/one/actions/runs/40615117302), and duplicate attempts [#40615111885](https://github.com/panglimanetizen01/one/actions/runs/40615111885), [#40615111946](https://github.com/panglimanetizen01/one/actions/runs/40615111946), [#40615111804](https://github.com/panglimanetizen01/one/actions/runs/40615111804). Their job step lists are empty and log retrieval returns `BlobNotFound`; they are runner/job-start failures, not code-test results.
- The protected [ONE Package Provenance Release #40615111851](https://github.com/panglimanetizen01/one/actions/runs/40615111851) was triggered by the code-path push on exact SHA `fbb8824fc48717aef7605f2dee8da25dbe2acdb7`, but its job `122575656360` failed before steps with no logs. This is not production trusted-publisher acceptance and produced no verified release artifact.
- The independent verifier pin is updated to `fbb8824fc48717aef7605f2dee8da25dbe2acdb7` in this commit. All required exact-SHA mirror workflows, including E1, cross-platform, artifact integrity, E4, package lab, and Android runtime, must be checked against this new SHA. The earlier passing matrix on `89bd3297b53e21ec37180559ea20fe95ebb8f63e` remains historical and cannot certify this code-bearing candidate.
- E1 ledger score is not changed by the presence of the patch or test file; it remains pending exact-SHA executable evidence and full-row acceptance. E2 production trusted-publisher acceptance, E6, and final release remain NOT PASSED.


## E1 mapping-removal implementation and test-failure correction — 2026-10-28

- Candidate `fbb8824fc48717aef7605f2dee8da25dbe2acdb7` introduced source-level `hapus kunci pemetaan`, its semantic contract, interpreter dispatch, end-to-end tests, and normative docs. The independent [E1 Windows acceptance run #40615236159](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615236159), job `122576061524`, executed tests and exposed a real implementation defect: the test `mapping_remove_builtin_returns_a_new_map_and_missing_key_is_a_noop` failed with runtime `R3019: Pekerjaan 'hapus kunci pemetaan' belum dibuat.` The function was registered in semantic analysis and had a dispatch arm, but was missing from the interpreter's built-in recognition/arity gate.
- Fixed that defect in [canonical commit `f90f018`](https://github.com/panglimanetizen01/one/commit/f90f01874ea500ef1c7f280cba6b55a3a302405d) by adding `hapus kunci pemetaan` to the interpreter's built-in name set and its two-argument arity branch. The test failure on `fbb8824fc48717aef7605f2dee8da25dbe2acdb7` is a real red result, not an infrastructure classification.
- Canonical workflows on the fixed SHA `f90f01874ea500ef1c7f280cba6b55a3a302405d` were started by the source commit, but their latest outcomes are again runner-start failures: [One CI #40615411211](https://github.com/panglimanetizen01/one/actions/runs/40615411211) is queued at checkpoint; [E1 lab #40615406726](https://github.com/panglimanetizen01/one/actions/runs/40615406726), [focused stdlib #40615406605](https://github.com/panglimanetizen01/one/actions/runs/40615406605), [Linux distro #40615406509](https://github.com/panglimanetizen01/one/actions/runs/40615406509), [E2 lab #40615406660](https://github.com/panglimanetizen01/one/actions/runs/40615406660), and [protected provenance release #40615406526](https://github.com/panglimanetizen01/one/actions/runs/40615406526) have no executable job steps and log retrieval returns `BlobNotFound`. These are not green test results; the source-level regression must be rerun in the independent verification repository.
- The canonical verifier pin is now updated to exact source SHA `f90f01874ea500ef1c7f280cba6b55a3a302405d` in this commit. Required exact-SHA workflows are being retriggered. Prior passes on `89bd3297b53e21ec37180559ea20fe95ebb8f63e` and `fbb8824fc48717aef7605f2dee8da25dbe2acdb7` are historical only; no E1 score is awarded until the fixed candidate's test and acceptance evidence passes.


## Network-test isolation fix and new candidate — 2026-10-28

- Exact-SHA [E4 adversarial run #40615475441](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615475441) on source `f90f01874ea500ef1c7f280cba6b55a3a302405d` passed the Windows job but failed the Unix library-test job `122576836501`. The failing test was `network_runtime::tests::tcp_round_trip_uses_real_loopback_socket`; its log showed `InvalidOperation("Jumlah operasi jaringan aktif melampaui batas global.")`. The suite also contains `network_connections_hold_global_resource_permits_until_closed`, which deliberately consumes the shared process-global operation budget. These two tests were running concurrently, so the quota-exhaustion test could starve the independent TCP round-trip test. This is a test-isolation race, not evidence of a production runtime regression.
- Fixed in [canonical commit `06c3e74`](https://github.com/panglimanetizen01/one/commit/06c3e740d8c886d7d1a14493831ed41e09e2d3b9) by introducing a test-only mutex shared by the global-permit saturation test and real-loopback TCP/HTTP tests that consume global permits. The assertions and production quota are unchanged; only conflicting tests are serialized.
- The independent verifier pin now targets `06c3e740d8c886d7d1a14493831ed41e09e2d3b9` in this commit. The previous matrix for `f90f01874ea500ef1c7f280cba6b55a3a302405d` is historical and cannot certify the test-isolation patch. Re-run the exact-SHA E1, E3/E4, packaging, artifact, Android runtime and fixed-weight ledger checks against `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`.
- Canonical hosted Actions on `f90f01874ea500ef1c7f280cba6b55a3a302405d` again failed before any job step; protected package provenance release [#40615406526](https://github.com/panglimanetizen01/one/actions/runs/40615406526) had no executable steps or logs. The same path must be exercised on `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`; no release artifact or production trusted-publisher PASS has been established.


## Current exact-SHA acceptance results — `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`

Verified complete PASS results from the current pinned source:

- [E1 cross-platform acceptance lab #40615864788](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864788): Ubuntu 24.04 and Windows Server 2025 both **success**. Both logs confirm exact source SHA `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`, the new `mapping_remove_builtin_returns_a_new_map_and_missing_key_is_a_noop` test PASS, `stdlib_builtins` 38 passed / 0 failed, workspace tests 241 passed / 0 failed, warnings-denied Clippy, and `CONTRACT CHECK: PASS`.
- [E1 Standard Library Acceptance #40615864765](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864765): **success**, with the mapping-removal regression passing.
- [Full cross-platform verification #40615864970](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864970): Ubuntu and Windows both **success**. Ubuntu log confirms 250 passed / 0 failed and `OFFLINE VERIFICATION: PASS`; Windows log confirms workspace and integration tests, offline verification and contract checks.
- [Candidate artifact integrity #40615864879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864879): **success**. Linux artifact ID `12785057736`, ZIP SHA-256 `67a4fac13f7c1e6db87c1361fc89b8f27eb843c5539c92636d9738a16e1eb352`, binary SHA-256 `84f47dbd4c902151bb38dddfabe47835b9dbc133c59817aa3d13c3fcced41975`, ELF64 little-endian EM_X86_64. Windows artifact ID `12785207351`, ZIP SHA-256 `f9755458333a714433f2fd637130b1fa5c1eb3eec28fe49bc3b026a1a819c068`, binary SHA-256 `40cc76613e813469d417b74ddb3f59e3bab18c0db5a98848871fa07ad07d9422`, PE32+ x86-64. Both embedded manifests bind to the exact candidate SHA and Rust/Cargo 1.99.0 / CLI 0.1.0 metadata.
- [Linux distro matrix #40615864924](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864924): Ubuntu 24.04 and Debian 12 both **success**.
- [Focused standard-library/database #40615864973](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864973): **success**.
- [E4 adversarial filesystem/resource-bound #40615864798](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864798): Unix and Windows both **success** after the test-only global-permit isolation fix. The Unix log shows both `tcp_round_trip_uses_real_loopback_socket` and `network_connections_hold_global_resource_permits_until_closed` passed.
- [E4 SEC-05 subprocess timeout/output-limit #40615864837](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864837): Linux and Windows both **success**.
- [E4 subprocess resource guard #40615864935](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864935): **success**.
- [Cargo lockfile bootstrap #40615864835](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864835): **success**.
- [Package/provenance lab #40615864922](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864922): **success** for deterministic package bytes, lock/stale-lock, source-bound signature and tamper tests under disposable **synthetic trust only**. Artifact ID `12784699292`, ZIP SHA-256 `728a8335b9f61f2a25c09e2de5b0bb577b433ef47147041968af8028d210f4c1`.
- Android AArch64 cross-build jobs passed: [native ARM64-host workflow #40615864980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864980), ELF artifact ID `12785500562`, ZIP digest `sha256:d811d99df589732bf9dce3c6d21a0e4b706e7e9f0b97ec15a6d24101555ff7ec`; [community ARM64 fallback #40615865014](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615865014), ELF artifact ID `12785401068`, ZIP digest `sha256:15de6713fe2a8ccaeb338860df16ac4dcf9e48d39976669ceb44c6c81ba5dc2f`. The corresponding API 35 / `arm64-v8a` runtime jobs are still in progress; no current-SHA runtime PASS is claimed yet.
- [Android x86_64-host TCG runtime #40615864864](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864864) failed before ELF execution with the explicit QEMU fatal message that an `arm64` AVD is unsupported on an `x86_64` host. It uploaded a diagnostic artifact. This is a known incompatible guest/host path, not runtime acceptance.

## Canonical hosted CI and production release — current source SHA

- [Canonical One CI #40615809865](https://github.com/panglimanetizen01/one/actions/runs/40615809865) was retried once. The retry jobs `122580708943`, `122580709103`, and `122580709140` all completed failure with `runner_id=0`, empty runner names, and zero steps.
- [Protected package provenance release #40615804347](https://github.com/panglimanetizen01/one/actions/runs/40615804347) was retried once as job `122580654236`; it also completed failure with `runner_id=0`, empty runner name, and zero steps. No signing, trust-store verification, or artifact upload executed. This is not E2 production acceptance and no release was published.
- The independent exact-SHA matrix is strong current evidence, but it does not silently replace the canonical hosted-CI requirement. The final ledger must remain NOT PASSED while Android runtime, E1/E2/E6 full-row acceptance, and the required canonical/protected release execution are open.


## Exact-SHA regression results — 2026-10-28, candidate `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`

The following completed jobs have been checked against their actual latest-attempt job conclusions and are **PASS for the named checks only**:

- [E1 standard-library contract/integration/lint #40615864765](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864765): job `122578075833` success; new mapping-removal test passed, stdlib suite `38 passed, 0 failed`, workspace library tests `241 passed, 0 failed`, contract checker PASS.
- [E1 cross-platform lab #40615864788](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864788): Ubuntu job `122578076357` and Windows Server 2025 job `122578076750` both success.
- [Full cross-platform verification #40615864970](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864970): Ubuntu job `122578509383` and Windows job `122578509684` both success.
- [Candidate artifact integrity #40615864879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864879): job `122578075880` success.
- [Linux distro matrix #40615864924](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864924): Ubuntu 24.04 job `122578076172` and Debian 12 job `122578076438` both success.
- [Focused standard-library/database regressions #40615864973](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864973): job `122578076418` success.
- [E4 adversarial filesystem/resource-bound checks #40615864798](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864798): Unix job `122578075387` and Windows job `122578075705` both success. The previously failing loopback test and quota-saturation test both passed after the test-only mutex fix.
- [E4 SEC-05 timeout/output-limit #40615864837](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864837): Windows job `122578075736` and Linux job `122578076244` both success.
- [E4 subprocess resource guard #40615864935](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864935): job `122578075979` success.
- [Cargo lockfile bootstrap #40615864835](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864835): job `122578076311` success.
- [Package determinism/signature/tamper lab #40615864922](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864922): job `122578076407` success using synthetic trust only; **not E2 production trust acceptance**.

### Ledger and unresolved mandatory gates

- Initial [ledger run #40615864847](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864847) failed closed while current-SHA required jobs were still queued/in progress, seven DoD items remained unchecked, E1/E2/E6 rows had no full-row acceptance evidence, and protected release had failed.
- After the current-SHA matrix above completed, failed ledger job `122578075992` was explicitly re-run. New attempt job `122584057778` was queued at checkpoint; no conclusion is credited yet.
- Android native ARM64-host runtime [#40615864980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864980) built the exact-source ELF and produced artifact `12785500562` (SHA-256 `d811d99df589732bf9dce3c6d21a0e4b706e7e9f0b97ec15a6d24101555ff7ec`), but runtime job `122578974567` was still in the boot step; **no runtime PASS yet**.
- Community ARM64 fallback [#40615865014](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615865014) built the exact-source ELF and produced artifact `12785401068` (SHA-256 `15de6713fe2a8ccaeb338860df16ac4dcf9e48d39976669ceb44c6c81ba5dc2f`), but runtime job `122579375110` was still booting API 35; **no runtime PASS yet**.
- Protected package release [#40615804347](https://github.com/panglimanetizen01/one/actions/runs/40615804347), attempt 2, failed. Job `122580654236` has no step summaries; log retrieval returned `BlobNotFound`; no artifacts were produced. Run metadata confirms event `push`, candidate SHA `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`, and attempt 2, but does not expose a root cause. Do not infer secret or environment failure from missing logs.
- E1/E2/E6 full-row acceptance, all DoD checkboxes, production trusted-publisher verification, Android runtime execution, and final release remain open. Scores remain unchanged until the official ledger verifies all acceptance criteria.


## Android API 35 runtime PASS — exact source SHA `06c3e740d8c886d7d1a14493831ed41e09e2d3b9` (2026-10-28)

**Native ARM64-host runtime acceptance is now proven for this exact source SHA.** [Workflow #40615864980](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864980), job [`122578974567`](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864980/job/122578974567), completed successfully. Its exact-source checkout and ARM64 host checks passed; the API 35 `arm64-v8a` emulator reached `sys.boot_completed=1`; the generated ELF was pushed to the guest and executed. The job log records:

- ELF: `ELF 64-bit LSB pie executable, ARM aarch64`, interpreter `/system/bin/linker64`.
- Guest process exit code: `0`.
- Exact guest output: `ONE_NATIVE_BACKEND_OK`.
- Evidence artifact: [artifact `12786176877`](https://api.github.com/repos/panglimanetizen01/one-windows-verification/actions/artifacts/12786176877), `one-api35-arm64-runtime-evidence-06c3e740d8c886d7d1a14493831ed41e09e2d3b9`, archive SHA-256 `29e7bbd7e1dabe95ebc727a5b14bfa428476b3825fecfa57255839934b36180a`.

This closes the Android runtime execution criterion **for this candidate SHA only**; it does not alone close E3/E1/E2/E6 or the release gate. The community ARM64 fallback [#40615865014](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615865014) was still booting at the last check and is not credited; the native-host success is the valid alternative accepted by the ledger verifier.

### Latest ledger/release retries

- After the native-host Android success, the failed ledger job from [run #40615864847](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864847) was retried again. Latest attempt job `122584935681` is `in_progress` at this checkpoint; no result is credited yet.
- Protected release [run #40615804347](https://github.com/panglimanetizen01/one/actions/runs/40615804347), job retry `122584598175`, failed again before any readable step summaries; log retrieval still returns `BlobNotFound`, and no artifact exists. This remains an unresolved canonical runner/job-start failure, not production trusted-publisher acceptance. Do not infer missing secrets or environment configuration without job evidence.


## Ledger retry result after Android runtime acceptance — 2026-10-28

- [Ledger run #40615864847](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864847), latest retry job [`122584935681`](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40615864847/job/122584935681), completed and correctly returned **NOT PASSED** for pinned source SHA `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`.
- The current live workflow matrix no longer reports a missing Android runtime: native ARM64-host run `40615864980` succeeded with exit code 0 and exact `ONE_NATIVE_BACKEND_OK`.
- Remaining explicit ledger blockers are seven unchecked Definition of Done items, E1 `0/10` full-row evidence, E2 `0/8` production trusted-publisher acceptance, E6 `0/4` final forensic audit, and protected release run `40615804347` completed/failure. No points were awarded and no checklist was checked to bypass these requirements.
- Canonical protected-release job retry [`122584598175`](https://github.com/panglimanetizen01/one/actions/runs/40615804347) also completed/failure with no step summaries; log retrieval returned `BlobNotFound` and no artifacts were created. Root cause remains **UNKNOWN** from available metadata. This is an unresolved job-start/infrastructure-path failure, not proof that signing secrets/trust material are missing and not production acceptance.


## Canonical hosted CI diagnosis — exact source SHA `06c3e740d8c886d7d1a14493831ed41e09e2d3b9`

Inspected the canonical Actions job metadata for these current-SHA runs: [E2 lab #40615809803](https://github.com/panglimanetizen01/one/actions/runs/40615809803), [focused stdlib #40615809871](https://github.com/panglimanetizen01/one/actions/runs/40615809871), [E1 lab #40615809816](https://github.com/panglimanetizen01/one/actions/runs/40615809816), [One CI #40615809865](https://github.com/panglimanetizen01/one/actions/runs/40615809865), [Linux distro #40615809757](https://github.com/panglimanetizen01/one/actions/runs/40615809757), and push-triggered [E1 #40615804332](https://github.com/panglimanetizen01/one/actions/runs/40615804332), [Linux distro #40615804396](https://github.com/panglimanetizen01/one/actions/runs/40615804396), and [E2 lab #40615804464](https://github.com/panglimanetizen01/one/actions/runs/40615804464). All 15 associated job records inspected across these runs report empty step lists; all eight representative job-log retrievals returned GitHub `BlobNotFound`. No command/test output was produced by those jobs. This repeated cross-workflow pattern supports classification as **canonical Actions job-start/log infrastructure failure**, not as a code test failure and not as PASS. The protected release run's third attempt [#40615804347](https://github.com/panglimanetizen01/one/actions/runs/40615804347) likewise has `steps: null`, `logs_url: null`, and no artifacts. Available evidence does not identify the infrastructure root cause, so it remains **UNKNOWN**; do not infer missing secrets, environment configuration, or permissions.

The independent exact-SHA matrix remains separate and does execute tests. It has passed the named E1, E3 cross-platform, E4, package determinism/synthetic-trust, artifact-integrity and Linux-distro checks; native Android API 35 runtime also passed as documented above. These independent results do not silently satisfy the canonical hosted-CI requirement or E2 production trust requirement.


## Candidate pin update — 2026-10-28

- The independent verifier pin was advanced to canonical milestone branch HEAD `342a7641266f728c05f610d397d79867df678227` by verifier commit [`d7647b4`](https://github.com/panglimanetizen01/one-windows-verification/commit/d7647b4942df6499b93769eb63ba639e56229791).
- This source revision adds a focused regression test for first-match list removal and input-copy preservation. It is a new source SHA; prior E1/E3/E4/Android/package evidence tied to `06c3e740d8c886d7d1a14493831ed41e09e2d3b9` or earlier revisions is historical and is not automatically accepted for this pin.
- Exact-SHA matrix and fixed-weight ledger verification are now required for `342a7641266f728c05f610d397d79867df678227`. No score, Definition of Done checkbox, production trusted-publisher acceptance, or release status is changed by updating the pin.


## Candidate source delta — 2026-10-28

- Exact candidate pin advanced to `45b9c1220059eb5755faf67ee49d0d2382e6ac7a` after adding regression tests for empty-list display, list append order/empty/non-list inputs, and list removal with empty or absent values.
- Prior exact-SHA evidence for earlier source revisions does not certify this revision. The pin update triggers fresh independent ledger verification; accept no score or gate until the resulting exact-SHA jobs are inspected.

## Fresh exact-source matrix update — 2026-10-28T05:29Z

The candidate remains pinned to ONE source SHA `1a84d522a2953044c250ebe43c22989d6ec07dfc`. The following independent lab workflows completed successfully against that pin:

- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065845) — Ubuntu and Windows jobs passed.
- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065819) and [E1 Windows acceptance](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065811) — scoped suites passed; this is not a claim that the broader E1 row is complete.
- [Linux distro verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065997) — passed on the pinned source.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065808) and [Cargo lockfile bootstrap](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065836) — passed their defined scopes.
- [E4 adversarial filesystem/resource regressions](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065806), [SEC-05 subprocess timeout/output limits](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065919), and [subprocess resource guard](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065925) — passed their focused scopes. E4 remains unaccepted until the full threat review and full-row criteria are met.
- [Android API 35 arm64-v8a runtime](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40636250386) — **completed successfully on the exact source SHA**. The job checked out source SHA `1a84d522a2953044c250ebe43c22989d6ec07dfc`, built the AArch64 ELF, booted an API 35 `arm64-v8a` environment, pushed and executed the ELF, and recorded exit code `0` with output `ONE_NATIVE_BACKEND_OK`. Evidence artifact [12794720830](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40636250386/artifacts/12794720830), uploaded archive digest `sha256:2c616f1082158a281c09a9ec1d78bddd54ffa70ac9226cf8c28025cc1f671c22`.

Canonical-repository E1 and Linux distro workflow runs `40633942687` and `40633942635` failed before executing any step (runner ID `0`) even after retries. They remain classified as runner-start infrastructure failures, not passing tests or source-test failures. The independent lab results above do not conceal or reclassify those canonical failures.

The synthetic-trust provenance lab [40634065880](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40634065880) passed only its synthetic trust scope; it is **not** protected production release provenance and does not close E2. No protected source-bound release run is recorded for this candidate SHA. E1, E2, E4, and E6 remain open; no release is authorized.


## Corrective outcome delta — 2026-10-28 (supersedes earlier pending wording)

This dated delta preserves the earlier checkpoint as historical and records later completed results without rewriting prior run history.

- Canonical source pin remains `1119c450eda1437d79d75304a1daefb93e8a357f`, as recorded in `CANONICAL_COMMIT.txt`.
- Android API 35 AArch64 runtime run [40638899009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899009) subsequently completed successfully, including the native ARM64-host guest runtime job. This supersedes the earlier statement in the 05:46Z checkpoint that the guest runtime was still in progress. It is runtime PASS only for this run's tested scope and pinned source SHA.
- The post-runtime fixed-weight gate run [40640181816](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40640181816) and its failed-job retry both concluded **FAIL** at the acceptance gate. The exact-SHA source checkout was `1119c450eda1437d79d75304a1daefb93e8a357f`; verifier unit tests passed 7/7, but 8 DoD items remained unchecked and E1 0/10, E2 0/8, E4 0/6, E6 0/4. The Android runtime result is not a failure cause. Do not retry the gate again until relevant ledger/evidence or acceptance inputs change.
- The canonical source E1 lab [40638875488](https://github.com/panglimanetizen01/one/actions/runs/40638875488) and Linux distro run [40638875412](https://github.com/panglimanetizen01/one/actions/runs/40638875412) remain blocked before executable steps (`steps: null`) on their recorded attempts. These are infrastructure/job-start failures, not source-test PASS or FAIL evidence.
- The PR #80 description has been reconciled to the current candidate and the completed gate result. PR remains open/unmerged; no production release is authorized.
- No score, weight, or DoD checkbox is changed by this delta. Implementation remains 92/100 and verified remains 72/100 as the last recorded baseline, not a newly recalculated score. E1/E2/E4/E6 remain open.

### Next actions (no duplicate gate retry)

1. Continue E1's contract-to-language-call crosswalk and fix only confirmed implementation/test gaps; run focused tests and required suite on the resulting source SHA.
2. Continue E2 only through the authorized protected production provenance path.
3. Complete E4 threat-control/evidence crosswalk and E6 forensic reconciliation.
4. After a relevant acceptance input changes and is committed, run the gate against the exact pinned source and current verifier state; do not award points from workflow-green status alone.


## E1 source/spec/test crosswalk — 2026-10-28

This is a static source inspection of canonical candidate `1119c450eda1437d79d75304a1daefb93e8a357f`, not a substitute for executing the required acceptance matrix. It records what the checked-in files declare and test, without awarding E1 points.

### Normative sources inspected

- `docs/spec/one-v0.1-standard-library.md` — public API stability, deterministic operations, explicit effects, stable errors/signatures, and backend compatibility acceptance criteria.
- `docs/spec/one-v0.1-stdlib.md` — source-level call table, argument counts/result contracts, edge-case requirements, diagnostics, and required acceptance commands.
- `crates/one-core/src/semantic.rs` — static builtin registration/arity table.
- `crates/one-core/src/interpreter.rs` — runtime builtin recognition, arity enforcement, and delegation to typed `stdlib` helpers.
- `crates/one-core/src/stdlib.rs` — public Rust helper implementation and helper-level tests.
- `crates/one-core/tests/stdlib_builtins.rs` — source-pipeline integration and edge-contract tests.

### Parity result from source inspection

The 28 documented source-level calls were compared across the semantic registration and interpreter dispatch lists. The compared names are:

`panjang teks`, `teks memuat`, `teks diawali`, `teks diakhiri`, `huruf kecil`, `huruf besar`, `pangkas teks`, `ganti teks`, `pisah teks`, `ubah teks ke angka`, `panjang daftar`, `tambah elemen daftar`, `hapus elemen daftar`, `gabung teks`, `jumlah daftar angka`, `ambil indeks`, `nilai mutlak`, `bagi bulat`, `angka sisa bagi`, `angka minimum`, `angka maksimum`, `nilai pemetaan`, `atur pemetaan`, `hapus kunci pemetaan`, `ubah nilai ke json`, `nilai dari json`, `waktu utc dari unix`, and `unix dari waktu utc`.

**Static parity finding:** all 28 names appear in both the semantic registration and interpreter dispatch lists. No missing-name discrepancy was found in that comparison. The integration test file contains named tests for text, lists, mapping, JSON, integer boundaries/overflow, deterministic diagnostics, UTC canonicalization, invalid inputs, and public Rust helper contracts. This is evidence of declared coverage, not proof that each required command has passed on every required platform.

### E1 gaps that remain open

1. The normative acceptance commands must complete successfully on the same pinned source SHA: focused `stdlib_builtins`, `one-core --lib`, full workspace tests, warnings-denied Clippy, and `tools/check_contract.py`, with required platform coverage.
2. The current source lab's prior canonical Ubuntu/Windows run [40638875488](https://github.com/panglimanetizen01/one/actions/runs/40638875488) failed before executable steps (`steps: null`). It supplies no source-test result. The independent mirror Windows E1 run [40638899155](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899155) and cross-platform E1 run [40638899012](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899012) are scoped passes, but do not replace the full row's same-SHA acceptance requirements.
3. Source inspection alone cannot prove public Rust API stability, backend conformance, reproducible artifact provenance, or complete edge-case acceptance.
4. No E1 score, fixed weight, or DoD checkbox is changed by this crosswalk. E1 remains open until the required exact-SHA suite and ledger acceptance criteria are satisfied.

### Reproducible local acceptance sequence

Run from the canonical source checkout at the pinned SHA, preserving exit codes and full logs:

```bash
cargo --locked test -p one-core --test stdlib_builtins
cargo --locked test -p one-core --lib
cargo --locked test --workspace
cargo --locked clippy --workspace --all-targets --all-features -- -D warnings
python tools/check_contract.py
```

Each command's success must be captured as evidence; do not infer PASS from workflow creation/start, static inspection, or a different SHA.


## E4 threat-review reconciliation — 2026-10-28

Canonical source pin remains `1119c450eda1437d79d75304a1daefb93e8a357f`. This entry reconciles the threat review and current-pin workflow records; it does not claim complete sandboxing or award E4 points.

### Current-pin scoped workflow evidence

- [Filesystem/resource-bound adversarial regression, run 40638898955](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898955) — successful, scoped to its configured tests.
- [SEC-05 subprocess timeout/output limit, run 40638898978](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898978) — successful, scoped to its configured tests.
- [Subprocess resource guard, run 40638899440](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899440) — successful, scoped to its configured tests.
- [Cross-platform verification, run 40638898957](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638898957) and [Linux distribution verification, run 40638899092](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40638899092) — configured matrices passed.

These are bounded workflow outcomes. They do not independently prove every threat-review claim, nor do they replace a final frozen-SHA matrix after any future source change.

### Threat-claim acceptance still required

The source threat review itself lists these reconciliation targets: path traversal; symlink/reparse handling; mount-boundary detection; TOCTOU parent-swap races; capability denial before side effects; SQLite/query limits; shared operation quotas; subprocess descendant containment; timeout/output limits; and recovery after quota release. The current record explicitly retains Unix non-Linux mount-identity and caller-retained/intermediate-heap limitations.

The available workflow names/results establish scoped regressions, but do not by themselves provide a one-to-one claim → implementation invariant → adversarial assertion → platform result matrix for every target above. In particular, a successful subprocess timeout/output-limit workflow is not, without its assertions, proof of descendant-tree termination on every supported platform; a passing mount-boundary regression is not proof of universal filesystem confinement; and operation quotas do not prove a universal process heap cap.

### Disposition

- E4 implementation remains recorded as 6/6, but verified remains 0/6; this is not an acceptance contradiction because implementation and verification are distinct ledger dimensions.
- Do not check the E4 DoD item until the threat-review matrix is complete, all required platform tests pass against the final exact source SHA, residual limitations are accepted explicitly, and the fixed-weight gate validates the synchronized evidence.
- No new source workflow was dispatched by this documentation update. No merge, protected release, or release authorization is implied.


## E2 protected provenance workflow review — 2026-10-28

### Workflow inspected

Canonical candidate workflow: `.github/workflows/package-provenance-release.yml` at source branch `milestone/100-ecosystem-20261023`, file blob `9f8888608bb13a1748d75be49423893f26c19d61`. Its `workflow_dispatch` inputs are `project_path` and `publisher_id`; the job declares protected environment `one-release`. It validates the signing-seed format and trusted-publisher store, resolves the project root and checks it remains inside the checkout, builds the CLI with `cargo --locked`, packages twice and compares bytes, signs V2 source-bound Ed25519 provenance, verifies against the trust store and source tree, checks the source revision and artifact digest, and uploads the package, sidecar, and checksums.

### Security controls observed in workflow source

- The job runs in the protected `one-release` environment and requires the protected seed, publisher ID, and trusted-publisher store to be present.
- Project paths are constrained to repository-relative locations; `realpath -e` and a root-prefix check reject paths resolving outside the checkout.
- Deterministic package bytes are checked by building the package twice and comparing SHA-256 digests.
- The signed sidecar is checked against the checked-out Git revision, source-tree verification, final artifact digest, allowed artifact format, and dependency-model marker.
- Signing material is written under runner temporary storage with mode `0600`; this source inspection did not observe any command intentionally printing the seed or trusted-store contents.

### E2 remains blocked — no release was triggered

This is a workflow-source review, not a production provenance result. The current evidence record states that no successful protected `ONE Package Provenance Release` run exists for source SHA `1119c450eda1437d79d75304a1daefb93e8a357f`. No workflow dispatch or release publication was initiated during this continuation, because it would exercise protected signing material and potentially publish artifacts; that requires explicit release authorization and the appropriate protected-environment approval.

The workflow's push trigger only covers the candidate branch when selected package/workflow/source paths change. A documentation-only checkpoint commit in the independent verifier does not trigger the canonical source workflow. Do not infer that the workflow ran from its presence in the repository.

### Evidence required to close E2

1. Authorized run of the protected workflow against the intended frozen candidate source SHA and committed project input.
2. Successful protected-environment approval and evidence that the trusted publisher is independently configured.
3. Successful deterministic package comparison, V2 signature verification, source-tree/revision binding, artifact digest check, and portable checksum verification in the same run.
4. Retained artifact/sidecar/checksum identifiers and exact source SHA recorded in the evidence index.
5. Successful fixed-weight gate on the frozen source SHA after all required source evidence is available.

**Disposition:** E2 stays 7/8 implemented and 0/8 verified; DoD stays unchecked. This review awards no points, changes no source pin, and does not authorize merge or release.


## E6 forensic reconciliation — 2026-10-28

This pass reconciles the current candidate pin, fixed-weight ledger, DoD, E1/E2/E4 checkpoint findings, latest recorded gate result, and PR state. It is a consistency audit, not a release approval.

### Cross-document state at audit time

- Independent pin: `1119c450eda1437d79d75304a1daefb93e8a357f` in `CANONICAL_COMMIT.txt`.
- PR #80: open and unmerged; candidate branch remains `milestone/100-ecosystem-20261023`. The PR metadata has been updated to reference this checkpoint.
- Ledger baseline: implementation `92/100`, verified `72/100`, fixed row weights sum to 100. These are the last recorded ledger values, not a new PASS determination.
- DoD: exactly 8 unchecked items remain at the current source branch head. They cover final SHA freeze/evidence synchronization, failure classification and hosted-CI equivalence, full E1, protected production E2, complete E4, and E6.
- Acceptance rows still explicitly open: E1 `0/10`, E2 `0/8`, E4 `0/6`, E6 `0/4`. E3/E5 are numerically recorded as verified but explicitly provisional pending complete current-pin revalidation; do not treat those historical/scoped records as permission to close the global gate.
- Latest recorded gate: run [40640181816](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40640181816) failed closed. Its verifier tests passed 7/7, but the gate reported 8 unchecked DoD items and the open E1/E2/E4/E6 rows. The documented instruction is not to retry without a relevant evidence/acceptance-input change.
- The current E2 workflow review found the release workflow source controls, but no successful protected `ONE Package Provenance Release` run is recorded for the current source pin. No release was published or authorized.
- E1 static crosswalk confirms 28 builtin names are present in both semantic registration and interpreter dispatch. This does not replace the complete executable API/platform acceptance sequence.
- E4 current-pin scoped workflow results exist, but the one-to-one threat-claim matrix and explicit residual-limit disposition are still incomplete. E4 remains unaccepted.

### Consistency findings

1. The current pin and latest checkpoint statements agree on `1119c450eda1437d79d75304a1daefb93e8a357f`. Older SHAs and run links remain in the ledger/evidence index as historical records; they must not be relabeled as current-SHA results.
2. The `92/100` implementation and `72/100` verified figures are retained as a baseline, not asserted to mean the global gate passed. The ledger and DoD both say the gate is NOT PASSED.
3. The implementation/verified distinction for E4 is consistent: `6/6` implemented does not mean `6/6` accepted; verified remains `0/6`.
4. E2 workflow-source inspection is correctly distinguished from a protected release execution. A verifier documentation commit does not trigger the source workflow's path-filtered push event.
5. E6 cannot be marked complete while E1/E2/E4 acceptance is unresolved, the DoD has unchecked mandatory items, and the exact-SHA live gate is failed.

### Required next actions, in dependency order

1. Complete the remaining E1 public API contract and exact-SHA executable matrix; retain full logs and classify any job that fails before executable steps as infrastructure failure rather than a test pass.
2. Obtain explicit authorization for the protected `one-release` execution; run it only against the intended frozen SHA and preserve artifact, provenance sidecar, checksums, and run metadata. Do not bypass environment protection or expose secrets.
3. Finish the E4 claim → invariant → regression assertion → platform result matrix, including residual limitations and recovery behavior.
4. Freeze the intended candidate SHA only after source changes are finished. Re-pin the independent lab and rerun every mandatory exact-SHA workflow; synchronize the evidence index, ledger notes, DoD, PR body, and artifact metadata to that SHA.
5. Run the fixed-weight gate once the relevant evidence inputs above have changed; inspect the result and its job logs. Do not force a score or check a DoD item to manufacture a PASS.

**Disposition:** E6 remains `0/4`; no score, weight, or DoD checkbox is changed by this audit. The milestone remains NOT PASSED. PR #80 remains open/unmerged; no release is authorized.


## Candidate pin refresh — 2026-10-28T09:08Z

- **New canonical source SHA:** `1b950ebb3b9f4447229cec5055b9791520de87c5` ([commit](https://github.com/panglimanetizen01/one/commit/1b950ebb3b9f4447229cec5055b9791520de87c5)); source candidate branch `milestone/100-ecosystem-20261023` was fast-forwarded from the previous pin `1119c450eda1437d79d75304a1daefb93e8a357f`.
- **User-supplied Android/Termux local results for this SHA lineage:** `cargo --locked test -p one-core --lib` PASS (251 tests); `cargo --locked test -p one-core --test native_backend_linux_windows` PASS (8 tests); subsequent `cargo --locked test --workspace` PASS (`WORKSPACE=0`); `cargo --locked clippy --workspace --all-targets --all-features -- -D warnings` PASS; `python tools/check_contract.py` PASS (91 required artifacts, 85 concrete indexed artifacts, fixture checks pass). These are user-reported local results; this verifier has not executed them.
- Fixes in this candidate lineage address descriptor-relative filesystem access on Android/Termux, host gating for a GNU x86_64 Linux linker integration test, and unique temp fixture paths. The user-reported first full-workspace attempt had two human-core failures; the later final run reported `HUMAN_CORE=0 WORKSPACE=0 CLIPPY=0 CONTRACT=0`. Preserve both facts; the earlier failure is superseded by the later local run, not erased.
- Prior GitHub Actions runs listed above are bound to earlier source pins and are historical only. Do not carry their PASS results forward to `1b950ebb3b9f4447229cec5055b9791520de87c5`. Exact-SHA CI and verifier gate evidence must be regenerated for this pin.
- Fixed-weight ledger and DoD scores are unchanged. E1, E2, E4, E6 remain open; E3/E5 remain provisional. This pin update awards no points. No protected production provenance release was dispatched; no merge or release is authorized.


## Exact-SHA hosted evidence refresh — 2026-10-28T09:15Z

Source SHA remains `1b950ebb3b9f4447229cec5055b9791520de87c5`; these workflow runs check out that exact source pin. They were pending when the prior ledger gate evaluated and are now completed:

| Verification workflow | Run | Result |
|---|---:|---|
| E4 adversarial filesystem and resource-bound regression | [40661955051](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955051) | PASS |
| Android AArch64 cross-build and contract fallback x86_64 | [40661955036](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955036) | PASS |
| Candidate artifact integrity | [40661955029](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955029) | PASS |
| Cargo lockfile bootstrap | [40661955012](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955012) | PASS |
| Cross-platform verification | [40661955000](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955000) | PASS |
| Focused standard library/database | [40661954977](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954977) | PASS |
| E4 subprocess resource guard | [40661954963](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954963) | PASS |
| E1 Standard Library Windows acceptance | [40661954950](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954950) | PASS |
| Android AArch64 artifact build | [40661954942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954942) | PASS |
| Package provenance end-to-end with synthetic trust only | [40661954916](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954916) | PASS (synthetic trust only; not production release evidence) |
| E1 cross-platform acceptance lab | [40661954904](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954904) | PASS |
| E4 SEC-05 subprocess timeout/output limits | [40661954893](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954893) | PASS |
| Android AArch64 cross-build fallback | [40661954891](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954891) | PASS |
| Linux distribution verification | [40661954885](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661954885) | PASS |

The Android native ARM64 Linux-host runtime job [40661955153](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40661955153) was still in progress at this checkpoint and is not claimed as passed.

The source repository's E1, Linux distro, and E2 workflow attempts failed before executing any step (`runner_id=0`, `steps=0`). The non-release failed jobs were retried, but their latest attempts still report job-start failures without executable steps; this is infrastructure-unresolved, not test PASS and not a code-level regression finding. The protected production provenance release workflow was not retried or manually dispatched.

This refresh records observed workflow results only. It does not alter the fixed-weight ledger, award points, check Definition of Done items, or authorize merge/release. The next acceptance gate must re-evaluate live evidence against this source SHA and report any remaining failures.


## Candidate re-freeze after base-branch reconciliation — 2026-10-28T09:20Z

- **New exact candidate SHA:** `6d492006f9fa873fbd7d8ad61fa5833df707b1f6` ([merge commit](https://github.com/panglimanetizen01/one/commit/6d492006f9fa873fbd7d8ad61fa5833df707b1f6)).
- The candidate now contains current `main` as its second parent (`d35db95153f6ddd79885494c72f5aee16c899751`); PR #80 is now GitHub-mergeable (draft/open; not merged). This reconciles the three newer base-branch commits rather than leaving the PR in a dirty/conflicted state.
- The merge tree incorporates the main-branch direct-helper tests for `list_append` and `list_remove` (four tests: non-list rejection, remove-first duplicate behavior, absent-value no-op, and non-list removal rejection) and adds a matching direct-helper compatibility guard to `docs/spec/one-v0.1-stdlib.md`. The tests are present in the new source tree; hosted execution against this new SHA is still required.
- **All previous candidate-specific workflow results for `1b950ebb3b9f4447229cec5055b9791520de87c5` are historical after this source SHA change.** They remain useful as diagnostic history, but they must not satisfy the exact-SHA gate for `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`.
- User-supplied Termux test outcomes apply to the previous candidate lineage and have not yet been rerun against this merge SHA. Do not claim current-SHA local PASS based on them.
- The independent verifier pin has been updated to `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`; current-pin CI and acceptance must run again. Fixed-weight ledger remains implementation 92/100, verified 72/100 until new exact-SHA evidence supports any legitimate change. E1/E2/E4/E6 remain open. No production release or merge authorization is implied by making the PR conflict-free.


## Exact-SHA hosted evidence refresh — candidate `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`

Live runs below all checked out the exact pinned Project ONE source SHA `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`. These replace older-candidate results for current-pin acceptance; older evidence is historical only.

| Acceptance workflow | Exact-SHA run | Result |
|---|---:|---|
| E1 cross-platform acceptance lab | [40664235337](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235337) | PASS |
| Linux distribution conformance | [40664235479](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235479) | PASS |
| Focused standard library/database verification | [40664235556](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235556) | PASS |
| E1 Windows standard-library acceptance | [40664235517](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235517) | PASS |
| Cross-platform Linux/Windows verification | [40664235567](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235567) | PASS |
| Candidate artifact integrity | [40664235386](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235386) | PASS |
| Cargo lockfile bootstrap evidence | [40664235246](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235246) | PASS |
| E4 adversarial filesystem/resource-bound regression | [40664235672](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235672) | PASS |
| E4 subprocess resource guard | [40664235630](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235630) | PASS |
| E4 SEC-05 timeout/output limits | [40664235569](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235569) | PASS |
| Android AArch64 cross-build / contract fallback | [40664235293](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235293) | PASS |
| Android AArch64 device artifact build | [40664235620](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235620) | PASS |
| Android API 35 AArch64 runtime on ARM64 host | [40664235029](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235029) | PASS |
| Package provenance end-to-end lab | [40664235475](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235475) | PASS, synthetic trust only; not production publisher trust or release acceptance |

The exact-SHA ledger gate run [40664244856](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664244856) evaluated too early: its live workflow query saw several of the above runs still queued/in progress. A fresh gate evaluation is required after this evidence-index refresh and completion of the workflow matrix.

The source repository's One CI, focused standard-library, E1 lab, Linux distro, and E2 package/provenance lab jobs repeatedly failed before any steps executed (runner ID 0 / zero executable steps). These are unresolved GitHub job-start/runner failures, not test failures and not PASS. They were retried as non-release jobs; no additional blind retries will be issued without a runner/workflow change. The protected production package-provenance release workflow remains failed/unproven and was not retried or manually dispatched.

No score changes and no DoD items are checked by this evidence-index update. E1, E2, E4 and E6 ledger rows remain incomplete until their full acceptance definitions—not just individual green workflows—are satisfied. The candidate remains draft/open; no merge or production release authorization is implied.


## Documentation consistency correction — 2026-10-28

The earlier section dated `2026-10-28T05:45Z` is explicitly marked **historical/superseded**. Its `1119c450...` pin describes that checkpoint only and must not be interpreted as the current candidate. The authoritative current source SHA is the value at the top of this document and in `CANONICAL_COMMIT.txt`: `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`. Historical workflow references remain preserved as audit history and are not current-SHA acceptance evidence.


## Current-state precedence rule

For the current source pin and live status, use only the opening canonical SHA line, `CANONICAL_COMMIT.txt`, and the latest dated **Exact-SHA hosted evidence refresh** section. Any older checkpoint is historical even if its original heading used the word “Current”; those headings have been relabeled to prevent stale source SHAs or pending states from being mistaken for present acceptance. Historical logs remain available for forensic traceability and are not deleted.


## E1 source-surface inventory audit — candidate `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`

This is a coverage inventory, not a score promotion.

- Parsed the normative source-level call table in `docs/spec/one-v0.1-stdlib.md`: 28 declared call rows; every call name appears in `crates/one-core/tests/stdlib_builtins.rs`.
- The public `one_core::stdlib` module currently exports 29 helper functions. Its unit-test module includes direct regression coverage for display formatting; list append/remove including non-list rejection, first-duplicate removal and missing-value no-op; Unicode/text helpers; list/map helpers; checked integer helpers; JSON input/output size, depth, malformed input, deterministic ordering and integer boundaries; and strict UTC conversion.
- Exact-SHA hosted independent E1 evidence: [cross-platform E1 contract lab 40664235337](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235337) passed on Ubuntu 24.04 and Windows Server 2025; [Windows E1 acceptance 40664235517](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235517) passed; [focused standard-library/database run 40664235556](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40664235556) passed. All three are pinned to source SHA `6d492006f9fa873fbd7d8ad61fa5833df707b1f6`.
- These results establish that the currently documented source-level slice and helper regressions execute successfully on the exact candidate. They do **not** establish completion of standard-library domains outside the explicitly documented subset. The source spec itself says this is a partial library slice; E1 remains 0/10 until the project’s required reusable-standard-library scope is explicitly reconciled and fully satisfied. Do not infer broader completion from all 28 current call names being tested.
- Canonical source-repository CI remains independently blocked at job startup (zero steps / runner ID 0). The independent lab result is not mislabeled as canonical CI.


## Candidate SHA advance — E4 documentation consistency fix

The source branch advanced from `6d492006f9fa873fbd7d8ad61fa5833df707b1f6` to `28d1384588662cc93f405dc9dd5f3012183d249f` to relabel the old E4 reconciliation section as historical and add the current candidate evidence section. This is a documentation-only change; nevertheless, all prior workflow runs checked out the previous source SHA and are historical for the new pin. Do not count them as current-SHA acceptance. The new exact-SHA matrix must complete before the fixed-weight gate can accept this candidate. The verifier pin and README are being synchronized to `28d1384588662cc93f405dc9dd5f3012183d249f`. No ledger points or DoD items are changed by this pin update.


## Historical exact-SHA matrix — source SHA `28d1384588662cc93f405dc9dd5f3012183d249f` (superseded)

This section records current-pin workflow state as observed on 2026-10-28; all links below checked out the exact canonical source SHA `28d1384588662cc93f405dc9dd5f3012183d249f`.

| Required scoped workflow | Exact-SHA run | Observed result |
|---|---:|---|
| E1 cross-platform acceptance lab | [40669813386](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813386) | PASS — Ubuntu 24.04 and Windows Server 2025 |
| E1 Windows standard-library acceptance | [40669813471](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813471) | PASS |
| Focused standard library/database | [40669813400](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813400) | PASS |
| Cross-platform Linux/Windows verification | [40669813367](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813367) | PASS |
| Linux distribution conformance | [40669813433](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813433) | PASS |
| Candidate artifact integrity | [40669813330](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813330) | PASS |
| Cargo lockfile bootstrap | [40669813398](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813398) | PASS |
| E4 adversarial filesystem/resource bounds | [40669813282](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813282) | PASS for scoped tests |
| E4 SEC-05 subprocess timeout/output limit | [40669813337](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813337) | PASS for scoped tests |
| E4 subprocess resource guard | [40669813307](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813307) | PASS for scoped tests |
| Android AArch64 cross-build/contract fallback | [40669813340](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813340), [40669813341](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813341) | PASS |
| Android AArch64 device artifact | [40669813366](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813366) | PASS |
| Package provenance end-to-end lab | [40669813388](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813388) | PASS with synthetic trust only; not protected production release acceptance |
| Android API 35 AArch64 runtime on native ARM64 host | [40669813305](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813305) | PASS — API 35 / `arm64-v8a`; exact-SHA ELF exit code 0 and output `ONE_NATIVE_BACKEND_OK`; evidence artifact [12808866185](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813305/artifacts/12808866185) |

Canonical source repository workflows on the same SHA again failed before any executable steps: One CI run [40669773277](https://github.com/panglimanetizen01/one/actions/runs/40669773277), E1 lab [40669773287](https://github.com/panglimanetizen01/one/actions/runs/40669773287), E2 lab [40669773308](https://github.com/panglimanetizen01/one/actions/runs/40669773308), focused stdlib [40669773269](https://github.com/panglimanetizen01/one/actions/runs/40669773269), and Linux distro [40669773366](https://github.com/panglimanetizen01/one/actions/runs/40669773366). Their jobs expose empty step lists; this is job-start infrastructure failure, not a source test outcome.

The fixed-weight gate cannot pass yet. E1/E2/E4/E6 remain 0 verified until their complete row acceptance is recorded. E2 specifically requires the protected production release path and independently provisioned trusted-publisher material; synthetic trust is insufficient. Do not promote scores or mark DoD complete on the strength of this scoped matrix alone.


### Android API 35 runtime completion — 2026-10-28T10:24Z

The current-pin native ARM64 runtime [40669813305](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813305) has completed successfully on source SHA `28d1384588662cc93f405dc9dd5f3012183d249f`. The job verified Android API 35 and guest ABI `arm64-v8a`, executed the exact-source generated AArch64 ELF, recorded exit code `0` and output `ONE_NATIVE_BACKEND_OK`, and uploaded source-bound evidence artifact [12808866185](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40669813305/artifacts/12808866185). The matrix is now complete for the listed scoped workflows; the fixed-weight gate must be re-evaluated after this status update. This does not close E1/E2/E4/E6 or authorize a release.


## Current candidate freeze — source SHA `72c4d3d079a11d41e3410408898e6fe3ddcc9d05`

The canonical source advanced from `28d1384588662cc93f405dc9dd5f3012183d249f` to `72c4d3d079a11d41e3410408898e6fe3ddcc9d05` through a documentation-only acceptance record that provisionally accepts E4 at 6/6 within the declared Linux/Windows/Android scope and raises the ledger's provisional verified subtotal to 78/100. The prior matrix remains historical because it checked out `28d138...`; all required exact-SHA evidence must rerun against `72c4d3d079a11d41e3410408898e6fe3ddcc9d05` before the gate can accept the new ledger. The independent pin and README now target `72c4d3d079a11d41e3410408898e6fe3ddcc9d05`. The protected production release has not been dispatched, and E1/E2/E6 remain open.
