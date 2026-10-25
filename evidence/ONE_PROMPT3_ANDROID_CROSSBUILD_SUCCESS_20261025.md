# ONE Prompt 3/4 — Android cross-build retry evidence

Date: 2026-10-25
Canonical ONE source SHA: `56606c7f8076bc9a67e321835077315d321b8b7a`
Verifier repository/branch: `panglimanetizen01/one-windows-verification` / `verification`
Workflow harness commit: `498ed621684ee07000b36d0d1b4fdf7c405bfb63`
Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40165743578
Job: https://github.com/github?job=121086307555

## Verified in this run

- GitHub Actions run conclusion: `success`.
- The source checkout explicitly verified the expected canonical SHA and reported runner architecture `x86_64`.
- Android NDK 27.2.12479018 and Android API 35 setup completed.
- A real Android-targeted probe was compiled. The log identified it as `ELF 64-bit LSB pie executable, ARM aarch64`, with interpreter `/system/bin/linker64`; ELF header checks for ELF64 and AArch64 passed.
- `cargo test --locked -p one-core --test native_backend_android_aarch64` completed with `5 passed; 0 failed; 1 ignored`.

## Strict evidence boundary

The ignored test is `build_native_menghasilkan_dan_menjalankan_elf_android_aarch64`; it requires a connected Android emulator and `ONE_ANDROID_ADB`. This workflow did not run that test on Android. The probe was cross-compiled and inspected on the x86_64 host; it was not executed on Android.

Therefore, this run proves Android AArch64 cross-compilation and backend contract tests only. It does **not** satisfy Android API 35 arm64-v8a runtime acceptance. E3 remains NOT ACCEPTED.

## Next actions

1. Obtain a real Android API 35 arm64-v8a device or compatible runner with working `adb`, and execute the exact-source native backend integration test.
2. Preserve the source SHA, artifact SHA-256, device API/ABI properties, full test output, and exit code as evidence.
3. Continue E4 adversarial security/resource-limit coverage and disposition the residual risks documented in `ONE_PROMPT3_E3_E4_CHECKPOINT.md`.
4. Do not promote the fixed-weight ledger or declare PASS GREEN LOCKED until every mandatory acceptance criterion is proven.
