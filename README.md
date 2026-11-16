# Project ONE — Independent Verification Harness


## Current exact-SHA Windows verification — PASS — 2026-11-16

Windows run [#25](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43855644611) completed terminal **SUCCESS** for canonical Project ONE PR #95 source SHA `3cd71c6637169367109cf03d88911132c17dbf8b`, exactly matching `WINDOWS_SOURCE_COMMIT.txt` and the downloaded manifest.

- Verifier PR #42 branch HEAD at trigger: `34f119fd1d21adc5378a3eb6aa1fb8b5e2abc8e0`; manifest verifier merge-ref SHA: `25a3e3e6d0f1bf9c7459ff1f7fb236b7151f083f`.
- Run ID `43855644611`; job ID `133259081382`; Windows Server 2025 / AMD64; all 32/32 steps succeeded.
- Checks included exact source/verifier identity, source contract and user documentation, workspace build, Clippy with warnings denied, full workspace tests, deterministic .oneir/.onepkg, DNS, orchestration, database, HTTP GET and CLI, real-network, offline behavior, Windows native build, PE32+ AMD64 inspection, native execution, manifest generation, and artifact upload.
- Native target `x86_64-pc-windows-gnu`; runtime exit code `0`; output `Budi`.
- Executable: `examples/one-windows-native.exe`, 52,918 bytes; SHA-256 `cef46168f391c7cd0121d9a34c33e30f7f71086f40ae186522742f7e5d76e66f`.
- PE inspection independently confirmed MZ, PE signature `PE\\0\\0`, AMD64 machine `0x8664`, and PE32+ magic `0x20B`.
- Artifact ID `14221323350`; size 15,867 bytes; GitHub digest and independently recomputed downloaded ZIP SHA-256 both `4054aaa85293ad4e37d171d01b9e762b11be52f742849b27bb24a6ffb2d3065f`. Embedded manifest SHA-256 `5897b0712c0b6d79f268babf02b318cf6456d6a4b964789c0e987934e8568e27`; manifest source/verifier identities, executable digest, exit code, and output were inspected and matched.
- This Windows PASS applies only to source SHA `3cd71c6...`; previous e92 results remain historical. CircleCI Linux on the same 3cd71c source currently reports FAILURE (failure-report ID `52c0e80f-5982-4569-8411-2957ece10d18`); its root cause remains unknown without authenticated diagnostics. A Windows PASS does not replace the Linux gate.
