# ONE Prompt 3/4 — E4 adversarial regression run evidence

Date: 2026-10-25
Canonical ONE source SHA tested: `56606c7f8076bc9a67e321835077315d321b8b7a`
Verifier workflow commit: `aa00bcb72b1c1931600ece5835d60929a48dc940`
Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166287021

## Actual results

The independent lab workflow completed with conclusion **success** on the exact pinned candidate source SHA.

- Unix no-follow regression job: PASS. The job executed the descriptor-relative parent-symlink rejection, final-component symlink read/write rejection and no-target-modification assertions using `cargo test --locked -p one-core descriptor_relative_`.
- SQLite security/resource regression job: PASS. `cargo test --locked -p one-core database::tests` passed, including final-symlink rejection and configured query/parameter/column/row/output/engine-value/time-bound regressions.
- Capability and scope regression job: PASS. `cargo test --locked -p one-core governance::tests` passed, including default denial, explicit-denial precedence, least-privilege separation, and lexical root-scope descendant/sibling/traversal cases.
- Windows reparse-point regression job: PASS. `cargo test --locked -p one-core filesystem_windows_reparse_tests` passed on Windows Server 2025, including directory-junction escape rejection.

The workflow verified the exact candidate SHA before tests. The workflow commit SHA identifies the lab harness, not the source code being tested.

## Acceptance boundary

This is new direct regression evidence for the listed existing tests on Linux and Windows. It is not an exhaustive race/mount-boundary penetration test and does not prove runtime-wide memory/open-resource/process-output/concurrency quotas. It does not change the implementation, close SEC-01 through SEC-04 automatically, or authorize claims of complete sandboxing.

E4 remains **NOT ACCEPTED** until the complete Definition of Done is satisfied, residual risks are either fixed with appropriate tests or explicitly accepted under an authorized, narrower threat model, and the fixed-weight ledger is reconciled on the final frozen source SHA.
