---
description: Analyze git history to understand code evolution and find issues
allowed-tools: Bash(git log:*), Bash(git blame:*), Bash(git show:*)
argument-hint: [file/directory] [--since=date] [--author=name]
---

# Git History Analysis

**Target:** $ARGUMENTS

## History Investigation

### 1. Recent Activity

Understand recent changes in the codebase:

Recent commits: !`git log --oneline --graph --all -20`

### 2. File-Specific History

If analyzing specific files or directories, trace their evolution:

Think deeply about patterns in the history:
- When were major changes introduced?
- Who has been working on this code?
- What was the context of changes?

### 3. Blame Analysis

For understanding specific line origins:
- Identify when problematic code was introduced
- Find related commits for context
- Understand the reasoning behind changes

## Analysis Areas

### Change Patterns
- Frequency of changes (stable vs volatile code)
- Types of changes (features vs fixes)
- Correlation with issues or bugs

### Author Insights
- Main contributors to specific areas
- Knowledge holders for components
- Collaboration patterns

### Timeline Analysis
- Release correlations
- Bug introduction points
- Refactoring history

## Required Output Format

### 📊 History Summary

**Period Analyzed:** [date range]

**Key Statistics:**
- Total commits: [number]
- Contributors: [count]
- Most active files: [list]

### 🔍 Notable Findings

**Major Changes:**
1. **[Date]** - `[commit hash]` - [description]
   - Author: [name]
   - Impact: [what changed]
   - Context: [why it was changed]

**Patterns Observed:**
- [Pattern 1: description]
- [Pattern 2: description]

### 👥 Contributor Analysis

**Primary Authors:**
| Author | Commits | Focus Area |
|--------|---------|------------|
| [name] | [count] | [area] |

### 🐛 Issue Correlation

**Potential Problem Commits:**
- `[hash]` - [reason for concern]
- `[hash]` - [what might be problematic]

### 📈 Evolution Timeline

```
[Visualization of major milestones]
v1.0 ──→ refactor ──→ v2.0 ──→ bug fixes ──→ current
  ↑         ↑           ↑          ↑
[date]   [date]      [date]     [date]
```

### 💡 Insights

**Code Health:**
- Stability: [assessment]
- Maintenance burden: [high/medium/low]
- Technical debt indicators: [findings]

**Recommendations:**
1. [Recommendation based on history]
2. [Area needing attention]
3. [Refactoring opportunity]

### 🔎 Deep Dive Commands

For further investigation:
```bash
# Detailed log for specific file
git log -p [file]

# Find when text was added/removed
git log -S "[search text]"

# Show specific commit details
git show [commit-hash]
```