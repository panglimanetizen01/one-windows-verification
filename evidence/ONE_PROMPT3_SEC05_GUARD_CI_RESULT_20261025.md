# E4 SEC-05 fail-closed CI result

Date: 2026-10-25

## Exact candidate inspected
- Repository: https://github.com/panglimanetizen01/one
- Branch: `milestone/100-ecosystem-20261023`
- SHA: `56606c7f8076bc9a67e321835077315d321b8b7a`
- Source file: `crates/one-core/src/interop.rs`

## Lab guard run
- Workflow: `E4 subprocess resource guard`
- Lab commit: `3a85632850d04cfb6f5457b24831844d6bfda4d6`
- Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166852906
- Job: `121089567870`
- Actual result: FAIL (expected fail-closed outcome)
- Log assertion: `Unbounded Command::output() remains; subprocess timeout/output quotas are not enforced.`

This is evidence that the guard detects the known gap on the exact candidate SHA. It is NOT evidence that the candidate passes, nor a dynamic adversarial test of a corrected implementation.

## Android E3 status at this checkpoint
- Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166320867
- Last observed: `in_progress`, job step `Boot Android API 35 arm64-v8a emulator and execute ELF`
- No final runtime result was available at this checkpoint; do not count cross-build as device execution.

## Gate
- SEC-05: OPEN / NOT ACCEPTED
- E3 Android runtime: IN PROGRESS / NOT ACCEPTED
- E4 overall: NOT ACCEPTED
- Global milestone: NOT PASS GREEN LOCKED

## Next required action
Implement a bounded, deadline-aware process runner in the canonical candidate, including an explicit supported-OS child-process cleanup policy; add adversarial tests for timeout, stdout/stderr floods, normal non-zero exit and cleanup; run Linux and Windows suites against the resulting exact SHA. Separately obtain a terminal Android runtime result.
