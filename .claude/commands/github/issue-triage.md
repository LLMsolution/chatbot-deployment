---
description: Systematically triage GitHub issues with codebase context and actionable decisions
allowed-tools: Bash(gh issue:*), Read, Grep, Glob
argument-hint: [issue number] or "all" for full triage
---

# Issue Triage System

**Target:** $ARGUMENTS

## Triage Process

### 1. Gather Issues

Determine triage scope:

If specific issue number provided: `gh issue view $ARGUMENTS --json number,title,body,labels,assignees,createdAt,comments`

If "all" or no argument: `gh issue list --limit 30 --json number,title,labels,state,createdAt,updatedAt,assignees`

### 2. Issue Analysis Strategy

Think deeply about each issue:

- What is the real problem being reported?
- Where in the codebase would this be implemented?
- What's the complexity and effort required?
- Are there existing patterns to follow?
- Who should handle this?

## For Each Issue

### Deep Investigation

For each issue to triage, perform:

1. **Issue Understanding**
   - Parse the issue description
   - Identify acceptance criteria
   - Note any reproduction steps
   - Check comments for clarifications

2. **Codebase Research**
   - Search for relevant files mentioned
   - Find related existing code
   - Identify similar implementations
   - Locate tests that might break

3. **Impact Assessment**
   - User-facing or internal?
   - Breaking change potential?
   - Performance implications?
   - Security considerations?

## Required Output Format

### 📋 Issue Triage Report

---

### Issue #[number]: [title]

**📊 Quick Facts:**

- Created: [date]
- Labels: [existing labels]
- Assignee: [current assignee or "None"]
- Last Activity: [days ago]

**📝 Issue Summary:**
[One paragraph explaining what this issue is about]

**🔍 Codebase Context:**

**Relevant Files Found:**

- `[file:path]` - [why it's relevant]
- `[file:path]` - [connection to issue]

**Similar Patterns:**

- `[file:lines]` - [existing implementation that could be copied]
- `[file:lines]` - [related functionality]

**Implementation Location:**

- Primary changes needed in: `[file/directory]`
- Tests to add/modify: `[test file]`
- Documentation updates: `[docs location]`

**📐 Technical Analysis:**

**Approach Options:**

1. **Quick Fix** - [description] (Est: [time])
2. **Proper Solution** - [description] (Est: [time])
3. **Comprehensive** - [description] (Est: [time])

**Dependencies:**

- [ ] [Needs X to be completed first]
- [ ] [Requires library/tool Y]
- [ ] [Blocked by Z]

**Risk Assessment:**

- Complexity: [Low/Medium/High]
- Breaking Changes: [Yes/No - details]
- Testing Required: [Unit/Integration/E2E]

**🎯 Triage Recommendation:**

**Priority:** [P0-Critical/P1-High/P2-Medium/P3-Low]

**Suggested Action:**

- [ ] **ASSIGN** - Ready for development
- [ ] **CLARIFY** - Needs more information
- [ ] **DEFER** - Not priority right now
- [ ] **CLOSE** - Won't fix or duplicate
- [ ] **BREAK DOWN** - Too large, needs splitting

**Suggested Labels:**

- Add: `[good-first-issue]` (if applicable)
- Add: `[bug/feature/enhancement]`
- Add: `[effort-small/medium/large]`
- Add: `[priority-X]`

**Suggested Assignee:**

- Best fit: [reasoning - frontend dev, backend specialist, etc.]
- Alternative: [backup option]

**Implementation Plan:**

1. [Step 1 with specific file changes]
2. [Step 2 with testing approach]
3. [Step 3 with documentation]

**Time Estimate:** [X hours/days]

---

### 🤔 User Decision Required

**What would you like to do with Issue #[number]?**

1. **ASSIGN** - Assign to suggested developer and add labels
2. **CLARIFY** - Add comment requesting more information
3. **DEFER** - Label as backlog/future
4. **CLOSE** - Close with explanation
5. **BREAK DOWN** - Create subtasks
6. **SKIP** - Move to next issue
7. **STOP** - End triage session

**Enter choice (1-7):** _[Wait for user input]_

---

## After User Decision

### Execute Action

Based on user choice:

**If ASSIGN:**

```bash
gh issue edit [number] --add-label "[labels]" --assignee "[user]"
gh issue comment [number] --body "Triaged: Ready for development. [implementation notes]"
```

**If CLARIFY:**

```bash
gh issue comment [number] --body "Needs clarification: [specific questions]"
gh issue edit [number] --add-label "needs-info"
```

**If DEFER:**

```bash
gh issue edit [number] --add-label "backlog"
gh issue comment [number] --body "Deferred to backlog: [reason]"
```

**If CLOSE:**

```bash
gh issue close [number]
gh issue comment [number] --body "Closing: [explanation]"
```

**If BREAK DOWN:**
Create subtask issues with:

```bash
gh issue create --title "[Subtask 1]" --body "[details]" --label "subtask"
# Repeat for each subtask
```

---

### 📊 Triage Session Summary

_(After all issues processed)_

**Issues Triaged:** [count]

**Decisions Made:**

- Assigned: [count] issues
- Need Clarification: [count] issues
- Deferred: [count] issues
- Closed: [count] issues
- Broken Down: [count] issues

**Work Queue Created:**

1. **High Priority:** [Issue numbers]
2. **Medium Priority:** [Issue numbers]
3. **Low Priority:** [Issue numbers]

**Next Steps:**

- [ ] Review assigned issues with developers
- [ ] Follow up on clarification requests in X days
- [ ] Re-evaluate deferred issues next sprint

### 💡 Patterns Observed

**Common Issues:**

- [Pattern noticed across multiple issues]
- [Recurring problem that needs systemic fix]

**Documentation Gaps:**

- [Areas where better docs would prevent issues]

**Technical Debt Indicators:**

- [Code areas that generate multiple issues]
