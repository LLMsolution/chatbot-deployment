---
description: Analyze and reorganize dependencies into proper groups
argument-hint: [--audit] [--suggest-groups] [--fix]
---

# Dependency Group Analysis

**Action:** $ARGUMENTS

## Dependency Audit

### 1. Scan Current Dependencies

Analyze pyproject.toml for:
- Dependencies in wrong sections
- Missing dependency groups
- Test libraries in production deps
- Dev tools in main dependencies
- Optional deps that should be required

### 2. Categorize Dependencies

**Common Dependency Categories:**

**Production (Main):**
- Web frameworks (FastAPI, Flask, Django)
- Database drivers (psycopg, pymongo)
- Core business logic libraries
- API clients for external services

**Development Tools:**
- IPython, rich, devtools
- Debuggers (debugpy, pdb++)
- Code reload tools

**Testing:**
- pytest and plugins
- Test factories (factory-boy, faker)
- Mocking libraries
- Test clients (httpx for FastAPI)

**Linting & Formatting:**
- ruff, black, isort
- mypy for type checking
- bandit for security

**Documentation:**
- mkdocs, sphinx
- API documentation tools

**Type Stubs:**
- types-* packages for mypy

## Dependency Reorganization

### 📋 Current Analysis

**Misplaced Dependencies Found:**

```toml
# ❌ CURRENT (Wrong placement)
[project]
dependencies = [
    "fastapi>=0.100.0",
    "pytest>=8.0",  # Should be in test group
    "black>=24.0",  # Should be in lint group
    "requests>=2.31",
    "mypy>=1.10",  # Should be in lint group
]
```

### 🔧 Suggested Reorganization

```toml
# ✅ FIXED (Proper organization)
[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.11"

# Only production runtime dependencies
dependencies = [
    "fastapi>=0.100.0,<1.0",
    "requests>=2.31,<3.0",
]

[project.optional-dependencies]
# Features users might want
api = ["httpx>=0.27", "aiohttp>=3.9"]
cli = ["typer>=0.12", "rich>=13.7"]

[dependency-groups]
# Core development tools
dev = [
    "ipython>=8.24",
    "rich>=13.7",
    "devtools>=0.12",
]

# Testing suite
test = [
    "pytest>=8.0,<9.0",
    "pytest-cov>=5.0",
    "pytest-asyncio>=0.23",
    "pytest-xdist>=3.6",
    "httpx>=0.27",  # Test client
]

# Code quality
lint = [
    "ruff>=0.5.0",
    "black>=24.0,<25.0",
    "isort>=5.13,<6.0",
    "mypy>=1.10,<2.0",
]

# Type checking support
types = [
    "types-requests",
    "types-python-dateutil",
]
```

### 📊 Dependency Group Suggestions

Based on your dependencies, consider these groups:

**Essential Groups:**
```toml
[dependency-groups]
# Minimum recommended groups
dev = ["ipython", "rich"]
test = ["pytest", "pytest-cov"]
lint = ["ruff", "mypy"]
```

**Extended Groups:**
```toml
[dependency-groups]
# More granular organization
format = ["black", "isort", "ruff format"]
typecheck = ["mypy", "pyright"]
security = ["bandit", "pip-audit", "safety"]
docs = ["mkdocs", "mkdocs-material"]
release = ["build", "twine", "setuptools-scm"]
```

**Composite Groups:**
```toml
[dependency-groups]
# Combining groups for workflows
qa = [
    { include-group = "lint" },
    { include-group = "typecheck" },
    { include-group = "test" },
]
all = [
    { include-group = "dev" },
    { include-group = "qa" },
    { include-group = "docs" },
]
```

### 🎯 Migration Plan

**Step 1: Identify Misplaced:**
```python
# These need to move:
TO_TEST = ["pytest", "pytest-*", "faker", "factory-boy", "httpx"]
TO_LINT = ["ruff", "black", "isort", "mypy", "flake8", "pylint"]
TO_DEV = ["ipython", "ipdb", "rich", "devtools"]
TO_DOCS = ["mkdocs", "sphinx", "furo", "myst-parser"]
```

**Step 2: Create Groups:**
```bash
# Add test group
uv add --group test pytest pytest-cov

# Add lint group
uv add --group lint ruff black mypy

# Remove from main
uv remove pytest black mypy
```

**Step 3: Update Scripts:**
```toml
[tool.uv.scripts]
# Update to use groups
test = "pytest"
lint = "ruff check ."
install-dev = "uv sync --dev --group test --group lint"
```

### ⚠️ Common Mistakes

**Don't Put in Main:**
- Testing frameworks (pytest, unittest)
- Linters (ruff, flake8, pylint)
- Formatters (black, isort)
- Development servers (reload tools)
- Documentation generators

**Don't Put in Dev:**
- Test-specific tools (should be in test)
- Type stubs (should be in types)
- CI/CD tools (might need separate group)

**Do Put in Optional:**
- Features not all users need
- Heavy ML libraries
- Database-specific drivers
- Export format support

### 💡 Best Practices

**Group Sizing:**
- Keep groups focused and small
- Don't mix unrelated tools
- Consider installation time

**Version Pinning:**
```toml
# Production: Be conservative
"fastapi>=0.100.0,<1.0"

# Dev tools: More flexible
"pytest>=8.0"

# Security tools: Keep updated
"pip-audit"  # No upper bound
```

**Group Naming:**
- Use standard names (test, lint, docs)
- Be consistent across projects
- Document non-obvious groups

### ✅ Audit Checklist

- [ ] All test tools in test group
- [ ] All formatters in lint/format group
- [ ] Dev tools separated from test tools
- [ ] Optional features identified
- [ ] Type stubs in types group
- [ ] Documentation tools grouped
- [ ] Composite groups for workflows
- [ ] Version constraints appropriate
- [ ] No duplicate dependencies
- [ ] Groups documented in README