# Android physical-device runtime fallback

This path avoids relying on the hosted CI emulator, which failed to boot before the ELF invocation. It builds an AArch64 Android ELF from the exact candidate source SHA and uploads it as a short-lived workflow artifact. It does **not** count as runtime acceptance until the ELF is executed on a real Android arm64 device and the actual output/exit status is recorded.

## Build artifact

Run the **Build Android AArch64 device artifact** workflow manually from the `verification` branch. Download artifact `one-android-aarch64-device-artifact` from that run. Verify its checksum in the extracted directory:

```sh
sha256sum -c SHA256SUMS
cat SOURCE.txt
cat ELF-FILE.txt
```

Expected source SHA: `56606c7f8076bc9a67e321835077315d321b8b7a`. Do not use the artifact if the source SHA differs.

## Execute on a physical Android arm64 device with Termux

Copy `one-android-aarch64` into Termux storage and run:

```sh
uname -m
getprop ro.build.version.sdk
getprop ro.product.cpu.abi
chmod 700 ./one-android-aarch64
./one-android-aarch64
printf 'exit=%s\n' "$?"
```

Acceptance requires all of the following in captured evidence:
- `uname -m` reports `aarch64` or `arm64`, and ABI reports `arm64-v8a`.
- Android API level is captured.
- SHA-256 matches the downloaded `SHA256SUMS`.
- Exact executable output is `ONE_NATIVE_BACKEND_OK`.
- Exit code is zero.
- The full command output and timestamp are attached to the lab evidence record.

If Android reports a missing dynamic linker/library or permission failure, record it as a runtime failure; do not treat ELF header checks as execution success. The CI artifact is retained for seven days only. The candidate remains unaccepted until device execution evidence is reviewed.
