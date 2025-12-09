# Implementatie Plan: LLM Solution Chatbot op VPS

## Overzicht

Dit document beschrijft de stappen om de chatbot backend te deployen op de bestaande VPS waar al een Agentic RAG systeem draait.

**Huidige situatie:**
- VPS heeft al Docker met `agentic-rag-twan_llm-solution-network` netwerk
- Caddy reverse proxy draait al (met `Caddyfile.prod`)
- Supabase project `llm-website` is geconfigureerd met benodigde tabellen

**Doel:**
- Backend API container toevoegen aan bestaande infrastructuur
- Chatbot bereikbaar maken via `api.llmsolution.nl`
- Alles draaien onder user `llmsolution` (niet root)

---

## Fase 1: Voorbereiding Lokaal

### 1.1 Bestanden Controleren

Zorg dat de `/deployment` folder compleet is:

```
deployment/
├── backend_agent_api/
│   ├── main.py              # FastAPI endpoints
│   ├── website_agent.py     # Pydantic AI agent met tools
│   ├── website_prompt.py    # System prompt
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Container build
├── docker-compose.yaml      # Container orchestratie
├── Caddyfile.prod          # Caddy config met api.llmsolution.nl
├── .env                    # Environment variables (NIET committen!)
└── README.md               # Documentatie
```

### 1.2 Environment Variables Checken

Controleer `.env` bestand:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Supabase (llm-website project)
SUPABASE_URL=https://uiwiwjkwnwqhliqoruaz.supabase.co
SUPABASE_SERVICE_KEY=eyJ...
SUPABASE_ANON_KEY=eyJ...

# RAG Pipeline (optioneel voor later)
RAG_WATCH_DIRECTORY=/app/Local_Files/data
```

### 1.3 Git Repository Voorbereiden

Zorg dat de deployment folder in git staat:

```bash
git add deployment/
git commit -m "Add chatbot deployment configuration"
git push origin master
```

**Let op:** `.env` bestand NIET committen! Voeg toe aan `.gitignore`:
```
deployment/.env
```

---

## Fase 2: VPS User Setup

### 2.1 SSH als Root (eenmalig)

```bash
ssh root@jouw-vps-ip
```

### 2.2 User `llmsolution` Aanmaken

```bash
# Maak user aan
adduser llmsolution

# Volg prompts voor wachtwoord

# Voeg toe aan sudo groep
usermod -aG sudo llmsolution

# Voeg toe aan docker groep (zodat docker zonder sudo werkt)
usermod -aG docker llmsolution
```

### 2.3 SSH Key Setup (optioneel maar aanbevolen)

```bash
# Als llmsolution user
su - llmsolution

# Maak .ssh directory
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Voeg je public key toe
nano ~/.ssh/authorized_keys
# Plak je public key

chmod 600 ~/.ssh/authorized_keys
```

### 2.4 Uitloggen en Opnieuw Inloggen

```bash
exit  # uit llmsolution
exit  # uit root

# Nu inloggen als llmsolution
ssh llmsolution@jouw-vps-ip
```

---

## Fase 3: Project Clone & Setup

### 3.1 Git Clone

```bash
# Als llmsolution user, clone direct in home directory
cd ~
git clone https://github.com/LLMsolution/chatbot-deployment.git
cd chatbot-deployment
```

### 3.2 Environment File Aanmaken

```bash
nano .env
```

Plak de environment variables:

```env
# OpenAI
OPENAI_API_KEY=sk-proj-...

# Supabase (llm-website project)
SUPABASE_URL=https://uiwiwjkwnwqhliqoruaz.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# RAG Pipeline
RAG_WATCH_DIRECTORY=/app/Local_Files/data
```

Sla op met `Ctrl+O`, `Enter`, `Ctrl+X`

### 3.3 Permissies Checken

```bash
# Zorg dat .env alleen leesbaar is voor owner
chmod 600 .env
```

---

## Fase 4: Docker Deployment

### 4.1 Controleer Docker Toegang

```bash
# Test of docker werkt zonder sudo
docker ps

# Als "permission denied": log uit en weer in
# Of: newgrp docker
```

### 4.2 Controleer Bestaand Netwerk

```bash
docker network ls | grep llm-solution
```

Verwacht resultaat:
```
agentic-rag-twan_llm-solution-network   bridge
```

Als het netwerk niet bestaat:
```bash
docker network create agentic-rag-twan_llm-solution-network
```

### 4.3 Build & Start Container

```bash
cd ~/chatbot-deployment

