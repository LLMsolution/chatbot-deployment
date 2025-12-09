---
description: Set up or improve configuration management and environment handling
argument-hint: [--library=dotenv/viper/config] [--generate-example]
---

# Configuration Management

**Options:** $ARGUMENTS

## Config Analysis

### 1. Current Setup

Check configuration approach:
- Environment variables (.env files)
- Config files (JSON, YAML, TOML)
- Hard-coded values
- Multiple environments (dev, staging, prod)
- Secret management

### 2. Best Practices

Apply these patterns:

**Environment Variables:**
```bash
# .env.example (commit this)
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=your_api_key_here
NODE_ENV=development
LOG_LEVEL=info

# .env (gitignored)
DATABASE_URL=postgresql://prod:secret@db/prod
API_KEY=sk_live_abc123
```

**JavaScript/TypeScript:**
```typescript
// config.ts
import dotenv from 'dotenv';
import { z } from 'zod';

const ConfigSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  PORT: z.string().transform(Number).default('3000'),
  NODE_ENV: z.enum(['development', 'production', 'test']),
  LOG_LEVEL: z.enum(['error', 'warn', 'info', 'debug']).default('info')
});

export const config = ConfigSchema.parse(process.env);
```

**Python:**
```python
# config.py
from pydantic import BaseSettings, Field, SecretStr
from typing import Literal

class Settings(BaseSettings):
    database_url: str
    api_key: SecretStr
    port: int = 3000
    environment: Literal['development', 'production', 'test']
    log_level: Literal['error', 'warn', 'info', 'debug'] = 'info'

    class Config:
        env_file = '.env'
        case_sensitive = False

settings = Settings()
```

**Go:**
```go
// config.go
type Config struct {
    DatabaseURL string `env:"DATABASE_URL,required"`
    APIKey      string `env:"API_KEY,required"`
    Port        int    `env:"PORT" envDefault:"3000"`
    Environment string `env:"NODE_ENV" envDefault:"development"`
    LogLevel    string `env:"LOG_LEVEL" envDefault:"info"`
}
```

### 3. Secret Management

- Never commit secrets
- Use .env.example as template
- Consider secret managers (Vault, AWS Secrets)
- Rotate keys regularly

## Configuration Setup

### 📋 Current Issues

**Problems Found:**
- Hard-coded values: [count]
- Missing validation: [locations]
- Secrets in code: [CRITICAL]

### 🔧 Improvements

**Config Module:**
```[language]
[Complete config setup]
```

**.env.example:**
```bash
[Template with all variables]
```

**Validation:**
```[language]
[Config validation code]
```

### ✅ Checklist

- [ ] All config externalized
- [ ] .env.example created
- [ ] Secrets removed from code
- [ ] Config validation added
- [ ] Different env support
- [ ] Documentation updated
- [ ] .env in .gitignore