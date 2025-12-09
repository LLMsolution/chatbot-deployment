---
description: Define comprehensive API contract for backend-frontend coordination
argument-hint: [feature-name] [--style rest|graphql] [--auth jwt|oauth|basic]
---

# API Contract Definition: $1

**API Style:** $2 (defaults to REST)
**Auth Method:** $3 (defaults to JWT)

## Phase 1: Feature Analysis

### 1. Understand Feature Requirements

Analyze the feature: $1

**Context Discovery:**
- Feature domain: [e.g., user management, payments, etc.]
- Data entities involved: [list entities]
- Operations needed: [CRUD, custom actions]
- Real-time requirements: [websockets needed?]
- File upload/download: [required?]

### 2. Codebase Convention Analysis

**Examine existing API patterns:**
```bash
# Search for similar endpoints
- Naming conventions (camelCase vs snake_case)
- URL structure (/api/v1/ vs /api/)
- Response wrapper patterns
- Error handling format
- Pagination style
- Authentication headers
```

## Phase 2: API Specification

### 1. RESTful Endpoints

```yaml
# API Base Configuration
base_url: /api/v1
version: 1.0.0
content_type: application/json
authentication: Bearer {token}

# Resource: $1
resource_name: {feature}
resource_plural: {features}

# Standard CRUD Endpoints
endpoints:
  list:
    method: GET
    path: /{features}
    description: List all {features} with pagination and filtering
    query_params:
      - page: integer (default: 0)
      - size: integer (default: 20, max: 100)
      - sort: string (format: "field,direction")
      - filter: string (format: "field:operator:value")
      - search: string (full-text search)
    response: Page<{Feature}Response>
    status_codes: [200]

  get:
    method: GET
    path: /{features}/{id}
    description: Get single {feature} by ID
    path_params:
      - id: string|number (UUID or Long)
    response: {Feature}Response
    status_codes: [200, 404]

  create:
    method: POST
    path: /{features}
    description: Create new {feature}
    request_body: {Feature}CreateRequest
    response: {Feature}Response
    status_codes: [201, 400, 409]

  update:
    method: PUT
    path: /{features}/{id}
    description: Update entire {feature}
    path_params:
      - id: string|number
    request_body: {Feature}UpdateRequest
    response: {Feature}Response
    status_codes: [200, 400, 404]

  patch:
    method: PATCH
    path: /{features}/{id}
    description: Partial update of {feature}
    path_params:
      - id: string|number
    request_body: {Feature}PatchRequest
    response: {Feature}Response
    status_codes: [200, 400, 404]

  delete:
    method: DELETE
    path: /{features}/{id}
    description: Delete {feature}
    path_params:
      - id: string|number
    response: null
    status_codes: [204, 404]

# Custom Endpoints (domain-specific)
custom_endpoints:
  activate:
    method: POST
    path: /{features}/{id}/activate
    description: Activate a {feature}
    response: {Feature}Response
    status_codes: [200, 404, 409]

  bulk_operation:
    method: POST
    path: /{features}/bulk
    description: Bulk operations on {features}
    request_body: BulkOperationRequest
    response: BulkOperationResponse
    status_codes: [200, 207, 400]
```

### 2. Data Transfer Objects (DTOs)

