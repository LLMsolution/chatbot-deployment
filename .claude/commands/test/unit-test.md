---
description: Generate focused unit tests for a specific function or class with mocking
argument-hint: [function/method/class] name
---

# Unit Test Generation

**Target Unit:** $ARGUMENTS

## Unit Test Strategy

### 1. Examine Test Infrastructure

Discover how unit tests are structured in this codebase:

- Locate existing unit tests for similar components
- Identify mocking strategies and test doubles
- Find test utilities and helper functions
- Understand isolation patterns used

Look for test files near the target code or in test directories to learn patterns.

### 2. Study Unit Test Patterns

Deeply analyze existing unit test examples:

- How are individual units isolated?
- What mocking library is used? (jest.mock, unittest.mock, sinon, etc.)
- How are test doubles created? (stubs, spies, mocks)
- Are there factory functions or builders?
- What's the arrange-act-assert structure?
- How are async units tested?

### 3. Analyze Unit Dependencies

Think harder about what needs to be mocked:

- External dependencies (APIs, databases, file system)
- Other modules/classes this unit depends on
- Time-dependent functionality (Date.now, setTimeout)
- Random values (Math.random, uuid)
- Environment variables and configuration
- Global state or singletons

### 4. Unit-Specific Edge Cases

Consider all paths through this specific unit:

**Input Validation:**

- Each parameter's valid range
- Type coercion scenarios
- Optional vs required parameters
- Default parameter behavior

**Control Flow:**

- Each if/else branch
- Each case in switch statements
- Early returns
- Loop iterations (0, 1, many)
- Recursion base and edge cases

**Error Handling:**

- Each catch block
- Error propagation
- Cleanup in finally blocks
- Custom error types

## Required Output Format

### 🎯 Unit Test Focus

**Unit Under Test:** `[module.function or Class.method]`

**Dependencies to Mock:**

- `[Dependency 1]` - [why it needs mocking]
- `[Dependency 2]` - [why it needs mocking]
- `[Dependency 3]` - [why it needs mocking]

### 🧪 Generated Unit Tests

```[language]
// Following existing test file patterns from the codebase
[imports matching project style]

// Mock setup following project conventions
[mock declarations as found in existing tests]

[describe/class/suite matching project pattern]('[Unit Name]', () => {

  // Shared test setup
  let [variables following project patterns];

  [beforeEach/setUp following project pattern](() => {
    // Reset mocks
    [mock reset pattern from project]

    // Initialize test fixtures
    [setup following existing patterns]
  });

  [afterEach/tearDown if used in project](() => {
    [cleanup pattern]
  });

  // Group: Core Functionality
  [describe/context]('core functionality', () => {

    [it/test]('should [expected behavior] when [condition]', () => {
      // Arrange
      const input = [test data];
      [mock setup following project patterns];

      // Act
      const result = [call unit under test];

      // Assert
      [expect/assert following project style](result).[matcher]([expected]);
      [verify mock calls if needed];
    });

    [it/test]('should handle [edge case 1]', () => {
      // Test for specific edge case
    });
  });

  // Group: Error Handling
  [describe/context]('error handling', () => {

    [it/test]('should throw when [invalid input]', () => {
      // Test error conditions
      [expect/assert pattern for errors];
    });

    [it/test]('should handle [dependency failure]', () => {
      // Mock dependency to fail
      [mock failure setup];

      // Verify graceful handling
    });
  });

  // Group: Edge Cases
  [describe/context]('edge cases', () => {

    [it/test]('should handle empty input', () => {
      // Test with null, undefined, empty
    });

    [it/test]('should handle boundary values', () => {
      // Test limits and boundaries
    });
  });

  // Group: Async Behavior (if applicable)
  [describe/context]('async behavior', () => {

    [it/test]('should resolve when [success condition]', async () => {
      // Async test following project patterns
    });

    [it/test]('should reject when [failure condition]', async () => {
      // Test promise rejection
    });
  });
});
```

### 🔬 Mock Strategy

**Mock Patterns Used:**

```[language]
// Example of mock setup following project conventions
[specific mock example from codebase]

// How this project creates test doubles
[test double pattern]

// How this project verifies mock interactions
[mock verification pattern]
```

### 📊 Coverage Report

**Unit Test Coverage:**

- **Lines:** [X/Y] lines covered (X%)
- **Branches:** [X/Y] branches covered (X%)
- **Functions:** [X/Y] functions covered (X%)

**Path Coverage:**
| Path | Covered | Test Case |
|------|---------|-----------|
| Happy path | ✅ | "should [test name]" |
| Error path 1 | ✅ | "should throw when..." |
| Edge case 1 | ✅ | "should handle empty..." |
| Edge case 2 | ❌ | Not covered: [reason] |

### 🎪 Test Isolation

**Isolation Verification:**

- ✅ No real external calls (all mocked)
- ✅ No database/file system access
- ✅ Deterministic (no random/time dependencies)
- ✅ No test interdependencies
- ✅ Runs in < 50ms

### 🏷️ Test Naming Convention

Following project pattern: `[discovered pattern]`

Examples from codebase:

- `"should return X when Y"`
- `"handles Z error correctly"`
- `"returns default when input is null"`

### 🔍 Pattern Adherence

**Matching Existing Unit Tests:**

- ✅ Mock style: `[project's mocking approach]`
- ✅ Assertion style: `[project's assertion pattern]`
- ✅ Test organization: `[project's structure]`
- ✅ Naming convention: `[project's naming]`
- ✅ Setup/teardown: `[project's pattern]`

### 💡 Testing Best Practices Applied

1. **Single Responsibility:** Each test verifies one behavior
2. **Independence:** Tests can run in any order
3. **Repeatability:** Same result every time
4. **Self-Validating:** Clear pass/fail
5. **Timely:** Fast execution
6. **Descriptive:** Clear test names explain intent

### 🚦 Quality Checks

- [ ] All dependencies properly mocked
- [ ] No implementation details tested
- [ ] Testing behavior, not implementation
- [ ] Each test has single assertion focus
- [ ] Mock verifications are meaningful
- [ ] Test data is realistic
- [ ] Error messages are helpful

### 📝 Notes

**Special Considerations:**

- [Any tricky mocking scenarios]
- [Performance considerations]
- [Known limitations]
- [Future test improvements]
