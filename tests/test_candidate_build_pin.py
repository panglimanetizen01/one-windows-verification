import unittest
from pathlib import Path


class CandidateBuildPinTests(unittest.TestCase):
    def test_candidate_build_pin_is_exact_and_matrix_is_separate_from_acceptance_pin(self):
        root = Path(__file__).resolve().parents[1]
        pin = (root / "CANDIDATE_BUILD_COMMIT.txt").read_text(encoding="utf-8").strip()
        workflow = (root / ".github" / "workflows" / "candidate-build-matrix.yml").read_text(encoding="utf-8")
        self.assertRegex(pin, r"^[0-9a-f]{40}$")
        self.assertIn("CANDIDATE_BUILD_COMMIT.txt", workflow)
        self.assertIn("runs-on: ubuntu-24.04", workflow)
        self.assertIn("runs-on: windows-2025", workflow)
        self.assertIn("cargo test --locked -p one-core", workflow)
        self.assertIn("ONE_WINDOWS_CLANG", workflow)
        self.assertIn("mingw-w64", workflow)
        self.assertIn("msys2/setup-msys2@ec48f7c5447b3140e2b088413ae3a55687bccb6e", workflow)


if __name__ == "__main__":
    unittest.main()
