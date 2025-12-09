---
description: Generate comprehensive tests following existing patterns with edge cases
argument-hint: [file/function/class] to test
---

# Test Generation

**Target:** $ARGUMENTS

## Systematic Test Generation Process

### 1. Discover Test Patterns

First, deeply analyze the existing test structure in this codebase:

- Find test directories (test/, tests/, **tests**, spec/, or _.test._, _.spec._)
- Identify test framework (Jest, Pytest, Mocha, Vitest, etc.)
- Study existing test file naming conventions
- Learn mocking patterns and test utilities used

Search for test files and examine their patterns to understand the testing approach.

### 2. Analyze Existing Tests

Think hard about the patterns you find:

- How are test files organized? (mirrors src/, separate test/, colocated?)
- What's the test file naming convention? (_.test.ts, test\__.py, \*.spec.js?)
- How are test suites structured? (describe/it, class TestX, test functions?)
- What assertion library is used? (expect, assert, chai, should?)
- How are mocks created? (jest.mock, unittest.mock, sinon?)
- Are there test fixtures or factories being used?
- What setup/teardown patterns exist?

### 3. Understand Target Code

Analyze the code to be tested:

- Input parameters and their types
- Return values and side effects
- Dependencies that need mocking
- Error conditions and exceptions
- State changes and mutations
- Async operations and timing issues

### 4. Edge Case Discovery

Think harder about comprehensive test scenarios:

**Input Boundaries:**

- Empty inputs (null, undefined, "", [], {})
- Boundary values (0, -1, MAX_INT, MIN_INT)
- Invalid types (string instead of number)
- Special characters and Unicode
- Very large inputs (memory/performance)

**State Variations:**

- Initial state vs modified state
- Concurrent modifications
- Race conditions in async code
- State after errors

**Error Scenarios:**

- Network failures
- Timeout conditions
- Permission errors
- Missing dependencies
- Invalid configurations

**Business Logic:**

- Happy path (expected use)
- Alternative flows
- Edge cases specific to domain
- Regression scenarios

## Required Output Format

### 📁 Test File Structure

**Test Location:** `[path following project convention]`

**Naming Convention:** `[filename following existing pattern]`

### 🧪 Generated Test Suite

```[language]
// Import statements matching existing test patterns
[imports following project style]

// Test suite structure matching existing patterns
[describe/class/module block]

  // Setup and teardown if needed
  [beforeEach/setUp patterns from codebase]

  // Test: Happy Path
  [test case following existing naming]
    // Arrange
    [setup test data]

    // Act
    [execute function]

    // Assert
    [assertions matching project style]

  // Test: Null/Undefined Inputs
  [test for empty inputs]

  // Test: Boundary Values
  [test for edge values]

  // Test: Error Handling
  [test for exceptions]

  // Test: [Specific Edge Case 1]
  [domain-specific edge case]

  // Test: [Specific Edge Case 2]
  [another edge case]

  // Test: Mocked Dependencies
  [test with mocks following project patterns]

  // Test: Async Operations (if applicable)
  [async test following project patterns]

  // Test: State Changes (if applicable)
  [test for mutations]

  // Test: Performance (if critical path)
  [test for timeout/performance]
```

### 📊 Test Coverage Analysis

**Test Coverage:**

- **Branches:** [X/Y branches covered]
- **Statements:** [X/Y statements covered]
- **Edge Cases:** [X edge cases identified]
- **Error Paths:** [X error scenarios tested]

**Critical Paths Covered:**
✅ [Path 1: description]
✅ [Path 2: description]
✅ [Path 3: description]
❌ [Uncovered: what's not tested and why]

### 🎯 Test Organization

**Following Project Patterns:**

- Test file location: `[where it goes]`
- Import style: `[how imports are done]`
- Assertion style: `[expect vs assert]`
- Mock style: `[how mocks are created]`
- Naming convention: `[test naming pattern]`

**Test Categories:**

1. **Unit Tests:** Testing in isolation
2. **Integration Tests:** Testing with real dependencies (if needed)
3. **Edge Cases:** Boundary and error conditions
4. **Regression Tests:** Previous bug scenarios

### 🔍 Pattern Compliance Check

**Matching Existing Tests:**

- ✅ Using same test framework: `[framework name]`
- ✅ Following naming convention: `[pattern]`
- ✅ Using project's assertion style: `[style]`
- ✅ Matching mock patterns: `[approach]`
- ✅ Following file organization: `[structure]`

**Deviations (if any):**

- ⚠️ [Any necessary deviations and why]

### 💡 Additional Test Suggestions

**Consider Adding:**

- Property-based tests for `[function]`
- Snapshot tests for `[output]`
- Performance benchmarks for `[critical path]`
- Fuzz testing for `[input validation]`

### 📝 Test Documentation

**Test Descriptions:**
Each test includes a clear description of:

- What is being tested
- Why it matters
- Expected behavior
- Edge case rationale

### ✅ Checklist

Before finalizing tests:

- [ ] Tests follow existing patterns exactly
- [ ] All edge cases covered
- [ ] Mocks match project style
- [ ] Tests are isolated and repeatable
- [ ] No test interdependencies
- [ ] Clear test names and descriptions
- [ ] Tests run quickly (< 100ms each ideally)
- [ ] No hardcoded values that might break

### 🚀 Next Steps

1. **Run tests:** Verify all tests pass
2. **Check coverage:** Ensure adequate coverage
3. **Add to CI:** Include in test suite
4. **Document:** Update test documentation if needed