# Build image
docker-compose build --no-cache

# Start container
docker-compose up -d
```

### 4.4 Controleer Status

```bash
# Container status
docker-compose ps

# Logs bekijken
docker-compose logs -f backend-api

# Health check
curl http://localhost:8001/health
```

Verwacht resultaat:
```json
{"status": "healthy", "service": "llm-solution-chatbot"}
```

---

## Fase 5: Caddy Configuratie

### 5.1 Caddyfile.prod Locatie

De `Caddyfile.prod` moet de `api.llmsolution.nl` configuratie bevatten:

```caddyfile
# LLM Solution Chatbot API
api.llmsolution.nl {
    # CORS headers
    header {
        Access-Control-Allow-Origin "https://llmsolution.nl"
        Access-Control-Allow-Methods "GET, POST, OPTIONS"
        Access-Control-Allow-Headers "Content-Type, Authorization"
    }

    # Handle preflight OPTIONS requests
    @options method OPTIONS
    respond @options 204

    # Proxy to backend container
    reverse_proxy backend-api:8001
}
```

### 5.2 Caddy Config Updaten

Kopieer of merge de nieuwe config:

```bash
# Vind waar Caddy config staat
# Meestal in de agentic-rag-twan folder of /etc/caddy/

# Als Caddy in Docker draait, check de volume mount
docker inspect caddy | grep -A5 "Mounts"
```

### 5.3 Caddy Herstarten

**Als Caddy in Docker draait:**

```bash
# Optie 1: Reload config (geen downtime)
docker exec caddy caddy reload --config /etc/caddy/Caddyfile

# Optie 2: Restart container
docker restart caddy
```

**Als Caddy als systemd service draait:**

```bash
# Reload (geen downtime)
sudo systemctl reload caddy

# Of restart
sudo systemctl restart caddy

# Check status
sudo systemctl status caddy
```

### 5.4 Verifieer Caddy

```bash
# Check of Caddy de nieuwe config heeft geladen
docker exec caddy caddy validate --config /etc/caddy/Caddyfile

# Of via logs
docker logs caddy --tail=50
```

---

## Fase 6: DNS Configuratie

### 6.1 A-Record Toevoegen

Bij je domein registrar (bijv. TransIP, Cloudflare):

| Type | Naam | Waarde |
|------|------|--------|
| A | api | [VPS-IP-ADRES] |

Of als je al een wildcard hebt: `*.llmsolution.nl` -> VPS-IP (dan is dit niet nodig)

### 6.2 DNS Propagatie Checken

```bash
# Check of DNS werkt
dig api.llmsolution.nl

# Of
nslookup api.llmsolution.nl
```

### 6.3 SSL Certificaat

Caddy regelt automatisch Let's Encrypt certificaten bij eerste request.

```bash
# Test HTTPS (kan even duren bij eerste keer)
curl -I https://api.llmsolution.nl/health
```

---

## Fase 7: Frontend Configuratie

### 7.1 API URL Instellen

In de Next.js frontend, update de chatbot API URL:

**`.env.production`** (of Vercel environment variables):
```env
NEXT_PUBLIC_CHATBOT_API_URL=https://api.llmsolution.nl
```

**Of hardcoded in `ChatPanel.tsx`:**
```typescript
const API_URL = process.env.NEXT_PUBLIC_CHATBOT_API_URL || 'https://api.llmsolution.nl';
```

### 7.2 Frontend Deployen

```bash
# Als Vercel
vercel --prod

# Als zelf-gehost
npm run build
```

---

## Fase 8: Verificatie & Testing

### 8.1 Backend Tests

```bash
# Health check
curl https://api.llmsolution.nl/health

# Chat test
curl -X POST https://api.llmsolution.nl/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hallo", "session_id": "test-123"}'
```

### 8.2 Frontend Test

1. Open https://llmsolution.nl
2. Klik op chatbot widget
3. Stuur testbericht
4. Controleer of antwoord terugkomt

### 8.3 RAG Test

```bash
curl -X POST https://api.llmsolution.nl/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Wat zijn jullie oplossingen?", "session_id": "test-rag"}'
```

### 8.4 Lead Submission Test

Test de volledige flow:
1. Klik "Vind jouw oplossing"
2. Beantwoord vragen
3. Geef contactgegevens
4. Controleer in Supabase:

```sql
SELECT * FROM contact_submissions ORDER BY created_at DESC LIMIT 5;
SELECT * FROM clients ORDER BY created_at DESC LIMIT 5;
```

---

## Fase 9: Monitoring & Maintenance

### 9.1 Log Monitoring

```bash
# Inloggen als llmsolution
ssh llmsolution@vps-ip

