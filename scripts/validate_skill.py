#!/usr/bin/env python3
"""Validate the Content Flywheel skill package.

The repository is intentionally dependency-free. This checker keeps the skill
portable by validating the Markdown package structure, local links, and example
schema shape with only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "LICENSE",
    "frameworks/core-eeat-dimensions.md",
    "frameworks/geo-techniques.md",
    "frameworks/seo-writing-checklist.md",
    "schemas/brand.example.yaml",
    "schemas/content-matrix.example.yaml",
    "schemas/weekly-plan.example.yaml",
]

REQUIRED_SKILL_FRONTMATTER = {"name", "description", "license"}
REQUIRED_SCHEMA_KEYS = {
    "schemas/brand.example.yaml": {
        "name",
        "domain",
        "tagline",
        "language",
        "site",
        "positioning",
        "authors",
        "analytics",
        "i18n",
        "publishing",
        "trust_score",
    },
    "schemas/content-matrix.example.yaml": {"pillars"},
    "schemas/weekly-plan.example.yaml": {"run_id", "window", "days"},
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    frontmatter: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def top_level_yaml_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for line in text.splitlines():
        if not line or line.startswith("#") or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def validate_local_links(root: Path, markdown_path: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(markdown_path)
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        target = raw_target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        target = unquote(target)
        if "://" in target:
            continue
        if not (markdown_path.parent / target).exists():
            errors.append(f"{markdown_path.relative_to(root)} links to missing local path: {raw_target}")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.is_file():
            errors.append(f"Missing required file: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        frontmatter = parse_frontmatter(read_text(skill_path))
        missing = REQUIRED_SKILL_FRONTMATTER - set(frontmatter)
        if missing:
            errors.append(f"SKILL.md frontmatter missing: {', '.join(sorted(missing))}")

    readme = root / "README.md"
    if readme.is_file() and "<!-- LANGS:en -->" not in read_text(readme):
        errors.append("README.md missing language manifest comment")

    i18n_files = sorted((root / "i18n").glob("README.*.md"))
    if len(i18n_files) < 16:
        errors.append("Expected at least 16 localized README files")
    for path in i18n_files:
        text = read_text(path)
        if "<!-- LANGS:" not in text:
            errors.append(f"{path.relative_to(root)} missing language manifest comment")
        if not text.lstrip().startswith("<!-- LANGS:") or "\n# " not in text:
            errors.append(f"{path.relative_to(root)} missing top-level title after language manifest")

    for rel, required_keys in REQUIRED_SCHEMA_KEYS.items():
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        if "\t" in text:
            errors.append(f"{rel} contains tab indentation")
        missing = required_keys - top_level_yaml_keys(text)
        if missing:
            errors.append(f"{rel} missing top-level keys: {', '.join(sorted(missing))}")

    for path in iter_markdown_files(root):
        errors.extend(validate_local_links(root, path))

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Content Flywheel skill package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
