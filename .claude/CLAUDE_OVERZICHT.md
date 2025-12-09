# Claude Code Commands en Agents Overzicht

Dit document geeft een compleet overzicht van alle beschikbare slash commands en agents in Claude Code, met uitleg over wanneer je ze moet gebruiken en wat ze doen.

## Inhoudsopgave
- [Slash Commands](#slash-commands)
- [Agents](#agents)
- [Combinaties en Workflows](#combinaties-en-workflows)

---

## Slash Commands

Slash commands zijn direct uitvoerbare commando's die je kunt gebruiken binnen je conversation. Ze beginnen altijd met een `/`.

### Code Quality Commands
- **Debugging en Refactoring**: `/code-quality:debug`, `/code-quality:refactor`
- **Validatie en Documentatie**: `/code-quality:validate`, `/code-quality:document`
- **Type Hints**: `/code-quality:type-hints`

### Git Commands
- **Branch management**: `/git:branch-start`, `/git:branch-cleanup`
- **Commit workflow**: `/git:commit`, `/git:rebase-interactive`
- **Historie analyse**: `/git:history`

### GitHub Commands
- **Pull Requests**: `/github:pr-create`, `/github:pr-review`
- **Issue management**: `/github:issues`, `/github:issue-triage`

### Testing Commands
- **Test generatie**: `/test:test`, `/test:unit-test`

### Product Management Commands
- **PRD creation**: `/product:prd-generate`
- **User stories**: `/product:user-story`
- **Technical breakdowns**: `/product:technical-breakdown`

### Python Specifiek
- **Project management**: `/python:pyproject-organize`, `/python:uv-dependencies`

### Review Commands
- **Code review**: `/review:review`, `/review:review-follow-up`

### Primers (Essentieel!)
- **Project context**: `/primers:prime-specific`
- **Diepe analyse**: `/primers:prime-deep`

### Utilities
- **Error handling**: `/utilities:error-handling`
- **API design**: `/utilities:api-design`
- **Dependencies**: `/utilities:dependencies`

---

## Agents

Agents zijn gespecialiseerde AI-assistenten die in een geïsoleerde context werken voor specifieke taken.

### Codebase Analysts
- **Codebase-analyst**: Diepe codebase verkenning en patroon analyse voor features
- **Frontend-analyst**: React/TypeScript frontend architectuur analyse
- **Backend-api-analyst**: FastAPI/Pydantic AI agent architectuur analyse
- **Rag-pipeline-analyst**: Document processing en vector storage architectuur

### Core Development
- **Code-reviewer**: Code kwaliteit en best practices review
- **Debugger**: Root cause analysis voor fouten en test failures
- **Test-generator**: Comprehensive test suite generatie
- **Performance-engineer**: Performance analyse en optimalisatie
- **Refactoring-specialist**: Code refactoring en technische debt reduction

### Quality Assurance
- **Security-auditor**: Security vulnerability en compliance analyse
- **Dependency-auditor**: Dependency security en license compliance
- **Api-contract-validator**: API contract validatie en alignment

### Pydantic AI Specialisten
- **Pydantic-ai-validator**: Testing en validation voor Pydantic AI agents
- **Pydantic-ai-prompt-engineer**: System prompt crafting voor Pydantic AI agents
- **Pydantic-ai-tool-integrator**: Tool development voor Pydantic AI agents
- **Pydantic-ai-dependency-manager**: Dependency en configuration voor Pydantic AI agents

### Project Management
- **Sprint-planner**: Agile sprint planning en velocity tracking
- **Task-runner**: Automated test execution en failure resolution

### Documentation
- **Documentation-generator**: Automated documentatie creatie en synchronisatie

### Architecture & DevOps
- **Architecture-planner**: Systeem architectuur en design patterns
- **Migration-strategist**: Database en framework migratie planning
- **Cicd-orchestrator**: CI/CD pipeline creation en optimalisatie
- **Error-detective**: Complex error investigation voor productie issues

### Data Operations
- **Database-architect**: Database schema design en query optimalisatie

### Meta Agents
- **Agent-Architect**: Creëert nieuwe Claude Code sub-agent configuratie bestanden

---

## AI Agents vs Commands: Wanneer Wat Gebruiken?

### 🎯 Belangrijkste Verschil
- **Commands**: Directe, snelle taken in huidige context (je blijft in dezelfde conversation)
- **Agents**: Gespecialiseerde taken in geïsoleerde context (creëert nieuwe AI agent met specifieke expertise)

### ⚡ Commands gebruiken voor:
- **Snelle taken**: Code review, git commits, simpele debugging
- **Routine taken**: Tests genereren, documentatie maken
- **Workflow stappen**: Onderdeel van groter proces
- **Wanneer je snelheid nodig hebt**: Direct uitvoerbaar

### 🤖 Agents gebruiken voor:
- **Diepgaande analyse**: Codebase verkenning, security audits
- **Complexe problemen**: Root cause analysis, architectuur planning
- **Gespecialiseerde expertise**: Domain-specifieke kennis nodig
- **Wanneer je focus nodig hebt**: Geïsoleerde context zonder afleiding

### 🎯 Primers (Begin hier!)
**Gebruik altijd eerst een primer voordat je begint aan een nieuwe taak:**
- `/primers:prime-specific` - Voor snelle context van specifieke bestanden
- `/primers:prime-deep` - Voor diepgaande project analyse

**Wanneer:** Voordat je features implementeert, bugs fixt, of tests schrijft.

## 🚀 Complete Workshop Workflows

Deze workflows volgen het volledige proces zoals beschreven in de workshop README.md - van context engineering tot implementatie.

### 🏗️ Workflow Nieuw Project (Greenfield) - Van Schets naar Productie

#### **Stap 1: Concept & Business Validatie**
1. **Idee Validatie & Market Research**
   ```
   /product:prd-generate [business idee + doelgroep]
   ```
   - Business case en value proposition
   - Competitor analysis via web search
   - Monetization strategie
   - User personas en journey mapping

2. **Technical Feasibility Study**
   ```
   @architecture-planner [business requirements + constraints]
   ```
   - Technology stack selectie
   - Scalability assessment
   - Security requirements
   - Integration possibilities

3. **Project Scoping & Roadmap**
   ```
   /product:user-story [MVP features, "early adopter"]
   /product:technical-breakdown [user stories]
   ```
   - MVP feature definition
   - Development timeline
   - Resource requirements
   - Success metrics definition

#### **Stap 2: Architecture & Foundation**
4. **Systeem Architectuur Design**
   ```
   @architecture-planner [technology stack + scope]
   @database-architect [data requirements + architectuur]
   ```
   - Microservices vs monolith beslissing
   - Database schema ontwerp
   - API design principles
   - Security architectuur

5. **Development Environment Setup**
   ```
   /utilities:config --generate-example
   /python:uv-dependencies --sync  (indien Python)
   /utilities:dependencies --fix
   ```
   - Development tools installatie
   - Environment configuratie
   - Package management setup
   - Local development server

6. **Project Structure & Conventions**
   ```
   /code-quality:document [architecture beslissingen + team conventions]
   /primers:prime-deep [technologie stack + project patterns]
   ```
   - CLAUDE.md met coding standards
   - Directory structuur ontwerp
   - Naming conventions
   - Development workflow regels

#### **Stap 3: Core Features Development**
7. **INITIAL.md voor MVP Features**
   - Schrijf requirements met:
     - **FEATURE**: Kern MVP functionaliteit
     - **EXAMPLES**: Reference implementaties uit similar projects
     - **DOCUMENTATION**: API docs van gekozen tech stack
     - **OTHER CONSIDERATIONS**: Performance, security, scalability

8. **PRP Generatie voor MVP**
   ```
   /prp-commands:generate-prp [INITIAL.md MVP requirements]
   ```
   - Onderzoek naar best practices voor gekozen stack
   - External API integratie research
   - Code examples en patterns verzameling
   - Complete implementation context

9. **Core Implementation**
   ```
   /prp-commands:execute-prp [MVP PRP]
   ```
   - Sequential MVP features implementatie
   - Progressive validation na elke feature
   - Architectuur pattern adherence

#### **Stap 4: Quality & Testing Framework**
10. **Testing Infrastructure Setup**
    ```
    @test-generator [MVP features + testing strategy]
    /code-quality:validate [test framework setup]
    ```
    - Test framework configuratie (Jest, pytest, etc.)
    - Test database setup
    - Mock strategies voor external services
    - CI/CD testing pipeline

11. **Comprehensive Test Suite**
    ```
    /test:test [alle MVP functionaliteit]
    @test-runner [volledige suite + coverage]
    ```
    - Unit tests voor alle components
    - Integration tests tussen services
    - End-to-end user journey tests
    - Performance benchmarking

12. **Security & Production Hardening**
    ```
    @quality-assurance/security-auditor
    @dependency-auditor
    @core-dev/performance-engineer
    ```
    - Security vulnerability assessment
    - OWASP compliance check
    - Performance optimization
    - Error handling en logging

#### **Stap 5: Deployment & Production Setup**
13. **Production Infrastructure**
    ```
    @cicd-orchestrator [deployment requirements]
    /utilities:api-design [production API patterns]
    ```
    - Cloud provider setup (AWS, GCP, Azure)
    - Database migration strategies
    - Environment configuration management
    - Monitoring en logging setup

14. **CI/CD Pipeline Implementation**
    ```
    @cicd-orchestrator
    ```
    - Automated testing integration
    - Staging environment setup
    - Blue-green deployment strategy
    - Rollback procedures

15. **Production Deployment**
    ```
    /git:branch-start production --from main
    /git:commit [production-ready changes]
    ```
    - Production branch management
    - Deployment documentation
    - Health checks en monitoring
    - User acceptance testing

#### **Stap 6: Post-Launch Optimization**
16. **Performance Monitoring & Optimization**
    ```
    @core-dev/performance-engineer [production metrics]
    @error-detective [production issues]
    ```
    - Real-time performance monitoring
    - Error tracking en alerting
    - User behavior analytics
    - Scaling optimization

17. **Documentation & Onboarding**
    ```
    @documentation-generator
    /code-quality:document [complete system]
    ```
    - API documentation (Swagger/OpenAPI)
    - Developer onboarding guides
    - Deployment runbooks
    - User documentation

18. **Feature Iteration Planning**
    ```
    /product:technical-breakdown [user feedback + analytics]
    @sprint-planner [next features + improvements]
    ```
    - User feedback analysis
    - Feature prioritization
    - Development roadmap updates
    - Team capacity planning

---

### 🔧 Workflow Bestaand Project (Brownfield) - Integratie & Maintenance

#### **Stap 1: Issue Analysis & Root Cause**
1. **Issue Identification & Triage**
   ```
   /github:issues list [label=bug|enhancement|hotfix]
   /github:issue-triage [critical issues]
   /code-quality:debug [production errors]
   ```
   - Active issues identification en prioritering
   - Production error analysis
   - User feedback categorisatie
   - Impact assessment op business

2. **Root Cause Investigation**
   ```
   @error-detective [production issues + stack traces]
   @debugger [complex errors + system behavior]
   /git:history [problem areas] --since="1 month ago"
   ```
   - Diepgaande error analyse
   - System behavior onderzoek
   - Historical pattern identification
   - Root cause documentation

3. **Technical Debt Impact Assessment**
   ```
   @tech-debt-analyzer [problematische areas]
   @dependency-auditor --security-only
   ```
   - Existing technical debt identificatie
   - Security vulnerabilities assessment
   - Performance bottlenecks mapping
   - Code quality metrics analysis

#### **Stap 2: Pattern Discovery & Architecture Analysis**
4. **Existing Pattern Extraction**
   ```
   /primers:prime-specific [CLAUDE.md, AGENTS.md, team docs]
   /primers:prime-deep [impact domein]
   @codebase-analysts/codebase-analyst [patterns + conventions]
   ```
   - Team coding conventions documentatie
   - Architectuur patterns identificatie
   - Integration patterns mapping
   - Anti-patterns avoidance strategies

5. **Domain-Specific Pattern Analysis**
   ```
   @codebase-analysts/frontend-analyst [UI component patterns]
   @codebase-analysts/backend-api-analyst [API design patterns]
   @rag-pipeline-analyst [data processing patterns]
   ```
   - Component architecture patterns
   - Service layer interaction patterns
   - Data flow en transformation patterns
   - Error handling en recovery patterns

6. **Integration Point Mapping**
   ```
   @architecture-planner [existing patterns + new requirements]
   /git:history [integration changes] --author=team
   ```
   - Service boundaries en interfaces
   - Database schema evolution patterns
   - External API integration patterns
   - Migration en deployment strategies

#### **Stap 3: Solution Planning met INITIAL.md**
7. **INITIAL.md voor Bugfix/Enhancement**
   - Schrijf requirements met:
     - **FEATURE**: Concrete bugfix of enhancement met context
     - **EXAMPLES**: Bestaande code patterns die gevolgd moeten worden
     - **DOCUMENTATION**: Interne docs + team conventions
     - **OTHER CONSIDERATIONS**: Backwards compatibility, migration impact

8. **Change Impact Analysis**
   ```
   @migration-strategist [proposed changes + existing system]
   @architecture-planner [breaking changes + mitigation]
   ```
   - Breaking changes identificatie
   - Migration path planning
   - Risk assessment en mitigation
   - Rollback strategies

#### **Stap 4: Focused PRP Generatie (STORY PRP)**
9. **Context-Aware PRP Creation**
   ```
   /prp-commands:prp-story-task-create [user story + existing patterns]
   ```
   - Pattern-consistent task decomposition
   - Integration point identificatie
   - Reusable componenten mapping
   - Existing test patterns adoption

10. **PRP Pattern Validation**
    ```
    @code-reviewer [PRP vs existing codebase patterns]
    /review:review [PRP completeness + pattern adherence]
    ```
    - Pattern consistency validation
    - Integration feasibility check
    - Team convention compliance

#### **Stap 5: Safe Implementation & Integration**
11. **Pattern-Compliant Implementation**
    ```
    /prp-commands:prp-story-task-execute [story PRP]
    ```
    - Sequential implementation met pattern adherence
    - Real-time integration testing
    - Backwards compatibility validation

12. **Continuous Quality Assurance**
    ```
    @code-reviewer [tijdens implementatie - pattern focus]
    /code-quality:validate [nieuwe code vs bestaande conventions]
    /code-quality:type-hints [type consistency]
    ```
    - Real-time pattern adherence checking
    - Convention compliance validation
    - Type safety en consistency

#### **Stap 6: Comprehensive Regression Testing**
13. **Regression Test Suite Enhancement**
    ```
    @test-generator [new functionality + regression scenarios]
    /test:test [affected areas + regression tests]
    @test-runner [volledige suite + coverage check]
    ```
    - Regression tests voor bestaande functionaliteit
    - Integration tests met aanpassingen
    - End-to-end scenario validatie
    - Performance regression checks

14. **System Integration Validation**
    ```
    @api-contract-validator [gewijzigde endpoints + backwards compatibility]
    @quality-assurance/security-auditor [security impact]
    ```
    - API contract compliance
    - Backwards compatibility verificatie
    - Security impact assessment
    - Performance impact validatie

#### **Stap 7: Production Readiness & Deployment**
15. **Production Deployment Strategy**
    ```
    @cicd-orchestrator [safe deployment strategy]
    /git:branch-start [feature/bugfix] --from develop
    /git:commit [atomic changes met duidelijke messages]
    ```
    - Feature branch met juiste base
    - Atomic commits per logical change
    - Deployment strategy (feature flags, canary, blue-green)
    - Rollback planning

16. **Code Quality & Technical Debt Management**
    ```
    @refactoring-specialist [code quality improvements]
    @tech-debt-analyzer [post-implementation debt assessment]
    ```
    - Code refactoring voor quality
    - Technical debt documentation
    - Improvement recommendations
    - Long-term maintenance planning

#### **Stap 8: Team Collaboration & Knowledge Sharing**
17. **Pull Request Management**
    ```
    /github:pr-create --draft [met context + patterns]
    /review:review [PR review + pattern validation]
    /review:review-follow-up [feedback implementation]
    ```
    - Comprehensive PR description
    - Pattern adherence review
    - Team knowledge sharing
    - Code review best practices

18. **Documentation & Knowledge Transfer**
    ```
    @documentation-generator [API + integration changes]
    /code-quality:document [patterns + decisions]
    ```
    - API documentation updates
    - Pattern documentation voor team
    - Integration guides
    - Decision records (ADRs)

#### **Stap 9: Post-Deployment Monitoring**
19. **Production Monitoring & Issue Resolution**
    ```
    @error-detective [post-deployment monitoring]
    /github:issues [new issues + user feedback]
    @core-dev/performance-engineer [performance impact]
    ```
    - Production health monitoring
    - User feedback collection en analysis
    - Performance impact assessment
    - Quick issue resolution workflow

20. **Continuous Improvement Planning**
    ```
    @sprint-planner [learnings + improvements]
    /product:technical-breakdown [feedback + next steps]
    ```
    - Lessons learned documentation
    - Process improvement identificatie
    - Future enhancement planning
    - Team capability development

---

### 🎯 Context Engineering Principles

#### **De Vier Pilaren**
1. **RAG (Retrieval-Augmented Generation)**
   - Real-time documentation toegang
   - Web search en Archon integratie
   - Voorkomt hallucinaties

2. **Task Management**
   - Archon project en task tracking
   - TodoWrite voor progress tracking
   - Structured development workflow

3. **Memory**
   - Conversation history
   - Project state en architectural decisions
   - Multi-step workflows zonder herhaling

4. **Prompt Engineering**
   - PRP framework voor structured context
   - Example-driven development
   - Reproducible results

#### **Critical Success Factors**
- **Never skip discovery phase**
- **Always validate context completeness**
- **Use agents for research, commands for execution**
- **Trust but verify** AI implementaties

---

## 🎯 Complete Beslissingsboom - Wanneer Welke Tool Gebruiken

### **1. Planning & Discovery Fase**

#### **Business Requirements & Planning**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Nieuw business idee                 → /product:prd-generate                         /product:user-story
User story nodig                     → /product:user-story                         /product:technical-breakdown
Technische uitwerking                → /product:technical-breakdown                /product:prd-generate
Sprint planning                      → /sprint-planner                              /product:technical-breakdown
Project vision nodig                 → /product:prd-generate                         /product:user-story
```

#### **Architecture & System Design**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Systeem architectuur                 → @architecture-planner                      /product:technical-breakdown
Database design nodig               → @database-architect                         /product:technical-breakdown
Migration nodig                      → @migration-strategist                       @architecture-planner
Integration patterns                 → @codebase-analysts/backend-api-analyst      @architecture-planner
API design nodig                     → /utilities:api-design                        @architecture-planner
```

#### **Codebase Understanding**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Project snelle context               → /primers:prime-specific                       /primers:prime-deep
Diepe codebase analyse                → @codebase-analysts/codebase-analyst         /primers:prime-deep
Frontend patterns                    → @codebase-analysts/frontend-analyst          /primers:prime-deep
Backend patterns                     → @codebase-analysts/backend-api-analyst       /primers:prime-deep
RAG/data patterns                    → @rag-pipeline-analyst                         /primers:prime-deep
```

### **2. Implementation Fase**

#### **Code Schrijven & Development**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
PRP implementation                   → /prp-commands:execute-prp                    Handmatige implementatie
Story PRP implementation             → /prp-commands:prp-story-task-execute        /prp-commands:execute-prp
Code writing met patterns            → @code-reviewer [tijdens schrijven]         /code-quality:validate
Type hints toevoegen                  → /code-quality:type-hints                     @code-reviewer
Code refactoring                     → @refactoring-specialist                     /code-quality:refactor
```

#### **Real-time Quality Assurance**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Code review tijdens schrijven        → @code-reviewer                               /review:review
Pattern validation                   → /code-quality:validate                      @code-reviewer
Code style check                      → /code-quality:document                      /review:review
Convention compliance                → @code-reviewer                               /code-quality:validate
```

### **3. Testing Fase**

#### **Test Generatie & Execution**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Test suite generatie                  → @test-generator                              /test:test
Unit tests                            → /test:test                                    @test-runner
Integration tests                    → @test-runner                                  /test:test
Volledige test suite                  → @test-runner                                  /test:test
Test coverage                         → @test-runner                                  /code-quality:validate
```

#### **Quality Assurance**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Code review                           → /review:review                                 @code-reviewer
Security audit                        → @quality-assurance/security-auditor         /dependencies:dependencies
Dependency check                     → @dependency-auditor                         /utilities:dependencies
Performance check                     → @core-dev/performance-engineer              /code-quality:debug
API validation                        → @api-contract-validator                     /review:review
```

### **4. Deployment & Git Workflow**

#### **Git Operations**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Nieuwe branch starten                  → /git:branch-start                            Git commandos handmatig
Commits maken                         → /git:commit                                   Git commandos handmatig
Branch cleanup                        → /git:branch-cleanup                          Git commandos handmatig
Rebase interactief                    → /git:rebase-interactive                      Git commandos handmatig
History analysis                      → /git:history                                  Git log commandos
```

#### **Team Collaboration**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Pull request maken                    → /github:pr-create                           GitHub CLI handmatig
Issues beheren                        → /github:issues                               GitHub website
Issue triage                          → /github:issue-triage                         Handmatige prioritering
PR review                             → /review:review                                 GitHub review features
```

#### **CI/CD & Deployment**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
CI/CD pipeline setup                  → @cicd-orchestrator                           Handmatige GitHub Actions
Deployment strategie                  → @cicd-orchestrator                           Handmatige deployment scripts
Production deployment                 → /git:commit + deployment tool               Deployment platforms
```

### **5. Monitoring & Maintenance**

#### **Error Analysis & Debugging**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Production errors                     → @error-detective                            /code-quality:debug
Complex debugging                     → @debugger                                    /code-quality:debug
Stack trace analysis                  → @error-detective                            Handmatige stack trace reading
System behavior investigation        → @debugger                                    Log analysis tools
```

#### **Performance & Technical Debt**
```
SITUATIE                              BESTE TOOL                                    ALTERNATIEFEN
────────────────────────────────────────────────────────────────────────────────────────────────────
Performance issues                    → @core-dev/performance-engineer              /code-quality:debug
Technical debt analysis              → @tech-debt-analyzer                         /review:review
Code quality improvement             → @refactoring-specialist                     /code-quality:refactor
System optimization                   → @core-dev/performance-engineer              /code-quality:debug
```

---

## 🚫 Overbodige/Verouderde Tools & Preferenties

### **Commands die Overbodig Zijn:**

| Overbodige Command | Betere Alternatief | Waarom |
|-------------------|-------------------|---------|
| `/code-quality:refactor` | `@refactoring-specialist` | Diepere refactoring expertise |
| `/code-quality:debug` | `@debugger` of `@error-detective` | Gespecialiseerde debug expertise |
| `/dependencies:dependencies` | `@dependency-auditor` | Meer comprehensive dependency analysis |
| `/utilities:dependencies` | `@dependency-auditor` | Security focus met dependency audit |
| `/product:user-story` (simpel) | `/product:prd-generate` + breakdown | Meer complete context |
| `/code-quality:document` (simpel) | `@documentation-generator` | Gespecialiseerde documentatie generatie |

### **Agents die Andere Tools Overbodig Maken:**

| Agent | Maakt Overbodig | Preferentie |
|-------|------------------|-------------|
| `@code-reviewer` | `/review:review` (voor simpele reviews) | `@code-reviewer` voor diepe analyse |
| `@test-generator` | `/test:test` (voor generatie) | `@test-generator` voor complete test suites |
| `@error-detective` | `/code-quality:debug` (voor production issues) | `@error-detective` voor complexe systemen |
| `@performance-engineer` | `/code-quality:debug` (voor performance) | `@performance-engineer` voor diepe optimalisatie |

### **Tools die Combineren Moeten worden Gebruikt:**

| Primaire Tool | Complementaire Tool | Wanneer Samen Gebruiken |
|---------------|-------------------|------------------------|
| `@codebase-analysts/codebase-analyst` | `/primers:prime-deep` | Complete codebase understanding |
| `@test-generator` | `/test:test` | Test generatie + uitvoering |
| `@security-auditor` | `@dependency-auditor` | Complete security assessment |
| `@architecture-planner` | `@database-architect` | Volledige systeem architectuur |

---

## 🎯 Quick Reference Cheat Sheets

### **Nieuw Project - Stap voor Stap:**
1. `/product:prd-generate [idee]`
2. `@architecture-planner [PRD]`
3. `/utilities:config --generate-example`
4. `/code-quality:document [conventions]`
5. `INITIAL.md` maken met MVP requirements
6. `/prp-commands:generate-prp [INITIAL.md]`
7. `/prp-commands:execute-prp [PRP]`
8. `@test-generator + /test:test`
9. `@cicd-orchestrator`
10. `/git:commit + /github:pr-create`

### **Bestaand Project - Issue Resolution:**
1. `/github:issues` + `/code-quality:debug`
2. `@error-detective` of `@debugger`
3. `/primers:prime-specific` + `@codebase-analysts/codebase-analyst`
4. `INITIAL.md` met fix requirements
5. `/prp-commands:prp-story-task-create [issue]`
6. `/prp-commands:prp-story-task-execute [PRP]`
7. `@test-runner` + `@api-contract-validator`
8. `/git:commit` + `/github:pr-create`

### **Emergency Situatie - Production Down:**
1. `@error-detective [production error]`
2. `/git:history [recent changes]`
3. `/code-quality:debug [specific error]`
4. `@debugger [complex issue]`
5. `/git:commit [hotfix]`
6. `@cicd-orchestrator [emergency deployment]`

---

## Speciale Agent Combinaties

### 🎯 Krachtige Combinaties
Commands en agents kunnen worden gecombineerd:
- `@codebase-analysts/codebase-analyst` - Codebase analyst agent
- `@core-dev/code-reviewer` - Code reviewer agent

### 🔄 Product Development Flow
1. `/product:prd-generate [idea]` → Genereert Product Requirements Document
2. `/product:user-story [feature, persona]` → Maakt user stories
3. `/product:technical-breakdown [story]` → Breekt down in technische taken
4. Implementatie met specialized agents

### 📝 PRP Workflow
1. `/prp-commands:prp-story-task-create` → Creëert Product Requirements Prompt
2. `/prp-commands:prp-story-task-execute` → Voert PRP uit met gerichte implementatie

### ⚡ Quality Flow
1. Schrijf code → `/test:test [code]` → `/review:review [changes]` → `/git:commit`
2. Gebruik specialized agents voor diepgaande analyse

---

## Tips en Best Practices

### 🎯 Kies de Juiste Tool
- **Snelle taken**: Gebruik slash commands
- **Complexe analyse**: Gebruik agents
- **Nieuwe features**: Begin met primers, gebruik product commands
- **Bug fixing**: Gebruik debugging commands en specialized agents

### 🔄 Workflow Optimalisatie
- Begin **altijd** met een primer voor context
- Gebruik agents voor diepgaande, gespecialiseerde taken
- Combineer commands voor workflows
- Pas aan naar jouw tech stack en project structuur

### ⚠️ Belangrijke Opmerkingen
- Deze zijn templates - pas aan naar jouw specifieke project
- Technology specifieke aanpassingen verbeteren prestaties
- Gebruik de juiste tools voor de juiste taken
- Agents werken in geïsoleerde contexten voor focus

---

## 🎯 Complete Quick Reference - Alle Tools & Combinaties

### **🚀 Nieuw Project (Greenfield) - Volledige Workflow**

#### **Fase 1: Business & Requirements (Stap 1-4)**
```
1. Business Idee → /product:prd-generate [idee + doelgroep]
2. User Stories → /product:user-story [MVP features, "early adopter"]
3. Technical Breakdown → /product:technical-breakdown [user stories]
4. Sprint Planning → /sprint-planner [features + timeline]
```

#### **Fase 2: Architecture & Foundation (Stap 5-8)**
```
5. Systeem Architectuur → @architecture-planner [requirements + scope]
6. Database Design → @database-architect [data requirements + architectuur]
7. Migration Strategy → @migration-strategist [existing data → new schema]
8. API Design → /utilities:api-design [REST/GraphQL patterns]
9. Environment Setup → /utilities:config --generate-example
10. Dependencies → /python:uv-dependencies --sync (Python) OF /utilities:dependencies --fix
11. Project Rules → /code-quality:document [architecture + conventions]
12. Git Setup → /git:branch-start main
```

#### **Fase 3: Context & Research (Stap 9-13)**
```
13. Project Context → /primers:prime-specific [README.md, tech stack]
14. Codebase Research → /primers:prime-deep [domain patterns]
15. Frontend Analysis → @codebase-analysts/frontend-analyst [UI requirements]
16. Backend Analysis → @codebase-analysts/backend-api-analyst [API requirements]
17. RAG Analysis → @rag-pipeline-analyst [data processing requirements]
18. Global Rules → /code-quality:document [CLAUDE.md patterns]
```

#### **Fase 4: PRP Generatie (Stap 14-16)**
```
19. INITIAL.md Creation → Schrijf [FEATURE + EXAMPLES + DOCUMENTATION + CONSIDERATIONS]
20. PRP Generation → /prp-commands:generate-prp [INITIAL.md inhoud]
21. PRP Validation → /review:review [generated PRP]
22. Pattern Review → @code-reviewer [PRP vs best practices]
```

#### **Fase 5: Implementation (Stap 17-19)**
```
23. Execute PRP → /prp-commands:execute-prp [PRP file]
24. Real-time Review → @code-reviewer [tijdens implementatie]
25. Type Validation → /code-quality:type-hints [nieuwe code]
26. Pattern Validation → /code-quality:validate [vs conventions]
27. Progress Tracking → @task-runner [task completion]
```

#### **Fase 6: Testing & Quality (Stap 20-24)**
```
28. Test Suite Generation → @test-generator [alle functionality]
29. Unit Tests → /test:test [specifieke components]
30. Integration Tests → /test-runner [full integration]
31. Security Audit → @quality-assurance/security-auditor
32. Dependency Audit → @dependency-auditor
33. Performance Check → @core-dev/performance-engineer
34. API Validation → @api-contract-validator [alle endpoints]
35. Code Review → /review:review [alle changes]
36. Documentation → @documentation-generator [API + setup guides]
```

#### **Fase 7: Deployment (Stap 25-27)**
```
37. CI/CD Setup → @cicd-orchestrator [deployment pipeline]
38. Git Workflow → /git:commit --all + /git:branch-cleanup
39. Team Collaboration → /github:pr-create [review ready code]
```

---

### **🔧 Bestaand Project (Brownfield) - Volledige Workflow**

#### **Fase 1: Issue Discovery (Stap 1-6)**
```
1. Issue Identification → /github:issues list [bug|enhancement|hotfix]
2. Issue Triage → /github:issue-triage [critical issues]
3. Error Analysis → /code-quality:debug [production errors]
4. Root Cause → @error-detective [stack traces + system behavior]
5. Complex Debugging → @debugger [deep system investigation]
6. History Analysis → /git:history [problem areas] --since="1 month"
7. Technical Debt → @tech-debt-analyzer [problematic components]
8. Security Assessment → @dependency-auditor --security-only
```

#### **Fase 2: Pattern Discovery (Stap 7-12)**
```
9. Project Rules → /primers:prime-specific [CLAUDE.md, AGENTS.md]
10. Deep Analysis → /primers:prime-deep [impact domain]
11. Pattern Extraction → @codebase-analysts/codebase-analyst [existing patterns]
12. Frontend Patterns → @codebase-analysts/frontend-analyst [UI component patterns]
13. Backend Patterns → @codebase-analysts/backend-api-analyst [API design patterns]
14. RAG Patterns → @rag-pipeline-analyst [data processing patterns]
15. Integration Mapping → @architecture-planner [existing + new requirements]
16. Team Patterns → /git:history [recent work] --author=team-name
```

#### **Fase 3: Solution Planning (Stap 13-15)**
```
17. Change Impact → @migration-strategist [proposed changes + existing system]
18. Breaking Changes → @architecture-planner [impact + mitigation]
19. INITIAL.md → Schrijf [FEATURE + EXAMPLES + DOCUMENTATION + CONSIDERATIONS]
20. Story PRP → /prp-commands:prp-story-task-create [user story + patterns]
21. PRP Validation → @code-reviewer [PRP vs existing patterns]
22. Review PRP → /review:review [completeness + pattern adherence]
```

#### **Fase 4: Implementation (Stap 16-18)**
```
23. Execute Story → /prp-commands:prp-story-task-execute [story PRP]
24. Pattern Compliance → @code-reviewer [tijdens implementatie]
25. Convention Validation → /code-quality:validate [vs existing patterns]
26. Type Consistency → /code-quality:type-hints [type safety]
27. Refactoring → @refactoring-specialist [code quality improvements]
28. Progress Tracking → @task-runner [task completion monitoring]
```

#### **Fase 5: Testing & Integration (Stap 19-22)**
```
29. Regression Tests → @test-generator [new + existing functionality]
30. Unit Tests → /test:test [affected components]
31. Integration Tests → /test-runner [full system integration]
32. Backwards Compatibility → @api-contract-validator [changed endpoints]
33. Security Impact → @quality-assurance/security-auditor [changes impact]
34. Performance Impact → @core-dev/performance-engineer [system performance]
35. Technical Debt Assessment → @tech-debt-analyzer [post-implementation]
36. Code Review → /review:review [all changes]
37. Follow-up Review → /review:review-follow-up [feedback implementation]
```

#### **Fase 6: Deployment & Documentation (Stap 23-25)**
```
38. Safe Deployment → @cicd-orchestrator [deployment strategy]
39. Git Workflow → /git:branch-start [feature-name] --from develop
40. Atomic Commits → /git:commit [specific files with clear messages]
41. PR Creation → /github:pr-create --draft [with context + patterns]
42. Documentation Updates → @documentation-generator [API + integration changes]
43. Pattern Docs → /code-quality:document [patterns + decisions]
```

---

### **🚨 Emergency Scenarios - Snelle Interventie**

#### **Production Down Scenario (7 stappen)**
```
1. Immediate Diagnosis → @error-detective [production error + logs]
2. Recent Changes → /git:history [last 24 hours] --since="1 day ago"
3. Specific Debug → /code-quality:debug [exact error message]
4. Complex Issues → @debugger [system behavior investigation]
5. Hotfix Implementation → Handmatige fix + @code-reviewer validation
6. Emergency Deploy → /git:commit [hotfix] + @cicd-orchestrator [emergency]
7. Monitoring → @error-detective [post-deployment health]
```

#### **Security Breach Scenario (7 stappen)**
```
1. Security Assessment → @quality-assurance/security-auditor
2. Dependency Scan → @dependency-auditor --security-only
3. Vulnerability Analysis → @security-auditor [identify breach vector]
4. Patch Implementation → @refactoring-specialist [security fixes]
5. Validation → @api-contract-validator + @test-runner
6. Documentation → @documentation-generator [security incident report]
7. Communication → /github:issues [security advisory]
```

#### **Performance Crisis Scenario (6 stappen)**
```
1. Performance Analysis → @core-dev/performance-engineer [bottleneck identification]
2. System Monitoring → @error-detective [performance metrics]
3. Optimization → @refactoring-specialist [performance improvements]
4. Testing → /test-runner [performance regression tests]
5. Validation → @core-dev/performance-engineer [verify improvements]
6. Documentation → /code-quality:document [optimization changes]
```

---

### **🔄 Routine Maintenance Workflows**

#### **Weekly Code Quality Check (6 stappen)**
```
1. Technical Debt Review → @tech-debt-analyzer
2. Security Scan → @quality-assurance/security-auditor
3. Dependency Check → @dependency-auditor
4. Performance Review → @core-dev/performance-engineer
5. Code Review → /review:review [recent changes]
6. Documentation → @documentation-generator [updated docs]
```

#### **Sprint Planning Workflow (5 stappen)**
```
1. Previous Sprint Review → /github:issues [completed items]
2. New Backlog → /product:technical-breakdown [new requirements]
3. Sprint Planning → /sprint-planner [features + capacity]
4. Task Creation → @task-runner [sprint tasks]
5. Resource Allocation → @sprint-planner [team assignment]
```

#### **Release Preparation Workflow (7 stappen)**
```
1. Feature Complete Check → /test-runner [full test suite]
2. Security Audit → @quality-assurance/security-auditor
3. Performance Validation → @core-dev/performance-engineer
4. Documentation → @documentation-generator [release notes]
5. Release Branch → /git:branch-start release --from main
6. Tagging → /git:commit [release version]
7. Deployment → @cicd-orchestrator [release deployment]
```

---

### **📊 Specialized Tool Combinaties**

#### **Complete Security Assessment**
```
@quality-assurance/security-auditor + @dependency-auditor + @api-contract-validator + /test:test [security tests]
```

#### **Full Performance Analysis**
```
@core-dev/performance-engineer + @error-detective + @tech-debt-analyzer + /test:test [performance tests]
```

#### **Comprehensive Code Review**
```
@code-reviewer + @refactoring-specialist + @tech-debt-analyzer + /review:review + /code-quality:validate
```

#### **Complete Testing Suite**
```
@test-generator + /test:test + @test-runner + @api-contract-validator + /code-quality:validate
```

#### **Full Architecture Review**
```
@architecture-planner + @database-architect + @migration-strategist + @codebase-analysts/codebase-analyst
```

#### **Deep Pattern Analysis**
```
@codebase-analysts/codebase-analyst + @codebase-analysts/frontend-analyst + @codebase-analysts/backend-api-analyst + @rag-pipeline-analyst
```

#### **Quality & Security Pipeline**
```
@code-reviewer + @quality-assurance/security-auditor + @dependency-auditor + @api-contract-validator + /review:review
```

---

### **⚡ Quick Decision Matrix**

| Situation | Primary Tool | Supporting Tools | Skip These |
|-----------|---------------|------------------|------------|
| **New Feature Idea** | `/product:prd-generate` | `/product:user-story`, `/product:technical-breakdown` | `/code-quality:debug` |
| **Production Bug** | `@error-detective` | `/git:history`, `/code-quality:debug`, `@debugger` | `/product:prd-generate` |
| **Performance Issue** | `@core-dev/performance-engineer` | `@error-detective`, `@tech-debt-analyzer` | `/product:user-story` |
| **Security Concern** | `@quality-assurance/security-auditor` | `@dependency-auditor`, `@api-contract-validator` | `/git:branch-start` |
| **Code Refactoring** | `@refactoring-specialist` | `@code-reviewer`, `@tech-debt-analyzer` | `/product:technical-breakdown` |
| **API Changes** | `@api-contract-validator` | `@codebase-analysts/backend-api-analyst`, `/test:test` | `/product:prd-generate` |
| **Database Changes** | `@database-architect` | `@migration-strategist`, `/test:test` | `/code-quality:type-hints` |
| **Testing Strategy** | `@test-generator` | `/test:test`, `@test-runner`, `/code-quality:validate` | `/product:user-story` |
| **Documentation** | `@documentation-generator` | `/code-quality:document`, `/review:review` | `@error-detective` |
| **Team Onboarding** | `/primers:prime-deep` + `/primers:prime-specific` | `@codebase-analysts/codebase-analyst`, `/review:review` | `/git:commit` |
| **CI/CD Setup** | `@cicd-orchestrator` | `/git:branch-start`, `/test-runner`, `/review:review` | `/product:user-story` |
| **Technical Debt** | `@tech-debt-analyzer` | `@refactoring-specialist`, `@code-reviewer` | `/product:technical-breakdown` |
| **Migration** | `@migration-strategist` | `@database-architect`, `@architecture-planner` | `/code-quality:type-hints` |
| **Pattern Discovery** | `@codebase-analysts/codebase-analyst` | `/primers:prime-deep`, `/git:history` | `/product:prd-generate` |

---

### **🎯 Essential Tools Per Scenario**

#### **Business Development**
```
Core: /product:prd-generate → @architecture-planner → @database-architect
Support: /product:user-story → /product:technical-breakdown → @sprint-planner
```

#### **Code Implementation**
```
Core: /prp-commands:execute-prp → @code-reviewer → /test-generator
Support: /code-quality:type-hints → /code-quality:validate → @task-runner
```

#### **Quality Assurance**
```
Core: @quality-assurance/security-auditor → @dependency-auditor → @api-contract-validator
Support: /test:test → @test-runner → /review:review
```

#### **Production Management**
```
Core: @error-detective → @core-dev/performance-engineer → @cicd-orchestrator
Support: /git:history → /git:commit → /github:pr-create
```

#### **Knowledge Management**
```
Core: @documentation-generator → /code-quality:document
Support: /primers:prime-specific → /primers:prime-deep → @codebase-analysts/codebase-analyst
```

*Dit overzicht bevat alle beschikbare commands en agents met hun specifieke toepassingen en combinaties.*