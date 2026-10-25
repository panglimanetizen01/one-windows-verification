# ONE Prompt 3 — Android artifact metadata and runtime verification (2026-10-25)

## Result

**PASS for the downloaded Run #7 Android AArch64 device artifact on a physical Android device running Termux.**

This evidence records the user's terminal output from the artifact downloaded as:
`one-android-aarch64-device-artifact (2).zip` (3,316 bytes, saved 2026-10-25 at 18:23 local device time).

- Verification workflow: [Build Android AArch64 device artifact — run 40188257557](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40188257557)
- Workflow artifact: [one-android-aarch64-device-artifact, artifact ID 12597386613](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40188257557/artifacts/12597386613)
- Workflow commit: `42d9f8b76d1b8ef770e85ed2651a68fdd7365c33`
- Source revision embedded in the artifact: `56606c7f8076bc9a67e321835077315d321b8b7a`

## Device-side results supplied from Termux

`SOURCE.txt` output from `cat -A`:

```text
source_sha=56606c7f8076bc9a67e321835077315d321b8b7a$
```

This confirms the SHA metadata ends with a real newline (the final `$` is the `cat -A` line-ending marker), not the literal two-character sequence `\\n`.

`SHA256SUMS`:

```text
b3a52ce990c157332ab39f25264fbdab3de9e796c26f827c497551237855967c  one-android-aarch64
```

Checksum verification:

```text
one-android-aarch64: OK
```

Runtime:

```text
ONE_NATIVE_BACKEND_OK
runtime_exit=0
```

## Acceptance

- [x] Source metadata names the expected source SHA and has a real newline.
- [x] Checksum manifest uses a portable relative filename.
- [x] `sha256sum -c SHA256SUMS` passes on Termux.
- [x] Android AArch64 executable runs successfully on the user's Android device.
- [x] Runtime reports `ONE_NATIVE_BACKEND_OK` and exits with status 0.

## Scope and integrity note

The earlier ZIP named `one-android-aarch64-device-artifact.zip` (3,338 bytes, saved at 18:11) was a stale artifact and failed checksum-manifest portability validation because it referenced a runner-local absolute path; its source metadata also contained a literal `\\n`. That failure was not hidden or overwritten. The successful result above is specifically from the newer 3,316-byte `(2).zip` artifact produced by workflow run #7.

This proves the packaging metadata/checksum and runtime smoke test for this artifact. It does **not** by itself prove full E3 platform conformance, E4 security/resource-limit acceptance, or the overall milestone is complete.
