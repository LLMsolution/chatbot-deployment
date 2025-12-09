---
description: Guide through interactive rebase to clean up commit history
allowed-tools: Bash(git log:*), Bash(git rebase:*), Bash(git status:*)
argument-hint: [number of commits] [--onto branch]
---

# Interactive Rebase Guide

**Target:** $ARGUMENTS

## Pre-Rebase Analysis

### 1. Current History

Examine commits to rebase:

Recent history: !`git log --oneline -10`
Branch divergence: !`git log --oneline --graph --all -20`

### 2. Identify Issues

Think about what needs cleaning:
- Multiple commits for same feature
- Typos in commit messages
- WIP or temporary commits
- Commits in wrong order
- Unnecessary merge commits

### 3. Plan the Rebase

Determine the rebase strategy:
- Squash related commits
- Reword commit messages
- Drop unnecessary commits
- Reorder for logical flow

## Rebase Operations

### Available Actions

**pick (p):** Use commit as-is
**reword (r):** Use commit, but edit message
**edit (e):** Use commit, but stop to amend
**squash (s):** Combine with previous commit
**fixup (f):** Like squash, but discard message
**drop (d):** Remove commit entirely

## Required Output Format

### 📊 History Analysis

**Current Branch:** [branch]
**Commits to Rebase:** [count]
**Base Point:** [commit or branch]

### 📝 Rebase Plan

**Original History:**
```
[hash] - [message] → [action: reason]
[hash] - [message] → [action: reason]
[hash] - [message] → [action: reason]
```

**Proposed New History:**
```
1. [New combined message]
   - Squashes: [commits being combined]

2. [Reworded message]
   - Original: [old message]

3. [Kept as-is]
```

### 🎯 Rebase Strategy

**Commands to Execute:**
```bash
# Start interactive rebase
git rebase -i [base]

# In editor, change:
pick [hash1] [message1]
squash [hash2] [message2]  # Combine with above
reword [hash3] [message3]  # Fix message
drop [hash4] [message4]    # Remove
```

**After Each Step:**
1. If squashing: Edit combined commit message
2. If rewording: Provide new message
3. If conflicts: Resolve and continue

### ⚠️ Safety Checks

**Before Rebasing:**
- [ ] No uncommitted changes
- [ ] Branch is backed up
- [ ] Not on shared branch without coordination
- [ ] Understand the implications

**Danger Zones:**
- ⛔ Never rebase public/shared history
- ⛔ Don't rebase if others depend on commits
- ⛔ Avoid rebasing already-merged branches

### 🔄 Conflict Resolution

**If Conflicts Occur:**
```bash
# Check status
git status

# Resolve conflicts in files
[edit conflicted files]

# Mark resolved
git add [resolved files]

# Continue rebase
git rebase --continue

# Or abort if needed
git rebase --abort
```

### 📋 Cleanup Checklist

**Commit Message Standards:**
- [ ] Follows conventional format
- [ ] Clear and descriptive
- [ ] No typos or formatting issues
- [ ] Proper scope indicated

**History Flow:**
- [ ] Logical commit order
- [ ] Related changes grouped
- [ ] No duplicate commits
- [ ] Clean linear history

### 💡 Best Practices

**DO:**
- Rebase feature branches before merging
- Keep commits atomic and focused
- Write clear commit messages
- Test after rebasing

**DON'T:**
- Rebase shared branches
- Force push without warning team
- Mix unrelated changes
- Lose commit context

### 🚀 Ready to Rebase?

**Final Confirmation:**
- Backup created: `git branch backup-[branch]`
- Team notified (if needed)
- Ready to handle conflicts

**Push After Rebase:**
```bash
# Will need force push
git push --force-with-lease origin [branch]
```