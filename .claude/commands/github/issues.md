---
description: Work with GitHub issues - create, analyze, or convert to tasks
allowed-tools: Bash(gh issue:*)
argument-hint: [create/list/view] [issue number or title]
---

# GitHub Issues Management

**Action:** $ARGUMENTS

## Issue Operations

### 1. Understand Intent

Determine what the user wants to do:
- Create a new issue
- View existing issues
- Analyze an issue for implementation
- Convert issue to actionable tasks

### 2. Gather Context

For existing issues, fetch details:
Check recent issues: !`gh issue list --limit 10`

For specific issue: !`gh issue view $ARGUMENTS` (if number provided)

## Action Workflows

### Creating New Issue

**Analyze the Need:**
- Is this a bug, feature request, or documentation issue?
- What's the user impact?
- What's the priority?

**Issue Template:**
```markdown
## Description
[Clear description of the issue/request]

## Problem/Motivation
[Why this matters]

## Current Behavior
[What happens now]

## Expected Behavior
[What should happen]

## Proposed Solution
[How to fix/implement]

## Acceptance Criteria
- [ ] [Specific criterion 1]
- [ ] [Specific criterion 2]
- [ ] [Specific criterion 3]

## Additional Context
[Screenshots, logs, environment details]
```

### Analyzing Existing Issue

**Break Down Into Tasks:**
1. Understand requirements
2. Identify technical approach
3. List implementation steps
4. Define testing needs
5. Note documentation updates

## Required Output Format

### For Issue Creation

**📝 New Issue Draft**

**Title:** `[type]: [concise description]`

**Labels:** [bug/feature/documentation/enhancement]

**Body:**
```markdown
[Generated issue body following template]
```

**Command:**
```bash
gh issue create \
  --title "[title]" \
  --body "[body]" \
  --label "[labels]"
```

### For Issue Analysis

**📋 Issue Breakdown**

**Issue #[number]:** [title]
**Type:** [bug/feature/enhancement]
**Priority:** [critical/high/medium/low]
**Estimated Effort:** [hours/days]

**📝 Implementation Plan**

**Technical Approach:**
[Description of how to implement]

**Tasks:**
1. **Setup/Research** ([time estimate])
   - [ ] [Specific subtask]
   - [ ] [Specific subtask]

2. **Implementation** ([time estimate])
   - [ ] [Core functionality]
   - [ ] [Edge cases]
   - [ ] [Error handling]

3. **Testing** ([time estimate])
   - [ ] Unit tests
   - [ ] Integration tests
   - [ ] Manual testing

4. **Documentation** ([time estimate])
   - [ ] Code comments
   - [ ] User documentation
   - [ ] API documentation

**Dependencies:**
- [External dependency]
- [Internal dependency]

**Risks:**
- [Potential issue]
- [Mitigation strategy]

### For Issue List

**📊 Open Issues Summary**

**By Priority:**
- 🔴 Critical: [count]
- 🟡 High: [count]
- 🟢 Normal: [count]

**By Type:**
- Bugs: [count]
- Features: [count]
- Documentation: [count]

**Top Issues:**
1. #[number] - [title] - [assignee]
2. #[number] - [title] - [assignee]
3. #[number] - [title] - [assignee]

**Stale Issues:**
[Issues with no recent activity]

### 💡 Recommendations

**Quick Wins:**
[Issues that can be resolved quickly]

**Needs Discussion:**
[Issues requiring clarification]

**Blocked:**
[Issues waiting on dependencies]

### 🎯 Next Actions

Based on issue analysis:
1. [Immediate action item]
2. [Follow-up needed]
3. [Long-term consideration]