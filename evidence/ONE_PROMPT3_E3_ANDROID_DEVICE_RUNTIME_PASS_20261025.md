# ONE Prompt 3 — E3 Android AArch64 Device Runtime Evidence

Date: 2026-10-25
Status: PASS for the device-runtime check recorded below; this does not independently close the entire E3/E4 milestone.

## Source and artifact identity

- Candidate source SHA: `56606c7f8076bc9a67e321835077315d321b8b7a`
- CI artifact: `one-android-aarch64-device-artifact`
- Artifact workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40186858747
- Artifact SHA-256 (binary): `b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c`
- Device-side SHA-256 matched the expected binary digest.
- Device-reported architecture: `aarch64`
- Android API level: `34`
- Android ABI: `arm64-v8a`
- ELF inspection: ELF64, little-endian, type DYN (PIE), machine AArch64.

## Device runtime result

The user ran the downloaded binary from Termux after extracting the CI artifact. The supplied terminal output showed:

```text
=== DEVICE ===
aarch64
34
arm64-v8a
...
=== ANDROID RUNTIME TEST ===
ONE_NATIVE_BACKEND_OK
exit=0
```

Result: PASS — the exact checksum-identified Android AArch64 binary executed on an Android 14 / API 34 ARM64 device, emitted `ONE_NATIVE_BACKEND_OK`, and returned exit code 0.

## Metadata note

The artifact's `SOURCE.txt` currently contains a literal `\\n` suffix after the source SHA rather than a real newline. This did not affect binary identity or runtime execution, but the artifact workflow should be corrected so source metadata is cleanly formatted. The recorded source SHA itself is identifiable and matches the intended candidate.

## Scope and remaining gates

This evidence establishes device execution for the identified binary. It does not establish full E3/E4 acceptance, full application-level integration, or sandbox completeness. E4 still has an unresolved subprocess resource-control finding (SEC-05): the candidate implementation uses unbounded `Command::output()` without an enforced timeout and stdout/stderr byte caps. Keep the overall milestone gate closed until remaining acceptance criteria are satisfied with reproducible evidence.