**TypeScript/Frontend Definitions:**
```typescript
// Base types
type UUID = string;
type ISODateTime = string; // ISO 8601 format

// Request DTOs
interface {Feature}CreateRequest {
  // Required fields
  name: string;           // min: 2, max: 100
  type: {Feature}Type;    // enum

  // Optional fields
  description?: string;   // max: 1000
  metadata?: Record<string, unknown>;
  tags?: string[];        // max: 10 items

  // Nested objects
  settings?: {
    enabled: boolean;
    priority: number;     // 1-10
    config?: unknown;
  };
}

interface {Feature}UpdateRequest extends {Feature}CreateRequest {
  // All fields from create request
  // Additional update-only fields
  version?: number;       // Optimistic locking
}

interface {Feature}PatchRequest {
  // All fields optional for partial update
  name?: string;
  description?: string;
  settings?: Partial<{Feature}Settings>;
}

// Response DTOs
interface {Feature}Response {
  // System fields
  id: UUID;
  createdAt: ISODateTime;
  updatedAt: ISODateTime;
  createdBy?: string;
  updatedBy?: string;
  version: number;

  // Business fields
  name: string;
  type: {Feature}Type;
  description?: string;
  status: {Feature}Status;
  metadata?: Record<string, unknown>;
  tags: string[];

  // Computed fields
  displayName: string;
  isActive: boolean;
  permissions?: string[];

  // Relations (embedded or referenced)
  owner?: UserSummary;
  children?: {Feature}Summary[];
  _links?: {
    self: string;
    update: string;
    delete: string;
  };
}

// Pagination wrapper
interface Page<T> {
  content: T[];
  page: {
    size: number;
    number: number;
    totalElements: number;
    totalPages: number;
  };
  sort?: {
    sorted: boolean;
    ascending: boolean;
    property?: string;
  };
  _links?: {
    first?: string;
    prev?: string;
    self: string;
    next?: string;
    last?: string;
  };
}

// Enums
enum {Feature}Type {
  BASIC = 'BASIC',
  PREMIUM = 'PREMIUM',
  ENTERPRISE = 'ENTERPRISE'
}

enum {Feature}Status {
  DRAFT = 'DRAFT',
  ACTIVE = 'ACTIVE',
  INACTIVE = 'INACTIVE',
  ARCHIVED = 'ARCHIVED'
}

// Error response
interface ErrorResponse {
  timestamp: ISODateTime;
  status: number;
  error: string;
  message: string;
  path: string;
  requestId?: string;
  errors?: ValidationError[];
}

interface ValidationError {
  field: string;
  code: string;
  message: string;
  rejectedValue?: unknown;
}
```

**Backend/Java Definitions:**
```java
// Request DTOs
@Data
@NoArgsConstructor
@AllArgsConstructor
public class {Feature}CreateRequest {
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100)
    private String name;

    @NotNull(message = "Type is required")
    private {Feature}Type type;

    @Size(max = 1000)
    private String description;

    @Valid
    private {Feature}Settings settings;

    @Size(max = 10)
    private List<@NotBlank String> tags;
}

// Response DTOs
@Data
@Builder
public class {Feature}Response {
    private UUID id;
    private String name;
    private {Feature}Type type;
    private String description;
    private {Feature}Status status;

    @JsonFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss'Z'")
    private LocalDateTime createdAt;

    @JsonFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss'Z'")
    private LocalDateTime updatedAt;

    private String createdBy;
    private String updatedBy;
    private Long version;

    // Computed fields
    public String getDisplayName() {
        return name.toUpperCase();
    }

    @JsonProperty("isActive")
    public boolean isActive() {
        return status == {Feature}Status.ACTIVE;
    }
}
```

### 3. Validation Rules

**Comprehensive Validation Matrix:**

| Field | Frontend (Zod) | Backend (Bean Validation) | Database |
|-------|----------------|--------------------------|----------|
| name | z.string().min(2).max(100) | @Size(min=2, max=100) | VARCHAR(100) NOT NULL |
| email | z.string().email() | @Email | VARCHAR(255) |
| phone | z.string().regex(/^\+?[1-9]\d{1,14}$/) | @Pattern | VARCHAR(20) |
| url | z.string().url() | @URL | TEXT |
| date | z.string().datetime() | @DateTimeFormat | TIMESTAMP |
| amount | z.number().positive().max(1000000) | @Positive @Max(1000000) | DECIMAL(10,2) |
| tags | z.array(z.string()).max(10) | @Size(max=10) | JSON |

**Custom Validation Rules:**
```typescript
// Frontend Zod schema
const {Feature}Schema = z.object({
  name: z.string()
    .min(2, 'Name must be at least 2 characters')
    .max(100, 'Name must not exceed 100 characters')
    .regex(/^[a-zA-Z0-9-_ ]+$/, 'Name contains invalid characters'),

  type: z.enum(['BASIC', 'PREMIUM', 'ENTERPRISE']),

  settings: z.object({
    enabled: z.boolean(),
    priority: z.number().int().min(1).max(10),
    config: z.record(z.unknown()).optional()
  }).optional(),

  metadata: z.record(z.unknown())
    .refine((meta) => Object.keys(meta).length <= 50, {
      message: 'Metadata cannot have more than 50 keys'
    })
}).refine((data) => {
  // Cross-field validation
  if (data.type === 'ENTERPRISE' && !data.settings?.enabled) {
    return false;
  }
  return true;
}, {
  message: 'Enterprise features must be enabled'
});
```

