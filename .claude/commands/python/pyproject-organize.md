---
description: Organize and clean up pyproject.toml dependencies and groups
argument-hint: [--sort] [--dedupe] [--split-groups]
---

# Organize pyproject.toml

**Options:** $ARGUMENTS

## Analysis Process

### 1. Current Structure Check

Read pyproject.toml and identify:
- Duplicate dependencies across groups
- Unsorted dependency lists
- Mixed dependency types (dev in main, etc.)
- Inconsistent version specifiers
- Missing dependency groups
- Overly broad version constraints

### 2. Organization Issues

Look for these problems:

**Dependency Issues:**
- Dev tools in main dependencies
- Test tools not in test group
- Linting tools scattered
- Optional deps that should be main
- Version conflicts between groups

**Structure Issues:**
- No logical grouping
- Missing optional dependencies section
- Inconsistent formatting
- Comments and documentation missing

## Reorganized Structure

### 📋 Recommended Organization

**Clean pyproject.toml:**
```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Project description"
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }

# Core runtime dependencies only
dependencies = [
    # Web framework
    "fastapi>=0.100.0,<1.0",
    "uvicorn>=0.30.0,<1.0",

    # Database
    "sqlalchemy>=2.0,<3.0",
    "alembic>=1.13,<2.0",

    # Data validation
    "pydantic>=2.0,<3.0",
    "pydantic-settings>=2.0,<3.0",

    # Utilities
    "httpx>=0.27,<1.0",
    "python-dateutil>=2.9,<3.0",
]

[project.optional-dependencies]
# Optional features users can install
excel = [
    "openpyxl>=3.1",
    "xlsxwriter>=3.2",
]
ml = [
    "scikit-learn>=1.5",
    "numpy>=1.26",
    "pandas>=2.2",
]
redis = [
    "redis>=5.0",
    "hiredis>=2.3",
]

[dependency-groups]
# Development tools
dev = [
    "ipython>=8.24",
    "rich>=13.7",  # Better terminal output
    "devtools>=0.12",
]

# Testing tools
test = [
    "pytest>=8.2",
    "pytest-cov>=5.0",
    "pytest-xdist>=3.6",  # Parallel tests
    "pytest-asyncio>=0.23",
    "pytest-mock>=3.14",
    "httpx>=0.27",  # Test client
    "factory-boy>=3.3",  # Test fixtures
]

# Code quality tools
lint = [
    "ruff>=0.5",
    "black>=24.4",
    "isort>=5.13",
    "mypy>=1.10",
    "bandit>=1.7",  # Security linting
]

# Documentation
docs = [
    "mkdocs>=1.6",
    "mkdocs-material>=9.5",
    "mkdocstrings[python]>=0.25",
]

# Type stubs
types = [
    "types-python-dateutil>=2.9",
    "types-requests>=2.32",
]

# Combined groups for CI/CD
qa = [
    { include-group = "lint" },
    { include-group = "test" },
    { include-group = "types" },
]
all = [
    { include-group = "dev" },
    { include-group = "qa" },
    { include-group = "docs" },
]
```

### 🔧 Cleanup Actions

**1. Sort Dependencies:**
```python
# Sort alphabetically within categories
dependencies.sort()

# Or group by category with comments
# Web framework
# Database
# Utilities
```

**2. Deduplicate:**
```python
# Remove duplicates
# If httpx appears in both main and test,
# keep only in main (or test if test-only)
```

**3. Version Constraints:**
```toml
# Too broad (avoid)
"package>=1.0"

# Better (upper bound)
"package>=1.0,<2.0"

# Best (compatible release)
"package~=1.5.0"  # Allows 1.5.x
```

**4. Move Dependencies:**
```toml
# FROM main dependencies:
"pytest>=8.0",  # ❌ Wrong place

# TO test group:
test = [
    "pytest>=8.0",  # ✅ Right place
]
```

### 📊 Dependency Analysis

**Misplaced Dependencies:**
- `[package]` in main → should be in `[group]`

**Duplicates Found:**
- `[package]` appears in multiple groups

**Missing Groups:**
- Consider adding: `[suggested groups]`

**Version Issues:**
- `[package]` has no upper bound
- `[package]` versions conflict between groups

### 💡 Best Practices

**Dependency Groups:**
- `dev`: Development tools (ipython, debuggers)
- `test`: Testing framework and tools
- `lint`: Code quality and formatters
- `types`: Type stubs for mypy
- `docs`: Documentation generation
- `qa`: Combined quality assurance
- `all`: Everything for development

**Version Specifiers:**
- Use `~=` for compatible releases
- Set upper bounds for libraries
- No upper bounds for applications
- Pin exact versions in lock file only

**Organization Tips:**
- Group related dependencies with comments
- Sort alphabetically within groups
- Keep descriptions for non-obvious packages
- Use include-group for combinations

### ✅ Cleanup Checklist

- [ ] Move dev dependencies to groups
- [ ] Create logical dependency groups
- [ ] Sort dependencies alphabetically
- [ ] Add version upper bounds
- [ ] Remove duplicate entries
- [ ] Add comments for clarity
- [ ] Create combined groups (qa, all)
- [ ] Update UV lock file after changes