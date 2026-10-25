# E3 Android runtime attempt result

Date: 2026-10-25

## Exact candidate
- Source SHA: `56606c7f8076bc9a67e321835077315d321b8b7a`
- Workflow commit: `3eff7300bedfcb13b8c331e1f0cf8f957ae4aed6`
- Run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40166320867
- Job ID: `121088001096`
- Final workflow conclusion: FAIL

## Observed log evidence
The workflow reached the Android emulator action, but the emulator never became available to ADB:
- repeated `adb: device 'emulator-5554' not found`
- `error: could not connect to TCP port 5554: Connection refused`
- terminal error: `Timeout waiting for emulator to boot.`

The command that runs the candidate ELF was never reached. This is an infrastructure/emulator boot failure, not a test failure in the candidate ELF and not proof of runtime success.

## Previous independent evidence
The x86_64 hosted runner cross-build produced an Android-targeted AArch64 ELF and passed the backend contract tests (5 passed, 1 ignored); the ignored test requiring a connected Android emulator did not execute the ELF.

## Status
- Android AArch64 cross-build: PASS for build/ELF format/backend non-device tests only.
- Android API 35 AArch64 runtime execution: NOT VERIFIED (emulator boot failure).
- E3 acceptance: NOT ACCEPTED.
- Global milestone: NOT PASS GREEN LOCKED.

## Next options
Use a real Android arm64 device with ADB available to the CI runner, or a verified Android arm64 emulator/runtime environment that can boot successfully. Any next attempt must show the ELF invocation and its actual exit/test result in logs; build success alone is insufficient.
