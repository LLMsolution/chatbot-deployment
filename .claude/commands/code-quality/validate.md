---
description: Add input validation using Pydantic, Zod, or language-appropriate validation libraries
argument-hint: [file/directory] [--library=pydantic/zod/joi] (auto-detects if not specified)
---

# Input Validation

**Target:** $ARGUMENTS

## Validation Analysis Process

### 1. Identify Validation Needs

Scan for validation gaps:
- API endpoints receiving raw input
- Functions processing external data
- Form handlers without validation
- Database models without constraints
- Configuration parsing without checks
- File upload handlers
- JSON/XML parsing without schemas

### 2. Detect Language and Library

Choose appropriate validation approach:
- **Python** → Pydantic v2 (preferred), marshmallow, cerberus
- **TypeScript/JavaScript** → Zod (preferred), Joi, Yup, Ajv
- **Go** → go-playground/validator, ozzo-validation
- **Java** → Bean Validation, Hibernate Validator
- **C#** → FluentValidation, DataAnnotations
- **Rust** → validator crate, garde

Check existing validation patterns in the project.

### 3. Validation Patterns

Apply modern validation approaches:

**Python with Pydantic v2:**
```python
from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic import EmailStr, HttpUrl, SecretStr, conint, constr
from typing import Optional, List, Literal
from datetime import datetime
from decimal import Decimal

class UserInput(BaseModel):
    """User registration input with comprehensive validation."""

    # Basic field with constraints
    username: constr(min_length=3, max_length=20, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    age: conint(ge=13, le=120)  # Greater equal 13, less equal 120

    # Optional with defaults
    bio: Optional[str] = Field(None, max_length=500)
    website: Optional[HttpUrl] = None

    # Sensitive data
    password: SecretStr = Field(..., min_length=8)

    # Enum/Literal validation
    role: Literal['user', 'admin', 'moderator'] = 'user'

    # Complex types
    interests: List[str] = Field(default_factory=list, max_length=10)
    metadata: dict = Field(default_factory=dict)

    # Field validators (Pydantic v2 style)
    @field_validator('username')
    @classmethod
    def username_not_reserved(cls, v: str) -> str:
        reserved = ['admin', 'root', 'system']
        if v.lower() in reserved:
            raise ValueError(f'Username {v} is reserved')
        return v

    @field_validator('interests', mode='before')
    @classmethod
    def validate_interests(cls, v: List[str]) -> List[str]:
        if len(v) > 10:
            raise ValueError('Maximum 10 interests allowed')
        return [interest.strip().lower() for interest in v]

    # Model validator for cross-field validation
    @model_validator(mode='after')
    def validate_admin_age(self) -> 'UserInput':
        if self.role == 'admin' and self.age < 18:
            raise ValueError('Admins must be 18 or older')
        return self

    model_config = {
        'str_strip_whitespace': True,  # Auto strip strings
        'validate_assignment': True,    # Validate on attribute assignment
        'use_enum_values': True,
        'json_schema_extra': {
            'examples': [
                {
                    'username': 'john_doe',
                    'email': 'john@example.com',
                    'age': 25,
                    'password': 'SecurePass123!'
                }
            ]
        }
    }
```

**TypeScript with Zod:**
```typescript
import { z } from 'zod';

// Define validation schema
const UserInputSchema = z.object({
    username: z.string()
        .min(3, 'Username too short')
        .max(20, 'Username too long')
        .regex(/^[a-zA-Z0-9_]+$/, 'Invalid characters in username'),

    email: z.string().email('Invalid email address'),

    age: z.number()
        .int('Age must be an integer')
        .min(13, 'Must be at least 13')
        .max(120, 'Invalid age'),

    bio: z.string().max(500).optional(),

    website: z.string().url().optional(),

    password: z.string()
        .min(8, 'Password too short')
        .regex(/[A-Z]/, 'Must contain uppercase')
        .regex(/[0-9]/, 'Must contain number'),

    role: z.enum(['user', 'admin', 'moderator']).default('user'),

    interests: z.array(z.string()).max(10).default([]),

    metadata: z.record(z.unknown()).default({})
})
// Refine for cross-field validation
.refine(
    (data) => !(data.role === 'admin' && data.age < 18),
    {
        message: 'Admins must be 18 or older',
        path: ['role']
    }
);

// Type inference
type UserInput = z.infer<typeof UserInputSchema>;

// Usage
function validateUser(data: unknown): UserInput {
    return UserInputSchema.parse(data);  // Throws if invalid
    // or
    const result = UserInputSchema.safeParse(data);
    if (!result.success) {
        console.error(result.error.format());
    }
}
```

