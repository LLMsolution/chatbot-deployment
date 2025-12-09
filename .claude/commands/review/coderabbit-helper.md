---
description: Analyze CodeRabbit suggestions and provide actionable options with tradeoffs
argument-hint: [CodeRabbit suggestion text]
---

# CodeRabbit Review Analysis

**CodeRabbit Suggestion:** $ARGUMENTS

## Instructions

Analyze this CodeRabbit suggestion and provide pragmatic implementation options.

### 1. Deep Analysis

- Understand the technical issue being raised and get to the root cause
- Check if it's a real problem or false positive
- Search the codebase for related patterns and context

### 2. Project Context

- Consider project phase (early beta, MVP, production)
- Follow KISS principles and existing patterns
- Avoid premature optimization
- Determine if this affects users or is internal only

### 3. Generate Options

Think harder about the problem and potential solutions.
Consider what's best for different priorities and contexts.

## Required Output Format

### 📋 Issue Summary

_[One sentence describing what CodeRabbit found]_

### ✅ Is This Valid?

**[YES/NO]** - _[Brief explanation]_

### 🎯 Priority for This PR

**[HIGH/MEDIUM/LOW/SKIP]**
_[One sentence reasoning based on PR scope and project context]_

### 🔧 Options & Tradeoffs

**Option 1: Best for This PR**

- **What:** _[Minimal fix that addresses the issue within PR scope]_
- **Why best for PR:** _[Keeps PR clean and focused]_
- **Effort:** _[5 mins/30 mins/2+ hours]_
- **Tradeoff:** _[What we're not addressing]_

**Option 2: Best for Code Quality (DRY/Clean)**

- **What:** _[Refactored approach reducing duplication or improving structure]_
- **Why best for quality:** _[Long-term maintainability benefit]_
- **Effort:** _[5 mins/30 mins/2+ hours]_
- **Tradeoff:** _[Scope expansion or time investment]_

**Option 3: CodeRabbit's Exact Suggestion**

- **What:** _[Their exact recommendation as stated]_
- **Why consider:** _[Valid points from their analysis]_
- **Effort:** _[5 mins/30 mins/2+ hours]_
- **Tradeoff:** _[Potential over-engineering or relevance to PR]_

**Option 4: Skip & Document**

- **Why skip:** _[Out of scope / False positive / Not critical for PR]_
- **Track as:** _[TODO comment / GitHub issue / Tech debt item]_
- **Revisit when:** _[Specific condition or timeline]_

### 💡 Recommendation

**Go with Option X** - _[1-2 sentence justification considering project context]_

### 🤔 Next Step?

Would you like me to:

1. **Implement** the recommended option now
2. **Explore** alternative approaches
3. **Skip** this suggestion
4. **Discuss** specific concerns

_Please respond with your choice or any questions_
