## Canonical workflow rerun observation — 2026-10-27

The independent verifier pin currently names candidate source SHA `c656c0d1f0b6fe7507467f49c59fe199e24c5c89` (confirmed from `CANONICAL_COMMIT.txt`). This supersedes the older `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9` evidence snapshot above for any claim about the current candidate; evidence tied to the older SHA is not silently carried forward.

Rerun requests were accepted for canonical runs:
- Standard Library Focused Verification: [40438771797](https://github.com/panglimanetizen01/one/actions/runs/40438771797)
- Linux Distribution Conformance: [40438771688](https://github.com/panglimanetizen01/one/actions/runs/40438771688)
- E1 Standard Library Test Lab: [40438771733](https://github.com/panglimanetizen01/one/actions/runs/40438771733)
- One CI: [40438771646](https://github.com/panglimanetizen01/one/actions/runs/40438771646)

The latest job metadata retrieved after these reruns reports failure conclusions and empty step arrays for the relevant jobs. Direct log retrieval returned `404 BlobNotFound`. Therefore these are **unclassified canonical workflow failures / evidence-access blocker**, not proven source-test failures and not passes. E2 run [40438771687](https://github.com/panglimanetizen01/one/actions/runs/40438771687) also reports failure; the connector's rerun action was blocked, and the protected release path remains unproven.

No source code, score, fixed weight, or Definition of Done checkbox was changed by this evidence update. Older matrix evidence tied to `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9` does not establish final-SHA acceptance for `c656c0d1f0b6fe7507467f49c59fe199e24c5c89`. The fixed-weight ledger remains implementation **92/100**, verified **78/100**; the gate remains closed pending exact-SHA canonical evidence, full E1 scope, protected E2 release/provenance, and E6 reconciliation.

---

## Fresh gate result after matrix completion — 2026-10-27 04:24 UTC

The fresh gate [run 40449434345](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449434345) completed **NOT PASSED** after all required exact-SHA mirror jobs had concluded. This is no longer a stale pending-job failure. The verifier's explicit remaining blockers are:

1. Seven unchecked Definition of Done acceptance items.
2. E1 full-row verified evidence remains 0/10. Exact-SHA standard-library suite passes on Linux and Windows, but the ledger requires the broader reusable API scope to be completed and formally accepted before full-row credit.
3. E2 verified evidence remains 0/8. No protected `one-release` package provenance workflow run exists for source SHA `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9`. The independent artifact integrity and package/build checks are not a substitute for a protected release signed by an independently configured trusted publisher.
4. E6 verified evidence remains 0/4 because the final forensic audit cannot close while E1/E2 and mandatory repository checks remain open.

Completed exact-SHA mirror evidence:
- E1 cross-platform acceptance [40446516694](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516694): Ubuntu and Windows pass.
- E4 filesystem/resource bounds [40446516704](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516704): Unix and Windows pass.
- SEC-05 subprocess limits [40446516581](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516581): Linux and Windows pass.
- Linux distribution [40446516598](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516598): pass.
- Artifact integrity [40446516592](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516592): pass.
- Cross-platform build/package [40446516600](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516600): Ubuntu and Windows pass.
- Android API 35 AArch64 runtime [40446516512](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516512): exact-source build and native ARM64 runtime pass.
- macOS HVF probe [40446516741](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516741): fails before guest execution with `HV_UNSUPPORTED`; superseded for runtime coverage by the successful native ARM64 run, not counted as a pass.

The canonical ONE repo's E1, focused stdlib, general CI, Linux distro, and E2 workflows remain failed on the exact source SHA after retry attempt 2; their logs are unavailable via the current GitHub connector and must be classified by the repository owner/maintainer using the Actions UI or repaired log access. They are not silently replaced by mirror tests.

Fixed weights and scores unchanged: implementation **92/100**, verified **78/100**. No DoD boxes or ledger row scores were changed. No source SHA changed in this update. The gate must remain closed until the actual E1 scope, protected E2 release/provenance, canonical hosted-workflow failures, and E6 forensic reconciliation are resolved.

---

## Completed exact-SHA matrix reconciliation — 2026-10-27 04:12 UTC

Canonical source SHA: `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9`. This entry records results from jobs that completed after the preceding gate snapshot; it does not alter source code, ledger weights, score, or DoD checkboxes.

- **PASS — candidate artifact integrity:** [run 40446516592](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516592), completed success.
- **PASS — cross-platform build/package verification:** [run 40446516600](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516600), Ubuntu and Windows jobs both successful.
- **PASS — Android API 35 AArch64 runtime on native ARM64 host:** [run 40446516512](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516512), exact-source ELF build and API 35 ARM64 runtime jobs both successful.
- **PASS — Linux distribution verification:** [run 40446516598](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516598).
- **PASS — E1 standard-library acceptance:** [run 40446516694](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516694), both Ubuntu and Windows jobs successful.
- **PASS — E4 filesystem/resource-bound adversarial tests:** [run 40446516704](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516704), Unix and Windows successful.
- **PASS — SEC-05 subprocess timeout/output cap:** [run 40446516581](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516581), Linux and Windows successful.
- **NOT CREDITED — macOS HVF Android probe:** [run 40446516741](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516741) failed with `HV_UNSUPPORTED` before guest execution. This is not treated as runtime evidence because the separate native ARM64 Android API 35 run passed.
- **Still pending / not credited:** macOS TCG alternative runtime [run 40446516732](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516732). It is not required to substitute for the successful native ARM64 runtime; retain it only as additional corroboration if it finishes.
- **Canonical ONE hosted workflows:** attempt 2 of E1, focused stdlib, CI, Linux distro and E2 remain failed with unavailable log blobs. These canonical workflow failures are still unresolved and must not be hidden by the independent lab passes.
- **Fixed-weight ledger gate:** the prior gate [run 40447344398](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40447344398) used a snapshot taken before artifact integrity, Linux distro, cross-platform and Android native ARM64 runs completed; its pending-job findings are stale. A fresh gate must be run. It will still correctly block full completion while E1/E2/E6 rows and seven DoD items remain open and no protected provenance release exists for this SHA.

Score remains implementation **92/100**, verified **78/100**. Do not promote E1's full-row verified score based only on its scoped suite, do not mark E2 accepted without the protected signed release, and do not mark E6 accepted before the final forensic audit.

---

## Reconciliation after completed matrix jobs — 2026-10-27 04:03 UTC

This entry supersedes the prior “still running” status for jobs that have since concluded. Canonical ONE source SHA remains `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9`.

- **PASS — E1 exact-SHA cross-platform acceptance:** [run 40446516694](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516694), Ubuntu 24.04 and Windows Server 2025 both successful.
- **PASS — E4 adversarial filesystem/resource bounds:** [run 40446516704](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516704), Unix and Windows jobs successful.
- **PASS — E4 SEC-05 subprocess timeout/output limit:** [run 40446516581](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516581), Windows and Linux jobs successful.
- **PASS — Linux distro matrix:** [run 40446516598](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516598), completed successfully.
- **FAIL — macOS ARM64 HVF Android runtime probe:** [run 40446516741](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516741) failed before ELF execution with `HVF error: HV_UNSUPPORTED` / `failed to initialize HVF: Invalid argument`. This is a runner virtualization limitation and is not Android runtime evidence. The independent native-ARM64 Linux-host and macOS TCG attempts remain in progress; neither is credited until actual API 35 guest ELF execution passes.
- **Still pending, not credited:** exact-SHA artifact integrity [run 40446516592](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516592), cross-platform build/package [run 40446516600](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516600), native ARM64 runtime [run 40446516512](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516512), and macOS TCG fallback [run 40446516732](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516732).
- **Canonical hosted workflows remain FAIL, cause unclassified:** retries (attempt 2) for E1 [40446485367](https://github.com/panglimanetizen01/one/actions/runs/40446485367), focused stdlib [40446485242](https://github.com/panglimanetizen01/one/actions/runs/40446485242), CI [40446485250](https://github.com/panglimanetizen01/one/actions/runs/40446485250), Linux distro [40446485354](https://github.com/panglimanetizen01/one/actions/runs/40446485354), and E2 [40446485332](https://github.com/panglimanetizen01/one/actions/runs/40446485332) all concluded failure again. GitHub exposes no step summaries for these jobs and the log endpoint returns BlobNotFound. Do not infer source-test failure or infrastructure-only failure without usable logs. Independent exact-SHA lab passes do not silently replace these mandatory canonical gates.
- Latest gate [run 40447344398](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40447344398) correctly remains **NOT PASSED**: required artifact/cross-platform/Android jobs were incomplete at its snapshot, E1/E2/E6 full-row acceptance remains open, seven DoD items remain unchecked, and no protected release exists for this exact SHA.

No points, weights, DoD checkboxes, or source code were changed. Score remains implementation 92/100, verified 78/100. The next gate evaluation must follow completion of the pending exact-SHA matrix; E2 still requires the authorized protected release path with the real trusted-publisher configuration.

---

## Exact-SHA continuation update — 2026-10-27 04:00 UTC

Canonical ONE source SHA remains `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9`. This is an evidence-only update; it does not change source code, ledger points, weights, or DoD acceptance.

- **PASS — E1 cross-platform acceptance:** [run 40446516694](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516694) completed successfully on Ubuntu 24.04 and Windows Server 2025. Both jobs passed the E1 integration suite, core library unit suite, full workspace tests, Clippy with warnings denied, and repository contract checker against the exact pinned source. The direct `display_value` runtime-value-shape assertions are included in this source revision's tested library suite.
- **PASS — E4 adversarial filesystem/resource-bound regression:** [run 40446516704](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516704) completed successfully on both Unix and Windows jobs.
- **PASS — Android AArch64 ELF cross-build:** [run 40446516588](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516588) build job completed successfully; the dependent API 35 ARM64 runtime job has not completed and is not runtime PASS.
- **Still running / not credited:** SEC-05 [run 40446516581](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516581), Android native ARM64 runtime [run 40446516512](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516512), Android HVF probe [run 40446516741](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516741), candidate artifact integrity [run 40446516592](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516592), Linux distro [run 40446516598](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516598), and cross-platform build/package [run 40446516600](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446516600).
- The canonical ONE hosted workflows initially failed and their log endpoint returned BlobNotFound, so their cause remains unclassified. Failed jobs have been re-queued for retry (attempt 2): E1 [run 40446485367](https://github.com/panglimanetizen01/one/actions/runs/40446485367), focused stdlib [run 40446485242](https://github.com/panglimanetizen01/one/actions/runs/40446485242), CI [run 40446485250](https://github.com/panglimanetizen01/one/actions/runs/40446485250), Linux distro [run 40446485354](https://github.com/panglimanetizen01/one/actions/runs/40446485354), and E2 [run 40446485332](https://github.com/panglimanetizen01/one/actions/runs/40446485332). Queued retries are not evidence of success.
- The fixed-weight gate [run 40446602789](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40446602789) failed on its snapshot because required exact-SHA workflows were pending, E1/E2/E6 acceptance rows remained open, seven DoD items remained unchecked, and no protected provenance release exists for this SHA. A fresh gate evaluation is required after the outstanding exact-SHA workflows complete.

Fixed-weight score remains implementation **92/100**, verified **78/100**. E1 remains 0/10 full-row verified, E2 0/8, E6 0/4. Scoped test success does not satisfy broader row acceptance by itself. The protected `one-release` path still requires repository-owner-configured signing/trust secrets and authorized execution. No acceptance checkbox or score is promoted by this update.

---

## Follow-up status update — 2026-10-27

Canonical source pin has advanced to `e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9` after adding direct unit coverage for the public `display_value` helper in [source commit](https://github.com/panglimanetizen01/one/commit/e6c0aaa5c14f0a2e00688956ebd1bc7c4716e7a9). This source change invalidates candidate-specific test evidence from the previous SHA `f5c703ae339b17f6fdba8673131cfc8a28a1b295`; all mandatory source-bound checks must be rerun against the new pin before acceptance. This update records subsequent workflow outcomes without awarding extra ledger points:

- **PASS — Windows E1 standard-library acceptance:** [run 40444641942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641942).
- **PASS — Android AArch64 cross-build and backend-contract fallback:** [run 40444642088](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642088). This is build/contract evidence only, not guest runtime evidence.
- **FAIL — Android API 35 runtime using Linux QEMU TCG:** [run 40444641872](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641872). Emulator boot failed and the actual ELF execution step was skipped; do not count as Android runtime PASS.
- **FAIL — canonical ONE hosted workflows on candidate SHA:** E1 test lab [run 40444639013](https://github.com/panglimanetizen01/one/actions/runs/40444639013), focused stdlib [run 40444639376](https://github.com/panglimanetizen01/one/actions/runs/40444639376), Linux distro [run 40444639097](https://github.com/panglimanetizen01/one/actions/runs/40444639097), One CI [run 40444639215](https://github.com/panglimanetizen01/one/actions/runs/40444639215), and E2 lab [run 40444639340](https://github.com/panglimanetizen01/one/actions/runs/40444639340). The current GitHub connector does not expose their job logs/steps, so root cause is unclassified; these failures receive no PASS credit and must not be called infrastructure-only without log evidence.
- **Still running at the latest poll — SEC-05 Linux:** [run 40444641971](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641971), specifically native cross-compiler installation; Windows side passed.
- **Still running at the latest poll — Android API 35 native ARM64 host:** [run 40444641879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641879), actual guest boot/ELF runtime has not yet completed.
- **Still running at the latest poll — Android API 35 community emulator fallback:** [run 40444642008](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642008), actual guest boot/ELF runtime has not yet completed.
- **Gate remains FAIL:** [run 40445790570](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40445790570) did not pass. A fresh gate evaluation is triggered by this evidence-index update; this documentation update does not change source SHA or satisfy E1/E2/E6.

E1 focused audit found 29 public Rust helper functions in `crates/one-core/src/stdlib.rs`. The new candidate adds direct unit assertions for `display_value` across text, integer, booleans, nothing, nested list, and ordered mapping representations. These assertions are not yet verified by CI on the new SHA. This does not by itself establish full E1 acceptance: the normative contract still requires stable signatures/errors, deterministic behavior, and supported-backend compatibility.

Current fixed-weight score remains 92/100 implementation and 78/100 verified. E1 remains 0/10, E2 remains 0/8, E6 remains 0/4; no weights or checklist items are changed by this update. Protected `one-release` signing and independently configured trusted-publisher verification are still absent from the exact-SHA evidence.

## Latest completed-run reconciliation — 2026-10-27

Candidate source SHA remains `f5c703ae339b17f6fdba8673131cfc8a28a1b295` (confirmed by `CANONICAL_COMMIT.txt`). These statuses supersede stale “in progress/queued” wording in the earlier evidence-delta paragraph below:

- **PASS — Linux distro matrix:** [run 40444641979](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641979).
- **PASS — focused standard library/database verification:** [run 40444642007](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642007).
- **PASS — E4 adversarial filesystem/resource regression:** [run 40444642016](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642016).
- **PASS — cross-platform Ubuntu/Windows E1 acceptance:** [run 40444642094](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642094).
- **PASS — artifact integrity:** [run 40444641986](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641986).
- **PASS — Cargo lockfile bootstrap:** [run 40444642107](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642107).
- **PASS — synthetic-trust provenance lab only:** [run 40444641919](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641919). This does not replace a protected release with production trust configuration.
- **Still in progress; no PASS credit yet — SEC-05:** [run 40444641971](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641971). The Windows job passed, but the Linux job is still installing its native cross-compilers and has not completed.
- **Still in progress; no runtime PASS credit yet — Android API 35 AArch64 native-host run:** [run 40444641879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641879); build job passed, runtime job is still booting the API 35 ARM64 emulator.
- **Still in progress; no runtime PASS credit yet — Android API 35 community-emulator fallback:** [run 40444642008](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642008); actual API 35 ARM64 boot/ELF execution step has not completed.

The fixed-weight gate run [40445598461](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40445598461) failed at 2026-10-27T03:42:30Z. Its snapshot preceded completion of the Linux distro, focused stdlib/database, E4 adversarial, artifact-integrity, and lockfile runs listed above, so that particular gate log has stale in-progress classifications for those runs. This reconciliation triggers a fresh gate evaluation; it does not itself award points or close acceptance rows.

Open acceptance blockers remain:
1. E1 is still 0/10 verified until the full scope-defined public reusable API and its complete row criteria are accepted; passing platform suites are necessary evidence but do not automatically satisfy full row scope.
2. E2 is still 0/8 verified because no protected `ONE Package Provenance Release` run exists for this source SHA. The release workflow requires owner-configured `one-release` environment secrets `ONE_RELEASE_SIGNING_SEED` and `ONE_TRUSTED_PUBLISHERS`, plus a publisher ID already in that trusted store.
3. E6 is still 0/4 verified until E1–E5, final-SHA freeze, evidence reconciliation, and protected provenance acceptance are complete.
4. SEC-05 Linux and Android API 35 runtime jobs above remain in progress; their result must be rechecked before gate acceptance.

Fixed weights remain unchanged. No unchecked DoD item is checked by this evidence-index update; final gate remains **NOT PASSED** pending the fresh gate result and closure of the blockers above.

## Exact-source evidence delta — 2026-10-27, candidate f5c703ae339b17f6fdba8673131cfc8a28a1b295

The independent pin `CANONICAL_COMMIT.txt` points to exact ONE source SHA `f5c703ae339b17f6fdba8673131cfc8a28a1b295`. New completed evidence for that exact source:

- **E1 Windows standard-library acceptance: SUCCESS** — [run 40444641942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641942). Windows Server 2025 completed the standard-library integration suite, core library unit suite, full workspace tests, warnings-denied Clippy, and repository contract checker.
- **E1 cross-platform acceptance: SUCCESS** — [run 40444642094](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642094). Both Ubuntu 24.04 and Windows Server 2025 jobs passed exact-SHA checks, standard-library integration and unit suites, full workspace tests, warnings-denied Clippy, and repository contract checks.
- **Candidate artifact integrity: SUCCESS** — [run 40444641986](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641986).
- **Cargo lockfile bootstrap: SUCCESS** — [run 40444642107](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642107).

The following exact-SHA evidence remains incomplete at this update: Linux distribution verification [run 40444641979](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641979) is in progress; SEC-05 [run 40444641971](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641971), Android native ARM64 runtime [run 40444641879](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641879), and synthetic-trust-only provenance lab [run 40444641919](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641919) are in progress; subprocess resource guard [run 40444642033](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642033), adversarial E4 regression [run 40444642016](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642016), and focused stdlib/database verification [run 40444642007](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444642007) are queued. Their results must not be inferred.

The fixed-weight gate remains **NOT PASSED**: E1 0/10, E2 0/8, E6 0/4; seven Definition-of-Done items remain unchecked, and no protected `ONE Package Provenance Release` run exists for this exact source SHA. Synthetic trust evidence cannot substitute for the protected release path. The candidate source SHA and ledger weights have not been changed by this evidence-index update.

## Exact-source continuation — 2026-10-27

The current canonical ONE candidate is `f5c703ae339b17f6fdba8673131cfc8a28a1b295` on `milestone/100-ecosystem-20261023`. The independent pin `CANONICAL_COMMIT.txt` points to that exact source SHA.

- **E1 Windows standard-library acceptance:** [run 40444641942](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40444641942) completed successfully against this exact SHA. The job passed the complete `stdlib_builtins` integration suite, `one-core` library unit suite, repository contract checker, and warnings-denied Clippy. This includes the newly added source-level `tambah elemen daftar` and `hapus elemen daftar` regression.
- **Remaining matrix:** cross-platform acceptance, Ubuntu/Linux distro, focused stdlib/database, artifact integrity, E4 regressions, SEC-05, Android API 35 runtime, and the fixed-weight gate are still pending/in progress for this exact SHA. They are not represented as PASS here.
- **Disposition:** E1 has a successful Windows focused run but the complete E1 row remains partial until the full scope-defined API and exact-SHA acceptance requirements are met. E2 protected release and E6 final forensic reconciliation remain open. Scores and fixed weights are unchanged; final gate remains **NOT PASSED**.


## E1 Windows resource-admission test hardening — 2026-10-27

The exact-SHA Windows E1 unit suite on candidate `467adaa5f310f60c3e10ca12f919a209e4591b03` exposed a test-harness weakness: `interop::tests::windows_job_object_immediate_descendant_spawn_stress` failed before spawning because the process-wide resource budget was transiently full ("Batas resource runtime terlampaui: terlalu banyak operasi resource aktif."). The implementation did not report a containment failure; the stress test treated valid admission back-pressure as an immediate test failure. Source commit [`c656c0d1f0b6fe7507467f49c59fe199e24c5c89`](https://github.com/panglimanetizen01/one/commit/c656c0d1f0b6fe7507467f49c59fe199e24c5c89) now retries only that specific admission-denied result for a bounded five seconds; all other process errors still fail. If capacity never becomes available, the test fails rather than suppressing the condition. This changes the candidate SHA, so all exact-SHA evidence is being rerun against `c656c0d1f0b6fe7507467f49c59fe199e24c5c89`; prior runs remain historical. E1's broader reusable-API scope, E2 protected release, and E6 reconciliation remain open.


## E4 exact-SHA acceptance reconciliation — 2026-10-27

E4 was promoted to 6/6 verified in the canonical ledger using successful exact-SHA evidence for candidate `3cd146c7f30190619bc766cea8746a5fbc5778de`: adversarial filesystem/resource tests [40437159101](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40437159101), cross-platform SEC-05 subprocess timeout/output-limit and Windows descendant-containment checks [40437158976](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40437158976), and resource guard [40437158994](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40437158994). The threat review's residual limits remain explicit. The ledger/DoD reconciliation produced new candidate HEAD `467adaa5f310f60c3e10ca12f919a209e4591b03`; the pin is being advanced to this exact commit and the complete required matrix must pass again before final gate acceptance. E1/E2/E6 and protected release remain open.


## Ledger arithmetic reconciliation — 2026-10-27

The canonical ledger's total row was corrected to match its unchanged fixed-weight rows: implementation remains 92/100 and verified row sum is 72/100 after E3 was accepted at 8/8. No row weight or criterion was changed. The resulting canonical candidate commit is `3cd146c7f30190619bc766cea8746a5fbc5778de`. The lab pin will be advanced to that exact commit and the required exact-SHA workflow matrix will run again. Previous candidate-SHA runs are not counted as proof for this new pin. E1, E2, E4, E6 and the protected-release requirement remain subject to their own evidence and acceptance.


## Candidate SHA realignment — 2026-10-27

The canonical candidate branch `milestone/100-ecosystem-20261023` now has documentation reconciliation commit `55a4d12303e4470704b777a66aed7a9e3dc89e45` containing the evidence-backed E3 ledger and DoD acceptance. The lab pin still referenced its parent source revision, which meant the gate checked stale ledger contents. The pin is being advanced to this exact candidate commit so the gate reads the reconciled ledger. Because this changes the frozen SHA, all exact-SHA evidence must be rerun against `55a4d12303e4470704b777a66aed7a9e3dc89e45`; older run links remain historical and do not count as proof for the new pin. E1/E2/E4/E6 and protected release acceptance remain open unless their new evidence proves otherwise.

# ONE v0.1 — Candidate Verification Index


## E3 acceptance reconciliation — 2026-10-27

The ledger and Definition of Done in the canonical candidate branch now record E3 as VERIFIED (8/8) for source SHA `d8ee564637f9fae3a7e95ff12be02413574c462f`, based on the cross-platform acceptance run [40360134456](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134456), cross-platform build/package run [40360134467](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134467), Linux distribution run [40360134902](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134902), artifact integrity run [40360134487](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134487), and Android API 35 AArch64 runtime [40368564134](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40368564134). The canonical pin was checked at the mirror commits for both the cross-platform and Android evidence. This records E3 only; E1, E2, E4, E6 and final DoD reconciliation remain open until their own acceptance evidence is complete.

## Latest evidence update — 2026-10-27 (exact source SHA d8ee564637f9fae3a7e95ff12be02413574c462f)

- **Android API 35 AArch64 runtime: SUCCESS** — [run 40368564134](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40368564134). The workflow checked out the pinned canonical source SHA, built the native AArch64 ELF, kept the emulator alive through execution, and completed the guest run with exit code 0 and exact output `ONE_NATIVE_BACKEND_OK`. This supersedes the earlier checkpoint text below that said no successful runtime execution was available; prior failed emulator experiments remain historical failures, not passing evidence.
- **Fixed-Weight Ledger Gate: NOT PASSED** — [run 40365813018, attempt 2](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40365813018). The live canonical Actions run-list query succeeded. The verifier still reports 92/100 implementation, 64/100 verified, 9 unchecked DoD items, E1 0/10, E2 0/8, E3 0/8, E4 0/6, E6 0/4, and no protected `ONE Package Provenance Release` run for the exact source SHA. Android runtime success does not by itself close E3's full acceptance row or the other rows.
- No ledger weights, verified points, DoD checkboxes, source code, release configuration, or protected secrets were changed by this evidence-index update. E2 remains blocked pending an authorized protected release-path execution with the real independently configured trust material; no production release was published.


## Continuation checkpoint — exact candidate d8ee564637f9fae3a7e95ff12be02413574c462f — refreshed 2026-10-26

Canonical source: [panglimanetizen01/one@d8ee564637f9fae3a7e95ff12be02413574c462f](https://github.com/panglimanetizen01/one/commit/d8ee564637f9fae3a7e95ff12be02413574c462f). PR #80 remains open/draft/unmerged. The only source change since c26e28789fb090ad8a684c6c6853ec2a88e3f9ca raises the SEC-05 Windows descendant-containment regression test timeout from 2s to 10s; parent and child still sleep for 30s and timeout/descendant-termination assertions remain active.

### Completed exact-SHA evidence (source d8ee564637f9fae3a7e95ff12be02413574c462f)
- E1 standard-library Windows acceptance [run 40360134377](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134377): SUCCESS.
- E1 cross-platform acceptance [run 40360134456](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134456): Ubuntu 24.04 and Windows Server 2025 jobs SUCCESS.
- Cross-platform build/package verification [run 40360134467](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134467): Ubuntu and Windows jobs SUCCESS, including build, release build, package metadata/SHA256, artifact integrity, AST regression, Clippy, tests, network runtime, and offline verification.
- E4 adversarial filesystem/resource-bound regression [run 40360134649](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134649): Unix no-follow/SQLite bounds and Windows reparse-point/handle checks SUCCESS.
- E4 subprocess resource guard [run 40360134455](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134455): SUCCESS.
- SEC-05 subprocess timeout/output-limit checks [run 40360134485](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134485): Windows and Linux jobs SUCCESS.
- Focused standard-library/database regression [run 40360134353](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134353): SUCCESS.
- Linux distribution verification [run 40360134902](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134902): SUCCESS.
- Candidate artifact integrity [run 40360134487](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134487): SUCCESS.
- Cargo lockfile bootstrap [run 40360134554](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134554): SUCCESS.
- Package/provenance end-to-end lab [run 40360134313](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134313): SUCCESS with **synthetic trust only**; this does not prove production protected-environment authorization, production signing secret readiness, or a real release.

These passing runs prove their named test scopes only. They do not, by themselves, satisfy every acceptance item in ledger rows E1/E2/E4 or the overall DoD.

### Android API 35 arm64-v8a runtime
- Native ARM64 Linux-host attempt [run 40360134381](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134381): remains in progress with boot step only; no ELF execution proof. A changed experiment [run 40362704802](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40362704802) uses explicit QEMU machine type `virt,gic-version=3` and a 20-minute boot polling bound; its install and backend contract steps passed, but boot remains in progress and no ELF execution proof exists yet.
- macOS TCG workaround [run 40360134486](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134486): still in progress at last check; no ELF execution proof.
- Community ARM64 emulator fallback [run 40360134549](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134549): build job passed, guest boot/ELF execution job still in progress at last check; no runtime PASS.
- Linux TCG [run 40360134479](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134479), alternate Linux TCG [run 40360134577](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134577), macOS capability probe [run 40360134544](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134544), and software-emulation fallback [run 40360136564](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360136564) failed before proving guest ELF execution.
- E3 remains unaccepted: there is still no evidence of actual API 35 `arm64-v8a` ELF execution exiting 0 and printing `ONE_NATIVE_BACKEND_OK`.

### Gate and remaining hard blockers
- Latest gate [run 40360473719](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360473719) checked source SHA `d8ee564637f9fae3a7e95ff12be02413574c462f` and returned **NOT PASSED**: implementation 92/100, verified 64/100, and 9 unchecked Definition of Done items. E1 verified 0/10, E2 0/8, E3 0/8, E4 0/6, and E6 0/4 remained unaccepted in the ledger gate.
- The token mapping was corrected in lab commit [1b1be97](https://github.com/panglimanetizen01/one-windows-verification/commit/1b1be97f6e1a72df60666706a1a9264c5e54f6b8): canonical source checkout uses `CANONICAL_READ_TOKEN`, while the verifier's live Actions API query uses `ONE_REPO_TOKEN`. Gate [run 40362806853](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40362806853) confirms the canonical Actions run-list query now succeeds. This resolves the earlier Actions: read proof blocker. The gate still cannot find a protected canonical release workflow run for the exact source SHA, and E2 remains blocked until the authorized protected release path is exercised with production trust configured. Do not expose any secret value in chat.
- Do not change fixed weights, acceptance rules, or DoD checkboxes to manufacture a pass. Do not merge PR #80 or publish a release. No PASS GREEN LOCKED claim is justified until the runtime evidence, authorized Actions evidence, production release prerequisites, full ledger acceptance, and final gate all pass on the exact frozen source SHA.

> **Fresh candidate reconciliation — 2026-10-26:** PR #80 is now at `2a7670c5166efee54426196f28a8152cbfe758b3` after formatting-only corrections in `crates/one-core/src/interop.rs` exposed by exact-SHA SEC-05 checks. All earlier matrix results remain tied to their recorded SHAs and are not current-SHA acceptance.


**Canonical repository:** [panglimanetizen01/one](https://github.com/panglimanetizen01/one)  
**PR:** [#80](https://github.com/panglimanetizen01/one/pull/80) — open, draft, unmerged  
**Previous source SHA:** `2a7670c5166efee54426196f28a8152cbfe758b3` (superseded by the frozen candidate checkpoint below; verifier branch HEAD is a separate lab-documentation/workflow SHA)  


> **Latest exact-source delta — 2026-10-26:** Candidate SHA `b35c7323df72a24e9e6a0376e63b350a6ae8907d` passed the lab E1 contract/integration/lint suite (239 tests; contract checker PASS), Linux Debian 12/Ubuntu 24.04, focused standard-library/database, lockfile, and E4 filesystem/resource guard. The E2 provenance lab passed using disposable synthetic trust only; it does not prove protected production trust or release acceptance. The SEC-05 Windows suite passed the full `one-core` tests and static guards but failed `rustfmt --edition 2024 --check crates/one-core/src/interop.rs` on formatting-only differences in the pipe-read failure change. Those formatting-only changes are applied in candidate SHA `5b0d94f4f5287648c60a438580d7d559101ee46d`; exact-SHA revalidation is required. The API 35 community emulator attempt is still pending and Linux TCG alternatives failed before guest execution. Gate run [40316970507](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40316970507) failed at source checkout with HTTP 403, `Write access to repository not granted`; therefore the configured secret's usable repository access and Actions: read remain unproven. No ledger score is changed.



> **Current exact-source delta — 2026-10-26:** Candidate SHA `b35c7323df72a24e9e6a0376e63b350a6ae8907d` passed lab E1 contract/integration/lint (239 tests; contract checker PASS), Linux distro, focused stdlib/database, lockfile, and E4 filesystem/resource guard. E2 provenance tests passed with disposable synthetic trust only. SEC-05 exposed formatting-only differences in `interop.rs`; those were corrected in `5b0d94f4f5287648c60a438580d7d559101ee46d` and a final brace placement was corrected in `2a7670c5166efee54426196f28a8152cbfe758b3`. The current candidate needs a fresh exact-SHA matrix. Gate run [40316970507](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40316970507) failed checkout when `ONE_REPO_TOKEN` was used for source checkout. The workflow now separates credentials: `CANONICAL_READ_TOKEN` for source Contents read and `ONE_REPO_TOKEN` for live Actions API reads; the latest gate run must confirm that configuration. No scores are changed.

**Fixed-weight ledger:** [one-completion-ledger.md](https://github.com/panglimanetizen01/one/blob/milestone/100-ecosystem-20261023/docs/verification/one-completion-ledger.md)  
**Release gate:** **NOT PASSED** — latest gate run directly inspected in this audit is [40294023191](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40294023191), which checked source SHA `990c4e80f657aa2ac0409cfaf3bbf522856bc889`, failed closed, and used the old `CANONICAL_READ_TOKEN` secret reference. After that run, `.github/workflows/ledger-gate.yml` was updated at lab commit `a83c514b7d9fc970e5b61044735650e555b802a9` to use `secrets.ONE_REPO_TOKEN` for checkout and map it to the verifier's `CANONICAL_READ_TOKEN` environment variable. The current workflow file is confirmed to contain that mapping, but a post-change run log has not yet been retrieved in this audit, so Actions: read access remains UNPROVEN. Exact-pin Linux distro (Ubuntu 24.04 + Debian 12), Ubuntu/Windows Server 2025, E4 adversarial tests, candidate artifact integrity, and Android AArch64 build/contract jobs passed their scoped checks. **Android API 35 `arm64-v8a` runtime is now proven on source SHA `990c4e80f657aa2ac0409cfaf3bbf522856bc889`** by [run 40275895417](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895417): the macOS ARM64 software-emulation workflow verified the guest, ran the ignored native ELF integration test, and logged `1 passed; 0 failed; 0 ignored`, with the runtime test completed successfully. The API 35 community-emulator route [40275895444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895444) still failed to boot; that failure is retained as historical evidence and is not conflated with the passing alternative. The successful runtime run is nevertheless tied to source SHA `990c4e80f657aa2ac0409cfaf3bbf522856bc889`; after the candidate advanced to `b35c7323df72a24e9e6a0376e63b350a6ae8907d`, it is historical for the final-SHA gate and must be revalidated or formally accepted under the project's exact-SHA rules. E3 runtime criterion is checked only for this exact pin and the successful route. Overall E3/E4 acceptance remains **NOT PASSED**: full threat review/residual-risk disposition remains open, and protected canonical release evidence is inaccessible with the current `CANONICAL_READ_TOKEN` Actions permissions. Do not label the milestone GREEN LOCKED.


## Latest exact-pin Android runtime acceptance — 2026-10-26

- **Source pin:** `990c4e80f657aa2ac0409cfaf3bbf522856bc889`, verified in both Android job logs by fetching and checking out the exact commit and asserting `git rev-parse HEAD` equals the pin.
- **Passing runtime:** [run 40275895417](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895417), job `121418456101`, successful. The boot step checks guest API level `35` and ABI `arm64-v8a`; the subsequent command ran `cargo --locked test -p one-core --test native_backend_android_aarch64 build_native_menghasilkan_dan_menjalankan_elf_android_aarch64 -- --ignored --exact --nocapture`, and the log reports `test ... ... ok` and `test result: ok. 1 passed; 0 failed; 0 ignored`.
- **Artifact/log evidence:** job logs are available from the run. Uploaded diagnostic artifact ID `12630852998`, archive SHA-256 `6366d8d98f2c597dcb7e223f5f8b8ae8b1f34808be28ae7c702b0db50d38fcbb`; artifact URL [open artifact](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895417/artifacts/12630852998). This artifact contains emulator/AVD diagnostics, not the full guest output as a separate text file; the successful integration-test assertion is evidenced in the job log.
- **Scope boundary:** this is a valid runtime pass on the exact canonical source pin using macOS ARM64 software emulation. It does not make the separate Linux/TCG or community emulator failures pass, and it does not close E4's open threat-review/residual-risk disposition or the independent protected-release evidence gate.

This file is the live exact-SHA evidence index. A workflow run counts only if its job logs assert the current source SHA and all required steps pass. Prior-SHA results are historical evidence, not current-candidate acceptance.


### SEC-05 subprocess guard — exact pinned source

Run [40264131009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264131009) completed successfully on Linux and Windows Server 2025, and both job logs explicitly check out source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`. Existing subprocess contract tests, the full `cargo test --locked -p one-core` suite, changed-file formatting, and the lab's static timeout/output-limit guard passed on both jobs. The Windows guard's checks also passed for the race-free process-creation markers (`CreateProcessW`, `InitializeProcThreadAttributeList`, `UpdateProcThreadAttribute`, `DeleteProcThreadAttributeList`, and `PROC_THREAD_ATTRIBUTE_JOB_LIST`) and reject `AssignProcessToJobObject` spawn-then-assign use. These are scoped CI results; they do not alone prove every descendant-process race, inherited-pipe, timeout, flood, and cleanup acceptance scenario. Keep SEC-05 and E4 unaccepted until the required dynamic adversarial assertions and ledger rows are evidenced.

### Latest ledger gate readback — 2026-10-26

Run [40265232307](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40265232307) checked out exact source SHA `78b9436c318032b1c19a4e5c110142fffc58b4d5`. Verifier unit tests passed, but the fail-closed gate returned **NOT PASSED**: 9 unchecked Definition of Done items; E3 verified 0/8 and E4 verified 0/6 in the ledger; Android API 35 runtime run [40264206706](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40264206706) remains queued; canonical release-workflow evidence cannot be read because `CANONICAL_READ_TOKEN` lacks required Actions read permission and anonymous fallback returns 404. Do not convert scoped CI passes into full row credit or weaken the gate to make it green.

## Android API 35 runtime retry — 2026-10-26

The ARM64-hosted runtime attempt [40273075912](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273075912) successfully built and provenance-checked an AArch64 ELF, installed the digest-verified official API 35 `arm64-v8a` system image, and installed a checksum-verified ARM64 emulator. Runtime failed before guest boot because the selected SDK `adb` executable was the wrong host architecture (`Exec format error`, exit 126). This is a host-tool selection defect, not an Android binary failure and not runtime acceptance.

The first native-ADB correction [40273563278](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273563278) failed earlier than boot because `file` inspected `/usr/bin/adb` as a symlink rather than resolving its target; the architecture assertion therefore failed closed before emulator execution. The workflow now uses `file -L /usr/bin/adb` to inspect the resolved binary and explicitly invokes `/usr/bin/adb`. Definition validation passed at [40273802431](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273802431); the new exact-pin retry [40273802443](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273802443) is running. Runtime remains **NOT ACCEPTED** until API level 35 and ABI `arm64-v8a` are read from a booted guest and the actual ONE ELF produces the expected assertion/output with exit code 0. KVM is unavailable on this runner, so software-emulation boot remains a risk.

## Current canonical source pin — `73bd504ac81a14737b321817b94c7bc2fbb17a15`

The verifier's current `CANONICAL_COMMIT.txt` pins the ONE source commit above. The following runs explicitly checked out that source SHA in their logs; they are scoped passes, not blanket acceptance.

| Gate | Run | Result on exact source pin |
|---|---|---|
| Linux distro matrix: Debian 12 + Ubuntu 24.04 | [40272900538](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900538) | Both jobs **SUCCESS**; logs explicitly checkout `73bd504ac81a14737b321817b94c7bc2fbb17a15` |
| E4 adversarial filesystem / SQLite bounds | [40272900540](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900540) | Unix no-follow/SQLite and Windows reparse/handle jobs **SUCCESS**; scope limited to assertions executed |
| E4 subprocess timeout/output bounds | [40272900575](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900575) | Linux and Windows jobs **SUCCESS**; subprocess baseline and SEC-05 guard only, not full descendant/race proof |
| E4 subprocess resource guard | [40272900536](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900536) | **SUCCESS** for the resource guard audit only |
| Focused standard-library/database regression | [40272900585](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900585) | **SUCCESS** |
| Android API 35 cross-build/contract (no runtime claim) | [40272900641](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900641) | **SUCCESS** for cross-build/contract only |
| Android API 35 AArch64 runtime | [40273563278](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273563278) | **IN PROGRESS** at index update; runtime not accepted |
| Fixed-weight ledger gate | [40273632102](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40273632102) | **IN PROGRESS** at index update; no acceptance credit until the gate completes |

The Windows E1 and Cargo lockfile jobs also succeeded on this pin ([E1](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900587), [lockfile](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900633)). The runtime retry is fixing a host-architecture mismatch in the `adb` tool; previous runtime attempts did not boot Android or execute the ONE binary. Keep E3/E4 overall acceptance **NOT PASSED** until the remaining criteria, including actual API 35 guest execution, pass.

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

## E3/E4 exact-source checkpoint — 2026-10-26

Canonical ONE candidate SHA: `99600e112e389ffa6712022f77c1203244566ae1`. This is the current candidate branch HEAD; the verifier pin `CANONICAL_COMMIT.txt` matches it. No merge or release is authorized.

### E4 changes under verification
The candidate adds the shared process-wide resource admission permit to filesystem read/write, DNS resolution, and HTTP GET adapters, in addition to the existing subprocess and SQLite paths. File writes now check the input length before making a second content allocation. The 8-operation shared cap and 4-query nested SQLite cap remain fail-closed; this does not claim a complete heap quota for caller-retained outputs.

- [E4 adversarial filesystem/resource run 40266497090](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266497090): completed success on the canonical pin. Unix no-follow/SQLite/resource job and Windows reparse-point/handle job both passed.
- [E4 SEC-05 subprocess run 40266497129](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266497129): Linux job passed; Windows job was still running at checkpoint time. Not counted as a full cross-platform PASS until the run concludes.
- [Linux distro matrix 40266497077](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266497077): Ubuntu 24.04 and Debian 12 completed successfully on the canonical pin.
- [Cross-platform matrix 40266497066](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266497066): Linux and Windows jobs were still running at checkpoint time.
- [Candidate artifact integrity 40266497119](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266497119): still running; no PASS recorded yet.
- [Android AArch64 cross-build/contract run 40266630223](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266630223): exact-source cross-build and contract tests were running; build success is not Android runtime acceptance.
- [Android API 35 arm64-v8a community-emulator fallback 40266668439](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266668439): exact-source runtime attempt in progress. It uses the official API 35 arm64-v8a system image and a third-party Linux ARM64 emulator binary pinned by SHA-256; its provenance and runtime assertions must be checked in logs before any acceptance.
- [Linux TCG fallback 40266630239](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40266630239): exact-source alternative attempt in progress. The earlier TCG run 40266497191 is not valid exact-source evidence because the workflow at that time checked out a hard-coded older SHA; that workflow is now corrected to resolve the canonical pin.

Android API 35 runtime acceptance remains pending until a completed run proves system API 35, ABI `arm64-v8a`, execution of the actual source-built ELF, exit code 0, and exact output `ONE_NATIVE_BACKEND_OK`. Cross-builds, ELF headers, successful emulator setup, and boot-only checks do not substitute for this.

This checkpoint is evidence-only: no DoD checkbox, ledger score, verified weight, or release gate is promoted. E3/E4 milestone remains unaccepted until every mandatory criterion has direct evidence.



## E3/E4 exact-SHA continuation — 2026-10-26

- Canonical ONE candidate branch: `milestone/100-ecosystem-20261023`.
- Exact source SHA: `52060994d19ecede9b2a7dd770b6e1842e30e8bb`.
- Candidate implementation commit: https://github.com/panglimanetizen01/one/commit/52060994d19ecede9b2a7dd770b6e1842e30e8bb.
- Lab pin commit: https://github.com/panglimanetizen01/one-windows-verification/commit/5b81b71a2e810b5fe5a9f53e80934ea18c204d83; `CANONICAL_COMMIT.txt` resolves to the exact source SHA above.
- E4 lint correction: the network connection stores its global resource permit in underscore-prefixed named fields so the RAII lifetime remains intact without `dead_code` warnings.
- E4 test correction: `network_connections_hold_global_resource_permits_until_closed` now accounts for other parallel tests sharing the process-wide quota. It retries transient quota denial, fills capacity until denial, closes a connection, and verifies admission recovers; no assertions were removed or weakened.
- Exact-SHA matrix triggered by the pin commit; run links below are the current attempts and must be checked for final conclusions before any checkbox is promoted:
  - Linux distro: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030674 — **SUCCESS**; Ubuntu 24.04 and Debian 12 completed successfully on the pinned source SHA.
  - Cross-platform Linux/Windows: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030600 — **SUCCESS**; Ubuntu and Windows Server 2025 jobs completed successfully on the pinned source SHA.
  - SEC-05 subprocess: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030654 — **SUCCESS**; Linux and Windows subprocess contract/guard jobs completed successfully. The whole-repository rustfmt diagnostic is non-blocking and still reports unrelated formatting differences.
  - E4 adversarial filesystem/resource: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030628 — **SUCCESS**; Unix no-follow/mount-boundary/SQLite job and Windows reparse-point/handle job completed successfully.
  - Focused standard-library/database regression: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030687 — **SUCCESS**; 245 passed, 0 failed, including the repaired parallel-safe global network quota regression.
  - Candidate artifact integrity: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030622 — **SUCCESS**; exact-SHA Linux/Windows bundle digest, embedded manifest, build metadata, and executable-format checks passed. Linux artifact ID `12627935826`, SHA-256 `de43b495eb701b3175395ee9b64286977f6fdee8a345d4c19f9da16bf4767bf7`; Windows artifact ID `12628325537`, SHA-256 `02a2ac08e34130b8f6ad8adccc8c113087da24aa97037e6d42c48fb01a1395ba`. Inspected binaries: Linux SHA-256 `a6a61de3a8da675192596ad8a8607899792075803963724f69985658cc654d69` (ELF64 little-endian EM_X86_64); Windows SHA-256 `c3c439a6d6599f0878339619705983848ea32e7ed0695383d3598c453b6f223f` (PE32+ x86-64).
  - Android API 35 arm64-v8a community-emulator runtime, first attempt: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40270030624 — **FAILURE** before boot; SDK manager could not resolve its missing host-emulator dependency on ARM64. This is not runtime acceptance.
  - Android cross-build/contract jobs are separate from runtime acceptance and cannot substitute for executing the ELF on API 35.
- Known prior failure preserved: candidate SHA `ac4bd9ae5106d50ccd43cae9829dd406aa6a45d1` failed the focused suite because parallel tests could temporarily occupy the global operation quota. This prompted the test-isolation correction above; that failed run remains historical evidence and is not relabeled.
- Additional artifact audit: failed runtime run [40271450342](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271450342) produced ELF artifact ID `12628152067` (ZIP SHA-256 `394e5cd9dd14896103380f4728f9b43ecdc1fb7db8b3ad7987d8b091b97cb2f8`), binary SHA-256 `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`, source SHA `52060994d19ecede9b2a7dd770b6e1842e30e8bb`, ELF64 little-endian AArch64, interpreter `/system/bin/linker64`. Inspection showed this artifact was built with `aarch64-linux-android24-clang` and reports Android 24, so it is historical build-only evidence and does **not** meet the stricter API 35 build-target requirement. The workflow was corrected to use `aarch64-linux-android35-clang` and assert `file` reports Android 35; the exact-SHA rebuild is pending in run [40271842141](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271842141).
- The previous API 35 Linux TCG attempts failed because the stock Android emulator reports that an `arm64` system image is unsupported on an `x86_64` host. The native ARM64-host attempt failed during SDK setup because the official emulator package was unavailable for that host. Neither is Android runtime acceptance.
- The community fallback workflow was corrected to fetch the official `repository2-1.xml` metadata, select the exact API 35 `default;arm64-v8a` package, verify its published SHA-1/SHA-256 digest, and install the image without relying on the unavailable SDK-manager emulator package. Workflow schema validation passed in https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271041831. The retry https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271450342 successfully installed the checksum-verified API 35 image and verified the ELF build, but AVD creation failed because `avdmanager` requires the unavailable SDK-registered emulator package; no boot or ELF execution occurred. The workflow now creates the AVD config explicitly (without falsifying SDK package metadata). Run https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271842141 failed because `file` did not emit an Android 35 label, so that heuristic was removed. Run https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40271988474 failed at the compiler-macro assertion. Runs https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272108662 and https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272163703 exposed a malformed duplicated workflow tail; the workflow was truncated to the single valid definition and an actionlint guard was added. The current exact-pin runtime retry is https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272235277 and schema validation is https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272235329. The build now checks the `aarch64-linux-android35-clang` wrapper, the compiler target log, ELF64/AArch64/interpreter metadata, and the API 35/ABI/boot/output assertions. No successful boot or ELF execution has been recorded yet.
- E3/E4 acceptance remains **NOT ACCEPTED** until all required exact-SHA jobs finish successfully, the actual API 35 `arm64-v8a` ELF executes with asserted output and exit code, and the ledger/Definition of Done agree. Do not promote any score or checkbox based on pending jobs.


## E3/E4 final candidate API 35 target correction — 2026-10-26

- Candidate branch: `milestone/100-ecosystem-20261023`.
- Exact source SHA pinned in `CANONICAL_COMMIT.txt`: `6302b6f1407648b273f1b73891800183c1c8c894`.
- Source commits in this correction: [native backend target fix](https://github.com/panglimanetizen01/one/commit/a867026d3fdcfa350cfab2be6d9596af6522542e) and [target definition + regression test](https://github.com/panglimanetizen01/one/commit/6302b6f1407648b273f1b73891800183c1c8c894).
- Root cause: the native Android backend hard-coded `aarch64-linux-android24` in both the toolchain contract and compiler argument, while acceptance requires API 35. The backend now declares `aarch64-linux-android35` and derives the compiler `--target` argument from the toolchain contract; a unit test locks the Android target definition to API 35.
- The prior API24 ELF artifact remains historical build-only evidence and is not accepted as the final API35-target binary.
- New exact-SHA matrix triggered by pin commit [a61164a6930030e0c845dd14df64d76623eadbbe](https://github.com/panglimanetizen01/one-windows-verification/commit/a61164a6930030e0c845dd14df64d76623eadbbe). Current run links:
  - Linux distro matrix: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455186 — queued.
  - Cross-platform Linux/Windows: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455142 — queued.
  - Candidate artifact integrity: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455281 — queued.
  - Focused standard-library/database suite: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455146 — queued.
  - SEC-05 subprocess contract: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455238 — queued.
  - E4 adversarial filesystem/resource regression: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455125 — in progress.
  - E4 subprocess resource guard: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455134 — in progress.
  - Android API 35 `arm64-v8a` community-emulator runtime: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455162 — running the earlier API macro assertion; new retry https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272505172 removes that unreliable macro check while retaining the explicit API35 target-triple assertion. Workflow validation for that retry is https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272505145.
  - Android cross-build/contract: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455150 — in progress.
  - Android device artifact build: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272455193 — in progress.
- Do not promote E3/E4 ledger rows or the milestone status until these exact-SHA jobs finish, the API 35 guest boots, the actual ELF executes, and its output/exit code are asserted. The overall project release gate remains separate from this milestone and must not be marked green while out-of-scope ledger rows remain open.


## E3/E4 candidate API35 contract regression fix — 2026-10-26

- Exact candidate source SHA pinned in `CANONICAL_COMMIT.txt`: `0301dc88aeb1d97e0a8a80ec5479364b1fab6276`.
- The exact-SHA Android contract test exposed one remaining stale API 24 expectation in `crates/one-core/tests/native_backend_android_aarch64.rs`; it was updated to API 35. The backend and target-definition regression tests now share the API 35 contract.
- Lab pin commit: https://github.com/panglimanetizen01/one-windows-verification/commit/88d85e14028b78b609561cfde63a82a78912c424.
- New exact-SHA matrix on source SHA `0301dc88aeb1d97e0a8a80ec5479364b1fab6276`:
  - Linux distribution matrix: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632218 — pending.
  - Cross-platform Linux/Windows: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632284 — pending.
  - Candidate artifact integrity: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632201 — queued.
  - Focused standard-library/database suite: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632333 — queued.
  - SEC-05 subprocess: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632309 — queued.
  - E4 adversarial filesystem/resource regression: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632226 — queued.
  - E4 subprocess resource guard: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632199 — queued.
  - Android API 35 `arm64-v8a` community-emulator runtime: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632297 — queued.
  - Android cross-build/contract fallback: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632305 — queued.
  - Android device artifact build: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632296 — queued.
- Previous source SHA `6302b6f1407648b273f1b73891800183c1c8c894` failed the Android backend contract test because the integration test still expected API 24; that failure is preserved and prompted the correction. Do not promote the milestone until the current exact-SHA matrix and actual API 35 runtime both pass.


## E4 threat-review disposition — 2026-10-26

**Review scope:** candidate source `52060994d19ecede9b2a7dd770b6e1842e30e8bb` for the E4 implementation review; the same E4 code is present in candidate `0301dc88aeb1d97e0a8a80ec5479364b1fab6276`. Exact-SHA E4 reruns for `0301dc8` are pending in the matrix above.

- **Capability denial:** adapter entry points check explicit capabilities before protected operations. Regression coverage includes denied network/process operations and verifies no unauthorized side effect/adapter call.
- **Unix filesystem:** rejects NUL and parent traversal; absolute paths must remain under the resolved working-directory root. Directory components are opened descriptor-relative with `openat` and `O_NOFOLLOW`; regular-file opens use `O_NOFOLLOW` and `O_NONBLOCK`; Linux compares `statx` mount IDs in addition to device IDs. Exact-SHA regression coverage includes final symlink denial, parent-component swap, mount-boundary denial, and file-type/error behavior.
- **Windows filesystem:** canonical/lexical containment is checked; opens use `FILE_FLAG_OPEN_REPARSE_POINT`; the opened handle is checked for a regular non-reparse file and its final path must match the expected path. The Windows adversarial job exercises reparse-point/junction escape and handle-boundary cases.
- **SQLite and quotas:** query-only/read-only behavior, SQL/parameter/row/column/output bounds, interruption/failure handling, a shared cap of four active SQLite queries, and a shared cap of eight active resource operations are implemented. The quota regression test fills capacity, verifies denial, closes a connection, and verifies admission recovers.
- **Subprocess lifecycle:** Windows process creation includes the Job Object in the creation attributes before the child starts; the job is configured to terminate descendants on close. Timeout, per-stream and aggregate stdout/stderr bounds, pipe cleanup, process-launch failure, and descendant containment are exercised by SEC-05 and resource-guard jobs.
- **Failure recovery:** permit release is tied to RAII/drop and connection close; failed or denied operations are checked for cleanup and unauthorized side effects. The full focused suite on source SHA `520609` passed 245 tests with zero failures; exact-SHA rerun on `0301dc8` is pending.

**Residual limits, not concealed:** this implementation is not a general OS sandbox and executes with the caller's OS privileges. The 16 MiB interpreter-output cap is per execution/event dispatch, not an accounting system for arbitrary caller-retained strings or every intermediate heap allocation. Non-Linux Unix mount identity uses `st_dev` best-effort and cannot distinguish same-device bind mounts; unsupported non-Unix/non-Windows filesystem paths fail closed. The filesystem root is resolved from the process working directory per operation rather than held as a permanent process-wide root handle. These boundaries remain documented; no claim of zero residual risk or complete sandboxing is made.

**Disposition:** no critical E4 defect was observed in the reviewed implementation or passing E4 tests on source SHA `520609`; E4 acceptance for the final candidate remains pending until the exact-SHA `0301dc8` E4 reruns pass and the ledger/DoD are reconciled. This review does not authorize global release or merge.


## E3/E4 final source candidate after API35 registry-test correction — 2026-10-26

- Candidate branch: `milestone/100-ecosystem-20261023`.
- Current exact source SHA: `73bd504ac81a14737b321817b94c7bc2fbb17a15`; lab pin commit: https://github.com/panglimanetizen01/one-windows-verification/commit/4e5ab0d6e387c216bf2c14eda03adf251ee6a7db.
- Root cause from the first API35 candidate run: `target_backend_foundation.rs` still asserted API 24. That test was updated to API 35; prior failure remains preserved in run https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272632218. No assertions were removed or weakened.
- Current exact-SHA runs:
  - Linux distribution matrix: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900538 — queued.
  - Cross-platform Linux/Windows: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900560 — pending.
  - Candidate artifact integrity: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900570 — queued.
  - Focused standard-library/database suite: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900585 — in progress.
  - SEC-05 subprocess contract: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900575 — queued.
  - E4 adversarial filesystem/resource regression: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900540 — queued.
  - E4 subprocess resource guard: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900536 — queued.
  - Android API 35 `arm64-v8a` community-emulator runtime: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900565 — in progress.
  - Android AArch64 cross-build/contract: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900641 — queued.
  - Android device artifact build: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40272900506 — in progress.
- The API35 ELF build artifact from source SHA `0301dc8` (historical candidate, before the last test-only assertion fix) proved the compiler target `aarch64-unknown-linux-android35`, ELF64 little-endian AArch64, interpreter `/system/bin/linker64`, binary SHA-256 `28c1552a8fdd96e79c096611a36118347aef7849d38f0b84b09cfd75b62bf5f7`, and artifact ZIP SHA-256 `5205712efb18f265470f9fc2b75e802968a00ebc627a7c226d9cb5359bea5f89`. This is build/metadata evidence only; runtime acceptance is still pending.
- Do not mark E3/E4 rows complete until the above runs finish on source SHA `73bd504`, the API35 guest reaches boot completion, and the actual ELF produces the expected output with exit code zero. The global project release gate remains separate and must stay blocked while out-of-scope rows remain open.


## Final E3/E4 documentation checkpoint pin — 2026-10-26

The current canonical source SHA is now `990c4e80f657aa2ac0409cfaf3bbf522856bc889`. It is the PR #80 head after the official completion ledger, Definition of Done, and session checkpoint were updated. `CANONICAL_COMMIT.txt` is pinned to this exact SHA. The earlier run matrix on `73bd504ac81a14737b321817b94c7bc2fbb17a15` is historical evidence for the code-bearing predecessor and is not promoted to final-SHA evidence.

### Fresh exact-pin matrix status

- Linux distro matrix [40275895385](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895385): Debian 12 passed; Ubuntu 24.04 was still running at the time of this checkpoint.
- Cross-platform Ubuntu/Windows Server 2025 [40275895382](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895382): both jobs were running.
- SEC-05 timeout/output/descendant-process checks [40275895425](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895425): Linux job passed after the harness added `binutils-x86-64-linux-gnu`; Windows job was still running.
- E4 adversarial filesystem/resource suite [40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449): both Unix and Windows jobs passed on the final pin.
- E4 subprocess resource guard [40275895416](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895416): passed on the final pin.
- Focused SQLite/stdlib/resource suite [40275895487](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895487): passed on the final pin.
- Candidate artifact integrity [40275895457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895457): still running.
- Android API 35 cross-build/contract [40275895431](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895431): still running; build success alone is not runtime acceptance.
- Android API 35 `arm64-v8a` community-emulator runtime [40275895444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895444): ELF build job passed and the runtime job had reached the boot/execute step; no final guest boot/output/exit-code result was available at checkpoint time. Additional Android runtime alternatives [40275895468](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895468), [40275895447](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895447), [40275895378](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895378), and [40275895417](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895417) were queued or running; these remain separate attempts, not runtime passes.
- Fixed-weight ledger gate [40275895403](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895403) was still running. It cannot authorize the global release while out-of-scope E1/E2/E6 rows remain open.

### Android artifact facts on final pin

The exact-source Android build artifact is [artifact ID 12630660350](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895444/artifacts/12630660350), ZIP SHA-256 `24de248930be0b6fa20a4ec1bc77b8aeb7db2b8ad81a61b26f8b0142bdb4c961`. Its `SOURCE.txt` matches `990c4e80f657aa2ac0409cfaf3bbf522856bc889`; compiler target is `aarch64-unknown-linux-android35`; ELF is 64-bit little-endian AArch64, interpreter `/system/bin/linker64`; binary SHA-256 `28c1552a8fdd96e79c096611a36118347aef7849d38f0b84b09cfd75b62bf5f7`. This is verified build/header/dependency evidence only. Android runtime acceptance remains unchecked until the actual ELF runs on a booted API 35 guest with ABI `arm64-v8a`, emits exactly `ONE_NATIVE_BACKEND_OK`, exits 0, and retains the runtime result and logs.

**Status at this checkpoint:** E3 0/8 verified; E4 0/6 verified; global gate NOT PASSED. Do not check any row solely from a successful workflow/job or build artifact. Update this evidence index after the fresh matrix completes, preserving these intermediate results and failures.


## Historical granular acceptance checklist — source SHA 990c4e80 (superseded by candidate SHA b35c7323df72a24e9e6a0376e63b350a6ae8907d)

Every checked item below is tied to source SHA `990c4e80f657aa2ac0409cfaf3bbf522856bc889`. Historical SHA `73bd504ac81a14737b321817b94c7bc2fbb17a15` evidence remains separately identified above and is not used as final-SHA proof.

### E3 — Platform conformance

- [x] Linux distribution jobs: Ubuntu 24.04 and Debian 12 passed in [run 40275895385](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895385).
- [x] Windows Server 2025 and Ubuntu cross-platform jobs passed in [run 40275895382](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895382).
- [x] Android AArch64 build contract, compiler target, ELF64/AArch64 header, little-endian format, and `/system/bin/linker64` interpreter verified by the build job in [run 40275895444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895444). This is build/header evidence only.
- [x] Candidate Linux/Windows bundle integrity, source metadata, embedded checksums, and executable formats passed in [run 40275895457](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895457).
- [ ] Android API 35 `arm64-v8a` guest has not yet produced a completed runtime result. [Run 40275895444](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895444) is still running the boot/execute step; it must assert guest SDK 35, ABI `arm64-v8a`, actual ELF execution, exact output `ONE_NATIVE_BACKEND_OK`, and exit code 0.
- [ ] All platform acceptance tests are not yet complete because Android runtime is still open.
- [ ] All required logs/reports/artifacts for the final matrix are not yet complete because the Android runtime result is outstanding.
- [ ] Cross-platform verification is not yet complete as a whole until Android runtime acceptance passes, despite Linux/Windows jobs passing.
- [x] At this historical checkpoint, completed jobs explicitly checked out and asserted `990c4e80f657aa2ac0409cfaf3bbf522856bc889`. This was superseded by candidate SHA `b35c7323df72a24e9e6a0376e63b350a6ae8907d`; these runs are not current-SHA acceptance.

### E4 — Security and resource bounds

- [x] Capability denial prevents adapter invocation: `orchestrator::tests::denied_request_never_reaches_adapter_invocation` passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449).
- [x] Unix descriptor-relative/no-follow filesystem confinement passed: final-symlink rejection, symlinked-parent rejection without precheck, and write denial without modifying target passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449).
- [x] Parent-component traversal, concurrent parent/symlink swap race, and Linux `/proc` mount-boundary denial without truncating the target passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449).
- [x] Windows directory-junction/reparse-point escape rejection and project-root confinement/no-side-effect tests passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449).
- [x] Windows opened-handle/reparse checks ran in the same successful Windows job; the tested junction escape was explicitly exercised.
- [x] SQLite row/value/output/query/parameter limits and typed timeout/interruption behavior passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449); the focused SQLite/stdlib suite also passed in [run 40275895487](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895487).
- [x] Runtime-wide active-operation admission and connection-quota assertions passed in [run 40275895449](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895449); the separate subprocess resource guard passed in [run 40275895416](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895416).
- [x] Process timeout/reaping, aggregate output cap, stdout flood, stderr flood, and normal exit/stream semantics passed on Linux and Windows in [SEC-05 run 40275895425](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895425).
- [x] Windows descendant containment passed at process creation: `windows_job_object_terminates_descendant_after_parent_exits`, `windows_job_object_terminates_descendant_on_timeout`, and `windows_job_object_immediate_descendant_spawn_stress` passed in [run 40275895425](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895425); the full Windows `one-core` suite reported 238 passed.
- [x] Denial side-effect regression and process failure cleanup/recovery assertions listed above passed in the final-pin focused jobs.
- [ ] No unresolved critical security finding / complete threat review: not checked. The complete threat review remains open, non-Linux Unix mount identity is best-effort `st_dev`, and arbitrary heap/caller-retained output memory is not fully accounted. No full OS sandbox claim.
- [x] No required source tests were deleted or weakened in this continuation. The SEC-05 harness received an explicit GNU x86_64 linker dependency; Android harness fixes added the native ADB symlink and diagnostics. Existing strict implementation-format checks remain enabled.

### Governance and auditability

- [x] At the historical checkpoint, PR #80 head, lab pin, and final-SHA workflow checkout agreed on `990c4e80f657aa2ac0409cfaf3bbf522856bc889`. Current candidate/pin is now `b35c7323df72a24e9e6a0376e63b350a6ae8907d`; a fresh exact-SHA matrix is required.
- [x] Historical SHA `73bd504ac81a14737b321817b94c7bc2fbb17a15` results are separated from the final-pin results.
- [x] Official completion ledger, Definition of Done, session checkpoint, independent evidence index, PR #80 body, and issue #81 were updated.
- [x] Release gate remains fail-closed; [run 40275895403](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40275895403) reported NOT PASSED and did not promote points. It ran before all matrix jobs completed, so its pending-run findings are historical for that evaluation.
- [x] Current records do not claim Android runtime success or complete sandbox security beyond the tests performed.
- [ ] Overall E3 + E4 acceptance remains OPEN until Android API 35 runtime completes and the full threat-review item is resolved or explicitly accepted under the project's formal review process.

**Current status:** E3 **NOT ACCEPTED** (Android runtime pending); E4 focused regressions pass but full E4 acceptance remains **NOT ACCEPTED** (full threat review/residuals remain open). Do not mark **PASS GREEN LOCKED** yet.


## Latest live audit — 2026-10-26 12:06 UTC

- The most recent ledger gate visible during this audit is [run 40319700019](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40319700019). It checked out the lab pin `2a7670c5166efee54426196f28a8152cbfe758b3`, ran verifier unit tests successfully, and then correctly failed closed: implementation `91/100`, verified `64/100`; 9 Definition of Done items unchecked; E1 0/10, E2 0/8, E3 0/8, E4 0/6, E6 0/4 accepted in the ledger; no successful Android API 35 runtime result for the exact pinned SHA; and no protected ONE Package Provenance Release for that exact SHA.
- The gate log proves the verifier process was given a masked `CANONICAL_READ_TOKEN` environment variable and that its unit tests passed. It does **not** prove the secret can read Actions runs from the canonical ONE repository: the acceptance output still reports missing exact-SHA evidence, and this run predates the latest checkout-secret correction.
- The latest observed workflow-file correction separates credentials: `CANONICAL_READ_TOKEN` for checkout of the canonical ONE source (read access), and `ONE_REPO_TOKEN` mapped to `CANONICAL_READ_TOKEN` for verifier API calls. No post-correction gate run is visible yet, so Actions-read access is **not yet proven**.
- Candidate source/pin at the latest main-branch comparison was `2a7670c5166efee54426196f28a8152cbfe758b3`. Exact-SHA successful evidence observed in this lab still has to be reconciled to that SHA; previous successful Android runtime evidence for predecessor SHAs is not substituted.
- Newer E4 runs [subprocess resource guard 40318051774](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051774) and [adversarial filesystem/resource-bound regression 40318051897](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051897) completed successfully, with Unix and Windows jobs passing. This supports the E4 implementation/test behavior on the source those runs actually checked out, but it does not by itself satisfy E4's six ledger points or prove the candidate SHA now pinned is the same.
- Android Linux TCG runtime [40318051835](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051835) failed at emulator boot; macOS TCG [40318051790](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051790) and community fallback [40318051803](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051803) were still in progress at the last query. Android cross-build/contract fallback [40318051755](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40318051755) succeeded, but cross-build is not runtime proof.
- No ledger score or acceptance status is promoted by this note. Historical failures remain intact. Gate remains **NOT PASSED**.


## Exact-SHA matrix reconciliation — candidate 2a7670c5166efee54426196f28a8152cbfe758b3

All statuses below were checked live on 2026-10-26. The canonical ONE source pin remains `2a7670c5166efee54426196f28a8152cbfe758b3`; the lab commits only changed verification workflows, the evidence index, and pin-file newline formatting. The ONE source branch/PR was not changed.

### Completed exact-SHA evidence

- E1 full candidate cross-platform matrix: [run 40321188806](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321188806) — Ubuntu 24.04 and Windows Server 2025 both **success** after the Windows Clang override was configured.
- E1 standard-library contract/integration/lint: [run 40321345683](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345683) — **success**.
- Cross-platform candidate verification: [run 40321345494](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345494) — Ubuntu and Windows jobs **success**.
- Linux distro verification: [run 40321345671](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345671) — Ubuntu 24.04 and Debian 12 **success**.
- Candidate artifact integrity: [run 40321345614](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345614) — **success**.
- Focused standard-library/database regressions: [run 40321345739](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345739) — **success**.
- Cargo lockfile bootstrap: [run 40321345586](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345586) — **success**.
- E4 adversarial filesystem/resource-bound regressions: [run 40321345484](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345484) — Unix and Windows jobs **success**.
- E4 subprocess resource guard: [run 40321345794](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345794) — **success**.
- E4 SEC-05 subprocess timeout/output limits: [run 40321345615](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345615) — Linux and Windows jobs **success**.
- Android AArch64 cross-build/contract fallback: [run 40321345576](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345576) — **success**, but this is not runtime acceptance.
- Synthetic-trust package provenance lab: [run 40321345885](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345885) — **success**, but synthetic trust is not protected canonical release provenance.

### Android API 35 runtime — failures retained, no substitute credit

- Linux TCG [run 40321345619](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345619) — **failure**: the stock Android emulator reports that ARM64 guest CPU architecture is unsupported by QEMU2 on the x86_64 host.
- macOS HVF probe [run 40321345559](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345559) — **failure**: `HV_UNSUPPORTED`.
- macOS software-emulation fallback [run 40321345669](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345669) — **failure**: the QEMU launch still selected HVF and exited with `HV_UNSUPPORTED`; this is infrastructure/accelerator failure, not an ELF execution result.
- Native ARM64 Linux-host attempt [run 40321345556](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345556) — **failure** during API 35 image installation; no runtime execution occurred.
- Community ARM64 emulator fallback [run 40321345654](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345654) — **still running** at this checkpoint. Its exact-source ELF build passed; runtime acceptance awaits successful API 35 boot, execution, exit code 0, and expected `ONE_NATIVE_BACKEND_OK` output.
- macOS TCG workaround [run 40321345523](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345523) — **still running** at this checkpoint; no runtime result is accepted until it completes with the required assertions.

### Gate and score reconciliation

- Latest gate [run 40321708009](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321708009) correctly remains **failure**. It reads the current pin and live Actions run list, retains implementation `91/100` and verified `64/100`, and reports 9 unchecked Definition of Done items, E1/E2/E3/E4/E6 ledger verified points still `0`, and no protected canonical `ONE Package Provenance Release` run for this exact source SHA.
- The gate was strengthened to require both `ONE Milestone 1 E1 Cross-Platform Acceptance Lab` and `ONE E1 Standard Library Windows Acceptance` in the exact-source workflow matrix. Added tests assert both names remain mandatory. Fixed weights and acceptance criteria were not changed.
- No completed evidence listed above automatically awards ledger points. Row acceptance remains subject to each original criterion; full E1 scope, complete E4 threat/coverage requirements, Android runtime, protected release provenance, and E6 reconciliation remain distinct acceptance obligations.
- No score was changed. Historical failed runs remain intact.


## Credentialed Actions access diagnostic — 2026-10-26

- The workflow wiring was inspected directly: `.github/workflows/ledger-gate.yml` checks out the canonical source using `secrets.CANONICAL_READ_TOKEN` and maps `secrets.ONE_REPO_TOKEN` to the verifier's `CANONICAL_READ_TOKEN` environment variable for the source Actions API query. No secret values are printed.
- The latest gate [run 40323027077](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40323027077) logged: `Canonical Actions run-list query succeeded using the supplied source token.` It then found no protected `ONE Package Provenance Release` run for the exact pinned source SHA. This confirms the credentialed query path worked; it is not evidence that a release run exists.
- The gate's 403 path was changed to emit a safe diagnostic and to retain an explicit failure if the supplied token receives HTTP 403, even when public unauthenticated fallback can list public runs. This prevents fallback from masking a token-access failure.
- The gate still fails on substantive acceptance: Android API 35 runtime [40321345654](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345654) is still in progress/no conclusion, and protected package provenance is absent. Scores remain `91/100` implementation and `64/100` verified; no points or weights were changed.


## Exact-SHA revalidation and gate access correction — 2026-10-26

- **Canonical ONE source SHA:** `2a7670c5166efee54426196f28a8152cbfe758b3`, pinned in `CANONICAL_COMMIT.txt`. The gate log for [run 40323143286](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40323143286) explicitly checked out that exact source SHA and verified `git rev-parse HEAD` matched it.
- **Actions access is now demonstrated for the query exercised by the gate:** the workflow passes `secrets.ONE_REPO_TOKEN` as the verifier's `CANONICAL_READ_TOKEN` environment variable, and the gate log says `Canonical Actions run-list query succeeded using the supplied source token.` No token value is logged. This proves the live run-list query works; it does not by itself prove that every protected workflow's job logs/artifacts are readable.
- **Latest gate remains NOT PASSED:** run [40323143286](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40323143286) reports implementation 91/100, verified 64/100, 9 unchecked Definition of Done items, E1 0/10, E2 0/8, E3 0/8, E4 0/6, E6 0/4. It specifically rejects the missing completed exact-SHA Android API 35 AArch64 runtime and missing protected `ONE Package Provenance Release` run. Scores and criteria were not changed.
- **Exact-SHA matrix on the current pin:** [cross-platform run 40321345494](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345494), [candidate artifact integrity 40321345614](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345614), [E1 Windows acceptance 40321345683](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345683), [focused stdlib/database 40321345739](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345739), [Cargo lockfile bootstrap 40321345586](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345586), [E4 adversarial filesystem/resource bounds 40321345484](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345484), and [E4 subprocess resource guard 40321345794](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345794) completed successfully for their stated scopes. These scoped passes do not establish full E1 or E4 row acceptance.
- **Android runtime failures remain failures:** [Linux TCG run 40321345619](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345619) failed before guest boot because the Android emulator rejects an arm64 guest on an x86_64 host. [Native ARM64 host run 40321345556](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345556) failed installation because SDK Manager did not provide the `emulator` package for Linux ARM64. The workflow was corrected in lab commit `df5d644d5af5508f5b942f6b887d98358332c74e` to install a pinned ARM64 emulator archive separately from the official API 35 image; the new run is [40323932099](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40323932099) and is not accepted until the guest boots and the ONE ELF output/exit assertion passes.
- [Community ARM64 runtime fallback run 40321345654](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40321345654) successfully built the exact-source AArch64 ELF; its runtime job was still in progress when this checkpoint was written. Build success is not runtime acceptance.
- **Protected release boundary:** `.github/workflows/package-provenance-release.yml` is `workflow_dispatch`-only and requires the protected `one-release` environment plus signing/trust secrets. No release was published or authorized by this work. The gate's missing protected-release evidence remains open; do not manufacture a release run or count synthetic trust as production trust.
- Historical failures remain preserved. No fixed weight, acceptance criterion, score, PR merge, main branch, or release state was changed.


Frozen candidate checkpoint — source SHA 7fe9ce3adbf83f6b5b2c427d163df44df43b1c24

- **Canonical ONE source SHA:** `7fe9ce3adbf83f6b5b2c427d163df44df43b1c24`, current PR #80 head. The lab pin in `CANONICAL_COMMIT.txt` has been updated to this exact SHA after adding the scoped E4 threat review and reconciling the fixed-weight total. These are documentation-only source commits; the full exact-SHA matrix is being rerun and no previous-SHA test is automatically accepted for the new SHA.
- **Ledger arithmetic:** implementation subtotal is now 92/100 provisional (E4 implementation 6/6 after the threat-review artifact); verified subtotal remains 64/100. No verified points were added. The E4 row and TOTAL row now agree on the same fixed-weight sum.
- **Access:** the gate run [40324100070](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40324100070) successfully queried the canonical repository's Actions run list with the configured source token. This proves that query works; protected release logs and release-run evidence remain a separate requirement.
- **Fresh exact-SHA matrix for this pin:** [gate run 40324908922](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40324908922) and the workflows triggered alongside it were tied to the immediately preceding source SHA `d603fffcb091185edcba6dfe68b8496335fe9b92`; they are superseded for final acceptance by the total-row correction. New runs triggered by pin `7fe9ce3adbf83f6b5b2c427d163df44df43b1c24` must complete successfully before any final-SHA verification acceptance.
- **Open acceptance:** E1 full-row API scope; E2 protected `one-release` run with independently configured trusted publisher; E3 real API 35 `arm64-v8a` ELF execution with expected output and exit code 0; E4 full row acceptance on the frozen SHA; and E6 final forensic audit remain open. No release was published, PR #80 remains unmerged, and the main branch was not changed.


## Final candidate pin update — c26e28789fb090ad8a684c6c6853ec2a88e3f9ca

- Candidate source SHA is now `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca` after adding the in-scope E1 CI trigger correction so verification/ledger checkpoint changes also start the hosted E1 acceptance lab.
- `7fe9ce3adbf83f6b5b2c427d163df44df43b1c24` and earlier exact-SHA runs are historical for this candidate. The lab's `CANONICAL_COMMIT.txt` now pins `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`; the required matrix, including the newly-triggered canonical E1 lab, must finish on this exact SHA before final acceptance.
- The E4 scoped threat-review artifact remains in the candidate branch; implementation is 92/100 provisional and verified remains 64/100 until legitimate row acceptance.
- No code behavior was changed by the trigger correction. No score was changed in this update. The gate remains NOT PASSED until exact-SHA workflows, the protected release evidence, and all Definition of Done items pass.


## Exact-SHA execution continuation — candidate c26e28789fb090ad8a684c6c6853ec2a88e3f9ca

Candidate ONE source SHA: `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`. The source pin was checked against PR #80 HEAD before these runs. Historical failures remain unchanged and are not rewritten.

Completed exact-SHA evidence:

- [Cross-platform verification, run 40325670295](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325670295): Ubuntu and Windows Server 2025 jobs both completed successfully.
- [Linux distro verification, run 40325666931](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666931): Ubuntu 24.04 and Debian 12 jobs both completed successfully.
- [E1 standard-library acceptance, run 40325666608](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666608): contract/integration/lint job completed successfully for its defined scope; this does not alone accept the entire E1 row.
- [Focused standard-library/database regressions, run 40325666312](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666312): completed successfully for its focused scope.
- [Cargo lockfile bootstrap, run 40325666316](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666316): completed successfully.
- [Candidate artifact integrity, run 40325666405](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666405): exact-source Linux/Windows bundle inspection completed successfully.
- [SEC-05 subprocess timeout/output-limit, run 40325666598](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666598): Linux and Windows jobs both completed successfully.
- [E4 adversarial filesystem/resource-bound regressions, run 40325666570](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666570): Unix and Windows jobs both completed successfully for the implemented test scope.
- [E4 subprocess resource guard, run 40325666499](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666499): completed successfully.

Android runtime is still **OPEN / NOT ACCEPTED** at this checkpoint. The following exact-SHA attempts were still running when this entry was written: [community ARM64 emulator fallback, run 40325666409](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666409), [macOS TCG attempt, run 40325666426](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666426), and [native ARM64 Linux host, run 40326438426](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40326438426). No build-only or emulator-boot-only result is accepted as runtime success; the required result is actual API 35 `arm64-v8a` execution of the exact-source ELF with exit code 0 and output `ONE_NATIVE_BACKEND_OK`.

Gate run [40325704710](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325704710) was evaluated while several matrix jobs were queued/in progress. Its NOT PASSED result is retained as history and must not be described as a final post-matrix decision. Re-run the gate after the Android runtime and all other required exact-SHA workflows conclude.

The source ledger's row sum is implementation `92/100`, verified `64/100`. E1/E2/E3/E4/E6 full-row verification is not inferred from these scoped workflow passes. No weights or acceptance criteria were changed. PR #80 remains open/draft/unmerged; no release was published.


## E1 cross-platform acceptance result — exact source SHA c26e28789fb090ad8a684c6c6853ec2a88e3f9ca

The newly triggered E1 acceptance run [40346574861](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40346574861) completed successfully on both Ubuntu 24.04 and Windows Server 2025. Both job logs confirm checkout/assertion of exact ONE source SHA `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`; on both platforms the E1 standard-library integration regression suite, standard-library library unit suite, full workspace tests, workspace Clippy with warnings denied, and repository contract checker completed successfully. This is direct exact-SHA evidence for the workflow's declared scope. It does not by itself award full E1 ledger credit or close the other E1 API acceptance criteria. The earlier ledger-gate run [40346058660](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40346058660) queried before this E1 run had completed and therefore reported no completed matching E1 run; its historical failure is retained. A fresh gate evaluation is required to read the completed result.



## Latest live evidence reconciliation — 2026-10-26

Canonical candidate source SHA remains `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`, and lab `CANONICAL_COMMIT.txt` matches that SHA. PR #80 remains open, draft, and unmerged.

- **E1 exact-SHA cross-platform scope PASS:** [run 40346574861](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40346574861) completed successfully on Ubuntu 24.04 and Windows Server 2025. The job logs confirm the exact canonical source SHA and successful E1 integration regression, library unit tests, workspace tests, Clippy with warnings denied, and contract checker. This is scoped evidence only; the ledger's E1 full-row acceptance criteria are not thereby satisfied.
- **Android API 35 runtime remains OPEN:** [run 40343229772](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40343229772) is still `in_progress`. The exact source checkout, ARM64 host assertion, Android toolchain/image setup, and backend contract tests passed. The boot step remains `in_progress`; the actual AArch64 ELF execution step is still pending. Job-log retrieval returned `BlobNotFound`, which is log unavailability, not runtime evidence. Do not accept this run until it completes successfully with the ELF exit code 0 and `ONE_NATIVE_BACKEND_OK`.
- **Latest gate remains NOT PASSED:** [run 40348297441](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40348297441) checked out the exact source SHA and passed verifier unit tests, but the live Actions run-list query received HTTP 403 using the currently wired `CANONICAL_READ_TOKEN`; public fallback returned 404 for the private source repository. Actions-read access is therefore not proven by this run. This requires repository-secret/permission correction by an authorized repository administrator; do not weaken the gate.
- **Canonical hosted workflows:** current-SHA runs [One CI 40325645795](https://github.com/panglimanetizen01/one/actions/runs/40325645795), [focused stdlib 40325645707](https://github.com/panglimanetizen01/one/actions/runs/40325645707), [E1 40325645817](https://github.com/panglimanetizen01/one/actions/runs/40325645817), [E2 40325645737](https://github.com/panglimanetizen01/one/actions/runs/40325645737), and [Linux distro 40325645679](https://github.com/panglimanetizen01/one/actions/runs/40325645679) report failure conclusions. Their accessible job summaries do not include step-level details, and the job-log endpoint was unavailable in prior checks; do not infer that source tests failed or passed without step/log evidence.
- **Ledger unchanged:** implementation `92/100`, verified `64/100`, nine Definition of Done items unchecked. E1/E2/E3/E4/E6 remain unaccepted at full-row level; protected `one-release` provenance and the final forensic audit remain open. No fixed weights, acceptance criteria, scores, checkboxes, main branch, PR merge, or release state were changed.



## Android runtime failure classification — 2026-10-26

The native ARM64-host attempt [run 40343229772](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40343229772) has now completed with **FAILURE**. Its job log is available and identifies the concrete boot blocker: QEMU emitted `qemu-system-aarch64-headless: gic-version=host requires KVM`, then the emulator process exited with code 1. The actual ELF execution step was skipped, so this run is not runtime evidence and must not be counted as PASS. Source checkout at `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`, ARM64 host assertion, Android SDK/image installation, and backend contract tests passed before the boot failure.

The separate Linux TCG workflow `.github/workflows/android-api35-tcg-runtime.yml` exists and is designed to exercise the Android guest without hardware acceleration, but it still needs a completed run whose exact-source ELF execution succeeds; no success is inferred from workflow existence.

The latest ledger gate [run 40350762856](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40350762856) remains **NOT PASSED**. It passed verifier unit tests, then failed enforcement because the canonical Actions run-list request using `CANONICAL_READ_TOKEN` returned HTTP 403, public fallback returned HTTP 404, and E1/E2/E3/E4/E6 acceptance plus nine DoD items remain incomplete. Correct the lab repository secret/permissions through GitHub settings with an authorized account; never paste the token into chat and never bypass the fail-closed gate.

No source SHA, score, fixed weight, acceptance criterion, main-branch state, PR merge state, or release state was changed by this reconciliation.


## Android API 35 runtime route reconciliation — 2026-10-26 (follow-up)

The exact-SHA Linux TCG runtime attempt [run 40325666239](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666239) also failed before ELF execution. Its log gives the concrete cause: `Avd's CPU Architecture 'arm64' is not supported by the QEMU2 emulator on x86_64 host. System image must match the host architecture.` The Android API 35 arm64-v8a image cannot be run by this x86_64 hosted emulator configuration; the run is not runtime PASS.

The community ARM64 emulator fallback [run 40325666409](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666409) failed at emulator startup. Its job log reports `ERROR | Unable to spawn process due to: No such file or directory`, followed by exit code 1. The actual ELF execution was not proven; this is not runtime PASS. The macOS TCG workaround [run 40325666426](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666426) and the older Linux TCG fallback [run 40325666380](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40325666380) also failed at emulator boot, before ELF execution. Native ARM64-host run [40343229772](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40343229772) failed because the emulator's host GIC configuration required KVM. Thus none of these attempts proves the required Android runtime behavior.

A lab-only trigger marker was added at `evidence/triggers/prompt3-android-tcg-runtime.txt` in commit [24780455ba26294e8944b8df708230d4cbdebbbf](https://github.com/panglimanetizen01/one-windows-verification/commit/24780455ba26294e8944b8df708230d4cbdebbbf), documenting the intended strict exact-SHA runtime acceptance. At the time of this entry, no new run for `.github/workflows/android-api35-tcg-runtime.yml` was visible in the recent Actions run listing; therefore this marker commit is not represented as a successful trigger or a test result.

Current conclusion remains **Android E3 runtime NOT ACCEPTED**. Next valid route must use a supported ARM64 Android emulator/runtime environment with its KVM/GIC configuration correctly supported, or an actual API 35 arm64-v8a device; it must execute the candidate ELF and assert exit code 0 plus `ONE_NATIVE_BACKEND_OK`. Build-only, contract tests, image installation, and boot attempts do not satisfy this criterion.


## Latest gate reconciliation — 2026-10-26

The newest gate run [40355195526](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40355195526), lab commit `7ba3505742e9c125edd5a20309ff67ecc69a4b97`, rechecked canonical ONE source SHA `c26e28789fb090ad8a684c6c6853ec2a88e3f9ca`. Verifier unit tests passed, but enforcement remains **NOT PASSED**. The canonical Actions run-list request with the supplied source token returned HTTP 403; the run recorded nine unchecked Definition of Done items and E1 0/10, E2 0/8, E3 0/8, E4 0/6, E6 0/4 verified for full-row acceptance. It also explicitly rejected Android runtime run 40343229772 because its conclusion was failure.

The gate workflow and acceptance rules were not modified to accommodate these failures. To clear the token blocker, an authorized repository owner must repair the `CANONICAL_READ_TOKEN` secret/permissions in GitHub settings so it can read Actions runs in `panglimanetizen01/one`; do not disclose the token in chat. Android runtime remains unaccepted until an exact-SHA API 35 arm64-v8a ELF execution succeeds and emits `ONE_NATIVE_BACKEND_OK`.


## Live continuation — 2026-10-26 17:00 UTC

- Latest gate run [40363039613](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40363039613), lab workflow commit `1309d97b2e6ea6313ba5961a025fdae7e0dd29a3`, completed **failure**. Its live-evidence checker successfully queried canonical Actions using the corrected token mapping, but still rejects the candidate because the required acceptance ledger rows and nine DoD checkboxes remain incomplete, API 35 Android runtime run [40362704802](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40362704802) is still in progress, and no protected canonical `ONE Package Provenance Release` run exists for source SHA `d8ee564637f9fae3a7e95ff12be02413574c462f`.
- The Android run has passed source-pin verification, ARM64 host check, API 35 image/NDK install, and Android backend contract tests. The emulator boot step is still running; the ELF execution step has not started. No Android runtime PASS is claimed.
- The native-host workflow experiment now explicitly uses QEMU `-machine virt,gic-version=3`, `-cpu cortex-a57`, software acceleration, and a bounded boot poll. This is a changed hypothesis versus the earlier `gic-version=host requires KVM` failure, but until the boot step completes and the ELF is executed with exit code 0 plus `ONE_NATIVE_BACKEND_OK`, E3 remains unaccepted.
- The earlier Actions:read access blocker is resolved at the API-query level by mapping the verifier to `ONE_REPO_TOKEN`; this is not a substitute for production release authorization or signing trust. No ledger points, fixed weights, DoD criteria, source branch, protected environment, release, or PR merge were changed by this checkpoint.


### E4 test-name audit — exact source SHA d8ee564637f9fae3a7e95ff12be02413574c462f

The detailed logs for [Unix job 121703018574](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134649) and [Windows job 121703020246](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134649) confirm the focused tests actually executed (not just empty filtered test invocations):

- Unix: `descriptor_relative_read_race_never_follows_swapped_parent_symlink`, `final_component_mount_boundary_denial_does_not_truncate_file`, `descriptor_relative_walk_rejects_proc_mount_boundary`, `descriptor_relative_read_rejects_final_symlink`, `descriptor_relative_read_rejects_symlinked_parent_even_without_precheck`, `descriptor_relative_write_rejects_final_symlink_without_modifying_target`, plus filesystem-root scope and capability-isolation tests. These test invocations reported passing results.
- Windows: `filesystem_reader_rejects_directory_junction_escape`, `filesystem_reader_reads_absolute_target_inside_project_root`, `filesystem_adapters_confine_absolute_targets_to_project_root_without_side_effects`, `filesystem_write_adapter_writes_text_target`, `filesystem_write_adapter_rejects_oversized_content`, and `filesystem_adapters_reject_parent_directory_traversal` reported passing results.
- This is strong exact-SHA evidence for those named filesystem cases, but it does not alone prove every E4 criterion (notably shared operation/query caps, aggregate interpreter output cap, and Windows Job Object process-creation containment). Keep E4 row and DoD unchecked until the complete exact-final-SHA evidence set is reconciled.

## Android runtime failure diagnosis — 2026-10-26 17:04 UTC

Inspection of completed native-host attempt [run 40360134381](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40360134381) corrected the previous diagnosis: emulator boot and API 35 ABI assertions completed; the job failed before compiling the backend ELF because the next step ran `"$ONE_ANDROID_CLANG" --version` with `ONE_ANDROID_CLANG: unbound variable`. This was a workflow environment propagation defect, not proof of emulator boot failure or an ELF runtime failure.

Fix committed to the lab workflow in [97b02dc](https://github.com/panglimanetizen01/one-windows-verification/commit/97b02dc73ff6cc24961cb13caecd572c038841a7): after installing NDK r27.2, discover and validate the `aarch64-linux-android35-clang` executable and export its path through `GITHUB_ENV` so the build/execute step receives it. The retry is queued as [run 40365103399](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40365103399). This retry will establish whether the ARM64 runner's installed NDK provides a runnable host compiler; no runtime PASS is claimed while it is queued or until the exact ELF execution/output assertion passes.

## Android cross-build evidence update — 2026-10-26 17:08 UTC

Correction to the earlier retry note: the workflow now separates the NDK build onto an x86_64 Ubuntu host and the runtime onto an ARM64 host. The build job in [run 40365397466](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40365397466), pinned to source SHA `d8ee564637f9fae3a7e95ff12be02413574c462f`, completed successfully. Its logs prove the ONE backend generated C containing `puts("ONE_NATIVE_BACKEND_OK");`, the generated C compiled with the API 35 NDK, and the resulting executable was identified as ELF64 AArch64 with interpreter `/system/bin/linker64`; the artifact upload also passed.

The dependent ARM64 runtime job installed the API 35 image and emulator, passed Android backend contract tests, and entered the emulator boot step. At the latest check that boot step was still in progress; the ELF had not yet been executed on Android. Therefore E3 remains **not accepted** until the exact artifact runs on the API 35 `arm64-v8a` guest with exit code `0` and final output `ONE_NATIVE_BACKEND_OK`.


## Exact-source matrix update — 2026-10-27 04:32 UTC

Canonical ONE source SHA: `c656c0d1f0b6fe7507467f49c59fe199e24c5c89`. The independent verification pin is synchronized to this SHA. Results below belong to this candidate only:

- [E1 cross-platform acceptance lab](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449737977) — completed success on Ubuntu 24.04 and Windows Server 2025.
- [Windows E1 standard-library acceptance](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449737984) — completed success.
- [Linux distribution verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449737988) — completed success.
- [Cross-platform verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738072) — completed success.
- [SEC-05 subprocess timeout/output cap](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738070) — completed success.
- [E4 adversarial filesystem/resource-bound regressions](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449737975) — completed success.
- [Focused standard-library/database verification](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449737961) — completed success.
- [Android AArch64 device artifact build](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738040) and [x86_64-host cross-build/contract fallback](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738058) — completed success; these prove build/contract only, not guest runtime.
- [Android API 35 Linux TCG runtime attempt](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738003) — failed during emulator boot; no ELF guest execution is claimed.
- [Candidate artifact integrity](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738046), [native ARM64 Android runtime](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738071), and [community ARM64 emulator fallback](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40449738029) were still in progress at this checkpoint.

These completed successes are useful exact-SHA evidence, but they do not by themselves award full E1 row points or close E2/E6. The fixed-weight gate must be rerun after all required jobs finish. E2 still requires a protected canonical release/provenance run for this exact SHA using owner-configured signing and trusted-publisher secrets; no secret is recorded here. Do not change fixed weights or check DoD items without direct evidence.
