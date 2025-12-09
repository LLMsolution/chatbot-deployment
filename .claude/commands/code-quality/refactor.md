---
description: Identify and prioritize critical refactoring opportunities across the codebase
argument-hint: [directory/file] (defaults to entire project)
---

# Refactoring Analysis

**Scope:** $ARGUMENTS

## Systematic Refactoring Assessment

### 1. Check Project Standards

First, review the project's architecture and coding standards:

- Check CLAUDE.md and .claude/CLAUDE.md for documented patterns
- Note any specific refactoring guidelines or constraints
- Identify preferred utilities and shared components structure

### 2. Code Metrics Scan

Analyze codebase for refactoring opportunities:

Deeply explore the codebase with tools like `ripgrep` `glob` `find`, `wc`, and `grep` etc to identify potential areas for improvement.

### 3. Critical Analysis Areas

Think harder about code quality issues across multiple dimensions:

**Size & Complexity:**

- Files exceeding 500 lines (or violates CLAUDE.md guidance)
- Functions exceeding 50 lines
- Classes exceeding 100 lines
- Cyclomatic complexity > 10
- Deep nesting (> 3 levels)

**Code Duplication:**

- Repeated code blocks across files
- Similar functions with slight variations
- Copy-pasted error handling
- Duplicate business logic

**Architecture Violations:**

- Cross-feature imports breaking vertical slices
- Mixed responsibilities in single modules
- Business logic in UI components
- Data access in presentation layer

**Type Safety & Validation:**

- Missing type hints/interfaces
- No input validation (Pydantic models, Zod schemas)
- Untyped function returns
- Any/unknown types proliferation
- Naming conventions not followed or incosistency

**Maintainability Issues:**

- God objects/modules doing too much
- Long parameter lists (> 4 params)
- Dead code and unused exports
- Inconsistent patterns within same feature

## Required Output Format

### 🎯 Refactoring Priority Matrix

**Critical (Do Now):**
| Issue | Location | Impact | Effort |
|-------|----------|--------|--------|
| _[Issue]_ | `file:lines` | _[High/Med/Low]_ | _[1-4 hours]_ |

**Important (This Sprint):**
| Issue | Location | Impact | Effort |
|-------|----------|--------|--------|
| _[Issue]_ | `file:lines` | _[High/Med/Low]_ | _[2-8 hours]_ |

**Nice to Have (Backlog):**
| Issue | Location | Impact | Effort |
|-------|----------|--------|--------|
| _[Issue]_ | `file:lines` | _[High/Med/Low]_ | _[1-3 days]_ |

### 📋 Top 5 Refactoring Opportunities

#### 1. **[Most Critical Issue Name]**

**Problem:** _[What's wrong and why it matters]_

**Current Code Location:** `file:lines`

**Metrics:**

- Lines of code: _[X]_
- Complexity: _[cyclomatic/cognitive]_
- Dependencies: _[count]_
- Test coverage: _[X%]_

**Refactoring Approach:**

```
Current Structure:
- [Current organization]

Proposed Structure:
- [New organization following CLAUDE.md patterns]
```

**Implementation Steps:**

1. _[Step 1 with specific file operations]_
2. _[Step 2 with specific extractions]_
3. _[Step 3 with test updates]_

**New Files to Create:**

- `path/to/new/utility.ext` - _[Purpose]_
- `path/to/new/types.ext` - _[Shared types/models]_

#### 2-5. _[Repeat structure for next critical issues]_

### 🔄 DRY Violations

**Duplicate Code Patterns Found:**

1. **Pattern:** _[Description of repeated code]_
   - **Locations:** `file1:lines`, `file2:lines`, `file3:lines`
   - **Extract to:** `shared/utils/[name].ext`
   - **Benefit:** _[Lines saved, maintenance improvement]_

2. **Pattern:** _[Another duplication]_
   - **Locations:** _[List all occurrences]_
   - **Extract to:** _[Proposed utility location]_
   - **Benefit:** _[Impact description]_

### 🏗️ Architecture Improvements

**Vertical Slice Violations:**

- **Issue:** _[Cross-feature dependency]_
- **From:** `feature1/component`
- **To:** `feature2/component`
- **Fix:** _[Move to shared or restructure]_

**Separation of Concerns:**

- **Issue:** _[Mixed responsibilities]_
- **Location:** `file:class/function`
- **Split into:** _[List of focused components]_

### 📦 Suggested Utilities

Based on repeated patterns, create these utilities:

1. **`shared/utils/validation.ext`**
   - Extract: _[Common validation logic]_
   - Used by: _[List of consumers]_
   - Benefits: _[Consistency, testing]_

2. **`shared/utils/formatting.ext`**
   - Extract: _[Formatting functions]_
   - Used by: _[List of consumers]_
   - Benefits: _[Single source of truth]_

3. **`shared/types/models.ext`**
   - Extract: _[Shared data models]_
   - Used by: _[List of consumers]_
   - Benefits: _[Type safety, validation]_

### 📊 Impact Assessment

**If all refactorings completed:**

- **Lines reduced:** ~_[X]_ lines (_[Y]_%)
- **Files affected:** _[X]_ files
- **Duplicate code eliminated:** _[X]_ instances
- **Type coverage improved:** _[X]_% → _[Y]_%
- **Test maintenance reduced:** _[X]_ test files simplified

### 🚀 Quick Wins

**Can be done in < 30 minutes each:**

1. _[Quick improvement with location]_
2. _[Another quick fix]_
3. _[Easy extraction]_

### ⚠️ Risk Assessment

**High Risk Refactorings:**

- _[Refactoring that touches many files]_
- _[Core functionality changes]_
- _[Breaking API changes]_

**Mitigation Strategy:**

- Feature flags for gradual rollout
- Comprehensive test coverage before refactoring
- Incremental refactoring in small PRs

### 💡 Next Steps

1. **Immediate Action:** Start with #1 critical refactoring
2. **Team Discussion:** Review architectural improvements
3. **Documentation:** Update CLAUDE.md with new patterns
4. **Testing:** Add tests before refactoring begins

### 🔍 CLAUDE.md Alignment Check

**Following CLAUDE.md guidelines:**

- ✅ _[Guideline being followed]_
- ✅ _[Another guideline met]_

**Violating CLAUDE.md guidelines:**

- ❌ _[Violation with reference to CLAUDE.md section]_
- ❌ _[Another violation]_

**Recommended CLAUDE.md additions:**

- _[New pattern to document]_
- _[Clarification needed]_
