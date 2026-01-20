# uv-python-3-11-starter-template

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

A minimal, production-ready Python 3.11 development environment using
 Docker Compose and VS Code devcontainers. Eliminates "works on my
 machine" problems by providing a fully reproducible development setup
 with uv package management, pre-commit hooks, and integrated testing.

## Features

- **Fast dependency management** with
 [uv](https://github.com/astral-sh/uv) - up to 10-100x faster than pip
- **Docker Compose integration** for reproducible environments across
 all platforms
- **Pre-configured tooling**: pytest with coverage, ruff formatting,
 pre-commit hooks
- **GitHub Actions CI/CD** with automated testing and semantic releases

## Installation

**Prerequisites**:
 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  or Docker Engine with Docker Compose
Clone this repository:

```bash
git clone https://github.com/shanemcgovern/uv-python-3-11-starter-template.git
cd uv-python-3-11-starter-template
```

### Option 1: VS Code Dev Container (Recommended)

Install [VS Code](https://code.visualstudio.com/) with
 [Dev Containers extension](https://github.com/Microsoft/vscode-remote-release)
 , then:

```bash
code .
```

Click **"Reopen in Container"** or use Command Palette
 (`Cmd/Ctrl+Shift+P`) → **"Dev Containers: Reopen in Container"**

### Option 2: Docker Compose

Run the container directly with Docker Compose:

```bash
# Start the container
docker compose --file .devcontainer/compose.yml up -d

# Check container status
docker ps

# Stop the container
docker compose --file .devcontainer/compose.yml down
```

Then install dependencies:

```bash
uv sync
uv run pre-commit install
```

## Quick Start

Once the container is running:

```bash
# Run the example application
python main.py
# Output: INFO:src.stub:Don't forget to read the LICENSE file.

# Run tests with coverage
uv run pytest

# Format code
uv run ruff format .
```

## Documentation

- **[uv Documentation](https://github.com/astral-sh/uv)** -
 Fast Python package installer and resolver
- **[VS Code Dev Containers](https://tinyurl.com/5n83w6au)** -
 Container development guide
- **[Docker Compose Reference](https://docs.docker.com/compose/)** -
 Compose file specification
- **[pytest Documentation](https://docs.pytest.org/)** - Testing
 framework guide

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing
 guidelines, and contribution workflow.

## License

MIT License - see the [LICENSE](LICENSE) file for details.
