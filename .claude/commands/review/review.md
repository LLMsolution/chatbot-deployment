---
description: Comprehensive code review with actionable feedback
argument-hint: [file/directory/PR-number] (defaults to staged changes)
---

# Code Review Request

Deeply review the following code changes for quality, security, and best practices.

## Scope

$ARGUMENTS

## Context

- Current git status: !`git status --short`
- Recent commits: !`git log --oneline -5`

## Review Checklist

### Must Check

- [ ] **Security**: Input validation, SQL injection, XSS, authentication
- [ ] **Error Handling**: Proper exception handling, edge cases covered
- [ ] **Testing**: Tests exist and cover the main functionality
- [ ] **Performance**: No obvious bottlenecks (N+1 queries, inefficient loops)
- [ ] **Code Style**: Consistent formatting, clear naming conventions

### Project-Specific Rules

<!-- Add your project-specific requirements here -->
<!-- Example: - [ ] All API endpoints have rate limiting -->
<!-- Example: - [ ] React components use TypeScript interfaces -->
<!-- Example: - [ ] Database queries use parameterized statements -->

## Consider

When you have gather all the necessary review context think hard about the findings and create useful suggestions that are actionable.

always consider the angles:

- Best option based on the project context
- Best option for dry code
- Best option for performance
- Best option for security
- Best option for maintainability
- Etc

## Required Output Format

Provide a structured review following this EXACT format:

```markdown
## 📊 Review Summary

[One sentence overall assessment]

## 🔴 Critical Issues (Must Fix)

[List critical security/breaking issues with file:line references]

- **[Issue]** in `file:line`: [Specific problem and fix]

## 🟡 Important Issues (Should Fix)

[List important but non-breaking issues]

- **[Issue]** in `file:line`: [Problem and recommendation]

## 🟢 Suggestions (Consider)

[List nice-to-have improvements]

- **[Suggestion]**: [Enhancement idea]

## ✅ Good Practices Observed

[List 2-3 things done well]

## 📈 Metrics

- Files reviewed: X
- Lines changed: +X -Y
- Test coverage: [Estimated]
- Complexity: [Low/Medium/High]
```

Focus on actionable feedback. For each issue, provide:

1. What is wrong
2. Why it matters
3. How to fix it (with specific code example when helpful)

Keep the review concise and prioritized. Maximum 15 issues total.
