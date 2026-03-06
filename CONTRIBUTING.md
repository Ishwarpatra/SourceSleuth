# Contributing to SourceSleuth

First off, thank you for considering contributing to SourceSleuth! It's people like you that make open-source educational tools possible. 

Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

## Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to the project maintainers.

## How to Contribute

### Reporting Bugs
If you find a bug, please open an issue using the "Bug Report" template. Include:
* Your operating system and Python version.
* The exact steps to reproduce the issue.
* Any relevant error logs or tracebacks.

### Suggesting Enhancements
Have an idea for a new feature (like integrating a new embedding model or adding OCR support)? Open an issue using the "Feature Request" template. Explain the problem your feature solves and propose a potential solution.

### First Contribution Guide
If you are new to the project, look for issues labeled `good first issue` or `help wanted`. These are specifically curated to be approachable. If you want to work on one, simply comment "I'd like to work on this!" and we will assign it to you.

## Development Setup
To set up your local development environment:

1. Fork the repository and clone your fork locally.
2. Ensure you have Python 3.10+ installed.
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install development dependencies: `pip install -r requirements-dev.txt`

## Coding Standards
* **Formatting:** We use `black` for code formatting. Run `black .` before committing.
* **Linting:** We use `flake8`. Ensure your code passes by running `flake8 src/`.
* **Typing:** Use Python type hints for all function arguments and return types.

## Branch Naming Conventions
Please use the following conventions when creating a branch:
* `feature/your-feature-name` for new features.
* `bugfix/issue-description` for bug fixes.
* `docs/update-description` for documentation updates.

## Commit Message Format
We follow [Conventional Commits](https://www.conventionalcommits.org/). This helps us auto-generate changelogs.
* `feat: added PyPDF2 extraction logic`
* `fix: resolved tensor shape mismatch in embeddings`
* `docs: updated architecture diagram in README`

## Pull Request Process
1. Push your branch to your fork.
2. Open a Pull Request against the `main` branch of the upstream repository.
3. Ensure all CI/CD checks (linting, tests) pass.
4. A maintainer will review your code. We look for clean architecture, test coverage for new logic, and updated documentation.
5. Once approved, the maintainer will merge your PR.