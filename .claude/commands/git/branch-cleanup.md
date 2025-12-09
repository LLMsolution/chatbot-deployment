---
description: Clean up local and remote branches systematically
allowed-tools: Bash(git branch:*), Bash(git remote:*), Bash(git checkout:*)
argument-hint: [--dry-run] [--force]
---

# Git Branch Cleanup

**Options:** $ARGUMENTS

## Branch Analysis

### 1. Current State

Analyze the branch situation:

Local branches: !`git branch -v`
Remote branches: !`git branch -r`
Current branch: !`git branch --show-current`

### 2. Identify Cleanup Candidates

Think about which branches to clean:
- Merged branches (already in main/master)
- Stale branches (no recent commits)
- Abandoned feature branches
- Temporary experiment branches

### 3. Safety Checks

Before cleaning, verify:
- No uncommitted changes
- Not on branch to be deleted
- Branch is truly merged or abandoned
- No one else is using the branch

## Required Output Format

### 📊 Branch Status Report

**Current Branch:** [branch name]
**Total Branches:** [local: X, remote: Y]

### 🧹 Cleanup Candidates

**Merged Branches:**
```
Local:
- [branch] - last commit: [date] - [safe to delete]
- [branch] - last commit: [date] - [safe to delete]

Remote:
- origin/[branch] - merged to main
- origin/[branch] - merged to main
```

**Stale Branches (>30 days):**
```
- [branch] - last activity: [X days ago]
- [branch] - last activity: [X days ago]
```

**Orphaned Branches:**
```
- [branch] - no remote tracking
- [branch] - remote deleted
```

### ⚠️ Branches to Keep

**Active Development:**
- [branch] - [reason to keep]
- [branch] - [reason to keep]

**Protected:**
- main/master
- develop
- release/*

### 🗑️ Cleanup Commands

**Safe Cleanup (merged only):**
```bash
# Delete local merged branches
git branch --merged main | grep -v "main\|master\|develop" | xargs -n 1 git branch -d

# Delete remote tracking branches
git remote prune origin
```

**Aggressive Cleanup (with confirmation):**
```bash
# Local branches
git branch -d [branch1]
git branch -d [branch2]

# Remote branches
git push origin --delete [branch1]
git push origin --delete [branch2]
```

### 📋 Cleanup Plan

**Phase 1: Safe Deletions**
- [ ] Delete [X] merged local branches
- [ ] Prune [Y] deleted remote branches

**Phase 2: Stale Branches**
- [ ] Review [Z] stale branches
- [ ] Delete agreed upon branches

**Phase 3: Remote Cleanup**
- [ ] Push deletions to remote
- [ ] Notify team of cleanup

### 💡 Best Practices

**Before Deleting:**
1. Ensure branch is fully merged
2. Check with team members
3. Backup important work
4. Document why deleted

**Branch Naming:**
- Use descriptive names
- Include ticket numbers
- Add date for temporary branches

### 🚀 Execute Cleanup?

Ready to proceed with cleanup plan above?
- Use `--dry-run` to preview without deleting
- Use `--force` to skip confirmations (dangerous)