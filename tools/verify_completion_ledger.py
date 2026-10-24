#!/usr/bin/env python3
"""Fail-closed structural verifier for ONE's fixed-weight completion ledger.

This tool never awards points. It checks arithmetic and the required acceptance
checklist; evidence owners must supply passing, exact-source-SHA evidence before
the ledger can be marked PASS GREEN LOCKED.
"""
from __future__ import annotations

import argparse
import re
import sys
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
            weight_match = re.search(r"\b(\d+)\b", cells[1].replace("**", ""))
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
        elif re.match(r"^\|\s*\*\*TOTAL\*\*\s*\|", line):
            cells = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(cells) >= 5:
                total = {"implementation": fraction(cells[3]), "verified": fraction(cells[4]), "line": line_no}
    return rows, total, errors


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
        if row["verified"][0] != row["weight"]:
            errors.append(f"{row['id']}: verified {row['verified'][0]}/{row['weight']}; full row acceptance evidence is not recorded")
        if row["status"].upper().find("VERIFIED") < 0 and row["verified"][0] == row["weight"]:
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
    for key, value in summary.items():
        print(f"{key}: {value}")
    if errors:
        print("\nACCEPTANCE FAILURES:")
        for error in errors:
            print(f"- {error}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
