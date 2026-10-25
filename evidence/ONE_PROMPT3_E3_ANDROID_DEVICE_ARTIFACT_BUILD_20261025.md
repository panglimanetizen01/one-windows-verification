# E3 Android AArch64 device artifact — CI evidence

Date: 2026-10-25

## Build result
- Workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40186858747
- Workflow revision: b1fef25ec191657cc1bb29a1f68f46ba0147e28b
- Canonical ONE source SHA checked out by workflow: 56606c7f8076bc9a67e321835077315d321b8b7a
- Build test: `build_android_device_artifact` — 1 passed, 0 failed.
- Artifact: `one-android-aarch64-device-artifact`
- Artifact page: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40186858747/artifacts/12595884778
- Artifact ID: 12595884778
- ZIP size: 3338 bytes
- ZIP SHA-256: `e70b141a4013c8a07a61925a3c31ff9fcd9a974355f8793cb0de4ed87c3ae2c7`
- Binary SHA-256 from build log: `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`
- Binary identification: ELF 64-bit LSB PIE, ARM AArch64, dynamically linked, interpreter `/system/bin/linker64`.
- ELF header confirms class `ELF64` and machine `AArch64`.

## Acceptance boundary
This proves successful cross-compilation, ELF architecture/header checks, and upload of the device artifact. It does NOT prove execution on a physical Android device. E3 runtime acceptance remains pending until the artifact is run on an Android ARM64 device (e.g. Termux) and the output, exit code, device API/ABI, and locally computed SHA-256 are recorded. Expected program output: `ONE_NATIVE_BACKEND_OK`; exit code must be 0.

## Run instructions
Download the artifact from the Artifact page above, extract it, then in Termux run:

```sh
uname -m
getprop ro.build.version.sdk
getprop ro.product.cpu.abi
sha256sum ./one-android-aarch64
chmod 700 ./one-android-aarch64
./one-android-aarch64
printf 'exit=%s\\n' "$?"
```

Compare the binary SHA-256 to the value above before execution. Do not mark runtime PASS if the binary cannot execute or output differs.
