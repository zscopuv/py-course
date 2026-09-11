# Contributing to Python Course

Thank you for improving the course. Contributions can correct lesson content,
add clearer examples, or improve exercises and project materials.

## Before opening an issue

- Search existing issues to avoid duplicates.
- Include the lesson filename, section heading, and a concise description of
the problem.
- For code examples, include the Python version and the complete error output.

## Pull requests

1. Create a focused branch from the default branch.
2. Keep each pull request limited to one concern, such as a lesson correction
   or a content-check improvement.
3. Preserve the existing lesson format: introduction, examples, notes, and
   practice exercises.
4. Use inclusive, beginner-friendly language and explain any new terminology.
5. Run the content checks before submitting:

   ```bash
   python scripts/check_content.py
   ```

6. In the pull request description, state what changed, why it changed, and
   how you verified it.

## Lesson examples

- Mark a code block as `python` only when it is valid Python syntax.
- Keep runnable examples self-contained whenever practical.
- Use relative links for repository files and verify that each target exists.
- Do not commit secrets, personal data, or generated environment files.

By contributing, you agree that your contributions are licensed under the
[MIT License](LICENSE).