### 4. Error Handling

**Standardized Error Responses:**

```json
// 400 Bad Request - Validation Error
{
  "timestamp": "2024-01-20T10:30:00.000Z",
  "status": 400,
  "error": "Bad Request",
  "message": "Validation failed for object '{feature}'",
  "path": "/api/v1/{features}",
  "requestId": "abc-123-def",
  "errors": [
    {
      "field": "name",
      "code": "Size",
      "message": "Name must be between 2 and 100 characters",
      "rejectedValue": "a"
    },
    {
      "field": "settings.priority",
      "code": "Range",
      "message": "Priority must be between 1 and 10",
      "rejectedValue": 15
    }
  ]
}

// 404 Not Found
{
  "timestamp": "2024-01-20T10:30:00.000Z",
  "status": 404,
  "error": "Not Found",
  "message": "{Feature} not found with id: 123",
  "path": "/api/v1/{features}/123",
  "requestId": "xyz-456-abc"
}

// 409 Conflict
{
  "timestamp": "2024-01-20T10:30:00.000Z",
  "status": 409,
  "error": "Conflict",
  "message": "{Feature} with name 'Example' already exists",
  "path": "/api/v1/{features}",
  "requestId": "def-789-ghi"
}

// 500 Internal Server Error
{
  "timestamp": "2024-01-20T10:30:00.000Z",
  "status": 500,
  "error": "Internal Server Error",
  "message": "An unexpected error occurred",
  "path": "/api/v1/{features}",
  "requestId": "ghi-012-jkl"
}
```

**Status Code Matrix:**

| Code | Meaning | When to Use | Response Body |
|------|---------|------------|---------------|
| 200 | OK | Successful GET, PUT, PATCH | Resource data |
| 201 | Created | Successful POST | Created resource |
| 204 | No Content | Successful DELETE | Empty |
| 400 | Bad Request | Validation failure | Error details |
| 401 | Unauthorized | Missing/invalid auth | Error message |
| 403 | Forbidden | Insufficient permissions | Error message |
| 404 | Not Found | Resource doesn't exist | Error message |
| 409 | Conflict | Duplicate/state conflict | Error details |
| 422 | Unprocessable | Business rule violation | Error details |
| 429 | Too Many Requests | Rate limit exceeded | Retry-After header |
| 500 | Server Error | Unexpected error | Generic message |
| 503 | Service Unavailable | Maintenance/overload | Retry-After header |

### 5. Authentication & Authorization

**Headers Configuration:**
```yaml
# Authentication headers
Authorization: Bearer {jwt_token}
X-API-Key: {api_key}  # Alternative/additional

# Request headers
Content-Type: application/json
Accept: application/json
X-Request-ID: {uuid}  # Tracking
X-Client-Version: 1.0.0

# Response headers
X-Request-ID: {uuid}
X-Rate-Limit-Remaining: 100
X-Rate-Limit-Reset: 1642684800
```

**JWT Token Structure:**
```json
{
  "sub": "user-id",
  "email": "user@example.com",
  "roles": ["USER", "ADMIN"],
  "permissions": ["read:{feature}", "write:{feature}"],
  "exp": 1642684800,
  "iat": 1642681200
}
```

### 6. Integration Requirements

**CORS Configuration:**
```yaml
allowed_origins:
  - http://localhost:3000
  - https://app.example.com
allowed_methods: [GET, POST, PUT, PATCH, DELETE, OPTIONS]
allowed_headers: [Authorization, Content-Type, X-Request-ID]
exposed_headers: [X-Request-ID, X-Rate-Limit-Remaining]
max_age: 3600
```

**Rate Limiting:**
```yaml
limits:
  - endpoint: GET /api/v1/*
    limit: 1000/hour
  - endpoint: POST /api/v1/*
    limit: 100/hour
  - endpoint: DELETE /api/v1/*
    limit: 50/hour
```

