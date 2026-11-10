import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from verify_completion_ledger import REQUIRED_ANDROID_RUNTIME_WORKFLOWS, REQUIRED_MIRROR_WORKFLOWS, evaluate_required_mirror_runs, select_required_evidence_run, verify

SHA = "2ead9dba45db4ce4105deaa81720aacc8fcadd6c"
WEIGHTS = {
    "F1": 8, "F2": 7, "F3": 5, "F4": 5, "F5": 3, "F6": 2,
    "C1": 8, "C2": 8, "C3": 6, "C4": 4, "C5": 4, "C6": 0,
    "E1": 10, "E2": 8, "E3": 8, "E4": 6, "E5": 4, "E6": 4,
}


def fixture(verified_overrides=None, unchecked=False):
    verified_overrides = verified_overrides or {}
    lines = [
        "| ID | Requirement / weight | Acceptance evidence | Current implementation points | Current verified points | Status |",
        "|---|---|---|---:|---:|---|",
    ]
    impl_total = verified_total = 0
    for row_id, weight in WEIGHTS.items():
        verified = verified_overrides.get(row_id, weight)
        impl_total += weight
        verified_total += verified
        status = "VERIFIED" if verified == weight else "IMPLEMENTED — PARTIAL"
        lines.append(f"| {row_id} | requirement **{weight}** | evidence | {weight}/{weight} | {verified}/{weight} | {status} |")
    lines.append(f"| **TOTAL** | | | {impl_total}/100 | {verified_total}/100 | {'PASS' if verified_total == 100 else 'NOT PASSED'} |")
    dod = "- [ ] required acceptance" if unchecked else "- [x] required acceptance"
    evidence = f"Candidate source SHA: {SHA}"
    return "\n".join(lines), dod, evidence


