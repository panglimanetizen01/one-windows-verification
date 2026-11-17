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
