#!/usr/bin/env python3
"""Collect exact-SHA GitHub Actions, Check Run, annotation, and artifact metadata."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"

_BILLING_BLOCK_RE = re.compile(
    r"\b(?:billing.{0,60}(?:disabled|suspended|blocked)|"
    r"spending.{0,30}limit.{0,25}(?:reached|exceeded|hit)|"
    r"(?:reached|exceeded|hit).{0,25}spending.{0,20}limit)\b",
    re.IGNORECASE,
)
_SECRET_REPLACEMENTS = (
    (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})\b"), "[REDACTED]"),
    (re.compile(r"(?i)\b(password|token|secret|api[_-]?key)\s*[:=]\s*([^\s,;]+)"), r"\1=[REDACTED]"),
)


def _safe_annotation_text(value: object, limit: int = 500) -> str:
    text = str(value or "")
    for pattern, replacement in _SECRET_REPLACEMENTS:
        text = pattern.sub(replacement, text)
    text = re.sub(
        r"-----BEGIN [^-]{0,80}PRIVATE KEY-----.*?-----END [^-]{0,80}PRIVATE KEY-----",
        "[REDACTED PRIVATE KEY]", text, flags=re.IGNORECASE | re.DOTALL,
    )
    return text[:limit]


def _billing_blocked(*values: object) -> bool:
    return any(_BILLING_BLOCK_RE.search(str(value or "")) for value in values)

SCHEMA_VERSION = "one-ci-health-evidence/2"


def _request_json(url: str, token: str) -> object:
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "one-repository-health",
    })
    with urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def _git_head(root: Path) -> str | None:
    try:
        env = os.environ.copy()
        env["GIT_PAGER"] = "cat"
        return subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=5, env=env,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _git_worktree_clean(root: Path) -> bool | None:
    try:
        env = os.environ.copy()
        env["GIT_PAGER"] = "cat"
        status = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
            check=True, capture_output=True, text=True, timeout=5, env=env,
        ).stdout
        return not status.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _paginate(request_json, url: str, token: str, key: str | None) -> list:
    items = []
    for page in range(1, 21):
        separator = "&" if "?" in url else "?"
        response = request_json(f"{url}{separator}per_page=100&page={page}", token)
        if key is None:
            page_items = response
        else:
            if not isinstance(response, dict):
                raise ValueError(f"{key} response was not an object")
            page_items = response.get(key, [])
        if not isinstance(page_items, list):
            raise ValueError(f"{key or 'annotation'} response was not a list")
        items.extend(page_items)
        if len(page_items) < 100:
            return items
    raise ValueError(f"{key or 'annotation'} pagination exceeded 20 pages; collection is incomplete")


def collect_ci_health(repo: str, source_sha: str, token: str, root: Path,
                      request_json=_request_json) -> dict:
    source_sha = source_sha.lower() if isinstance(source_sha, str) else source_sha
    checked_out_sha = _git_head(root)
    working_tree_clean = _git_worktree_clean(root)
    result = {
        "schema_version": SCHEMA_VERSION,
        "collector": "tools/collect_ci_health.py",
        "repository": repo,
        "source_sha": source_sha,
        "checked_out_sha": checked_out_sha,
        "working_tree_clean": working_tree_clean,
        "collector_status": "blocked",
        "runs": [],
        "jobs": [],
        "artifacts": [],
        "check_runs": [],
        "annotations": [],
        "correlations": [],
        "collection_errors": [],
        "limitations": [
            "GitHub API metadata only; job logs are not downloaded or interpreted.",
            "Artifact presence and digest metadata are recorded, not treated as proof of artifact correctness.",
            "Only runs whose head_sha exactly matches source_sha are included.",
            "Runs, jobs, artifacts, Check Runs, and annotations are paginated up to 2,000 records per endpoint; exceeding that cap marks collection blocked or partial, never complete.",
            "High-signal secret patterns are redacted from Check Run and annotation text.",
        ],
    }
    if not isinstance(repo, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        result["collection_errors"].append("invalid repository input; expected owner/repository")
        return result
    if not isinstance(source_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        result["collection_errors"].append("invalid source SHA input; expected 40 hexadecimal characters")
        return result
    if not token:
        result["collection_errors"].append("GITHUB_TOKEN is unavailable; live Actions evidence was not collected")
        return result
    if checked_out_sha != source_sha:
        result["collection_errors"].append(
            f"checked-out HEAD {checked_out_sha!r} does not match requested source SHA"
        )
        return result
    if working_tree_clean is not True:
        result["collection_errors"].append(
            "working tree is dirty or Git status is unavailable; exact-SHA CI evidence collection was blocked"
        )
        return result

    base = f"{API_ROOT}/repos/{repo}"
    job_collection_complete = set()
    artifact_collection_complete = set()
    try:
        runs_url = f"{base}/actions/runs?{urlencode({'head_sha': source_sha})}"
        matching = [
            run for run in _paginate(request_json, runs_url, token, "workflow_runs")
            if isinstance(run, dict) and run.get("head_sha") == source_sha
        ]
        result["runs"] = [{
            "id": run.get("id"),
            "name": run.get("name"),
            "path": run.get("path"),
            "event": run.get("event"),
            "status": run.get("status"),
            "conclusion": run.get("conclusion"),
            "run_attempt": run.get("run_attempt"),
            "head_sha": run.get("head_sha"),
            "html_url": run.get("html_url"),
        } for run in matching]
        if not matching:
            result["correlations"].append({
                "rule_id": "no-exact-sha-runs",
                "classification": "no-exact-sha-evidence",
                "evidence": "The Actions API completed but returned no workflow runs whose head_sha exactly matched source_sha.",
                "next_step": "Trigger the required workflows for this exact SHA or attach independent exact-SHA verification; an empty run list is not PASS.",
            })

        for run in matching:
            run_id = run.get("id")
            if not isinstance(run_id, int):
                result["collection_errors"].append("Actions run had no integer ID")
                continue

            try:
                jobs = _paginate(
                    request_json, f"{base}/actions/runs/{run_id}/jobs", token, "jobs"
                )
                job_collection_complete.add(run_id)
                for job in jobs:
                    if not isinstance(job, dict):
                        continue
                    steps = job.get("steps") if isinstance(job.get("steps"), list) else []
                    result["jobs"].append({
                        "run_id": run_id,
                        "run_name": run.get("name"),
                        "run_url": run.get("html_url"),
                        "name": job.get("name"),
                        "id": job.get("id"),
                        "status": job.get("status"),
                        "conclusion": job.get("conclusion"),
                        "runner_id": job.get("runner_id"),
                        "job_url": job.get("html_url"),
                        "steps": [{
                            "name": step.get("name"),
                            "number": step.get("number"),
                            "status": step.get("status"),
                            "conclusion": step.get("conclusion"),
                        } for step in steps if isinstance(step, dict)],
                    })
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
                result["collection_errors"].append(f"run {run_id}: jobs {type(exc).__name__}: {exc}")

            try:
                artifacts = _paginate(
                    request_json, f"{base}/actions/runs/{run_id}/artifacts", token, "artifacts"
                )
                artifact_collection_complete.add(run_id)
                for artifact in artifacts:
                    if isinstance(artifact, dict):
                        result["artifacts"].append({
                            "run_id": run_id,
                            "run_name": run.get("name"),
                            "name": artifact.get("name"),
                            "size_in_bytes": artifact.get("size_in_bytes"),
                            "expired": artifact.get("expired"),
                            "digest": artifact.get("digest"),
                            "created_at": artifact.get("created_at"),
                            "url": artifact.get("url"),
                        })
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
                result["collection_errors"].append(f"run {run_id}: artifacts {type(exc).__name__}: {exc}")

        # Check Runs expose annotations that can explain a job-start block even
        # when Actions reports failed jobs with no runner or visible steps.
        try:
            check_runs = _paginate(
                request_json, f"{base}/commits/{source_sha}/check-runs", token, "check_runs"
            )
        except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
            result["collection_errors"].append(f"check-runs {type(exc).__name__}: {exc}")
            check_runs = []

        for check_run in check_runs:
            if not isinstance(check_run, dict) or check_run.get("head_sha") != source_sha:
                continue
            check_run_id = check_run.get("id")
            output = check_run.get("output") if isinstance(check_run.get("output"), dict) else {}
            output_title = _safe_annotation_text(output.get("title"), 300)
            output_summary = _safe_annotation_text(output.get("summary"), 1000)
            result["check_runs"].append({
                "id": check_run_id,
                "name": _safe_annotation_text(check_run.get("name"), 200),
                "status": check_run.get("status"),
                "conclusion": check_run.get("conclusion"),
                "head_sha": source_sha,
                "html_url": check_run.get("html_url"),
                "output_title": output_title,
                "output_summary": output_summary,
            })
            raw_billing_evidence = [output.get("title"), output.get("summary"), output.get("text")]
            if isinstance(check_run_id, int):
                try:
                    annotations = _paginate(
                        request_json, f"{base}/check-runs/{check_run_id}/annotations", token, None
                    )
                    for annotation in annotations:
                        if not isinstance(annotation, dict):
                            continue
                        result["annotations"].append({
                            "check_run_id": check_run_id,
                            "check_run_name": _safe_annotation_text(check_run.get("name"), 200),
                            "annotation_level": annotation.get("annotation_level"),
                            "path": _safe_annotation_text(annotation.get("path"), 300),
                            "start_line": annotation.get("start_line"),
                            "end_line": annotation.get("end_line"),
                            "title": _safe_annotation_text(annotation.get("title"), 300),
                            "message": _safe_annotation_text(annotation.get("message"), 500),
                        })
                        raw_billing_evidence.extend([
                            annotation.get("title"), annotation.get("message"),
                            annotation.get("raw_details"),
                        ])
                except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
                    result["collection_errors"].append(
                        f"check run {check_run_id}: annotations {type(exc).__name__}: {exc}"
                    )
            if _billing_blocked(*raw_billing_evidence):
                result["correlations"].append({
                    "rule_id": "billing-spending-limit-blocked",
                    "check_run_id": check_run_id,
                    "check_run_name": _safe_annotation_text(check_run.get("name"), 200),
                    "classification": "billing-blocked",
                    "evidence": "Check Run output or annotation matched an explicit billing/spending-limit denial pattern.",
                    "next_step": "Periksa status billing dan spending limit GitHub Actions; jangan klasifikasikan job yang tidak mulai sebagai kegagalan source code.",
                })

        result["collector_status"] = "complete" if not result["collection_errors"] else "partial"

    except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
        result["collection_errors"].append(f"{type(exc).__name__}: {exc}")
        result["collector_status"] = "partial" if result["runs"] or result["jobs"] else "blocked"

    # Correlate only observable metadata. These classifications are triage hints,
    # never a root-cause claim and never evidence that a source test failed.
    jobs_by_run = {}
    artifacts_by_run = {}
    for job in result["jobs"]:
        jobs_by_run.setdefault(job["run_id"], []).append(job)
    for artifact in result["artifacts"]:
        artifacts_by_run.setdefault(artifact["run_id"], []).append(artifact)
    for run in result["runs"]:
        run_id = run["id"]
        run_jobs = jobs_by_run.get(run_id, [])
        run_artifacts = artifacts_by_run.get(run_id, [])
        failed_jobs = [job for job in run_jobs if job.get("conclusion") == "failure"]
        if run.get("conclusion") == "failure" and run_id in job_collection_complete and not run_jobs:
            result["correlations"].append({
                "rule_id": "failed-run-without-job-metadata",
                "run_id": run_id, "run_name": run.get("name"),
                "classification": "blocked-unknown",
                "evidence": "Run failed and the complete jobs endpoint returned no jobs.",
                "next_step": "Inspect the run page and Actions service/runner status; do not attribute the failure to source code.",
            })
        for job in failed_jobs:
            steps = job.get("steps") or []
            failed_steps = [step for step in steps if step.get("conclusion") == "failure"]
            if not steps or job.get("runner_id") in (None, 0):
                result["correlations"].append({
                    "rule_id": "failed-job-without-visible-steps",
                    "run_id": run_id, "job_id": job.get("id"), "job_name": job.get("name"),
                    "classification": "blocked-unknown",
                    "evidence": f"runner_id={job.get('runner_id')!r}; visible_steps={len(steps)}",
                    "next_step": "Review job logs/annotations or runner availability; no source-test failure is established.",
                })
            if failed_steps:
                result["correlations"].append({
                    "rule_id": "failed-step-needs-log-review",
                    "run_id": run_id, "job_id": job.get("id"), "job_name": job.get("name"),
                    "classification": "needs-log-review",
                    "evidence": [step.get("name") for step in failed_steps],
                    "next_step": "Inspect the failed step logs before classifying the cause.",
                })
        if run.get("status") == "completed" and run_id in artifact_collection_complete and not run_artifacts:
            result["correlations"].append({
                "rule_id": "no-artifacts-observed",
                "run_id": run_id, "run_name": run.get("name"),
                "classification": "informational-review",
                "evidence": "The complete Actions artifacts endpoint returned no artifacts for this run.",
                "next_step": "Compare with the workflow's declared artifact contract; absence alone is not a failure.",
            })

    # A specific billing/spending-limit denial is stronger than a generic
    # runner-start failure, but remains an account/CI blocker rather than a code failure.
    if not any(item.get("rule_id") == "billing-spending-limit-blocked" for item in result["correlations"]):
        for check_run in result["check_runs"]:
            if _billing_blocked(check_run.get("output_title"), check_run.get("output_summary")):
                result["correlations"].append({
                    "rule_id": "billing-spending-limit-blocked",
                    "check_run_id": check_run.get("id"),
                    "check_run_name": check_run.get("name"),
                    "classification": "billing-blocked",
                    "evidence": "Check Run output matched an explicit billing/spending-limit denial pattern.",
                    "next_step": "Periksa status billing dan spending limit GitHub Actions; jangan klasifikasikan job yang tidak mulai sebagai kegagalan source code.",
                })
                break

    return result

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    parser.add_argument("--sha", default=os.environ.get("GITHUB_SHA", ""))
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("ci-health-evidence.json"))
    args = parser.parse_args(argv)
    report = collect_ci_health(args.repo, args.sha, os.environ.get("GITHUB_TOKEN", ""), args.root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"CI evidence collection: {report['collector_status']} ({len(report['runs'])} runs, "
          f"{len(report['jobs'])} jobs, {len(report['artifacts'])} artifacts)")
    if report["collection_errors"]:
        print("; ".join(report["collection_errors"]), file=sys.stderr)
    # Collection outages are recorded as blocked evidence rather than misreported as source failures.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
