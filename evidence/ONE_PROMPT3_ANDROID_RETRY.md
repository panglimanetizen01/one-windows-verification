# Prompt 3 continuation — Android runtime retry evidence

Date: 2026-10-25
Canonical ONE source SHA under test: `56606c7f8076bc9a67e321835077315d321b8b7a`.

## Attempt 1: failed due to workflow defect

Workflow: `android-aarch64-tcg-fallback.yml`
Harness commit: `68d2e0bbbad8c806acdddcc7f08f15ec5bb32707`
Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40162008643
Result: FAILED before source build or Android runtime. The checkout step log reports invalid refspec `+refs/heads/${ steps.target.outputs.sha }}*:refs/remotes/origin/${ steps.target.outputs.sha }}*`. Root cause: malformed GitHub Actions expression interpolation in the workflow. No Android execution was attempted. This failure is a lab workflow defect, not an ONE code failure.

## Attempt 2: corrected exact-SHA retry

Workflow: `.github/workflows/android-aarch64-tcg-fallback-v2.yml`
Harness commit: `9126e23507ffc6e74efb072fda4b36c28ca9290e`
Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40162050060
The retry pins canonical source SHA literally, verifies `git rev-parse HEAD`, then runs backend contract tests, boots Android API 35 arm64-v8a with emulator `-accel off` (TCG), and invokes the ignored native ELF build/execute regression test. At checkpoint writing, the job had passed runner setup and harness checkout; canonical source checkout was still in progress. No conclusion about Android runtime can yet be made.

## Acceptance status

E3 remains NOT ACCEPTED until the exact-SHA Android ELF execution step completes and its output/assertions are inspected. Do not count either the failed workflow or an in-progress retry as runtime evidence. Preserve previous Linux/Windows successes and the E4 residual risks from `evidence/ONE_PROMPT3_E3_E4_CHECKPOINT.md`.
