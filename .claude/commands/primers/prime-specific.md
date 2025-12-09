---
description: Quick context priming by reading essential project files
argument-hint: [file1] [file2] [file3...] (defaults to README and docs)
---

# Quick Project Primer

**Additional Files:** $1 $2 $3

## Project Discovery

### 1. Get Structure Overview

Check project layout: `ls -la`

If available, get tree view: `tree -L 2 -I 'node_modules|__pycache__|.git'`

### 2. Read Core Documentation

**Essential Files:**

- README.md (if exists)
- CLAUDE.md or .claude/CLAUDE.md (if exists)
- CONTRIBUTING.md (if exists)
- docs/ or documentation/ main files

**User-Specified Files:**

- Read $1 (if provided)
- Read $2 (if provided)
- Read $3 (if provided)

### 3. Identify Key Components

Based on files found, determine:

- Main entry points (main._, index._, app.\*)
- Configuration files (._rc, _.config.\*, .env.example)
- Package definitions (package.json, requirements.txt, go.mod, Cargo.toml)
- Test structure (test/, tests/, spec/, **tests**/)

### 4. Quick Analysis

From what you've read, identify:

- **Technology Stack**: Languages and frameworks used
- **Project Type**: Web app, CLI tool, library, API, etc.
- **Key Patterns**: Architecture style, code organization
- **Development Workflow**: How to run, test, and build

## Summary Report

### 📋 Project Overview

**Purpose:** [One sentence about what this project does]

**Tech Stack:** [Primary language] + [Main framework] + [Database/Storage]

**Structure:**

```
[Simplified view of important directories]
```

### 📁 Key Files

**Core Logic:** `[main file locations]`
**Configuration:** `[config file locations]`
**Entry Point:** `[where execution starts]`

### 💡 Key Insights

[2-3 important things to know about this codebase]
