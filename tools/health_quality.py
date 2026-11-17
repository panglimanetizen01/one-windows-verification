#!/usr/bin/env python3
"""Summarize reviewed detector outcomes and guarded-repair results without changing the acceptance ledger."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCHEMA_VERSION = "one-health-quality/1"
ADJUDICATION_OUTCOMES = {"true_positive", "false_positive", "false_negative", "not_reproducible", "pending"}
REPAIR_OUTCOMES = {"success", "failed", "reverted", "pending"}


class QualityLedgerError(ValueError):
    pass


def load_ledger(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise QualityLedgerError(f"cannot read quality ledger: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION:
        raise QualityLedgerError(f"schema_version must be {SCHEMA_VERSION!r}")
    adjudications = data.get("adjudications")
    repairs = data.get("repairs")
    if not isinstance(adjudications, list) or not isinstance(repairs, list):
        raise QualityLedgerError("'adjudications' and 'repairs' must both be arrays")

    seen_adjudications = set()
    for index, item in enumerate(adjudications):
        if not isinstance(item, dict):
            raise QualityLedgerError(f"adjudications[{index}] must be an object")
        for field in ("finding_id", "detector_id", "outcome", "reviewed_at", "evidence"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise QualityLedgerError(f"adjudications[{index}].{field} must be a non-empty string")
        if item["outcome"] not in ADJUDICATION_OUTCOMES:
            raise QualityLedgerError(f"adjudications[{index}].outcome is not supported")
        if item["finding_id"] in seen_adjudications:
            raise QualityLedgerError(f"duplicate adjudication for finding_id {item['finding_id']!r}")
        seen_adjudications.add(item["finding_id"])

    seen_repairs = set()
    for index, item in enumerate(repairs):
        if not isinstance(item, dict):
            raise QualityLedgerError(f"repairs[{index}] must be an object")
        for field in ("repair_id", "finding_id", "repair_type", "outcome", "attempted_at", "evidence"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise QualityLedgerError(f"repairs[{index}].{field} must be a non-empty string")
        if item["outcome"] not in REPAIR_OUTCOMES:
            raise QualityLedgerError(f"repairs[{index}].outcome is not supported")
        if not isinstance(item.get("verified"), bool):
            raise QualityLedgerError(f"repairs[{index}].verified must be a boolean")
        if item["repair_id"] in seen_repairs:
            raise QualityLedgerError(f"duplicate repair_id {item['repair_id']!r}")
        seen_repairs.add(item["repair_id"])
    return data


def summarize(ledger: dict) -> dict:
    """Return observed sample metrics; never imply statistically representative accuracy."""
    per_detector = defaultdict(Counter)
    for item in ledger["adjudications"]:
        per_detector[item["detector_id"]][item["outcome"]] += 1

    detector_metrics = {}
    for detector, counts in sorted(per_detector.items()):
        tp, fp, fn = counts["true_positive"], counts["false_positive"], counts["false_negative"]
        classified_detections = tp + fp
        labelled_truths = tp + fn
        detector_metrics[detector] = {
            "outcome_counts": dict(sorted(counts.items())),
            "reviewed_records": sum(counts.values()),
            "observed_false_positive_share": round(fp / classified_detections, 4) if classified_detections else None,
            "observed_miss_share": round(fn / labelled_truths, 4) if labelled_truths else None,
        }

    repair_counts = Counter()
    verified_terminal = []
    for item in ledger["repairs"]:
        repair_counts[item["outcome"]] += 1
        if item["verified"] and item["outcome"] in {"success", "failed", "reverted"}:
            verified_terminal.append(item)
    verified_successes = sum(1 for item in verified_terminal if item["outcome"] == "success")
    return {
        "schema_version": SCHEMA_VERSION,
        "adjudication_count": len(ledger["adjudications"]),
        "detector_metrics": detector_metrics,
        "repair_count": len(ledger["repairs"]),
        "repair_outcome_counts": dict(sorted(repair_counts.items())),
        "verified_terminal_repair_count": len(verified_terminal),
        "verified_successful_repair_count": verified_successes,
        "verified_repair_success_rate": round(verified_successes / len(verified_terminal), 4) if verified_terminal else None,
        "unverified_terminal_repair_count": sum(
            1 for item in ledger["repairs"] if not item["verified"] and item["outcome"] in {"success", "failed", "reverted"}
        ),
        "limitations": [
            "Metrics describe only manually reviewed records; they are not statistically representative accuracy or recall estimates.",
            "A missing adjudication is unknown, not a true positive or false negative.",
            "A repair counts as successful only when outcome=success and verified=true.",
            "This report is independent of the fixed-weight acceptance ledger and cannot grant release approval.",
        ],
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# One Health Detector Quality Report", "",
        f"- Schema: {report['schema_version']}",
        f"- Adjudicated findings: {report['adjudication_count']}",
        f"- Repair attempts: {report['repair_count']}",
        f"- Verified terminal repairs: {report['verified_terminal_repair_count']}",
        f"- Verified repair success rate: {report['verified_repair_success_rate'] if report['verified_repair_success_rate'] is not None else 'not available'}", "",
        "## Detector outcomes", "",
        "| Detector | Reviewed | True positive | False positive | False negative | Observed false-positive share | Observed miss share |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for detector, item in report["detector_metrics"].items():
        counts = item["outcome_counts"]
        fp_share = item["observed_false_positive_share"]
        miss_share = item["observed_miss_share"]
        lines.append(
            f"| {detector} | {item['reviewed_records']} | {counts.get('true_positive', 0)} | "
            f"{counts.get('false_positive', 0)} | {counts.get('false_negative', 0)} | "
            f"{fp_share if fp_share is not None else 'not available'} | "
            f"{miss_share if miss_share is not None else 'not available'} |"
        )
    lines.extend(["", "## Repair outcomes", "", "| Outcome | Count |", "|---|---:|"])
    lines.extend(f"| {name} | {count} |" for name, count in report["repair_outcome_counts"].items())
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="reviewed JSON ledger conforming to one-health-quality/1")
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    args = parser.parse_args(argv)
    try:
        report = summarize(load_ledger(args.ledger))
    except QualityLedgerError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded, encoding="utf-8")
    if args.markdown_out:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(render_markdown(report), encoding="utf-8")
    if not args.json_out and not args.markdown_out:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