class LedgerGateTests(unittest.TestCase):
    def test_required_mirror_matrix_covers_e3_runtime_and_e4_security(self):
        self.assertIn("ONE Milestone 1 E1 Cross-Platform Acceptance Lab", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("ONE E1 Standard Library Windows Acceptance", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback", REQUIRED_ANDROID_RUNTIME_WORKFLOWS)
        self.assertIn("ONE Android AArch64 runtime — native ARM64 Linux host", REQUIRED_ANDROID_RUNTIME_WORKFLOWS)
        self.assertIn("ONE E4 adversarial filesystem and resource-bound regression", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("E4 subprocess resource guard", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("E4 SEC-05 subprocess timeout and output-limit verification", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("ONE Windows Native Backend Runtime — Windows Server 2025", REQUIRED_MIRROR_WORKFLOWS)

    def test_required_windows_native_runtime_is_exact_sha_and_executes_artifact(self):
        workflow_path = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "windows-native-backend-runtime.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("name: ONE Windows Native Backend Runtime — Windows Server 2025", workflow)
        self.assertIn("CANONICAL_COMMIT.txt", workflow)
        self.assertIn("CANONICAL_READ_TOKEN", workflow)
        self.assertIn("ONE_WINDOWS_CLANG=clang", workflow)
        self.assertIn("clang --target=x86_64-w64-windows-gnu", workflow)
        self.assertIn("MinGW clang PE probe PASS.", workflow)
        self.assertIn("one-native --locked -- build --target windows-x86_64", workflow)
        self.assertIn("examples/one-windows-native.exe", workflow)
        self.assertIn("examples/hello.one one-windows-native.exe", workflow)
        self.assertNotIn("examples/hello.one examples/one-windows-native.exe", workflow)
        self.assertIn("Execute Windows native artifact", workflow)
        self.assertIn("runtime_exit_code=$exitCode", workflow)
        self.assertIn("if ($exitCode -ne 0)", workflow)
        self.assertIn("one-windows-native-runtime-manifest.txt", workflow)
        self.assertNotIn("LOCAL_CI_CANONICAL_COMMIT.txt", workflow)

    def test_android_alternative_accepts_latest_success_of_either_supported_runtime(self):
        runs = [
            {
                "name": "ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback",
                "created_at": "2026-10-27T02:30:00Z",
                "status": "completed",
                "conclusion": "failure",
            },
            {
                "name": "ONE Android AArch64 runtime — native ARM64 Linux host",
                "created_at": "2026-10-27T02:29:00Z",
                "status": "completed",
                "conclusion": "success",
            },
        ]
        selected = select_required_evidence_run(runs, REQUIRED_ANDROID_RUNTIME_WORKFLOWS)
        self.assertEqual(selected["name"], "ONE Android AArch64 runtime — native ARM64 Linux host")
        self.assertEqual(selected["conclusion"], "success")

    def test_android_alternative_does_not_reuse_stale_success_for_same_workflow(self):
        runs = [
            {
                "name": "ONE Android AArch64 runtime — native ARM64 Linux host",
                "created_at": "2026-10-27T02:20:00Z",
                "status": "completed",
                "conclusion": "success",
            },
            {
                "name": "ONE Android AArch64 runtime — native ARM64 Linux host",
                "created_at": "2026-10-27T02:30:00Z",
                "status": "completed",
                "conclusion": "failure",
            },
            {
                "name": "ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback",
                "created_at": "2026-10-27T02:29:00Z",
                "status": "completed",
                "conclusion": "failure",
            },
        ]
        selected = select_required_evidence_run(runs, REQUIRED_ANDROID_RUNTIME_WORKFLOWS)
        self.assertEqual(selected["conclusion"], "failure")

    def test_full_exact_sha_acceptance_can_pass(self):
        ledger, dod, evidence = fixture()
        code, errors, summary = verify(ledger, dod, evidence, SHA)
        self.assertEqual(code, 0, errors)
        self.assertEqual(summary["verified_points"], 100)
        self.assertEqual(summary["gate"], "PASS GREEN LOCKED — FINAL RELEASE")

    def test_unverified_row_cannot_be_promoted_by_total(self):
        ledger, dod, evidence = fixture({"E1": 0})
        code, errors, summary = verify(ledger, dod, evidence, SHA)
        self.assertEqual(code, 1)
        self.assertEqual(summary["verified_points"], 90)
        self.assertTrue(any("E1" in error for error in errors))

    def test_unchecked_definition_of_done_blocks_pass(self):
        ledger, dod, evidence = fixture(unchecked=True)
        code, errors, _ = verify(ledger, dod, evidence, SHA)
        self.assertEqual(code, 1)
        self.assertTrue(any("unchecked" in error for error in errors))

    def test_missing_exact_source_sha_blocks_pass(self):
        ledger, dod, _ = fixture()
        code, errors, _ = verify(ledger, dod, "stale SHA only", SHA)
        self.assertEqual(code, 1)
        self.assertTrue(any("exact source SHA" in error for error in errors))



    def _exact_sha_matrix_runs(self):
        runs = []
        for index, name in enumerate(sorted(REQUIRED_MIRROR_WORKFLOWS)):
            runs.append({
                "name": name,
                "head_sha": "mirror-commit",
                "created_at": f"2026-11-11T00:{index:02d}:00Z",
                "status": "completed",
                "conclusion": "success",
            })
        runs.append({
            "name": "ONE Android AArch64 runtime — native ARM64 Linux host",
            "head_sha": "mirror-commit",
            "created_at": "2026-11-11T00:20:00Z",
            "status": "completed",
            "conclusion": "success",
        })
        return runs

    def test_live_matrix_waits_for_in_progress_required_workflow(self):
        runs = self._exact_sha_matrix_runs()
        target = next(run for run in runs if run["name"] == "E4 subprocess resource guard")
        target["status"] = "in_progress"
        target["conclusion"] = None
        errors, pending = evaluate_required_mirror_runs(SHA, runs, lambda _mirror_sha: SHA)
        self.assertEqual([], errors)
        self.assertTrue(any("E4 subprocess resource guard" in item for item in pending))

    def test_live_matrix_terminal_failure_is_failure_not_pending(self):
        runs = self._exact_sha_matrix_runs()
        target = next(run for run in runs if run["name"] == "E4 subprocess resource guard")
        target["conclusion"] = "failure"
        errors, pending = evaluate_required_mirror_runs(SHA, runs, lambda _mirror_sha: SHA)
        self.assertTrue(any("E4 subprocess resource guard" in item for item in errors))
        self.assertEqual([], pending)

    def test_android_success_alternative_satisfies_group_while_other_alternative_runs(self):
        runs = self._exact_sha_matrix_runs()
        runs.append({
            "name": "ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback",
            "head_sha": "mirror-commit",
            "created_at": "2026-11-11T00:21:00Z",
            "status": "in_progress",
            "conclusion": None,
        })
        errors, pending = evaluate_required_mirror_runs(SHA, runs, lambda _mirror_sha: SHA)
        self.assertFalse(any("Android API 35 AArch64 runtime" in item for item in pending))
        self.assertFalse(any("Android API 35 AArch64 runtime" in item for item in errors))

    def test_required_cross_platform_workflow_is_restored_and_uses_canonical_pin(self):
        self.assertIn("One Cross-Platform Verification", REQUIRED_MIRROR_WORKFLOWS)
        workflow_path = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "one-cross-platform-verification.yml"
        workflow = workflow_path.read_text(encoding="utf-8")
        self.assertIn("name: One Cross-Platform Verification", workflow)
        self.assertIn("CANONICAL_COMMIT.txt", workflow)
        self.assertNotIn("LOCAL_CI_CANONICAL_COMMIT.txt", workflow)
        self.assertIn("tools/check_user_docs.py", workflow)
        self.assertIn("tools/check_user_docs_test.py", workflow)
        self.assertIn("tools/verify_offline.sh", workflow)
        self.assertIn("verify_offline.ps1", workflow)
        self.assertIn("cancel-in-progress: false", workflow)



class WorkflowActionPinTests(unittest.TestCase):
    def test_all_external_workflow_actions_are_pinned_to_full_commit_sha(self):
        root = Path(__file__).resolve().parents[1]
        workflow_dir = root / ".github" / "workflows"
        uses_pattern = re.compile(r"^\\s*uses:\\s*([^\\s#]+)", re.MULTILINE)
        failures = []
        for workflow_path in sorted(workflow_dir.glob("*.yml")):
            content = workflow_path.read_text(encoding="utf-8")
            for action_ref in uses_pattern.findall(content):
                if action_ref.startswith("./"):
                    continue
                if not re.fullmatch(r"[^@]+@[0-9a-f]{40}", action_ref):
                    failures.append(f"{workflow_path.relative_to(root)}: {action_ref}")
        self.assertEqual([], failures, "Every external GitHub Action must be pinned to a full immutable commit SHA.")

if __name__ == "__main__":
    unittest.main()
