# LLM Solution - Backend Deployment

Deze map bevat alle bestanden voor de backend deployment op de VPS.

## Structuur

```
deployment/
├── docker-compose.yaml     # Docker compose voor agent-api en rag-pipeline
├── Caddyfile               # Caddy config voor api.llmsolution.nl (toevoegen aan bestaande Caddy)
├── .env.example            # Voorbeeld environment variabelen
├── backend_agent_api/      # FastAPI chatbot backend
│   ├── Dockerfile
│   ├── agent_api.py
│   ├── website_agent.py
│   ├── website_prompt.py
│   └── ...
└── backend_rag_pipeline/   # RAG document processor
    ├── Dockerfile
    ├── website_docs/       # Documentatie voor RAG embeddings
    │   └── llmsolution_documentatie.md
    └── ...
```

## Deployment Stappen

### 1. Kopieer naar VPS

```bash
scp -r deployment/ user@vps:/path/to/deployment/
```

### 2. Environment Variables

```bash
cd /path/to/deployment
cp .env.example .env
# Vul de juiste waarden in
nano .env
```

### 3. Caddy Configuratie

Voeg de inhoud van `Caddyfile` toe aan je bestaande Caddy configuratie:

```bash
# Backup bestaande config
cp /etc/caddy/Caddyfile /etc/caddy/Caddyfile.backup

# Voeg api.llmsolution.nl blok toe
cat Caddyfile >> /etc/caddy/Caddyfile

# Herlaad Caddy
docker exec caddy caddy reload --config /etc/caddy/Caddyfile
```

### 4. Start Containers

```bash
docker-compose up -d --build
```

### 5. Controleer Status

```bash
# Check logs
docker-compose logs -f

# Check health
curl https://api.llmsolution.nl/health
```

## Database Setup

Voer eerst de SQL scripts uit in Supabase:
- `sql/8-contact_submissions.sql`
- `sql/9-website_chat_sessions.sql`

## RAG Pipeline

De RAG pipeline kijkt naar `/app/Local_Files/data` in de container, die gemount is op `./backend_rag_pipeline/website_docs`.

Om nieuwe documenten toe te voegen:
1. Plaats `.md`, `.pdf`, of `.txt` bestanden in `backend_rag_pipeline/website_docs/`
2. De pipeline pikt ze automatisch op en maakt embeddings

## Netwerk

De containers draaien op het externe netwerk `agentic-rag-twan_llm-solution-network`.
Zorg dat dit netwerk bestaat voordat je de containers start:

```bash
docker network ls | grep llm-solution-network
```
