---
description: Analyze review feedback and provide implementation options with tradeoffs
argument-hint: [issue from review] or [entire review report]
---

# Review Issue Analysis

**Issue to analyze:** $ARGUMENTS

## Instructions

Analyze this code review feedback and provide actionable implementation options.

### 1. Understand the Issue

- Parse the specific problem raised in the review
- Search the codebase for context and related patterns
- Determine if this is a critical fix or enhancement

### 2. Context Check

- Consider project maturity and priorities
- Check if similar patterns exist elsewhere
- Assess impact on functionality vs code quality

### 3. Generate Solutions

Think harder about the best approaches for this specific issue.
Consider multiple angles and provide options that represent different priorities.

## Required Output Format

### 📋 Issue Analysis

_[One sentence summary of the issue]_

### ✅ Validity & Impact

- **Valid concern?** [YES/NO]
- **User-facing impact?** [YES/NO]
- **Security/Breaking?** [YES/NO]
- **Related to this PR?** [YES/NO]

### 🎯 Priority Assessment

**[CRITICAL/HIGH/MEDIUM/LOW/SKIP]**
_[One sentence justification based on PR scope and project context]_

### 🔧 Implementation Options

**Option 1: Best for This PR**

- **Approach:** _[Minimal change that fixes the issue within PR scope]_
- **Time:** ~X minutes
- **Why best for PR:** _[Keeps PR focused and mergeable]_
- **Tradeoff:** _[What we're compromising]_

**Option 2: Best for Code Quality (DRY)**

- **Approach:** _[Refactored solution reducing duplication]_
- **Time:** ~X minutes
- **Why best for DRY:** _[How it improves maintainability]_
- **Tradeoff:** _[Scope creep or complexity added]_

**Option 3: Best Long-term Solution**

- **Approach:** _[Comprehensive fix addressing root cause]_
- **Time:** ~X hours
- **Why best long-term:** _[Future benefits]_
- **Tradeoff:** _[Time investment and PR bloat]_

**Option 4: Skip & Track**

- **Why skip:** _[Out of scope / Not critical / Unrelated to PR]_
- **Create issue:** _[GitHub issue title and description]_
- **When to address:** _[Specific trigger or timeline]_

### 💡 Recommendation

**Go with Option X** - _[One sentence reasoning]_

### 🤔 Next Step?

1. **Implement now** - Would you like me to apply Option X?
2. **Modify approach** - Should we adjust the solution?
3. **Skip** - Move to next issue?

_Please choose 1, 2, or 3_
