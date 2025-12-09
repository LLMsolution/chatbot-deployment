---
description: Add comprehensive documentation with docstrings and inline comments following language conventions
argument-hint: [file/directory] [--style=google/jsdoc/golang] (auto-detects if not specified)
---

# Code Documentation

**Target:** $ARGUMENTS

## Documentation Process

### 1. Identify Language and Style

Detect the language from file extensions and existing patterns:
- Python → Google Style docstrings (default) or NumPy/Sphinx
- JavaScript/TypeScript → JSDoc
- Go → Godoc format
- Java → Javadoc
- Rust → Rust doc comments
- C/C++ → Doxygen style

Look for existing documentation patterns in the codebase to match style.

### 2. Analyze Code Structure

For each file, identify what needs documentation:
- Functions/methods without docstrings
- Classes missing descriptions
- Complex logic blocks needing explanation
- Magic numbers or unclear constants
- Public APIs lacking usage examples
- Modules/packages missing overview docs

### 3. Documentation Standards

Apply the appropriate style for the language:

**Python (Google Style):**
```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of function purpose.

    More detailed explanation if needed, describing what the
    function does and any important behavior.

    Args:
        param1: Description of first parameter.
        param2: Description of second parameter.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param2 is negative.

    Example:
        >>> function_name("test", 42)
        True
    """
```

**JavaScript/TypeScript (JSDoc):**
```javascript
/**
 * Brief description of function purpose.
 *
 * More detailed explanation if needed.
 *
 * @param {string} param1 - Description of first parameter
 * @param {number} param2 - Description of second parameter
 * @returns {boolean} Description of return value
 * @throws {Error} When invalid input provided
 *
 * @example
 * // Example usage
 * functionName("test", 42);
 */
```

**Go (Godoc):**
```go
// FunctionName performs a specific task.
// It takes a string and integer, returning a boolean result.
//
// The detailed behavior explanation goes here if needed.
//
// Example:
//
//	result := FunctionName("test", 42)
//	if result {
//	    fmt.Println("Success")
//	}
func FunctionName(param1 string, param2 int) bool {
```

**Inline Comments Guidelines:**
- Explain WHY, not WHAT (code shows what)
- Complex algorithms need step-by-step comments
- Business logic needs context
- Workarounds need explanation and TODO if temporary
- Performance optimizations need justification

### 4. Generate Documentation

For the target code:

**Functions/Methods:**
- One-line summary (imperative mood)
- Detailed description if complex
- Parameter descriptions with types
- Return value description
- Exceptions/errors that can be raised
- Usage examples for public APIs

**Classes:**
- Purpose and responsibility
- Important attributes
- Relationship to other classes
- Usage examples
- Thread safety notes if relevant

**Modules/Files:**
- Module-level docstring explaining purpose
- List of public exports
- Usage examples
- Dependencies and requirements

**Inline Comments:**
- Above complex logic blocks
- For non-obvious algorithms
- Explaining business rules
- Marking TODOs with context

### 5. Quality Checks

Ensure documentation:
- Uses correct format for the language
- Is accurate and up-to-date
- Includes examples for complex functions
- Avoids redundant obvious comments
- Follows existing project patterns

## Documentation Output

### 📝 Documentation Plan

**Files to Document:** [count]
**Documentation Style:** [detected or specified]
**Existing Patterns:** [what was found]

### 🔧 Documentation Updates

For each file, provide the documented version:

**[filename]:**
- Functions needing docs: [count]
- Classes needing docs: [count]
- Complex blocks needing comments: [count]

```[language]
[Complete file with added documentation]
```

### 📊 Coverage Report

**Before:**
- Documented functions: X/Y
- Documented classes: X/Y
- Public API coverage: X%

**After:**
- Documented functions: Y/Y ✅
- Documented classes: Y/Y ✅
- Public API coverage: 100% ✅

### 💡 Documentation Tips

Based on this codebase:
- [Specific pattern to follow]
- [Common terminology to use]
- [Level of detail appropriate]

### ✅ Checklist

- [ ] All public functions have docstrings
- [ ] All classes have descriptions
- [ ] Complex logic has inline comments
- [ ] Examples provided for public APIs
- [ ] Consistent style throughout
- [ ] No redundant/obvious comments
- [ ] TODOs have context and assignee