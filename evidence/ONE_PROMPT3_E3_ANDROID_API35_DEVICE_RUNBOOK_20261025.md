# Prompt 3 — Android API 35 arm64-v8a runtime acceptance runbook

**Candidate source SHA:** `26d3d30be773cfc403daa002f7116c176ef31fc8`  
**Build workflow:** [run 40213748069](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40213748069)  
**Artifact:** `one-android-aarch64-device-artifact-26d3d30be773cfc403daa002f7116c176ef31fc8`  
**Binary SHA-256:** `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`  
**Expected output:** `ONE_NATIVE_BACKEND_OK`  
**Acceptance status:** BUILD/ELF HEADER PASS; RUNTIME NOT YET VERIFIED.

The artifact is an ELF64 little-endian AArch64 PIE with interpreter `/system/bin/linker64`. Its successful build and header inspection do not satisfy the runtime requirement.

## Requirements before running

The target must report **Android API 35** and ABI **arm64-v8a**. API 34 or an x86_64 emulator is not an acceptable substitute.

## Run from an attached API 35 device with ADB

1. Download and extract the artifact ZIP from the build workflow above.
2. Confirm the target device:

   ```sh
   adb shell getprop ro.build.version.sdk
   adb shell getprop ro.product.cpu.abi
   ```

   The outputs must be `35` and `arm64-v8a`, respectively.

3. Verify the artifact hash on the host:

   ```sh
   sha256sum one-android-aarch64
   ```

   It must equal `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`.

4. Execute the exact binary on the device and preserve the complete output:

   ```sh
   adb push one-android-aarch64 /data/local/tmp/one-android-aarch64
   adb shell chmod 755 /data/local/tmp/one-android-aarch64
   adb shell '/data/local/tmp/one-android-aarch64; rc=$?; echo EXIT_CODE=$rc; exit $rc'
   ```

5. Acceptance requires the output `ONE_NATIVE_BACKEND_OK`, remote exit code `0`, API `35`, and ABI `arm64-v8a`. Save the raw command output, device properties, binary hash, and source SHA together as evidence.

## Run directly in Termux on an API 35 arm64-v8a device

After extracting the artifact into a Termux-accessible directory:

```sh
getprop ro.build.version.sdk
getprop ro.product.cpu.abi
sha256sum ./one-android-aarch64
chmod 700 ./one-android-aarch64
./one-android-aarch64 >runtime.stdout 2>runtime.stderr
rc=$?
printf 'EXIT_CODE=%s\n' "$rc"
cat runtime.stdout
cat runtime.stderr
```

Do not mark the gate PASS if the API/ABI check differs, the hash differs, execution fails, the output assertion is absent, or the log is incomplete.

## Why this runbook exists

The hosted macOS API 35 arm64-v8a emulator image installed, but the runner reported `HV_UNSUPPORTED` and did not execute the ELF. The Linux ARM64-host fallback could not install a compatible Android emulator package. This runbook is the remaining valid route to obtain real API 35 runtime evidence; it is not itself evidence of a successful runtime.
