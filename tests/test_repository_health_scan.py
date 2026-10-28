import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import repository_health_scan as scanner


class RepositoryHealthScannerTests(unittest.TestCase):
    def test_balanced_markdown_and_existing_relative_link_are_clean(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            fence = chr(96) * 3
            doc = "# Readme\n\n[Target](target.md)\n\n" + fence + "text\n[not a link](missing.md)\n" + fence + "\n"
            (root / "README.md").write_text(doc, encoding="utf-8")
            findings = []
            scanner.markdown_checks(root, findings, "fixture")
            self.assertEqual([], findings)

    def test_missing_local_link_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[missing](does-not-exist.md)\n", encoding="utf-8")
            findings = []
            scanner.markdown_checks(root, findings, "fixture")
            self.assertEqual(1, len(findings))
            self.assertEqual("broken_local_link", findings[0]["detector_id"])
            self.assertEqual("medium", findings[0]["severity"])

    def test_unclosed_fence_is_high_severity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Title\n\n" + chr(96) * 3 + "python\nprint('x')\n", encoding="utf-8")
            findings = []
            scanner.markdown_checks(root, findings, "fixture")
            self.assertTrue(any(x["detector_id"] == "markdown_fence" and x["severity"] == "high" for x in findings))

    def test_duplicate_workflow_names_and_missing_local_action_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wf = root / ".github" / "workflows"
            wf.mkdir(parents=True)
            (wf / "one.yml").write_text("name: Same\njobs:\n  test:\n    steps:\n      - uses: ./missing-action\n", encoding="utf-8")
            (wf / "two.yaml").write_text("name: Same\njobs: {}\n", encoding="utf-8")
            findings = []
            scanner.scan_workflows(root, findings)
            ids = {x["detector_id"] for x in findings}
            self.assertIn("duplicate_workflow_name", ids)
            self.assertIn("broken_local_action", ids)

    def test_pin_mismatch_is_critical_and_fails_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "source"
            verifier = base / "verifier"
            source.mkdir()
            verifier.mkdir()
            (source / ".github" / "workflows").mkdir(parents=True)
            (source / "docs" / "verification").mkdir(parents=True)
            (verifier / "CANONICAL_COMMIT.txt").write_text("a" * 40 + "\n", encoding="utf-8")
            tick = chr(96)
            (verifier / "CANDIDATE_VERIFICATION.md").write_text(
                "Canonical source SHA under verification: " + tick + "a" * 40 + tick + "\n", encoding="utf-8")
            for name in ("README.md", "DEFINITION_OF_DONE.md", "one-completion-ledger.md"):
                (source / "docs" / "verification" / name).write_text("# Fixture\n", encoding="utf-8")
            (source / ".github" / "workflows" / "ci.yml").write_text("name: CI\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=source, check=True)
            subprocess.run(["git", "config", "user.email", "health-scan@example.invalid"], cwd=source, check=True)
            subprocess.run(["git", "config", "user.name", "Health Scan Test"], cwd=source, check=True)
            subprocess.run(["git", "add", "."], cwd=source, check=True)
            subprocess.run(["git", "commit", "-qm", "fixture"], cwd=source, check=True)
            report = scanner.scan(source, verifier)
            self.assertEqual("FAIL", report["summary"]["gate"])
            self.assertIn("source_pin_mismatch", {x["detector_id"] for x in report["findings"]})


if __name__ == "__main__":
    unittest.main()
