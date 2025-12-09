---
description: Add comprehensive type hints and type annotations following language best practices
argument-hint: [file/directory] [--strict] (strict mode for maximum type coverage)
---

# Type Hints & Annotations

**Target:** $ARGUMENTS

## Type Analysis Process

### 1. Identify Language and Type System

Detect the language and available type system:
- Python → Type hints (3.5+), typing module, Optional, Union, Literal
- TypeScript → Full type system, interfaces, generics
- JavaScript → JSDoc type annotations or migrate to TypeScript
- Go → Static types (already enforced)
- Java/C#/C++ → Static types (already enforced)
- Rust → Static types with inference

Check for existing type checking configuration:
- Python: mypy.ini, pyproject.toml, setup.cfg
- TypeScript: tsconfig.json strictness settings
- JavaScript: JSDoc conventions or @ts-check

### 2. Analyze Current Type Coverage

Identify missing type information:
- Function parameters without types
- Function return types missing
- Class attributes untyped
- Variables needing annotation
- Generic types using Any/any/unknown
- Callback/function types undefined
- Dictionary/object shapes unspecified

### 3. Type Hint Standards

Apply appropriate typing for each language:

**Python Type Hints:**
```python
from typing import List, Dict, Optional, Union, Tuple, Callable, TypeVar, Generic
from typing import Protocol, Literal, TypedDict, Final  # Python 3.8+
from collections.abc import Iterator, Sequence  # Python 3.9+ prefer stdlib generics

def process_data(
    items: List[str],
    config: Dict[str, Any],
    callback: Optional[Callable[[str], bool]] = None
) -> Tuple[List[str], int]:
    """Process items with optional filtering."""
    pass

class DataProcessor:
    def __init__(self, name: str, batch_size: int = 100) -> None:
        self.name: str = name
        self.batch_size: int = batch_size
        self._cache: Dict[str, Any] = {}

    async def process_async(
        self,
        data: bytes
    ) -> List[Dict[str, Union[str, int, float]]]:
        pass
```

**TypeScript Types:**
```typescript
interface Config {
    apiUrl: string;
    timeout: number;
    retries?: number;
}

type Status = 'pending' | 'active' | 'completed';
type Callback<T> = (data: T) => void | Promise<void>;

function processData<T extends object>(
    items: T[],
    config: Config,
    callback?: Callback<T>
): [T[], number] {
    // implementation
}

class DataProcessor<T = unknown> {
    private cache: Map<string, T>;

    constructor(
        public readonly name: string,
        private batchSize: number = 100
    ) {}

    async process(data: Buffer): Promise<Record<string, string | number>[]> {
        // implementation
    }
}
```

**JavaScript with JSDoc:**
```javascript
/**
 * @typedef {Object} Config
 * @property {string} apiUrl
 * @property {number} timeout
 * @property {number} [retries]
 */

/**
 * @template T
 * @callback ProcessCallback
 * @param {T} data
 * @returns {void|Promise<void>}
 */

/**
 * Process data items with configuration
 * @template {object} T
 * @param {T[]} items - Items to process
 * @param {Config} config - Configuration object
 * @param {ProcessCallback<T>} [callback] - Optional callback
 * @returns {[T[], number]} Processed items and count
 */
function processData(items, config, callback) {
    // implementation
}
```

### 4. Complex Type Patterns

Handle advanced typing scenarios:

**Union and Literal Types:**
```python
# Python
from typing import Union, Literal
ResponseType = Union[dict, list, str, None]
Method = Literal["GET", "POST", "PUT", "DELETE"]

# TypeScript
type ResponseType = object | array | string | null;
type Method = "GET" | "POST" | "PUT" | "DELETE";
```

**Generic Types:**
```python
# Python
T = TypeVar('T')
def first(items: Sequence[T]) -> Optional[T]:
    return items[0] if items else None

# TypeScript
function first<T>(items: T[]): T | undefined {
    return items[0];
}
```

**Protocol/Interface Types:**
```python
# Python
from typing import Protocol

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

# TypeScript
interface Comparable<T> {
    compareTo(other: T): number;
}
```

### 5. Type Checking Validation

Ensure types are:
- Accurate (match actual usage)
- Specific (avoid Any/any when possible)
- Complete (all parameters and returns)
- Consistent (same types for same concepts)
- Compatible (with existing type definitions)

## Type Hint Output

### 📊 Type Coverage Analysis

**Current Coverage:**
- Functions with typed parameters: X/Y
- Functions with return types: X/Y
- Class attributes typed: X/Y
- Any/any usage: Z instances

**Target Coverage:**
- Functions with typed parameters: Y/Y ✅
- Functions with return types: Y/Y ✅
- Class attributes typed: Y/Y ✅
- Any/any usage: 0 (or justified) ✅

### 🔧 Type Updates

For each file, provide the typed version:

**[filename]:**
```[language]
[Complete file with added type hints]
```

### 🎯 Type Definitions Needed

**Custom Types to Define:**
```[language]
# Type aliases for clarity
UserId = int
EmailAddress = str

# Complex type structures
UserData = TypedDict('UserData', {
    'id': UserId,
    'email': EmailAddress,
    'roles': List[str]
})
```

### ⚠️ Type Issues Found

**Inconsistencies:**
- [Function A returns `str` but caller expects `int`]
- [Parameter type mismatch between interface and implementation]

**Improvements:**
- [Replace `Any` with specific type `Dict[str, str]`]
- [Use Union type instead of accepting multiple types]

### 💡 Type Checking Setup

**For Python:**
```bash
# Install type checker
pip install mypy

# Run type checking
mypy --strict [target]
```

**For TypeScript:**
```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```

### ✅ Type Checklist

- [ ] All function parameters typed
- [ ] All function returns typed
- [ ] Class attributes have type annotations
- [ ] No unnecessary Any/any types
- [ ] Generic types used where appropriate
- [ ] Type aliases for complex types
- [ ] Passes strict type checking