**JavaScript with Joi:**
```javascript
const Joi = require('joi');

const userInputSchema = Joi.object({
    username: Joi.string()
        .alphanum()
        .min(3)
        .max(20)
        .required(),

    email: Joi.string()
        .email()
        .required(),

    age: Joi.number()
        .integer()
        .min(13)
        .max(120)
        .required(),

    bio: Joi.string()
        .max(500)
        .optional(),

    password: Joi.string()
        .min(8)
        .pattern(/[A-Z]/)
        .pattern(/[0-9]/)
        .required(),

    role: Joi.string()
        .valid('user', 'admin', 'moderator')
        .default('user'),

    interests: Joi.array()
        .items(Joi.string())
        .max(10)
        .default([])
})
.custom((value, helpers) => {
    if (value.role === 'admin' && value.age < 18) {
        return helpers.error('any.invalid');
    }
    return value;
});
```

### 4. Common Validation Patterns

**Email Validation:**
```python
# Pydantic v2
from pydantic import EmailStr
email: EmailStr
```

**URL Validation:**
```python
# Pydantic v2
from pydantic import HttpUrl, AnyUrl
website: HttpUrl
api_endpoint: AnyUrl
```

**Phone Numbers:**
```python
# Pydantic v2 with custom validator
from pydantic import field_validator
import re

@field_validator('phone')
@classmethod
def validate_phone(cls, v: str) -> str:
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, v):
        raise ValueError('Invalid phone number')
    return v
```

**Credit Cards:**
```python
# Pydantic v2
from pydantic import Field
import re

card_number: str = Field(..., pattern=r'^\d{13,19}$')
```

**File Uploads:**
```python
# Pydantic v2
from pydantic import field_validator

@field_validator('file_size')
@classmethod
def validate_file_size(cls, v: int) -> int:
    max_size = 10 * 1024 * 1024  # 10MB
    if v > max_size:
        raise ValueError('File too large')
    return v
```

### 5. API Integration

Connect validation to endpoints:

**FastAPI with Pydantic v2:**
```python
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

app = FastAPI()

@app.post("/users/")
async def create_user(user: UserInput):  # Automatic validation
    # user is already validated
    return {"message": "User created", "username": user.username}
```

**Express with Zod:**
```typescript
import express from 'express';

app.post('/users', async (req, res) => {
    try {
        const validated = UserInputSchema.parse(req.body);
        // Process validated data
        res.json({ message: 'User created', username: validated.username });
    } catch (error) {
        if (error instanceof z.ZodError) {
            res.status(400).json({ errors: error.format() });
        }
    }
});
```

## Validation Output

### 📊 Validation Coverage

**Current State:**
- Unvalidated endpoints: X
- Raw input processing: Y locations
- Missing data models: Z

**After Implementation:**
- All endpoints validated ✅
- Input models defined ✅
- Validation errors handled ✅

### 🔧 Validation Updates

For each file needing validation:

**[filename]:**
```[language]
[Complete implementation with validation added]
```

### 🎯 Validation Models Created

**New Models/Schemas:**
```[language]
# User input validation
[UserInput model]

# Config validation
[ConfigSchema model]

# API request validation
[RequestModel model]
```

### ⚠️ Security Improvements

**Prevented Vulnerabilities:**
- SQL injection (via input sanitization)
- XSS (via HTML escaping)
- Path traversal (via path validation)
- Buffer overflow (via size limits)

### 💡 Validation Best Practices

Based on this codebase:
- Use strict validation at boundaries
- Fail fast with clear error messages
- Validate early in the request cycle
- Keep validation rules DRY
- Document validation constraints

### ✅ Validation Checklist

- [ ] All API endpoints have input validation
- [ ] File uploads have size/type restrictions
- [ ] User inputs are sanitized
- [ ] Configuration is validated on load
- [ ] Database inputs are validated
- [ ] Error messages are user-friendly
- [ ] Validation is tested