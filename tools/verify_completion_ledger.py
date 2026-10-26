#!/usr/bin/env python3
"""Fail-closed structural verifier for ONE's fixed-weight completion ledger.

This tool never awards points. It checks arithmetic and the required acceptance
checklist; evidence owners must supply passing, exact-source-SHA evidence before
the ledger can be marked PASS GREEN LOCKED.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROW_RE = re.compile(r"^\|\s*(F[1-6]|C[1-6]|E[1-6])\s*\|")
FRACTION_RE = re.compile(r"(\d+)\s*/\s*(\d+)")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def fraction(cell: str) -> tuple[int, int] | None:
    match = FRACTION_RE.search(cell)
    return (int(match.group(1)), int(match.group(2))) if match else None


def parse_ledger(text: str) -> tuple[list[dict], dict | None, list[str]]:
    rows = []
    total = None
    errors = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if ROW_RE.match(line):
            cells = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                errors.append(f"ledger line {line_no}: malformed weighted row")
                continue
            row_id = cells[0]
            weight_match = re.search(r"\*\*(\d+)\*\*", cells[1])
            impl = fraction(cells[3])
            verified = fraction(cells[4])
            if not weight_match or not impl or not verified:
                errors.append(f"ledger line {line_no} ({row_id}): weight/points are not parseable")
                continue
            rows.append({
                "id": row_id,
                "weight": int(weight_match.group(1)),
                "implementation": impl,
                "verified": verified,
                "status": cells[5],
                "line": line_no,
            })
        elif re.search(r"\*\*TOTAL\*\*", line):
            cells = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cells) >= 5:
                total = {"implementation": fraction(cells[3]), "verified": fraction(cells[4]), "line": line_no}
    return rows, total, errors




REQUIRED_MIRROR_WORKFLOWS = {
    "One Cross-Platform Verification",
    "ONE Linux Distro Verification",
    "ONE Focused Standard Library and Database Verification",
    "ONE Cargo Lockfile Bootstrap Evidence",
    "ONE Candidate Artifact Integrity Verification",
    # This alternate is accepted only because it installs API 35 arm64-v8a,
    # boots the guest, checks SDK/ABI/boot completion, and executes the exact-SHA ELF.
    "ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback",
    "ONE E4 adversarial filesystem and resource-bound regression",
    "E4 subprocess resource guard",
    "E4 SEC-05 subprocess timeout and output-limit verification",
}


def github_json(url: str, token: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "one-ledger-gate",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def pin_at_mirror_commit(commit_sha: str, token: str, cache: dict[str, str | None]) -> str | None:
    if commit_sha in cache:
        return cache[commit_sha]
    url = (
        "https://api.github.com/repos/panglimanetizen01/one-windows-verification/"
        f"contents/CANONICAL_COMMIT.txt?ref={commit_sha}"
    )
    try:
        payload = github_json(url, token)
        pin = base64.b64decode(payload["content"]).decode("utf-8").strip()
    except (OSError, ValueError, KeyError, urllib.error.HTTPError) as exc:
        print(f"WARNING: cannot resolve source pin for mirror commit {commit_sha}: {exc}", file=sys.stderr)
        pin = None
    cache[commit_sha] = pin
    return pin


def check_live_workflow_evidence(source_sha: str) -> list[str]:
    errors: list[str] = []
    mirror_token = os.environ.get("GITHUB_TOKEN", "")
    source_token = os.environ.get("CANONICAL_READ_TOKEN", "")
    if not mirror_token:
        return ["live evidence check requires GITHUB_TOKEN with Actions/Contents read access"]
    if not source_token:
        return ["live evidence check requires CANONICAL_READ_TOKEN with source Actions read access"]

    mirror_url = (
        "https://api.github.com/repos/panglimanetizen01/one-windows-verification/"
        "actions/runs?branch=verification&per_page=100"
    )
    try:
        mirror_runs = github_json(mirror_url, mirror_token).get("workflow_runs", [])
    except (OSError, ValueError, urllib.error.HTTPError) as exc:
        return [f"cannot query live independent workflow evidence: {exc}"]

    pin_cache: dict[str, str | None] = {}
    for workflow_name in sorted(REQUIRED_MIRROR_WORKFLOWS):
        candidates = []
        for run in mirror_runs:
            if run.get("name") != workflow_name:
                continue
            pin = pin_at_mirror_commit(run.get("head_sha", ""), mirror_token, pin_cache)
            if pin == source_sha:
                candidates.append(run)
        candidates.sort(key=lambda run: run.get("created_at", ""), reverse=True)
        if not candidates:
            errors.append(f"no independent run found for current source SHA: {workflow_name}")
            continue
        latest = candidates[0]
        if latest.get("status") != "completed" or latest.get("conclusion") != "success":
            errors.append(
                f"{workflow_name} for source SHA {source_sha} is "
                f"{latest.get('status')}/{latest.get('conclusion') or 'no conclusion'} "
                f"(run {latest.get('id')}); only completed success is accepted"
            )

    release_url = (
        "https://api.github.com/repos/panglimanetizen01/one/"
        "actions/runs?branch=milestone%2F100-ecosystem-20261023&per_page=100"
    )
    try:
        release_runs = github_json(release_url, source_token).get("workflow_runs", [])
    except urllib.error.HTTPError as exc:
        # The canonical repository is public. If a read-only source token lacks
        # Actions permission (403), retry the public read without credentials.
        # This only improves evidence visibility; it never turns missing release
        # evidence into a pass.
        if exc.code != 403:
            return errors + [f"cannot query canonical release workflow evidence: {exc}"]
        try:
            release_runs = github_json(release_url, "").get("workflow_runs", [])
        except (OSError, ValueError, urllib.error.HTTPError) as fallback_exc:
            return errors + [f"cannot query canonical release workflow evidence: CANONICAL_READ_TOKEN must have Actions: read access to the private canonical repository; unauthenticated fallback is unavailable ({fallback_exc})"]
    except (OSError, ValueError) as exc:
        return errors + [f"cannot query canonical release workflow evidence: {exc}"]

    matching_release = [
        run for run in release_runs
        if run.get("name") == "ONE Package Provenance Release"
        and run.get("head_sha") == source_sha
    ]
    matching_release.sort(key=lambda run: run.get("created_at", ""), reverse=True)
    if not matching_release:
        errors.append(
            "no protected ONE Package Provenance Release run exists for the exact source SHA; "
            "E2 cannot be accepted from unsigned candidate bundles"
        )
    elif matching_release[0].get("status") != "completed" or matching_release[0].get("conclusion") != "success":
        run = matching_release[0]
        errors.append(
            f"protected release workflow for exact source SHA is "
            f"{run.get('status')}/{run.get('conclusion') or 'no conclusion'} (run {run.get('id')})"
        )
    return errors


def verify(ledger_text: str, dod_text: str, evidence_text: str, source_sha: str) -> tuple[int, list[str], dict]:
    errors: list[str] = []
    if not SHA_RE.fullmatch(source_sha):
        errors.append("source SHA must be a full 40-character lowercase Git commit SHA")

    rows, total, parse_errors = parse_ledger(ledger_text)
    errors.extend(parse_errors)
    expected_ids = {f"{prefix}{i}" for prefix in "FCE" for i in range(1, 7)}
    actual_ids = [row["id"] for row in rows]
    if set(actual_ids) != expected_ids or len(actual_ids) != len(expected_ids):
        missing = sorted(expected_ids - set(actual_ids))
        duplicates = sorted({x for x in actual_ids if actual_ids.count(x) > 1})
        errors.append(f"ledger row set mismatch; missing={missing}, duplicates={duplicates}")

    weight_sum = sum(row["weight"] for row in rows)
    implementation_sum = sum(row["implementation"][0] for row in rows)
    verified_sum = sum(row["verified"][0] for row in rows)
    for row in rows:
        if row["weight"] != row["implementation"][1] or row["weight"] != row["verified"][1]:
            errors.append(f"{row['id']}: denominator must equal fixed row weight {row['weight']}")
        if row["implementation"][0] > row["weight"] or row["verified"][0] > row["weight"]:
            errors.append(f"{row['id']}: points exceed fixed row weight")
        if row["verified"][0] > row["implementation"][0]:
            errors.append(f"{row['id']}: verified points exceed implemented points")

    if weight_sum != 100:
        errors.append(f"fixed weights sum to {weight_sum}, expected 100")
    if total is None or total["implementation"] is None or total["verified"] is None:
        errors.append("ledger TOTAL row is missing or malformed")
    else:
        if total["implementation"][0] != implementation_sum or total["implementation"][1] != 100:
            errors.append(f"TOTAL implementation says {total['implementation']}, row sum is {implementation_sum}/100")
        if total["verified"][0] != verified_sum or total["verified"][1] != 100:
            errors.append(f"TOTAL verified says {total['verified']}, row sum is {verified_sum}/100")

    # A checked checkbox is only a declaration; the independent evidence index
    # must also name the exact source SHA, and release gates require all items.
    unchecked = re.findall(r"^- \[ \] (.+)$", dod_text, re.MULTILINE)
    if source_sha not in evidence_text:
        errors.append(f"independent evidence index does not name exact source SHA {source_sha}")
    if unchecked:
        errors.append(f"Definition of Done has {len(unchecked)} unchecked acceptance item(s)")

    for row in rows:
        if row["weight"] > 0 and row["verified"][0] != row["weight"]:
            errors.append(f"{row['id']}: verified {row['verified'][0]}/{row['weight']}; full row acceptance evidence is not recorded")
        if row["weight"] > 0 and row["status"].upper().find("VERIFIED") < 0 and row["verified"][0] == row["weight"]:
            errors.append(f"{row['id']}: full points without VERIFIED status")

    passed = not errors and verified_sum == 100 and implementation_sum == 100
    if not passed and not errors:
        errors.append("release gate requires 100/100 verified and implemented")
    summary = {
        "fixed_weight_total": weight_sum,
        "implementation_points": implementation_sum,
        "verified_points": verified_sum,
        "ledger_total": total,
        "rows_checked": len(rows),
        "unchecked_definition_of_done_items": len(unchecked),
        "source_sha": source_sha,
        "gate": "PASS GREEN LOCKED — FINAL RELEASE" if passed else "NOT PASSED",
    }
    return (0 if passed else 1), errors, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--dod", required=True, type=Path)
    parser.add_argument("--evidence-index", required=True, type=Path)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--require-live-workflows", action="store_true")
    args = parser.parse_args()
    try:
        code, errors, summary = verify(
            args.ledger.read_text(encoding="utf-8"),
            args.dod.read_text(encoding="utf-8"),
            args.evidence_index.read_text(encoding="utf-8"),
            args.source_sha,
        )
    except OSError as exc:
        print(f"ERROR: cannot read required input: {exc}", file=sys.stderr)
        return 2
    if args.require_live_workflows:
        live_errors = check_live_workflow_evidence(args.source_sha)
        errors.extend(live_errors)
        if live_errors:
            code = 1
            summary["gate"] = "NOT PASSED"
    for key, value in summary.items():
        print(f"{key}: {value}")
    if errors:
        print("\nACCEPTANCE FAILURES:")
        for error in errors:
            print(f"- {error}")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as report:
            report.write("## ONE fixed-weight completion ledger gate\n\n")
            report.write(f"- **Gate:** {summary['gate']}\n")
            report.write(f"- **Pinned source SHA:** \`{summary['source_sha']}\`\n")
            report.write(f"- **Implementation:** {summary['implementation_points']}/100\n")
            report.write(f"- **Verified:** {summary['verified_points']}/100\n")
            report.write(f"- **Fixed-weight sum:** {summary['fixed_weight_total']}/100\n")
            report.write(f"- **Unchecked Definition of Done items:** {summary['unchecked_definition_of_done_items']}\n")
            if errors:
                report.write("\n### Acceptance failures\n")
                for error in errors:
                    report.write(f"- {error}\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
