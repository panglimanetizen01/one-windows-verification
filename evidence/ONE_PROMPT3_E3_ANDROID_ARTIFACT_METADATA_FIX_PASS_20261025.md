# ONE Prompt 3 — Android Artifact Metadata Workflow Re-run

Date: 2026-10-25

## Result

PASS — workflow completed successfully after correcting the source metadata printf format.

- Workflow run: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40187541096
- Workflow commit: `e0bf99bd381f1f116441f729f8a3dedccf8f0bab`
- Run conclusion: `success`
- Build job: `success`
- Build and upload steps: `success`
- Artifact: `one-android-aarch64-device-artifact`
- Artifact ID: `12597305565`
- ZIP size: 3337 bytes
- Artifact download page: https://github.com/panglimanetizen01/one-windows-verification/actions/runs/40187541096/artifacts/12597305565

## Change

The workflow now uses a single shell newline escape in the `printf` format when writing `SOURCE.txt`:

```bash
printf 'source_sha=%s\n' "$(git -C "$GITHUB_WORKSPACE/source" rev-parse HEAD)" > "$RUNNER_TEMP/one-android-device-artifact/SOURCE.txt"
```

This addresses the previously observed literal backslash-n metadata formatting defect.

## Scope

This workflow rerun verifies successful artifact build and upload after the metadata formatting correction. The physical-device runtime PASS for the previous artifact is separately recorded in `ONE_PROMPT3_E3_ANDROID_DEVICE_RUNTIME_PASS_20261025.md`. Do not infer that the newly uploaded artifact was run on the device merely because the build/upload workflow succeeded; if a byte-for-byte device runtime proof is required for the new artifact, download artifact ID `12597305565`, verify its binary SHA-256, and execute it on the Android device again.

E4 / SEC-05 remains open. The overall milestone is not GREEN LOCKED.
