# Linux hosted-runner openat2 probe — exact run evidence

**Date:** 2026-11-21  
**Workflow:** `.github/workflows/openat2-linux-runner-probe.yml`  
**Run:** [#44921770910](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44921770910)  
**Job:** [#136899157733](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44921770910/job/136899157733)  
**Conclusion:** <strong>SUCCESS</strong> — isolated Linux hosted-kernel capability probe only.

## Runner environment

- Ubuntu 26.04.1 LTS
- x86_64
- Linux kernel `7.0.0-1020-azure`
- GCC 15.2.0

## Terminal job steps

All five steps completed with `conclusion=success`:
1. Set up job
2. Record runner environment
3. Compile isolated probe
4. Execute path-confinement probe
5. Complete job

## Observed assertions

| Assertion | Expected result | Observed result |
|---|---|---|
| Open nested file inside root | Success | PASS |
| Open `../outside.txt` with `RESOLVE_BENEATH` | Reject with EXDEV | PASS, errno 18 |
| Open symlink with `RESOLVE_NO_SYMLINKS` | Reject with ELOOP | PASS, errno 40 |
| Open escaping symlink with `RESOLVE_BENEATH` | Reject with EXDEV | PASS, errno 18 |

Final output: `RESULT=PASS all openat2 resolution checks enforced`.

## Scope and limitations

This run proves that the tested Ubuntu hosted runner accepts `openat2` and enforces the tested BENEATH / NO_SYMLINKS resolution behavior. It does not test:
- the Project ONE Rust filesystem adapter;
- `RESOLVE_NO_XDEV`;
- detached-mount nested atomic writes;
- rename/mount race resistance;
- hard-link or resource-limit policy;
- Android/Termux syscall availability.

The Project ONE backend regression is maintained separately in [ONE source commit 4dec131bce0fc123d32260c50bbfe16abe471162](https://github.com/panglimanetizen01/one/commit/4dec131bce0fc123d32260c50bbfe16abe471162), with its own CircleCI status evidence. Do not transfer this generic probe's PASS to ONE backend acceptance or Issue #104.

Issue #104 remains OPEN / NOT ACCEPTED.
