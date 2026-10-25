# ONE Prompt 3 — SEC-05 Linux and Windows baseline verification (2026-10-25)

## Summary

The cross-platform GitHub Actions run completed on both Linux and Windows. The existing subprocess contract unit tests passed on both platforms, while the explicit SEC-05 acceptance guard failed on both platforms because the candidate still uses `Command::output()`, which buffers stdout/stderr without configured byte limits and does not enforce an execution deadline.

- Workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40189472225
- Workflow commit: `31f536124c0274bcb4da4b476dc62affe1d4718d`
- Candidate source SHA tested: `56606c7f8076bc9a67e321835077315d321b8b7a`
- Workflow file: `.github/workflows/e4-sec05-subprocess-cross-platform.yml`

## Platform results

| Platform | Existing `interop::tests` | SEC-05 acceptance guard | Overall workflow job |
|---|---|---|---|
| Ubuntu 24.04 (Linux) | PASS — 2 passed, 0 failed | FAIL — unbounded `Command::output()` remains | FAIL (intentional fail-closed result) |
| Windows Server 2025 | PASS — 2 passed, 0 failed | FAIL — unbounded `Command::output()` remains | FAIL (intentional fail-closed result) |

The guard emitted the explicit failure:

```text
SEC-05 FAIL: Command::output() buffers unbounded stdout/stderr and has no execution deadline.
```

## Interpretation

The result is not a passing SEC-05 implementation. It confirms that the baseline process tests compile and pass on both platforms, and that the independent guard detects the known missing resource controls consistently on Linux and Windows.

Dynamic adversarial tests for timeout enforcement, stdout flooding, stderr flooding, aggregate output limits, child termination/reaping, and OS-specific descendant cleanup are still required after the implementation is changed. No claim is made here that those controls currently exist or have passed.

## Next acceptance steps

1. Implement documented/configurable execution deadlines and bounded concurrent stream capture for stdout and stderr, including aggregate limits.
2. Ensure timeout/limit violations terminate and reap the child; document and test descendant-process cleanup semantics separately for Unix and Windows.
3. Add adversarial tests for timeout, stdout flood, stderr flood, non-zero exit status, and cleanup.
4. Rerun `cargo test --locked -p one-core` and the SEC-05 cross-platform workflow against the final candidate SHA.
5. Keep SEC-05 open until both OS jobs and all adversarial acceptance tests pass.
