# Contributing

## Development Setup

### Using Dev Container

Open in VS Code with Docker installed:

1. Install the Dev Containers extension
2. Command palette → "Reopen in Container"
3. Everything installs automatically (Python 3.11, uv, dependencies)

### Local Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

## Making Changes

1. Fork and clone the repository
2. Create a branch: `git checkout -b fix/description` or `feature/description`
3. Make your changes
4. Run checks: `uv run pre-commit run --all-files`
5. Run tests: `uv run pytest`
6. Push and open a PR

## Code Quality

Format and lint with ruff:

```bash
uv run ruff format .
uv run ruff check . --fix
```

Pre-commit hooks run automatically on commit and check:

- YAML/JSON formatting (prettier)
- Ruff formatting and linting
- Dockerfile formatting
- Tests

## Testing

```bash
uv run pytest
```

Requirements:

- 80% minimum coverage (configured in `.pytest.toml`)
- Add tests for new features
- Add regression tests for bug fixes

Tests go in `tests/`, source in `src/`.

## Commit Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

`<type>: <description>`

Common types:

- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation
- `test`: tests
- `chore`: maintenance
- `refactor`: code restructuring

Breaking changes: add `!` after type or `BREAKING CHANGE:` in footer.

Examples:
feat: add user validation
fix: handle empty input
docs: update setup instructions

## Pull Requests

PR titles must follow semantic commit format (they become the squash commit message).

CI runs on every PR:

- Tests and coverage (80% minimum)
- Ruff checks
- Pre-commit hooks
- Semantic PR title validation

PRs are squashed and merged to `main` after passing CI.
