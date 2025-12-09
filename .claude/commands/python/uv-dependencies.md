---
description: Manage Python dependencies using Astral UV package manager
argument-hint: [--audit] [--update] [--sync] [--clean]
---

# UV Dependencies Management

**Action:** $ARGUMENTS

## UV Dependency Commands

### 1. Check Current State

Run these UV commands to understand dependencies:

```bash
# Show current Python version
uv python list

# Show installed packages
uv pip list

# Check for outdated packages
uv pip list --outdated

# View dependency tree
uv pip tree

# Check lock file status
uv lock --check
```

### 2. Dependency Management

**Add Dependencies:**
```bash
# Add production dependency
uv add numpy pandas

# Add with version constraint
uv add "fastapi>=0.100.0,<1.0"

# Add development dependencies
uv add --dev pytest ruff mypy

# Add to specific group
uv add --group test pytest-cov pytest-xdist

# Add optional dependencies
uv add --optional ml "torch>=2.0" scikit-learn

# Add from Git
uv add "httpx @ git+https://github.com/encode/httpx"

# Add local package as editable
uv add --editable ./local-package
```

**Update Dependencies:**
```bash
# Update all dependencies
uv sync --upgrade

# Update specific package
uv add --upgrade numpy

# Update within constraints
uv lock --upgrade-package numpy

# Update to latest patch versions
uv python upgrade
```

**Remove Dependencies:**
```bash
# Remove package
uv remove pandas

# Remove dev dependency
uv remove --dev pytest

# Remove from group
uv remove --group test pytest-cov
```

### 3. Lock File Management

**Working with uv.lock:**
```bash
# Generate/update lock file
uv lock

# Verify lock file
uv lock --check

# Sync environment with lock file
uv sync

# Sync including dev dependencies
uv sync --dev

# Sync specific groups
uv sync --group test --group docs

# Export to requirements.txt
uv export > requirements.txt

# Export with hashes
uv export --format requirements-txt --hashes > requirements.lock.txt
```

### 4. Dependency Groups

**pyproject.toml structure:**
```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "fastapi>=0.100.0",
    "pydantic>=2.0",
    "sqlalchemy>=2.0"
]

[project.optional-dependencies]
ml = ["torch>=2.0", "scikit-learn"]
excel = ["openpyxl", "xlrd"]

[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.5",
    "mypy>=1.10"
]
test = [
    "pytest-cov>=5.0",
    "pytest-xdist",
    "httpx"  # for test client
]
lint = [
    "ruff>=0.5",
    "black>=24.0",
    "isort>=5.13"
]
docs = [
    "mkdocs>=1.5",
    "mkdocs-material"
]
# Groups can include other groups
ci = [
    { include-group = "test" },
    { include-group = "lint" }
]
```

### 5. Platform-Specific Dependencies

```toml
[project]
dependencies = [
    # Linux only
    "jax; sys_platform == 'linux'",
    # Python version specific
    "tomli; python_version < '3.11'",
    # Windows specific
    "pywin32; sys_platform == 'win32'"
]
```

### 6. Security Audit

```bash
# Check for vulnerabilities (using pip-audit)
uv pip install pip-audit
pip-audit

# Or use UV with safety
uv add --dev safety
safety check
```

## Dependency Report

### 📊 Current Status

**Python Version:** [version]
**Total Dependencies:** [count]
**Lock File:** [synced/out-of-date]

### 🔒 Security Issues

Run audit to find vulnerabilities:
```bash
uv add --dev pip-audit
uv run pip-audit
```

### 📦 Updates Available

**Production:**
- [package] current → latest

**Development:**
- [package] current → latest

### 🧹 Cleanup Opportunities

**Unused Dependencies:**
- Check with: `uv pip list` vs actual imports

**Duplicate Functionality:**
- [package1] and [package2] do similar things

### 💡 UV Best Practices

**DO:**
- Always commit `uv.lock` for reproducibility
- Use dependency groups for organization
- Specify upper bounds for libraries
- Use `--dev` for development tools
- Run `uv sync` after pulling changes

**DON'T:**
- Edit `uv.lock` manually
- Use `pip` directly in UV projects
- Ignore platform-specific needs
- Mix UV with other package managers

### ✅ UV Migration Checklist

From pip/poetry/pipenv to UV:

1. [ ] Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. [ ] Initialize: `uv init` (if new) or `uv venv` (existing)
3. [ ] Convert requirements: `uv add -r requirements.txt`
4. [ ] Add dev dependencies: `uv add --dev -r requirements-dev.txt`
5. [ ] Generate lock: `uv lock`
6. [ ] Test: `uv sync && uv run pytest`
7. [ ] Update CI/CD to use UV
8. [ ] Remove old files (Pipfile, poetry.lock, etc.)

### 🚀 Common UV Workflows

**Daily Development:**
```bash
# Start work (sync environment)
uv sync --dev

# Add new package
uv add package-name

# Run with environment
uv run python script.py
uv run pytest

# Before commit
uv lock --check
```

**CI/CD Pipeline:**
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install exact dependencies
uv sync --frozen

# Run tests
uv run pytest

# Build package
uv build
```

**Production Deployment:**
```bash
# Export for Docker
uv export --format requirements-txt > requirements.txt

# Or sync directly
uv sync --frozen --no-dev
```