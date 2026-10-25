# ONE Prompt 3/4 execution checkpoint — 2026-10-25 (follow-up)

## Candidate and governance state
- Main repository: https://github.com/panglimanetizen01/one
- PR #80: https://github.com/panglimanetizen01/one/pull/80
- PR remains open, draft, unmerged. No merge/release action performed.
- Candidate branch reported by PR: `milestone/100-ecosystem-20261023`
- Exact candidate source SHA pinned by test workflows: `56606c7f8076bc9a67e321835077315d321b8b7a`
- Lab branch: `verification`

## E4 — latest exact-SHA adversarial regressions
- Workflow: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166287021
- Workflow/harness commit: `aa00bcb72b1c1931600ece5835d60929a48dc940`
- Final workflow conclusion: SUCCESS.
- Linux job passed descriptor-relative no-follow filesystem tests, SQLite symlink/resource limit tests, and capability/scope policy tests.
- Windows Server 2025 job passed directory-junction escape rejection regression.
- Evidence record: https://github.com/panglimanetizen01/one-windows-verification/commit/07710bd320b9dca15d72a98070bec6a3e5263a0c

### E4 acceptance boundary
This verifies the tests listed above against the exact candidate SHA. It does not prove exhaustive TOCTOU/race resistance, automatic project-root confinement across adapters, mount isolation, or runtime-wide memory/open-file/process-output/concurrency quotas. Those remain open acceptance risks; E4 is NOT ACCEPTED.

## E3 — Android runtime
- Workflow attempt: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166320867
- Workflow commit: `3eff7300bedfcb13b8c331e1f0cf8f957ae4aed6`
- Candidate SHA checkout and NDK/API 35 installation/source verification completed.
- Latest observed state: emulator boot + actual ELF execution step remained in_progress, with no terminal conclusion available through the connector. Job-log fetch returned BlobNotFound while the step was running, so no log-based diagnosis can yet be asserted.
- The prior cross-build result remains limited to ELF inspection and backend tests (5 passed, 1 ignored); it is not Android runtime acceptance.
- E3 remains NOT ACCEPTED until API level 35, ABI arm64-v8a, actual binary execution, exit code and expected stdout are captured.

## Global gate
- Do not promote the fixed-weight ledger based on partial results.
- Global release gate remains NOT PASSED pending E3 runtime proof, E4 residual remediation/acceptance, and final exact-SHA ledger reconciliation.
- Next action: inspect Android run until terminal state. If emulator boot fails or stalls, use its terminal logs to select a genuinely different execution environment; do not report runtime PASS from cross-compilation.