**Pagination Standards:**
```typescript
// Request
GET /api/v1/{features}?page=0&size=20&sort=name,asc&filter=status:eq:ACTIVE

// Response headers
X-Total-Count: 150
X-Page-Number: 0
X-Page-Size: 20
Link: <...?page=1>; rel="next", <...?page=7>; rel="last"
```

## Phase 3: Implementation Guidelines

### Backend Implementation

**Controller Example:**
```java
@RestController
@RequestMapping("/api/v1/{features}")
@Tag(name = "{Feature}", description = "{Feature} management APIs")
public class {Feature}Controller {

    @GetMapping
    @Operation(summary = "List all {features}")
    public ResponseEntity<Page<{Feature}Response>> list(
            @PageableDefault(size = 20, sort = "createdAt,desc") Pageable pageable,
            @RequestParam(required = false) String filter) {
        // Implementation
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Create new {feature}")
    public {Feature}Response create(
            @Valid @RequestBody {Feature}CreateRequest request) {
        // Implementation
    }
}
```

### Frontend Implementation

**API Client Example:**
```typescript
// API client setup
const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API service
export const {Feature}API = {
  list: (params: ListParams) =>
    apiClient.get<Page<{Feature}Response>>('/{features}', { params }),

  get: (id: string) =>
    apiClient.get<{Feature}Response>(`/{features}/${id}`),

  create: (data: {Feature}CreateRequest) =>
    apiClient.post<{Feature}Response>('/{features}', data),
};

// React Query hook
export const use{Features} = (params: ListParams) => {
  return useQuery({
    queryKey: ['{features}', params],
    queryFn: () => {Feature}API.list(params),
  });
};
```

## Phase 4: Testing Contract

### Contract Tests

**Backend Contract Test:**
```java
@Test
void shouldReturn{Feature}WithCorrectStructure() {
    mockMvc.perform(get("/api/v1/{features}/1"))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.id").exists())
        .andExpect(jsonPath("$.name").isString())
        .andExpect(jsonPath("$.createdAt").matches(ISO_DATE_PATTERN));
}
```

**Frontend Contract Test:**
```typescript
describe('{Feature} API Contract', () => {
  it('should match response schema', async () => {
    const response = await {Feature}API.get('123');
    expect({Feature}ResponseSchema.parse(response)).toBeDefined();
  });
});
```

## Phase 5: Documentation

### OpenAPI/Swagger Specification

Generate OpenAPI spec file: `api-specs/{feature}-openapi.yaml`

```yaml
openapi: 3.0.3
info:
  title: {Feature} API
  version: 1.0.0
paths:
  /{features}:
    get:
      summary: List {features}
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Page{Feature}Response'
```

### API Documentation

Generate markdown documentation: `docs/api/{feature}-api.md`

## Phase 6: Save Contract

### File Structure

Save all contract files:

```
api-contracts/
├── {feature}/
│   ├── contract.md           # This complete contract
│   ├── openapi.yaml          # OpenAPI specification
│   ├── postman.json          # Postman collection
│   ├── frontend/
│   │   ├── types.ts          # TypeScript definitions
│   │   ├── schemas.ts        # Zod validation schemas
│   │   └── api-client.ts     # API client implementation
│   └── backend/
│       ├── dtos.java         # Java DTOs
│       ├── controller.java   # Controller interface
│       └── validation.java   # Validation rules
```

### Contract Validation Checklist

Before finalizing:
- [ ] All CRUD operations defined
- [ ] Request/response DTOs complete
- [ ] Validation rules specified
- [ ] Error responses standardized
- [ ] Status codes documented
- [ ] Authentication method clear
- [ ] Rate limits defined
- [ ] CORS settings specified
- [ ] Pagination format agreed
- [ ] Frontend types match backend
- [ ] Contract tests created
- [ ] OpenAPI spec generated
- [ ] Examples provided

**Contract Status:** [Draft/Reviewed/Approved]
**Version:** 1.0.0
**Last Updated:** [Date]
**Teams Aligned:** Backend ✓ Frontend ✓