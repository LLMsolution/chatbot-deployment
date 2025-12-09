---
description: Create and refine user stories with acceptance criteria
argument-hint: [feature/epic description] [target persona]
---

# User Story Creation

**Feature:** $1
**Target User:** $2 (or primary persona if not specified)

## Discovery Process

### 1. User Research
Analyze the feature request to understand:
- Who needs this feature (personas/roles)
- What problem it solves
- Why it's valuable to the user
- When/where they would use it
- How it fits into their workflow

### 2. Story Decomposition
Break down into atomic user stories following the INVEST criteria:
- **Independent** - Can be developed separately
- **Negotiable** - Details can be discussed
- **Valuable** - Delivers value to users
- **Estimatable** - Team can estimate effort
- **Small** - Fits in one sprint
- **Testable** - Clear pass/fail criteria

## User Story Format

### Epic: [High-level Feature]

**User Stories:**

#### Story 1: [Title]
**As a** [type of user]
**I want** [goal/desire]
**So that** [benefit/value]

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

**Definition of Done:**
- [ ] Code reviewed and approved
- [ ] Unit tests passing (coverage > 80%)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] No critical bugs
- [ ] Performance benchmarks met

**Story Points:** [1, 2, 3, 5, 8, 13]
**Priority:** [High/Medium/Low]
**Dependencies:** [List any blockers]

#### Story 2: [Title]
[Repeat format above]

## Technical Considerations

**API Changes:**
- Endpoints affected
- Data model updates
- Breaking changes

**UI/UX Impact:**
- Screens/components affected
- User flow changes
- Accessibility requirements

**Non-functional Requirements:**
- Performance targets
- Security considerations
- Scalability needs

## Success Metrics

**Quantitative:**
- User adoption rate target
- Performance benchmarks
- Error rate thresholds

**Qualitative:**
- User feedback themes
- Support ticket reduction
- Team satisfaction

## Edge Cases & Risks

**Edge Cases to Handle:**
1. [Scenario and expected behavior]
2. [Scenario and expected behavior]

**Risks:**
- **Risk:** [Description]
  **Mitigation:** [Strategy]

## Sprint Planning Notes

**Suggested Sprint Allocation:**
- Sprint 1: Stories 1-3 (Foundation)
- Sprint 2: Stories 4-6 (Core features)
- Sprint 3: Stories 7-8 (Polish & edge cases)

**Team Considerations:**
- Frontend effort: [Low/Medium/High]
- Backend effort: [Low/Medium/High]
- QA effort: [Low/Medium/High]
- Design needed: [Yes/No]