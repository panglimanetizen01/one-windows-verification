# Project ONE independent Windows exact-SHA verification


## Current exact-SHA Windows verification — PASS — 2026-11-17

**PASS** Exact source checkout, Windows native build, PE inspection, runtime execution, and evidence upload all succeeded.

- Canonical ONE source SHA: `a10a69afdf8675e703f38f1620abc935d8361897` (PR #102 lockfile candidate).
- Verifier workflow run #32: [Windows native runtime — Windows Server 2025](https://github.com/panglimanetizen01/one-windows-verification/actions/runs/43999096244).
- Verifier commit: `566a2edf7a30638d99a146e283c294b6bf707f2e`; job ID: `133758391930`.
- Exact source SHA assertion passed; Rust toolchain and MinGW clang/linker setup passed.
- Native Windows artifact built successfully and inspected as PE32+ AMD64.
- Runtime exit code: `0`; output: `Budi`.
- Executable SHA-256: `6ee176da3d9989a58c7dc1cb6280ee65c6973c858d266e298bbb42e87e9961be`.
- Uploaded artifact ID: `14290758793`; artifact ZIP SHA-256: `2fdc0f4ca7f76946cf71025608350f5cd7c38f02ccf97facd25d7f88fae83bc6`; size: 15,775 bytes.
- The artifact is retained by GitHub Actions until 2027-02-15.

The earlier run #31 on source SHA `e50748a...` remains a blocked attempt caused by the absent Cargo.lock. It is not relabeled; run #32 is the successful follow-up on the lockfile-bearing source SHA `a10a69...`.

Verifier PR #42 remains OPEN / DRAFT / UNMERGED. No merge or release is authorized.



## Latest PR #95 candidate — Windows verification PENDING — 2026-11-17

- Canonical ONE source SHA pinned for the next independent run: `dd9960ff52d005c4c5bf02bc11fc3c8ef8482ab9` (latest PR #95 documentation-only descendant; underlying code/config candidate `c71d81a...` has CircleCI FAILURE).
- The candidate includes a committed workspace `Cargo.lock` and matching target-specific `libc` / `windows-sys` dependencies. The independent Windows verifier must validate this exact SHA; run #32 remains historical PASS for `a10a69afdf8675e703f38f1620abc935d8361897` only.
- No Windows run for `dd9960f...` has been observed yet. The prior code/config candidate `c71d81a...` also has no Windows run. The PR's updated workflow defines `workflow_dispatch`, but the available GitHub integration in this session does not expose a workflow-dispatch action. Do not merge PR #42 merely to trigger verification; keep the result PENDING until a manual dispatch or eligible trigger runs the exact pin.
- Required result: exact source SHA assertion, Windows Server 2025 AMD64 build, PE32+ inspection, native execution, manifest and artifact hash verification. No PASS is claimed for this candidate.


### PR #95 Ubuntu APT mirror mitigation pin — 2026-11-17

- Canonical source SHA pinned: `23bb9ef79df129edaa848aa3388d8dbe39309fa2` (PR #95 current HEAD).
- The source includes the targeted CircleCI APT mirror mitigation: replace the stale regional GCE archive hostname with `archive.ubuntu.com`, clean/update APT indexes, and retain the required MinGW package set.
- The triggering failure was a CircleCI provisioning step with multiple MinGW package HTTP 404 responses from `us-east1.gce.archive.ubuntu.com`; source/config mitigation is not yet validated by a terminal CircleCI run.
- This pin update does not itself establish a Windows run. Record an independent Windows result only after a run reports this exact source SHA; prior run #32 remains tied to its historical SHA.


### PR #95 latest APT provisioning correction pin — 2026-11-17

- Canonical source pin advanced to `4db76fbaf651dd069c7000fb46a4dea61b11fbd8` (PR #95 latest HEAD at pin update).
- This source includes the Ubuntu regional APT mirror fallback and the follow-up shell-quoting correction to the `find` expression used to rewrite APT source entries.
- CircleCI exact-SHA status was not yet available at pin time; no Linux PASS is claimed. No independent Windows run for this source SHA is yet observed.


### PR #95 APT rerun checkpoint pin — 2026-11-17

- Canonical source SHA advanced to `9b233dfe75da8c0752c203af3711bf3da319dc02`, a documentation-only descendant of the APT shell-correction source `4db76fb...`.
- CircleCI for `4db76fb...` is pending at workflow `d436555e-6a03-4167-a844-acc2ac5e50d6`, job `b8478a26-15f6-457c-b8e4-f30e461e17e9`; no terminal result yet. The documentation-only descendant has no status reported at pin time.
- The verifier is pinned for a fresh exact-source check. No Windows run for `9b233df...` is claimed until a terminal run reports that SHA.


### Latest CircleCI-verified PR #95 source — Windows verification PENDING — 2026-11-17

- Canonical ONE source SHA: `cef1f41c97585b6e25bf91af6e8b4281efe299c4`.
- This exact PR #95 HEAD has CircleCI context `ci/circleci: one-linux` SUCCESS (workflow `930378d8-49bb-416e-a42c-63e1797b991c`, job `0e2642b0-bd94-4892-baca-df5b6c8fa4ed`).
- The verifier pin file has been advanced to this exact SHA in verifier commit `f5113c084fa978f275bc8426a4ca1e4d74376549`.
- No Windows run for this exact source SHA is observed. Historical run #32 remains PASS only for source `a10a69afdf8675e703f38f1620abc935d8361897`; it must not be reused for `cef1f41...`.
- The verifier workflow's eligible push trigger watches `WINDOWS_SOURCE_COMMIT.txt` on branch `verification`, or can be manually dispatched. This PR branch is `verify/windows-pr95-20261114`; updating its pin does not trigger the base-branch workflow. The currently available GitHub integration exposes no workflow-dispatch action. Do not merge PR #42 or modify the verifier base branch just to trigger a run.
- Required Windows result remains NOT VERIFIED until an authorized exact-SHA workflow run completes and its native artifact/manifest/checksum are inspected. PR #42 remains OPEN / DRAFT / UNMERGED; no merge or release.


### Latest PR #95 source after documentation synchronization — 2026-11-17

- Canonical ONE source pin: `5ba239ac3964dc147d1568dac2b819459f31b463` (PR #95 current head at this update).
- This is a documentation-only descendant of `cef1f41c97585b6e25bf91af6e8b4281efe299c4`; the prior CircleCI terminal SUCCESS is bound only to `cef1f41...`. Check the combined status for the new SHA separately; do not transfer the prior status automatically.
- The pin file was advanced in this verifier branch. Updating the PR branch does not trigger the base `verification` branch workflow. No exact-SHA Windows run is claimed.
- Windows verification remains NOT VERIFIED. Historical run #32 remains PASS only for `a10a69afdf8675e703f38f1620abc935d8361897`.
- The base workflow's push trigger and the PR workflow-dispatch path cannot be invoked through the current connected GitHub actions. No merge or base-branch mutation was performed to trigger it.


### Locked dependency verification update — 2026-11-17

- PR #95 source pin advanced to `d42689718870236694f6cab841f8b7be1afccfcc` after adding explicit `--locked` to all Cargo commands in both offline verification scripts and enforcing this contract in `tools/check_contract.py`.
- Independent Windows verifier workflow commit `19188f888ba5e2c7d65f8e06069ba1b65bbb1917` now applies `--locked` to all Cargo build, Clippy, test, real-network, and native-backend build commands.
- The PR #95 candidate's CircleCI status must be checked on the final exact source SHA; prior SUCCESS/PENDING statuses are not transferred.
- No Windows run is observed for `d426897...`; status NOT VERIFIED until a matching exact-SHA workflow run and artifact/manifest inspection complete.
