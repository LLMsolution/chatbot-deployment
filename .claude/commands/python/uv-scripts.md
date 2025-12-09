---
description: Manage UV scripts and commands in pyproject.toml
argument-hint: [--list] [--add script-name] [--organize]
---

# UV Scripts Management

**Action:** $ARGUMENTS

## Script Configuration

### 1. Current Scripts Analysis

Check pyproject.toml for:
- Existing `[tool.uv.scripts]` section
- Script organization and naming
- Complex vs simple scripts
- Missing common scripts
- Script dependencies

### 2. UV Script Types

UV supports multiple script formats:

**Simple Command Scripts:**
```toml
[tool.uv.scripts]
# Simple shell command
format = "ruff format ."
lint = "ruff check . --fix"

# Python module execution
server = "python -m uvicorn app.main:app --reload"
worker = "python -m celery -A app.worker worker --loglevel=info"
```

**Composite Scripts (Chain Commands):**
```toml
[tool.uv.scripts]
# Run multiple commands in sequence
check = { chain = ["lint", "typecheck", "test"] }
ci = { chain = ["check", "build"] }
```

**Python Script with Dependencies:**
```toml
[tool.uv.scripts]
# Script with extra dependencies
analyze = { call = "scripts.analyze:main", with = ["pandas", "matplotlib"] }
migrate = { call = "scripts.migrate:run", with = ["alembic"] }
```

**External Scripts:**
```toml
[tool.uv.scripts]
# Run external script files
deploy = { cmd = "bash scripts/deploy.sh" }
backup = { cmd = "python scripts/backup.py" }
```

### 3. Complete Script Setup

**Organized pyproject.toml scripts:**
```toml
[tool.uv]
# Development environment settings
dev-dependencies = [
    "ipython>=8.24",
    "rich>=13.7",
]

[tool.uv.scripts]
# ===== Development =====
# Start development server
dev = "uvicorn app.main:app --reload --port 8000"
dev-worker = "watchfiles 'celery -A app.worker worker --loglevel=info' app"

# Interactive shell
shell = "ipython"
db-shell = "python -m scripts.db_shell"

# ===== Database =====
# Database migrations
db-upgrade = "alembic upgrade head"
db-downgrade = "alembic downgrade -1"
db-migrate = { call = "scripts.migrate:create_migration" }
db-reset = { chain = ["db-downgrade-all", "db-upgrade", "db-seed"] }
db-downgrade-all = "alembic downgrade base"
db-seed = "python -m scripts.seed_data"

# ===== Testing =====
# Test commands
test = "pytest -v"
test-fast = "pytest -v -m 'not slow'"
test-cov = "pytest --cov=app --cov-report=html --cov-report=term"
test-watch = "watchfiles 'pytest -v' tests app"
test-integration = "pytest tests/integration -v"
test-unit = "pytest tests/unit -v"

# ===== Code Quality =====
# Linting and formatting
format = { chain = ["format-ruff", "format-isort"] }
format-ruff = "ruff format ."
format-isort = "isort ."

lint = { chain = ["lint-ruff", "lint-mypy"] }
lint-ruff = "ruff check . --fix"
lint-mypy = "mypy app"

# Type checking
typecheck = "mypy app --show-error-codes"
typecheck-strict = "mypy app --strict"

# Security scanning
security = "bandit -r app"
security-deps = "pip-audit"

# Combined quality checks
check = { chain = ["format", "lint", "typecheck", "test"] }
check-all = { chain = ["check", "security"] }

# ===== Documentation =====
docs-serve = "mkdocs serve --dev-addr 127.0.0.1:8001"
docs-build = "mkdocs build"
docs-deploy = "mkdocs gh-deploy --force"
docs-check = "mkdocs build --strict"

# ===== Build & Deploy =====
build = "python -m build"
build-docker = "docker build -t app:latest ."

clean = { chain = ["clean-cache", "clean-dist"] }
clean-cache = "find . -type d -name __pycache__ -exec rm -r {} +"
clean-dist = "rm -rf dist build *.egg-info"

# ===== Utilities =====
# Generate requirements files
export = "uv export --format requirements-txt > requirements.txt"
export-dev = "uv export --dev --format requirements-txt > requirements-dev.txt"

# Dependency management
deps-update = "uv lock --upgrade"
deps-outdated = "uv pip list --outdated"
deps-tree = "uv pip tree"

# Environment info
info = { chain = ["version", "deps-tree"] }
version = "python --version"

# ===== CI/CD Scripts =====
ci-test = { chain = ["lint", "typecheck", "test-cov"] }
ci-build = { chain = ["ci-test", "build"] }
ci-deploy = { chain = ["ci-build", "deploy-prod"] }

# ===== Custom Scripts with Dependencies =====
[tool.uv.scripts.data-analysis]
call = "scripts.analyze:main"
with = ["pandas>=2.0", "matplotlib>=3.8", "seaborn>=0.13"]

[tool.uv.scripts.report]
call = "scripts.generate_report:run"
with = ["jinja2>=3.1", "weasyprint>=60.0"]

# ===== Complex Script Example =====
[tool.uv.scripts.release]
chain = [
    "check-all",
    "build",
    { cmd = "git tag -a v$(python -m setuptools_scm) -m 'Release version $(python -m setuptools_scm)'" },
    { cmd = "git push --tags" },
    { call = "scripts.publish:upload_to_pypi" }
]
```

### 4. Script Patterns

**Environment-Specific Scripts:**
```toml
[tool.uv.scripts]
# Development
dev-server = { cmd = "uvicorn app:app --reload", env = { "ENV": "development" } }

# Production
prod-server = { cmd = "gunicorn app:app", env = { "ENV": "production" } }
```

**Conditional Scripts:**
```toml
[tool.uv.scripts]
# Platform specific
clean-unix = { cmd = "rm -rf build dist", if = "sys_platform != 'win32'" }
clean-windows = { cmd = "rmdir /s /q build dist", if = "sys_platform == 'win32'" }
```

## Script Organization Report

### 📊 Current Scripts

**Existing Scripts:** [count]
**Categories:** [list categories found]

### 🔧 Recommended Scripts

**Missing Essential Scripts:**
```toml
[tool.uv.scripts]
# Add these commonly needed scripts
dev = "[start dev server command]"
test = "pytest"
lint = "ruff check ."
format = "ruff format ."
check = { chain = ["format", "lint", "test"] }
```

**Organization Improvements:**
- Group scripts by category with comments
- Use consistent naming (kebab-case)
- Create composite scripts for workflows
- Add descriptions in comments

### 💡 Script Best Practices

**Naming Conventions:**
- Use kebab-case: `db-migrate` not `db_migrate`
- Prefix with category: `test-unit`, `test-integration`
- Be descriptive: `dev-server` not just `dev`

**Organization:**
- Group by function (test, lint, build, deploy)
- Use chain for workflows
- Keep simple scripts simple
- Document complex scripts

**Common Patterns:**
```toml
# Development workflow
dev = "start dev server"
check = { chain = ["lint", "test"] }

# Testing variants
test = "pytest"
test-watch = "pytest-watch"
test-cov = "pytest --cov"

# Database operations
db-upgrade = "alembic upgrade head"
db-reset = { chain = ["db-down", "db-up", "db-seed"] }
```

### ✅ Script Checklist

- [ ] Essential scripts defined (dev, test, lint)
- [ ] Scripts organized by category
- [ ] Composite scripts for workflows
- [ ] Consistent naming convention
- [ ] Comments for complex scripts
- [ ] Environment-specific variants
- [ ] CI/CD scripts included
- [ ] Cleanup scripts available