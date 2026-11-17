import unittest
from pathlib import Path
from unittest.mock import patch

from collect_ci_health import collect_ci_health


SHA = "a" * 40


class CollectorTests(unittest.TestCase):
    def test_collects_exact_sha_runs_jobs_steps_and_artifacts(self):
        calls = []

        def fake_request(url, token):
            calls.append(url)
            if "/actions/runs?" in url:
                return {"workflow_runs": [
                    {"id": 10, "name": "One CI", "path": ".github/workflows/ci.yml",
                     "event": "push", "status": "completed", "conclusion": "failure",
                     "head_sha": SHA, "html_url": "https://example.invalid/run/10"},
                    {"id": 11, "name": "Old run", "head_sha": "b" * 40},
                ]}
            if url.endswith("/runs/10/jobs?per_page=100&page=1"):
                return {"jobs": [
                    {"id": 20, "name": "test", "status": "completed", "conclusion": "failure",
                     "runner_id": 0, "html_url": "https://example.invalid/job/20", "steps": []},
                    {"id": 21, "name": "build", "status": "completed", "conclusion": "failure",
                     "runner_id": 123, "steps": [{"name": "cargo test", "number": 3,
                     "status": "completed", "conclusion": "failure"}]},
                ]}
            if url.endswith("/runs/10/artifacts?per_page=100&page=1"):
                return {"artifacts": [{"name": "report", "size_in_bytes": 42, "expired": False,
                                       "digest": "sha256:abc", "created_at": "2026-01-01"}]}
            if "/commits/" in url and "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual("complete", report["collector_status"])
        self.assertEqual([10], [run["id"] for run in report["runs"]])
        self.assertEqual(2, len(report["jobs"]))
        self.assertEqual([], report["jobs"][0]["steps"])
        self.assertEqual("failure", report["jobs"][1]["steps"][0]["conclusion"])
        self.assertEqual("report", report["artifacts"][0]["name"])
        self.assertEqual("https://example.invalid/job/20", report["jobs"][0]["job_url"])
        self.assertNotIn("logs_url", report["jobs"][0])
        self.assertEqual("one-ci-health-evidence/2", report["schema_version"])
        rules = [item["rule_id"] for item in report["correlations"]]
        self.assertIn("failed-job-without-visible-steps", rules)
        self.assertIn("failed-step-needs-log-review", rules)
        self.assertTrue(all("token" not in call for call in calls))

    def test_failed_run_without_jobs_and_missing_artifacts_are_cautious_correlations(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": [
                    {"id": 40, "name": "Runner startup failure", "status": "completed",
                     "conclusion": "failure", "head_sha": SHA}
                ]}
            if url.endswith("/runs/40/jobs?per_page=100&page=1"):
                return {"jobs": []}
            if url.endswith("/runs/40/artifacts?per_page=100&page=1"):
                return {"artifacts": []}
            if "/commits/" in url and "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        rules = {item["rule_id"]: item for item in report["correlations"]}
        self.assertEqual("blocked-unknown", rules["failed-run-without-job-metadata"]["classification"])
        self.assertEqual("informational-review", rules["no-artifacts-observed"]["classification"])
        self.assertIn("not attribute", rules["failed-run-without-job-metadata"]["next_step"])
        self.assertIn("absence alone is not a failure", rules["no-artifacts-observed"]["next_step"])

    def test_checkout_sha_mismatch_blocks_collection(self):
        report = collect_ci_health("owner/repo", SHA, "token", Path("/definitely/not/a/git/checkout"))
        self.assertEqual("blocked", report["collector_status"])
        self.assertTrue(any("does not match" in item for item in report["collection_errors"]))

    def test_missing_token_is_blocked_without_api_calls(self):
        def should_not_run(*args):
            raise AssertionError("API must not be called without token")

        report = collect_ci_health("owner/repo", SHA, "", Path("."), should_not_run)
        self.assertEqual("blocked", report["collector_status"])
        self.assertTrue(any("GITHUB_TOKEN" in item for item in report["collection_errors"]))

    def test_partial_collection_still_correlates_metadata_already_received(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": [{"id": 50, "name": "failed", "status": "completed",
                    "conclusion": "failure", "head_sha": SHA}]}
            if url.endswith("/runs/50/jobs?per_page=100&page=1"):
                return {"jobs": [{"id": 51, "name": "startup", "conclusion": "failure",
                    "runner_id": 0, "steps": []}]}
            if url.endswith("/runs/50/artifacts?per_page=100&page=1"):
                raise OSError("artifact API unavailable")
            if "/commits/" in url and "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual("partial", report["collector_status"])
        self.assertTrue(any(item["rule_id"] == "failed-job-without-visible-steps" for item in report["correlations"]))
        self.assertTrue(any("artifact API unavailable" in item for item in report["collection_errors"]))

    def test_api_error_is_recorded_as_blocked_not_source_failure(self):
        def fail_request(*args):
            raise OSError("API unavailable")

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fail_request)
        self.assertEqual("blocked", report["collector_status"])
        self.assertIn("API unavailable", report["collection_errors"][0])


    def test_collects_check_run_annotations_redacts_secrets_and_detects_billing_block(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": []}
            if f"/commits/{SHA}/check-runs?" in url:
                return {"check_runs": [{
                    "id": 77, "name": "CI startup", "status": "completed",
                    "conclusion": "failure", "head_sha": SHA,
                    "html_url": "https://example.invalid/check/77",
                    "output": {"title": "Actions job was not started", "summary":
                        "The spending limit has been reached for this account."}
                }]}
            if url.endswith("/check-runs/77/annotations?per_page=100&page=1"):
                return [{
                    "annotation_level": "failure", "path": ".github/workflows/ci.yml",
                    "start_line": 1, "end_line": 1, "title": "Billing blocked",
                    "message": "Billing disabled; token=" + "ghp_" + ("A" * 36)
                }]
            if "/commits/" in url and "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual("complete", report["collector_status"])
        self.assertEqual(77, report["check_runs"][0]["id"])
        self.assertEqual(1, len(report["annotations"]))
        self.assertNotIn("ghp_", report["annotations"][0]["message"])
        billing = [item for item in report["correlations"]
                   if item["rule_id"] == "billing-spending-limit-blocked"]
        self.assertEqual(1, len(billing))
        self.assertEqual("billing-blocked", billing[0]["classification"])
        self.assertIn("jangan", billing[0]["next_step"])

    def test_check_run_api_outage_is_partial_not_source_failure(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": []}
            if f"/commits/{SHA}/check-runs?" in url:
                raise OSError("check-run API unavailable")
            if "/commits/" in url and "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual("partial", report["collector_status"])
        self.assertTrue(any("check-run API unavailable" in item
                            for item in report["collection_errors"]))


    def test_check_runs_for_other_or_unknown_sha_are_excluded(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": []}
            if f"/commits/{SHA}/check-runs?" in url:
                return {"check_runs": [
                    {"id": 78, "name": "Other SHA", "head_sha": "b" * 40,
                     "output": {"summary": "Billing disabled"}},
                    {"id": 79, "name": "Missing SHA", "output": {"summary": "Billing disabled"}}
                ]}
            raise AssertionError("annotations must not be requested for untrusted check runs")

        with patch("collect_ci_health._git_head", return_value=SHA), patch("collect_ci_health._git_worktree_clean", return_value=True):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual([], report["check_runs"])
        self.assertFalse(any(item["rule_id"] == "billing-spending-limit-blocked"
                             for item in report["correlations"]))


if __name__ == "__main__":
    unittest.main()


    def test_dirty_worktree_blocks_collection_before_api_calls(self):
        def should_not_run(*args):
            raise AssertionError("API must not be called for a dirty checkout")

        with patch("collect_ci_health._git_head", return_value=SHA), patch(
            "collect_ci_health._git_worktree_clean", return_value=False
        ):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), should_not_run)
        self.assertEqual("blocked", report["collector_status"])
        self.assertFalse(report["working_tree_clean"])
        self.assertTrue(any("working tree is dirty" in item for item in report["collection_errors"]))

    def test_run_pagination_collects_exact_sha_runs_after_first_hundred(self):
        calls = []

        def fake_request(url, token):
            calls.append(url)
            if "/actions/runs?" in url and "page=1" in url:
                return {"workflow_runs": [
                    {"id": index, "head_sha": "b" * 40} for index in range(100)
                ]}
            if "/actions/runs?" in url and "page=2" in url:
                return {"workflow_runs": [
                    {"id": 2000, "name": "exact SHA later page", "head_sha": SHA}
                ]}
            if url.endswith("/runs/2000/jobs?per_page=100&page=1"):
                return {"jobs": []}
            if url.endswith("/runs/2000/artifacts?per_page=100&page=1"):
                return {"artifacts": []}
            if "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch(
            "collect_ci_health._git_worktree_clean", return_value=True
        ):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual([2000], [run["id"] for run in report["runs"]])
        self.assertTrue(any("page=2" in call for call in calls))
        self.assertEqual("complete", report["collector_status"])

    def test_invalid_repository_or_sha_is_rejected_before_api_call(self):
        def should_not_run(*args):
            raise AssertionError("invalid input must not reach GitHub API")

        with patch("collect_ci_health._git_head", return_value=SHA), patch(
            "collect_ci_health._git_worktree_clean", return_value=True
        ):
            bad_repo = collect_ci_health("owner/repo/extra", SHA, "token", Path("."), should_not_run)
            bad_sha = collect_ci_health("owner/repo", "z" * 40, "token", Path("."), should_not_run)
        self.assertEqual("blocked", bad_repo["collector_status"])
        self.assertEqual("blocked", bad_sha["collector_status"])


    def test_empty_exact_sha_run_list_is_not_reported_as_pass(self):
        def fake_request(url, token):
            if "/actions/runs?" in url:
                return {"workflow_runs": []}
            if "/check-runs?" in url:
                return {"check_runs": []}
            raise AssertionError(url)

        with patch("collect_ci_health._git_head", return_value=SHA), patch(
            "collect_ci_health._git_worktree_clean", return_value=True
        ):
            report = collect_ci_health("owner/repo", SHA, "token", Path("."), fake_request)
        self.assertEqual("complete", report["collector_status"])
        no_runs = [item for item in report["correlations"] if item["rule_id"] == "no-exact-sha-runs"]
        self.assertEqual(1, len(no_runs))
        self.assertEqual("no-exact-sha-evidence", no_runs[0]["classification"])
        self.assertIn("not PASS", no_runs[0]["next_step"])
