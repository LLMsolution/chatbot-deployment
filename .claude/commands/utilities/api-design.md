---
description: Review and improve REST/GraphQL API design patterns
argument-hint: [file/directory] [REST/GraphQL]
---

# API Design Review

**Target:** $ARGUMENTS

## API Analysis

### 1. Scan API Structure

Find API definitions:
- Route files (routes/, api/, endpoints/)
- Controller/handler files
- GraphQL schemas and resolvers
- OpenAPI/Swagger definitions
- API documentation

### 2. Review Current Design

Check for these patterns:

**RESTful Principles:**
- Resource-based URLs (/users, /posts)
- Proper HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 201, 400, 401, 404, 500)
- Consistent naming (plural nouns, kebab-case)

**GraphQL Best Practices:**
- Schema organization
- Resolver efficiency
- N+1 query problems
- Proper mutations vs queries

### 3. Common Issues to Fix

- Inconsistent naming conventions
- Missing pagination
- No versioning strategy
- Poor error responses
- Missing rate limiting
- No HATEOAS links
- Overfetching/underfetching

## Improvements

### 📋 API Assessment

**Current State:**
- [REST/GraphQL/Mixed]
- Consistency: [Score]
- Documentation: [Present/Missing]

### 🔧 Recommended Changes

**URL Structure:**
```
Current: [problematic endpoints]
Better:  [improved endpoints]
```

**Response Format:**
```json
{
  "data": {},
  "meta": {
    "page": 1,
    "total": 100
  },
  "links": {
    "self": "/api/v1/users?page=1",
    "next": "/api/v1/users?page=2"
  }
}
```

**Error Handling:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": []
  }
}
```

### ✅ Checklist

- [ ] Consistent resource naming
- [ ] Proper HTTP methods
- [ ] Pagination implemented
- [ ] Versioning strategy
- [ ] Error format standardized
- [ ] Rate limiting added
- [ ] Documentation updated