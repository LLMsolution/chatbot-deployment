---
description: Implement comprehensive error handling and recovery
argument-hint: [file/directory] [--style=try-catch/result/option]
---

# Error Handling

**Target:** $ARGUMENTS

## Error Analysis

### 1. Find Error Gaps

Look for:
- Unhandled promises/async operations
- Missing try-catch blocks
- Ignored error returns
- Console.error instead of proper handling
- Generic catch-all handlers
- Missing validation errors

### 2. Apply Error Patterns

**JavaScript/TypeScript:**
```typescript
// Async error wrapper
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Custom error class
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}
```

**Python:**
```python
# Custom exceptions
class ValidationError(Exception):
    """Raised when validation fails"""
    pass

# Context manager
from contextlib import contextmanager

@contextmanager
def error_handler():
    try:
        yield
    except ValidationError as e:
        logger.warning(f"Validation failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise
```

**Go:**
```go
// Error wrapping
if err != nil {
    return fmt.Errorf("failed to process: %w", err)
}

// Custom error types
type ValidationError struct {
    Field string
    Value interface{}
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation failed for %s: %v", e.Field, e.Value)
}
```

### 3. Recovery Strategies

- Retry with exponential backoff
- Circuit breaker pattern
- Graceful degradation
- Fallback values
- Error boundaries (React)
- Rollback transactions

## Error Improvements

### 📋 Current Issues

**Unhandled Errors:** [count]
**Generic Handlers:** [count]
**Missing Recovery:** [locations]

### 🔧 Implementations

**Global Error Handler:**
```[language]
[Global error handling setup]
```

**Specific Error Types:**
```[language]
[Custom error classes]
```

**Recovery Mechanisms:**
```[language]
[Retry/fallback logic]
```

### ✅ Checklist

- [ ] All promises have .catch()
- [ ] Async functions wrapped
- [ ] Custom error types defined
- [ ] Logging implemented
- [ ] User-friendly messages
- [ ] Recovery strategies added
- [ ] Tests for error cases