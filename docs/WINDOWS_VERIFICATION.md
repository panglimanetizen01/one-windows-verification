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


### Verifier lockfile guard — 2026-11-17

- Added a workflow self-check that scans every Cargo `build`, `clippy`, `test`, and `run` command in `.github/workflows/windows-native-backend-runtime.yml` and fails if any command omits `--locked`.
- Guard implementation and regex correction are in commits `2ee373263c434340143005ad2061884e818f0005` and `ff3511d005ffd40036162dbcc1b0744c83a22289` respectively.
- The workflow and offline source scripts now explicitly use the tracked `Cargo.lock`. This change has not yet been executed by the Windows workflow; it is a pending verification improvement, not a PASS claim.
- Canonical source pin remains `d42689718870236694f6cab841f8b7be1afccfcc`. No exact-SHA Windows run is observed.


### Latest documented PR #95 source pin — 2026-11-17

- Canonical ONE source SHA: `c207fb15bc19889a8c8e60923581ef1b1f7a6374` (documentation-only descendant of the CircleCI-verified locked-offline candidate `d426897...`).
- CircleCI terminal SUCCESS is recorded for `d426897...` only. The new docs-only source SHA must be checked independently; no status is transferred automatically.
- Pin file updated to `c207fb...` in verifier commit `8db417749753009ad5dbc69f8b4d2bb00c5d1642`. The current verifier workflow applies `--locked` to every Cargo command and self-checks that invariant.
- No Windows workflow run is observed for `c207fb...`; Windows status remains NOT VERIFIED. Historical run #32 applies only to `a10a69...`.


### Re-pin after recording terminal run #34 evidence — 2026-11-17

- Previous canonical source `c207fb15bc19889a8c8e60923581ef1b1f7a6374` passed CircleCI Linux and independent Windows run #34. Windows evidence: run `44030597595`, verifier `3f8e9b662805a89fd5145e8691a221218b098e11`, job `133861337521`, artifact `14305081962`, ZIP SHA-256 `7cbbf251efe2f56ba24965a76cd420ccddae8e84e8f0dcd727b09943014f3b8f`, executable SHA-256 `0c79f06f37f793061884acf43c9ba419bb0fc4ccf48c4a487f511e462cf55af5`, manifest SHA-256 `7ac05a71f1f5e5149f1dd721d2ca9c610bfe7504acb6b164938a51255c60b1d6`. Runtime exit 0 / `Budi`.
- PR #95 received a documentation-only evidence commit `048f87f5e9c14fdda33c7fa7a3d6dd77f469b9d4`; new canonical source pin is updated to `048f87f5e9c14fdda33c7fa7a3d6dd77f469b9d4` for a fresh exact-SHA verification.
- The PR-branch push trigger is enabled for this branch and pin/docs paths; this update should start a new Windows run without merging or mutating base `verification`.
- Prior run #34 remains PASS only for source `c207fb...`; it is not relabeled as a run on `048f87...`.


### Latest exact-SHA run #35 evidence and next pin — 2026-11-17

- Source `048f87f5e9c14fdda33c7fa7a3d6dd77f469b9d4` passed CircleCI Linux and independent Windows run #35 / `44031205160`; verifier `62f401db17e5bc2ff3ae4c53e02cc721ed1d191e`; job `133863311567`; artifact `14304459543`.
- Run #35 artifact: ZIP SHA-256 `0238718f261ba9f9840d26eb243ce3196931f1f9927c98e438b3077f7cf1a58b`; executable SHA-256 `7d9eaa745e561bafe4203404c9d6b0601b584ff93eec46a379e5fa1d0e9afd0a`; manifest SHA-256 `eace9930574e939e94a3f5d18c75901ffe883a43852ff43c281b236ece22543e`; native exit 0 / `Budi`.
- PR #95 added a docs-only evidence commit `54bf0973f59c2705decd91a8457cf08d6bbb7f8e`. This verifier pin is advanced to `54bf0973f59c2705decd91a8457cf08d6bbb7f8e` for a fresh exact-SHA check.
- The PR-branch push trigger covers this pin/doc path. New run should start without modifying base `verification` or default `main`.
- Run #35 remains PASS only for source `048f87...`; do not transfer it to `54bf097...`.
