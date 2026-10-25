# E4 finding: subprocess execution has no enforced timeout/output quota

Date: 2026-10-25
Candidate source SHA inspected: `56606c7f8076bc9a67e321835077315d321b8b7a`
Source: https://github.com/panglimanetizen01/one/blob/56606c7f8076bc9a67e321835077315d321b8b7a/crates/one-core/src/interop.rs

## Finding SEC-05 — unbounded process lifetime and captured output

The inspected implementation of `run_process` creates a child with piped stdout/stderr and calls `Command::output()`. No execution deadline, process termination policy, stdout/stderr byte ceiling, or aggregate output ceiling is enforced in this function. `ProcessAdapter::invoke` forwards the selected stdout (or stderr) into an adapter result without an output-size check.

This is a source-level implementation finding, not a claim that a dynamic adversarial test has already been run. Existing database and filesystem limits do not establish a process-execution quota.

## Required closure evidence
1. Implement an explicit process execution policy with a deadline, bounded stdout/stderr capture, and a defined error/result when limits are exceeded.
2. Ensure timeout cleanup does not leave the direct child running; document and test child-process-tree behavior per supported OS.
3. Add adversarial tests for a long-running process, stdout flood, stderr flood, non-zero exit, and timeout cleanup on Linux and Windows.
4. Run the tests against the final source SHA and record actual results.

## Status
- Result: FAIL (implementation gap identified; no closure implementation in this checkpoint)
- Acceptance: NOT ACCEPTED
- Do not promote E4/global milestone to PASS until closure and exact-SHA regressions are evidenced.
