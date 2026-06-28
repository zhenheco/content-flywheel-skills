from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_skill", ROOT / "scripts" / "validate_skill.py")
validate_skill = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_skill)


class ValidateSkillTest(unittest.TestCase):
    def test_repository_skill_package_validates(self):
        self.assertEqual(validate_skill.validate(ROOT), [])

    def test_markdown_link_validation_catches_missing_local_path(self):
        with self.subTest("missing local markdown link"):
            import tempfile

            with tempfile.TemporaryDirectory() as temp_dir:
                tmp_path = Path(temp_dir)
                markdown = tmp_path / "README.md"
                markdown.write_text("[Broken](missing.md)\n", encoding="utf-8")

                errors = validate_skill.validate_local_links(tmp_path, markdown)

        self.assertEqual(errors, ["README.md links to missing local path: missing.md"])


if __name__ == "__main__":
    unittest.main()
