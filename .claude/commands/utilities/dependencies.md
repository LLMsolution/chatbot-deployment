---
description: Audit dependencies for security, updates, and unused packages
argument-hint: [--fix] [--security-only]
---

# Dependency Audit

**Options:** $ARGUMENTS

## Dependency Analysis

### 1. Run Audit Commands

Check based on package manager:

**NPM/Yarn:**
- `npm audit`
- `npm outdated`
- `npx depcheck`

**Python:**
- `pip list --outdated`
- `safety check`
- `pip-audit`

**Go:**
- `go list -m -u all`
- `go mod tidy`
- `nancy sleuth`

**Rust:**
- `cargo audit`
- `cargo outdated`

### 2. Identify Issues

Look for:
- Security vulnerabilities (Critical/High/Medium/Low)
- Major version updates available
- Unused dependencies
- Duplicate packages
- Deprecated packages
- License conflicts

### 3. Analyze Usage

For each dependency:
- Is it actually used?
- Can it be replaced with native code?
- Is there a lighter alternative?
- Is it well-maintained?

## Audit Report

### 🔒 Security Issues

**Critical:** [count]
- [package@version] - [CVE-ID] - [description]

**High:** [count]
- [package@version] - [vulnerability]

### 📦 Updates Available

**Major Updates:**
- [package] current@X → latest@Y (breaking changes)

**Minor Updates:**
- [package] current@X.Y → latest@X.Z (features)

**Patch Updates:**
- [package] current@X.Y.Z → latest@X.Y.W (fixes)

### 🗑️ Unused Dependencies

**Can Remove:**
- [package] - Not imported anywhere
- [package] - Only in dev, not needed

### 💡 Recommendations

**Replace:**
- [heavy-package] → [lighter-alternative]
- [deprecated-pkg] → [maintained-fork]

**Security Fix Commands:**
```bash
[Commands to fix vulnerabilities]
```

**Update Commands:**
```bash
[Safe update commands]
```

### ✅ Action Plan

1. [ ] Fix critical vulnerabilities
2. [ ] Remove unused packages
3. [ ] Update patch versions
4. [ ] Review major updates
5. [ ] Document why certain versions are pinned
6. [ ] Add security scanning to CI