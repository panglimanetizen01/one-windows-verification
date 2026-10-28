#!/usr/bin/env python3
"""Read-only repository integrity scanner for Project ONE.

It reports evidence-backed findings only. It never edits source files, changes
acceptance scores, or performs protected actions. Exit 1 only for high/critical
findings so it can be used as a conservative CI gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

SCHEMA_VERSION = "1.0"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
FENCE_RE = re.compile(r"^\s*(\x60{3,}|~{3,})")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
WORKFLOW_NAME_RE = re.compile(r"(?m)^name:\s*[\"']?(.+?)[\"']?\s*$")


def finding(detector, severity, path, line, summary, evidence, remediation):
    key = f"{detector}:{path}:{line or 0}:{summary}"
    stable_id = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
    return {
        "finding_id": f"ONE-{detector.upper()}-{stable_id}",
        "schema_version": SCHEMA_VERSION,
        "detector_id": detector,
        "severity": severity,
        "status": "open",
        "path": path,
        "line": line,
        "summary": summary,
        "evidence": evidence,
        "recommended_action": remediation,
    }


def add(findings, *args):
    findings.append(finding(*args))


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None


def markdown_checks(root, findings, root_label):
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "target", "node_modules"} for part in path.parts):
            continue
        text = read_text(path)
        rel = f"{root_label}/{path.relative_to(root)}"
        if text is None:
            add(findings, "markdown_read", "medium", rel, None,
                "Markdown file is not readable as UTF-8.", "File read failed.",
                "Inspect encoding and file permissions.")
            continue

        lines = text.splitlines()
        inside = False
        marker = None
        marker_len = 0
        visible_lines = []
        for number, line in enumerate(lines, 1):
            match = FENCE_RE.match(line)
            if match:
                token = match.group(1)
                if not inside:
                    inside, marker, marker_len = True, token[0], len(token)
                elif token[0] == marker and len(token) >= marker_len:
                    inside, marker, marker_len = False, None, 0
                visible_lines.append("")
            else:
                visible_lines.append("" if inside else line)
        if inside:
            add(findings, "markdown_fence", "high", rel, None,
                "Unclosed Markdown fenced code block.",
                "A fenced block was opened but no matching closing fence was found.",
                "Close the code fence with the matching marker.")

        for number, line in enumerate(visible_lines, 1):
            for match in MD_LINK_RE.finditer(line):
                target = match.group(1).strip().strip("<>")
                if not target or target.startswith("#"):
                    continue
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                target_path = unquote(parsed.path)
                if not target_path:
                    continue
                candidate = (path.parent / target_path).resolve()
                try:
                    candidate.relative_to(root.resolve())
                except ValueError:
                    add(findings, "markdown_path_escape", "high", rel, number,
                        f"Relative link escapes repository root: {target}",
                        f"Link at line {number} resolves outside {root_label}.",
                        "Replace the link with a repository-local path or a deliberate external URL.")
                    continue
                if not candidate.exists():
                    add(findings, "broken_local_link", "medium", rel, number,
                        f"Local Markdown link target does not exist: {target}",
                        f"Resolved target: {candidate}",
                        "Correct the target or restore the referenced file.")


def scan_workflows(source_root, findings):
    workflow_dir = source_root / ".github" / "workflows"
    if not workflow_dir.is_dir():
        add(findings, "workflow_inventory", "high", ".github/workflows", None,
            "Canonical workflow directory is missing.",
            "The source checkout has no .github/workflows directory.",
            "Restore the canonical workflow directory or correct the source checkout.")
        return

    seen = {}
    paths = sorted(workflow_dir.glob("*.yml")) + sorted(workflow_dir.glob("*.yaml"))
    for path in paths:
        text = read_text(path)
        rel = str(path.relative_to(source_root))
        if text is None:
            add(findings, "workflow_read", "high", rel, None,
                "Workflow YAML is not readable as UTF-8.", "File read failed.",
                "Inspect the file encoding and permissions.")
            continue
        match = WORKFLOW_NAME_RE.search(text)
        if match:
            name = match.group(1).strip()
            if name in seen:
                add(findings, "duplicate_workflow_name", "medium", rel, 1,
                    f"Workflow name duplicates {seen[name].relative_to(source_root)}: {name}",
                    "Two workflow files declare the same display name; run triage may be ambiguous.",
                    "Give the workflows distinct names or document why the duplicate is intentional.")
            else:
                seen[name] = path
        for number, line in enumerate(text.splitlines(), 1):
            local_action = re.search(r"\buses:\s*[\"']?(\./[^\"'\s]+)", line)
            if local_action:
                target = (source_root / local_action.group(1)).resolve()
                if not target.exists():
                    add(findings, "broken_local_action", "high", rel, number,
                        f"Workflow references missing local action: {local_action.group(1)}",
                        f"Resolved path: {target}",
                        "Correct the local action path or restore the action directory.")


def run_git_sha(root):
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, str(exc)
    if proc.returncode:
        return None, proc.stderr.strip() or f"git exited {proc.returncode}"
    return proc.stdout.strip(), None


def scan(source_root, verifier_root):
    findings = []
    pin_file = verifier_root / "CANONICAL_COMMIT.txt"
    pin_text = read_text(pin_file)
    pin = pin_text.strip() if pin_text else ""
    if not SHA_RE.fullmatch(pin):
        add(findings, "invalid_source_pin", "critical", "CANONICAL_COMMIT.txt", None,
            "Canonical source pin is not exactly 40 lowercase hexadecimal characters.",
            f"Observed pin: {pin!r}",
            "Update the pin from the intended canonical source commit after review.")

    actual_sha, git_error = run_git_sha(source_root)
    if git_error:
        add(findings, "source_checkout_identity", "critical", "one-source", None,
            "Unable to establish the canonical source checkout SHA.", git_error,
            "Ensure the source checkout exists and Git metadata is available.")
    elif pin and SHA_RE.fullmatch(pin) and actual_sha != pin:
        add(findings, "source_pin_mismatch", "critical", "CANONICAL_COMMIT.txt", None,
            "Pinned source SHA does not match the checked-out source SHA.",
            f"pin={pin}; checkout={actual_sha}",
            "Check out the exact pinned SHA or deliberately update the pin and rerun required evidence.")

    required = [
        "docs/verification/README.md",
        "docs/verification/DEFINITION_OF_DONE.md",
        "docs/verification/one-completion-ledger.md",
        ".github/workflows",
    ]
    for item in required:
        if not (source_root / item).exists():
            add(findings, "required_path_missing", "high", item, None,
                f"Required canonical path is missing: {item}",
                "The read-only inventory check could not find this required path.",
                "Restore the path or update the normative verification contract after review.")

    index = read_text(verifier_root / "CANDIDATE_VERIFICATION.md")
    if index is None:
        add(findings, "evidence_index_missing", "critical", "CANDIDATE_VERIFICATION.md", None,
            "Independent evidence index is missing or unreadable.",
            "The scanner cannot compare the current candidate heading with the canonical pin.",
            "Restore the index and preserve its historical evidence.")
    else:
        first_lines = "\n".join(index.splitlines()[:20])
        pattern = re.compile(
            r"(?i)(?:source SHA under verification|canonical source SHA under verification|current candidate SHA)[^\n\x60]*\x60([0-9a-f]{40})\x60"
        )
        sha_mentions = pattern.findall(first_lines)
        if sha_mentions and any(value != pin for value in sha_mentions):
            add(findings, "evidence_index_pin_drift", "high", "CANDIDATE_VERIFICATION.md", None,
                "Current evidence-index header disagrees with CANONICAL_COMMIT.txt.",
                f"pin={pin}; current header SHA(s)={sorted(set(sha_mentions))}",
                "Reconcile the current header and pin; keep old SHAs only in clearly historical sections.")

    scan_workflows(source_root, findings)
    markdown_checks(source_root, findings, "source")
    markdown_checks(verifier_root, findings, "verifier")

    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    findings.sort(key=lambda item: (severity_order.get(item["severity"], 5), item["detector_id"], item["path"], item["line"] or 0))
    counts = {level: sum(1 for item in findings if item["severity"] == level)
              for level in ("critical", "high", "medium", "low", "info")}
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "canonical_source": {"pinned_sha": pin or None, "checked_out_sha": actual_sha,
                             "source_root": str(source_root)},
        "verifier_root": str(verifier_root),
        "summary": {"finding_count": len(findings), "by_severity": counts,
                    "gate": "FAIL" if counts["critical"] or counts["high"] else "PASS"},
        "findings": findings,
    }


def write_reports(report, json_path, markdown_path):
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = report["summary"]
    lines = [
        "# Repository Health Scan", "",
        f"- Gate: **{summary['gate']}**",
        f"- Generated: {report['generated_at']}",
        f"- Pinned source SHA: {report['canonical_source']['pinned_sha']}",
        f"- Checked-out source SHA: {report['canonical_source']['checked_out_sha']}",
        f"- Findings: {summary['finding_count']}",
        f"- Severity counts: {json.dumps(summary['by_severity'], sort_keys=True)}", "",
        "This scan is read-only. Findings are observations, not proof of root cause. No files, ledger scores, branch protections, or release settings were modified.", "",
    ]
    if not report["findings"]:
        lines += ["No findings detected by the currently implemented detectors.", ""]
    else:
        for item in report["findings"]:
            location = item["path"] + (f":{item['line']}" if item["line"] else "")
            lines += [
                f"## {item['finding_id']} — {item['severity'].upper()}", "",
                f"**Detector:** {item['detector_id']}  ",
                f"**Location:** {location}  ",
                f"**Finding:** {item['summary']}", "",
                f"**Evidence:** {item['evidence']}", "",
                f"**Recommended action:** {item['recommended_action']}", "",
            ]
    markdown_path.write_text("\n".join(lines), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--verifier-root", type=Path, default=Path("."))
    parser.add_argument("--json-out", type=Path, default=Path("health-report.json"))
    parser.add_argument("--markdown-out", type=Path, default=Path("health-report.md"))
    args = parser.parse_args(argv)
    report = scan(args.source_root.resolve(), args.verifier_root.resolve())
    write_reports(report, args.json_out.resolve(), args.markdown_out.resolve())
    print(json.dumps(report["summary"], sort_keys=True))
    return 1 if report["summary"]["gate"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
