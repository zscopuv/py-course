#!/usr/bin/env python3
"""Validate local Markdown links and executable Python examples in course lessons."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PYTHON_BLOCK = re.compile(r"^```python\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)


def check_links(markdown_file: Path) -> list[str]:
    """Return errors for local links that do not resolve to a file."""
    markdown_file = markdown_file.resolve()
    errors: list[str] = []
    for target in MARKDOWN_LINK.findall(markdown_file.read_text(encoding="utf-8")):
        target = target.strip().split(maxsplit=1)[0]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("#", "/")):
            continue
        destination = markdown_file.parent / unquote(parsed.path)
        if not destination.exists():
            errors.append(f"{markdown_file.relative_to(ROOT)}: missing link target: {target}")
    return errors


def check_python_blocks(markdown_file: Path) -> list[str]:
    """Return errors for Python fences that do not compile."""
    markdown_file = markdown_file.resolve()
    errors: list[str] = []
    for number, code in enumerate(PYTHON_BLOCK.findall(markdown_file.read_text(encoding="utf-8")), start=1):
        try:
            compile(code, f"{markdown_file}:{number}", "exec")
        except SyntaxError as error:
            errors.append(
                f"{markdown_file.relative_to(ROOT)}: Python block {number}, "
                f"line {error.lineno}: {error.msg}"
            )
    return errors


def main() -> int:
    markdown_files = sorted(ROOT.glob("*.md"))
    errors = [error for file in markdown_files for error in check_links(file)]
    errors.extend(error for file in markdown_files for error in check_python_blocks(file))
    if errors:
        print("Content checks failed:", *errors, sep="\n- ")
        return 1
    print(f"Content checks passed for {len(markdown_files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
