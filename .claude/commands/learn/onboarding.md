---
description: Comprehensive project onboarding for new developers
argument-hint: [optional: specific area like frontend/backend/tests]
---

# Developer Onboarding

**Focus Area:** $ARGUMENTS

## Project Discovery Process

### 1. Understand Project Context

First, deeply analyze the project structure and documentation:

- Read CLAUDE.md and .claude/CLAUDE.md for project conventions
- Check README.md for setup instructions and overview
- Look for CONTRIBUTING.md or similar developer guides
- Review package.json, requirements.txt, go.mod, or similar for dependencies
- Check for architecture docs in docs/ or documentation/ folders

Explore the project structure to understand its organization.

### 2. Map Project Architecture

Think hard about the project's structure:

**Codebase Analysis:**

- Run tree command or use glob to understand directory structure
- Identify main entry points (main.py, index.js, App.tsx, etc.)
- Find where business logic lives vs utilities vs UI
- Locate configuration files and environment setup
- Identify test directories and testing approach

**Technology Stack:**

- Programming languages used
- Frameworks and major libraries
- Database and storage solutions
- API patterns (REST, GraphQL, gRPC)
- Build tools and package managers

### 3. Development Workflow

Discover how developers work on this project:

- Version control workflow (branching strategy)
- Testing requirements and coverage goals
- Code review process and standards
- CI/CD pipeline configuration
- Deployment process and environments

### 4. Quick Start Guide

Based on project analysis, determine:

- Prerequisites needed (tools, accounts, API keys)
- Environment setup steps
- How to run the project locally
- How to run tests
- How to build for production

## Required Output Format

### 🎯 Project Overview

**What This Project Does:**
_[One paragraph explaining the project's purpose and value]_

**Tech Stack:**

- **Languages:** _[List primary languages]_
- **Framework:** _[Main frameworks]_
- **Database:** _[Data storage solutions]_
- **Key Libraries:** _[Important dependencies]_
- **Testing:** _[Test framework and approach]_

### 🏗️ Architecture Map

```
Project Structure:
├── [main directories with purposes]
├── src/           - [what's in here]
├── tests/         - [testing approach]
├── docs/          - [documentation]
└── config/        - [configuration]

Key Components:
1. [Component 1] - [Purpose and location]
2. [Component 2] - [Purpose and location]
3. [Component 3] - [Purpose and location]
```

### 🚀 Getting Started

**Prerequisites:**

- [ ] _[Tool/version required]_
- [ ] _[Account or API key needed]_
- [ ] _[System dependency]_

**Setup Steps:**

1. **Clone & Install:**

   ```bash
   [Specific commands for this project]
   ```

2. **Configure Environment:**

   ```bash
   [Environment setup commands]
   ```

3. **Run Locally:**

   ```bash
   [Commands to start development]
   ```

4. **Verify Setup:**
   ```bash
   [Commands to test if working]
   ```

### 📚 Key Files to Understand

**Entry Points:**

- `[file:path]` - _[What it does and why it matters]_
- `[file:path]` - _[Purpose and connections]_

**Core Logic:**

- `[file:path]` - _[Business logic location]_
- `[file:path]` - _[Main features]_

**Configuration:**

- `[file:path]` - _[What it configures]_
- `[file:path]` - _[Environment settings]_

### 🔄 Development Workflow

**Making Changes:**

1. Branch naming: `[convention discovered]`
2. Commit format: `[convention found]`
3. Testing before commit: `[test command]`
4. PR process: `[how to submit]`

**Common Commands:**

```bash
# Run development server
[command]

# Run tests
[command]

# Build project
[command]

# Lint/format code
[command]
```

### 🎓 Learning Path

**Week 1 - Fundamentals:**

1. Understand _[core component]_
2. Learn _[key pattern]_
3. Practice _[common task]_

**Week 2 - Contributing:**

1. Fix a small bug in _[accessible area]_
2. Add a test for _[untested feature]_
3. Improve documentation for _[unclear area]_

**Week 3 - Feature Development:**

1. Implement _[small feature]_
2. Review existing _[feature type]_
3. Propose improvement to _[area]_

### 🐛 First Contribution Suggestions

**Good First Issues:**

1. **Documentation Fix:**
   - Location: `[file:path]`
   - Issue: _[What needs fixing]_
   - Impact: Helps future developers

2. **Add Missing Test:**
   - Location: `[file:path]`
   - Coverage gap: _[What's not tested]_
   - Impact: Improves reliability

3. **Small Enhancement:**
   - Location: `[file:path]`
   - Enhancement: _[Specific improvement]_
   - Impact: Better user experience

### ⚠️ Common Gotchas

**Environment Issues:**

- _[Common setup problem and solution]_
- _[Version compatibility issue]_

**Development Pitfalls:**

- _[Anti-pattern to avoid]_
- _[Performance consideration]_

**Testing Challenges:**

- _[Test data setup]_
- _[Mock requirements]_

### 📖 Resources

**Documentation:**

- Main docs: `[location]`
- API docs: `[if applicable]`
- Architecture: `[if exists]`

**Code Standards:**

- Style guide: _[Convention or file]_
- Linting rules: `[config file]`
- Type checking: _[approach]_

**Getting Help:**

- Team communication: _[Slack/Discord/etc]_
- Issue tracker: _[GitHub/Jira/etc]_
- Code reviews: _[process]_

### 💡 Pro Tips

Based on this codebase:

1. _[Specific tip for productivity]_
2. _[Common pattern to follow]_
3. _[Tool or shortcut that helps]_

### ✅ Onboarding Checklist

**Day 1:**

- [ ] Environment setup complete
- [ ] Project runs locally
- [ ] Tests pass
- [ ] Understand basic architecture

**Week 1:**

- [ ] Made first commit
- [ ] Understand main workflows
- [ ] Familiar with codebase structure
- [ ] Identified area to contribute
- [ ] Completed first PR
- [ ] Added meaningful test
- [ ] Improved documentation
- [ ] Understands deployment process

### 🎯 Next Steps

Based on the focus area: **$ARGUMENTS**

_[Provide specific guidance based on their interest area - frontend, backend, testing, etc. If no area specified, suggest exploring the area with least documentation or test coverage as a good learning opportunity]_

Remember: Start small, ask questions, and iterate. Every expert was once a beginner in this codebase!
