---
description: Comprehensive multi-perspective PR review with actionable feedback
allowed-tools: Bash(gh pr:*), Read, Grep, Glob
argument-hint: [PR number/URL]
---

# Multi-Perspective PR Review

**PR:** $ARGUMENTS

## Fetch PR Details

Get PR information: !`gh pr view $ARGUMENTS --json title,body,files,additions,deletions,changedFiles`

## Systematic Review Process

### 1. Understand the Change

Think deeply about the PR's purpose:
- What problem is being solved?
- Who are the stakeholders?
- What's the scope of impact?
- Are there any risks?

### 2. Multi-Perspective Analysis

Evaluate the PR from different expert perspectives to ensure comprehensive review.

## Required Output Format

### 📊 PR Overview

**Title:** [PR title]
**Changes:** [files] files, +[additions] -[deletions]
**Type:** [feature/fix/refactor/docs]
**Risk Level:** [Low/Medium/High]

---

### 🎯 Product Perspective

**Business Value:** [Does this deliver immediate user value?]
**User Experience:** [Will users understand and appreciate this?]
**Priority Alignment:** [Does this match current priorities?]

**Recommendations:**
- [ ] [Specific product improvement]
- [ ] [User-facing enhancement needed]

---

### 💻 Engineering Perspective

**Code Quality:**
- Architecture: [Assessment]
- Maintainability: [Assessment]
- Performance: [Assessment]
- Best Practices: [Followed/Violations noted]

**Technical Concerns:**
1. [Concern in `file:lines`] - [Why it matters]
2. [Pattern issue] - [Better approach]

**Required Changes:**
- [ ] [Critical fix needed]
- [ ] [Refactoring suggestion]

---

### 🧪 Quality Perspective

**Test Coverage:**
- Unit Tests: [Adequate/Missing]
- Integration Tests: [Present/Needed]
- Edge Cases: [Covered/Gaps]

**Quality Issues:**
1. [Untested scenario] - [Risk]
2. [Missing validation] - [Impact]

**Testing Requirements:**
- [ ] Add test for [scenario]
- [ ] Cover edge case: [description]

---

### 🔒 Security Perspective

**Security Assessment:**
- Input Validation: [Status]
- Authentication: [Proper/Issues]
- Data Protection: [Adequate/Concerns]
- Dependencies: [Safe/Vulnerabilities]

**Security Actions:**
- [ ] [Fix vulnerability in `file:lines`]
- [ ] [Add validation for input]
- [ ] [Review permission check]

---

### 🔧 Operations Perspective

**Deployment Readiness:**
- Configuration: [Complete/Missing]
- Monitoring: [Adequate/Gaps]
- Rollback Plan: [Clear/Needed]
- Performance Impact: [Assessment]

**Operational Requirements:**
- [ ] Add monitoring for [metric]
- [ ] Document deployment steps
- [ ] Consider scaling implications

---

### 🎨 UX/UI Perspective
*(if applicable)*

**Design Compliance:**
- Visual Consistency: [Matches/Deviates]
- Accessibility: [WCAG compliant/Issues]
- Responsive Design: [Verified/Needs work]
- User Flow: [Intuitive/Confusing]

**Design Actions:**
- [ ] [Specific UI improvement]
- [ ] [Accessibility fix needed]

---

### 📝 Overall Recommendation

**Verdict:**
- [ ] **APPROVE** - Ready to merge
- [ ] **REQUEST CHANGES** - Address issues before merge
- [ ] **COMMENT** - Suggestions but not blocking

**Priority Issues to Address:**
1. 🔴 **Critical:** [Must fix before merge]
2. 🟡 **Important:** [Should address]
3. 🟢 **Optional:** [Nice to have]

**Summary:**
[One paragraph overall assessment and key action items]

---

### 💬 Suggested Review Comment

```markdown
## Review Summary

[Overall assessment]

### Must Fix
- [ ] [Critical issue 1]
- [ ] [Critical issue 2]

### Should Address
- [ ] [Important improvement]
- [ ] [Quality concern]

### Consider
- [ ] [Optional enhancement]

[Closing encouragement or specific praise for good work]
```

### 🎯 Focus for Author

**Immediate Actions:**
1. [Most critical fix]
2. [Second priority]
3. [Third priority]

**Questions for Author:**
- [Clarification needed]
- [Design decision rationale]