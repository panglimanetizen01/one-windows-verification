import json
import tempfile
import unittest
from pathlib import Path

from health_quality import QualityLedgerError, load_ledger, render_markdown, summarize


class HealthQualityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "quality.json"

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, data):
        self.path.write_text(json.dumps(data), encoding="utf-8")
        return self.path

    def test_observed_detector_shares_are_calculated_from_reviewed_records(self):
        ledger = {
            "schema_version": "one-health-quality/1",
            "adjudications": [
                {"finding_id": "OH-1", "detector_id": "markdown-links", "outcome": "true_positive", "reviewed_at": "2026-10-28", "evidence": "reproduced"},
                {"finding_id": "OH-2", "detector_id": "markdown-links", "outcome": "false_positive", "reviewed_at": "2026-10-28", "evidence": "valid reference-style link"},
                {"finding_id": "OH-3", "detector_id": "markdown-links", "outcome": "false_negative", "reviewed_at": "2026-10-28", "evidence": "missed anchor"},
            ],
            "repairs": [],
        }
        report = summarize(ledger)
        metrics = report["detector_metrics"]["markdown-links"]
        self.assertEqual(3, metrics["reviewed_records"])
        self.assertEqual(0.5, metrics["observed_false_positive_share"])
        self.assertEqual(0.5, metrics["observed_miss_share"])
        self.assertIn("not statistically representative", report["limitations"][0])

    def test_only_verified_terminal_repairs_count_toward_success_rate(self):
        ledger = {
            "schema_version": "one-health-quality/1",
            "adjudications": [],
            "repairs": [
                {"repair_id": "R1", "finding_id": "OH-1", "repair_type": "markdown-newline", "outcome": "success", "verified": True, "attempted_at": "2026-10-28", "evidence": "re-scan clean"},
                {"repair_id": "R2", "finding_id": "OH-2", "repair_type": "markdown-newline", "outcome": "failed", "verified": True, "attempted_at": "2026-10-28", "evidence": "test failed"},
                {"repair_id": "R3", "finding_id": "OH-3", "repair_type": "manual", "outcome": "success", "verified": False, "attempted_at": "2026-10-28", "evidence": "not rechecked"},
                {"repair_id": "R4", "finding_id": "OH-4", "repair_type": "manual", "outcome": "pending", "verified": False, "attempted_at": "2026-10-28", "evidence": "awaiting review"},
            ],
        }
        report = summarize(ledger)
        self.assertEqual(2, report["verified_terminal_repair_count"])
        self.assertEqual(1, report["verified_successful_repair_count"])
        self.assertEqual(0.5, report["verified_repair_success_rate"])
        self.assertEqual(1, report["unverified_terminal_repair_count"])

    def test_empty_ledger_reports_metrics_as_unavailable_not_zero_success(self):
        report = summarize({"schema_version": "one-health-quality/1", "adjudications": [], "repairs": []})
        self.assertIsNone(report["verified_repair_success_rate"])
        self.assertEqual({}, report["detector_metrics"])
        self.assertIn("not available", render_markdown(report))

    def test_duplicate_finding_adjudication_is_rejected(self):
        record = {"finding_id": "OH-1", "detector_id": "syntax", "outcome": "true_positive", "reviewed_at": "2026-10-28", "evidence": "reproduced"}
        self.write({"schema_version": "one-health-quality/1", "adjudications": [record, record], "repairs": []})
        with self.assertRaisesRegex(QualityLedgerError, "duplicate adjudication"):
            load_ledger(self.path)

    def test_unknown_schema_and_invalid_outcome_are_rejected(self):
        self.write({"schema_version": "one-health-quality/99", "adjudications": [], "repairs": []})
        with self.assertRaisesRegex(QualityLedgerError, "schema_version"):
            load_ledger(self.path)
        self.write({"schema_version": "one-health-quality/1", "adjudications": [
            {"finding_id": "OH-1", "detector_id": "syntax", "outcome": "maybe", "reviewed_at": "2026-10-28", "evidence": "unknown"}
        ], "repairs": []})
        with self.assertRaisesRegex(QualityLedgerError, "outcome"):
            load_ledger(self.path)


if __name__ == "__main__":
    unittest.main()