# Ga naar project
cd ~/chatbot-deployment

# Live logs
docker-compose logs -f backend-api

# Laatste 100 regels
docker-compose logs --tail=100 backend-api
```

### 9.2 Updates Deployen

```bash
# Als llmsolution user
cd ~/chatbot-deployment

# Pull nieuwe code
git pull origin main

# Rebuild en restart
docker-compose build --no-cache
docker-compose up -d

# Check logs
docker-compose logs -f backend-api
```

### 9.3 Container Restart Policy

In `docker-compose.yaml` staat:
```yaml
restart: unless-stopped
```

Container herstart automatisch bij crashes of server reboot.

---

## Troubleshooting

### Docker Permission Denied

```bash
# Als llmsolution geen docker toegang heeft
sudo usermod -aG docker llmsolution

# Dan uitloggen en opnieuw inloggen
exit
ssh llmsolution@vps-ip
```

### Caddy Reload Werkt Niet

```bash
# Check Caddy logs
docker logs caddy --tail=100

# Validate config
docker exec caddy caddy validate --config /etc/caddy/Caddyfile

# Force restart
docker restart caddy
```

### Container Start Niet

```bash
# Bekijk logs
docker-compose logs backend-api

# Check of poort vrij is
sudo netstat -tlnp | grep 8001

# Handmatig starten voor debug
docker-compose up backend-api
```

### CORS Errors

1. Check Caddyfile CORS headers
2. Controleer dat `https://llmsolution.nl` exact matcht (geen trailing slash)
3. Check browser console voor specifieke error

### SSL Certificaat Problemen

```bash
# Check Caddy certificates
docker exec caddy caddy certificates

# Force nieuwe certificaat
docker exec caddy caddy renew --force
```

---

## Quick Reference Commands

```bash
# SSH naar VPS
ssh llmsolution@vps-ip

# Ga naar project
cd ~/chatbot-deployment

# Start containers
docker-compose up -d

# Stop containers
docker-compose down

# Bekijk logs
docker-compose logs -f backend-api

# Rebuild
docker-compose build --no-cache && docker-compose up -d

# Caddy reload
docker exec caddy caddy reload --config /etc/caddy/Caddyfile

# Caddy restart
docker restart caddy

# Pull updates
git pull origin main
```

---

## Checklist Deployment

### User Setup
- [ ] User `llmsolution` aangemaakt
- [ ] User toegevoegd aan `docker` groep
- [ ] SSH key geconfigureerd (optioneel)

### Project Setup
- [ ] Git repository gecloned: `git clone https://github.com/LLMsolution/chatbot-deployment.git`
- [ ] `.env` bestand aangemaakt met correcte credentials
- [ ] `.env` permissies op 600

### Docker
- [ ] Docker werkt zonder sudo voor llmsolution user
- [ ] Docker netwerk `agentic-rag-twan_llm-solution-network` bestaat
- [ ] Container gebouwd en gestart
- [ ] Health check succesvol (`curl localhost:8001/health`)

### Caddy
- [ ] `api.llmsolution.nl` toegevoegd aan Caddyfile.prod
- [ ] Caddy herstart/reload uitgevoerd
- [ ] Geen errors in Caddy logs

### DNS & SSL
- [ ] A-record voor `api.llmsolution.nl` ingesteld
- [ ] DNS propagatie voltooid
- [ ] SSL certificaat actief (https werkt)

### Testing
- [ ] Health check via HTTPS werkt
- [ ] Chat functie werkt
- [ ] RAG functie werkt (haalt info uit docs)
- [ ] Lead submission werkt (data in Supabase)

### Frontend
- [ ] API URL geconfigureerd
- [ ] Frontend gedeployed
- [ ] Chatbot widget werkt op live site

---

## Contact & Support

Bij problemen:
- Check eerst de logs: `docker-compose logs backend-api`
- Supabase dashboard: https://supabase.com/dashboard
- Email: info@llmsolution.nl
