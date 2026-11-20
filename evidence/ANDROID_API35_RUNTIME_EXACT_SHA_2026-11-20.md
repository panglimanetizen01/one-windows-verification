# Android API 35 ARM64 runtime — exact-source evidence (2026-11-20)

## Identity

- Canonical repository: `panglimanetizen01/one`
- Exact ONE source SHA: `fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`
- Independent verifier repository: `panglimanetizen01/one-windows-verification`
- Exact verifier HEAD: `226360d00bc26f858128d3127591fce13ecd52d9`
- Workflow: [#44652693606](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44652693606)
- Workflow conclusion: SUCCESS

## Jobs

| Job | Purpose | Conclusion |
|---|---|---|
| 136011228119 | Build exact-source Android AArch64 ELF on supported x86_64 NDK host | SUCCESS |
| 136012787863 | API 35 arm64-v8a ELF runtime on ARM64 host | SUCCESS |

## Runtime evidence

The runtime job completed all steps, including Android backend contract tests, installation of the API 35 ARM64 image/emulator, emulator boot, binary transfer, execution, and evidence upload.

Relevant decoded job-log output:

```text
ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /system/bin/linker64, not stripped
Android ELF exit code: 0
ONE_NATIVE_BACKEND_OK
```

## Artifact integrity

- Artifact ID: `14592959506`
- Artifact name: `one-api35-arm64-runtime-evidence-fb5c8bc66a5cbdf8a6670d9d1e9dbe0caa631a20`
- Size: 12,788 bytes
- Uploaded: 2026-11-20T01:50:49Z
- SHA-256: `ab24bf6244652ccc6892dabcbbd3571cb4c4dda3bd2bf5ad902c922e3faf152d`
- [Download/view artifact](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/44652693606/artifacts/14592959506)

## Scope and limitations

This proves native backend executable runtime on the tested Android API 35 ARM64 emulator for the exact ONE source SHA above. It does not prove Android filesystem adapter support, all Android device/ABI combinations, release readiness, or Issue #104 acceptance. The filesystem adapter remains unavailable on Android/macOS and fails closed there. Linux nested writes remain fail-closed. Do not promote verifier pins or ledger weights based solely on this runtime result.

## Anti-duplication

Do not rerun this workflow for the same source and verifier inputs. Re-run only if the source SHA, Android workflow/toolchain/runtime contract, or relevant verifier input changes.
