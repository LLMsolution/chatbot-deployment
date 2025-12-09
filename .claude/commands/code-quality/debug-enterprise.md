---
description: Enterprise debugging with stakeholder-ready incident report and full audit trail
argument-hint: [incident description/ticket number/error report]
---

# Enterprise Incident Investigation

**Incident:** $ARGUMENTS

## Comprehensive Investigation Process

### 1. Initial Assessment

Deeply analyze the incident for business impact and scope:

- Severity level and affected systems
- User impact and business consequences
- Timeline of when issues started
- Related incidents or patterns

### 2. Historical Analysis

Investigate the git history to establish timeline and ownership:

Recent changes to affected components: !`git log --since="2 weeks ago" --format="%h %ad %an: %s" --date=short --name-only | head -30`

### 3. Root Cause Investigation

Think harder about all contributing factors:

- Primary cause (direct trigger)
- Contributing factors (what made it possible)
- Environmental factors (what made it happen now)
- Process failures (what should have caught this)

### 4. Impact Analysis

Assess the full scope of impact:

- Affected users/customers (count and segments)
- Data integrity implications
- Financial impact (if applicable)
- Compliance/regulatory concerns
- Reputation/trust impact

## Required Output Format

### 📊 Executive Summary

**Incident Level:** _[Critical/High/Medium/Low]_

**Business Impact:** _[One paragraph describing user and business impact]_

**Resolution Status:** _[Resolved/Mitigated/Under Investigation]_

**Time to Detection:** _[X hours/days from introduction]_

**Time to Resolution:** _[X hours from detection]_

### 🔍 Technical Analysis

**Incident Type:** _[Outage/Data Loss/Security/Performance/Functionality]_

**Affected Systems:**

- _[Primary system/service]_
- _[Dependent systems]_
- _[Downstream impacts]_

**Root Cause:** _[Detailed technical explanation]_

**Contributing Factors:**

1. _[Factor 1 with explanation]_
2. _[Factor 2 with explanation]_
3. _[Factor 3 with explanation]_

### 📈 Timeline & Attribution

**Incident Timeline:**

- **[Date Time]** - Code change introduced (Commit: `hash`)
- **[Date Time]** - Deployed to production
- **[Date Time]** - First user impact
- **[Date Time]** - Issue detected
- **[Date Time]** - Investigation started
- **[Date Time]** - Root cause identified
- **[Date Time]** - Fix deployed
- **[Date Time]** - Full resolution confirmed

**Change History:**

```
Commit: [hash] | Author: [name] | Date: [date]
File: [filename:line]
Change: [what was modified]
Reason: [commit message/PR context]
Review: [PR number and reviewers]
```

**Responsibility Chain:**

- **Author:** _[Developer who made change]_
- **Reviewer(s):** _[Who approved the PR]_
- **Deployer:** _[Who deployed to production]_
- **On-call:** _[Who was responsible when detected]_

### 🛠️ Resolution Details

**Immediate Mitigation:**

- **Action Taken:** _[What was done to stop the bleeding]_
- **Time to Mitigate:** _[X minutes/hours]_
- **Effectiveness:** _[Fully/Partially resolved]_

**Permanent Fix:**

- **Solution:** _[Technical solution implemented]_
- **Files Modified:** _[List of files:lines changed]_
- **Validation:** _[How we verified the fix]_
- **Rollout Plan:** _[Deployment strategy]_

### 🛡️ Prevention Measures

**Process Gaps Identified:**

1. **Gap:** _[What process failed]_
   - **Fix:** _[Process improvement]_
   - **Owner:** _[Team/person responsible]_
   - **Deadline:** _[Implementation date]_

2. **Gap:** _[What was missing]_
   - **Fix:** _[What we're adding]_
   - **Owner:** _[Team/person responsible]_
   - **Deadline:** _[Implementation date]_

**Technical Improvements:**

- [ ] **Testing:** _[New test cases to add]_
- [ ] **Monitoring:** _[New alerts/metrics to implement]_
- [ ] **Documentation:** _[Docs to update/create]_
- [ ] **Code Review:** _[Review checklist additions]_
- [ ] **Architecture:** _[Design improvements needed]_

### 📋 Lessons Learned

**What Went Well:**

- _[Positive aspect of incident response]_
- _[Team coordination that worked]_

**What Went Wrong:**

- _[Failure point 1]_
- _[Failure point 2]_

**Action Items:**

| Action       | Owner    | Priority | Due Date | Status      |
| ------------ | -------- | -------- | -------- | ----------- |
| _[Action 1]_ | _[Name]_ | High     | _[Date]_ | Not Started |
| _[Action 2]_ | _[Name]_ | Medium   | _[Date]_ | Not Started |
| _[Action 3]_ | _[Name]_ | Low      | _[Date]_ | Not Started |

### 🎯 Recommendations

**For Engineering:**

- _[Specific technical recommendations]_

**For Management:**

- _[Process/resource recommendations]_

**For Product:**

- _[Feature/priority recommendations]_

### 📊 Metrics & KPIs

**Incident Metrics:**

- Detection Time: _[Time from deployment to detection]_
- Resolution Time: _[Time from detection to fix]_
- User Impact Duration: _[Total time users affected]_
- Failed Requests/Transactions: _[Count if applicable]_

**Quality Metrics:**

- Test Coverage Gap: _[What wasn't tested]_
- Code Review Miss: _[What review should have caught]_
- Monitoring Gap: _[What alert was missing]_

### ✅ Sign-off

**Investigation Complete:** ☐

**Stakeholders Notified:** ☐

**Post-mortem Scheduled:** ☐

**Action Items Assigned:** ☐

---

_This report is intended for: Engineering Leadership, Product Management, Operations, and affected Stakeholders_
