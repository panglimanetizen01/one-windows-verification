import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from verify_completion_ledger import REQUIRED_MIRROR_WORKFLOWS, verify

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
        self.assertIn("ONE Android API 35 AArch64 runtime — community ARM64 emulator fallback", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("ONE E4 adversarial filesystem and resource-bound regression", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("E4 subprocess resource guard", REQUIRED_MIRROR_WORKFLOWS)
        self.assertIn("E4 SEC-05 subprocess timeout and output-limit verification", REQUIRED_MIRROR_WORKFLOWS)

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


if __name__ == "__main__":
    unittest.main()
