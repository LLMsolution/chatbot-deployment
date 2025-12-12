"""Website chatbot agent with RAG, lead generation, and meeting scheduling tools."""

from dataclasses import dataclass

from pydantic_ai import Agent, RunContext
from openai import AsyncOpenAI
from supabase import AsyncClient

from website_prompt import WEBSITE_CHATBOT_PROMPT


@dataclass
class WebsiteAgentDeps:
    """Dependencies for the website chatbot agent."""
    supabase: AsyncClient
    openai_client: AsyncOpenAI
    embedding_model: str = "text-embedding-3-small"


# Create the website agent
website_agent = Agent(
    'openai:gpt-4o-mini',
    deps_type=WebsiteAgentDeps,
    system_prompt=WEBSITE_CHATBOT_PROMPT,
)


@website_agent.tool
async def retrieve_relevant_documents(
    ctx: RunContext[WebsiteAgentDeps],
    query: str
) -> str:
    """
    Zoek relevante informatie in de LLM Solution documentatie.

    Gebruik voor:
    - Vragen over oplossingen (chatbots, dashboards, RAG, etc.)
    - FAQ vragen
    - Prijsinformatie
    - Werkwijze en proces

    Args:
        query: De zoekvraag om relevante documenten te vinden

    Returns:
        Relevante content uit de documentatie
    """
    try:
        # Generate embedding for the query
        embedding_response = await ctx.deps.openai_client.embeddings.create(
            model=ctx.deps.embedding_model,
            input=query
        )
        query_embedding = embedding_response.data[0].embedding

        # Search for similar documents using the match_documents function
        result = await ctx.deps.supabase.rpc(
            'match_documents',
            {
                'query_embedding': query_embedding,
                'match_count': 4,
                'filter': {}
            }
        ).execute()

        if not result.data:
            return "Geen relevante informatie gevonden in de documentatie."

        # Format the results
        documents = []
        for doc in result.data:
            content = doc.get('content', '')
            similarity = doc.get('similarity', 0)
            if similarity > 0.7:  # Only include relevant results
                documents.append(content)

        if not documents:
            return "Geen relevante informatie gevonden in de documentatie."

        return "\n\n---\n\n".join(documents)

    except Exception as e:
        return f"Er ging iets mis bij het zoeken in de documentatie: {str(e)}"


@website_agent.tool
async def submit_lead(
    ctx: RunContext[WebsiteAgentDeps],
    name: str,
    email: str,
    company: str,
    chat_summary: str
) -> str:
    """
    Verstuur lead informatie naar het sales team.

    Gebruik ALLEEN nadat je alle benodigde contactgegevens hebt verzameld:
    - name: Volledige naam van de klant
    - email: Email adres
    - company: Bedrijfsnaam (kan leeg zijn)
    - chat_summary: Samenvatting van het gesprek en de behoefte

    Dit triggert dezelfde flow als het contactformulier op de website.

    Args:
        name: Volledige naam van de klant
        email: Email adres van de klant
        company: Bedrijfsnaam (optioneel, mag lege string zijn)
        chat_summary: Samenvatting van het gesprek met de behoefte van de klant

    Returns:
        Bevestiging dat de lead is verstuurd
    """
    try:
        # Validate email format (basic check)
        if not email or '@' not in email:
            return "Ongeldig email adres. Vraag de klant om een geldig email adres."

        # 1. Insert into contact_submissions
        await ctx.deps.supabase.from_('contact_submissions').insert({
            'name': name,
            'email': email,
            'company': company or None,
            'message': chat_summary,
            'source': 'chatbot'
        }).execute()

        # 2. Upsert into clients (update if exists, insert if not)
        await ctx.deps.supabase.from_('clients').upsert(
            {
                'email': email,
                'name': name,
                'company': company or None,
                'source': 'chatbot'
            },
            on_conflict='email'
        ).execute()

        # 3. Trigger email via Edge Function (optional - may not be set up yet)
        try:
            await ctx.deps.supabase.functions.invoke(
                'send-contact-email',
                invoke_options={
                    'body': {
                        'name': name,
                        'email': email,
                        'company': company,
                        'message': chat_summary
                    }
                }
            )
        except Exception:
            # Edge function may not exist yet, that's okay
            pass

        return f"Lead succesvol verstuurd! We nemen binnen 24 uur contact op met {name} via {email}."

    except Exception as e:
        return f"Er ging iets mis bij het versturen van de lead: {str(e)}. Probeer het opnieuw of neem direct contact op via info@llmsolution.nl"


@website_agent.tool
async def schedule_meeting(
    ctx: RunContext[WebsiteAgentDeps],
    name: str,
    email: str,
    company: str,
    preferred_time: str,
    topic: str
) -> str:
    """
    Plan een gesprek in met het LLM Solution team.

    Gebruik wanneer een klant een gesprek wil inplannen.
    Verzamel EERST alle benodigde gegevens:
    - name: Volledige naam
    - email: Email adres
    - company: Bedrijfsnaam (optioneel)
    - preferred_time: Voorkeurstijd (bijv. "volgende week dinsdag ochtend", "zo snel mogelijk")
    - topic: Onderwerp van het gesprek (bijv. "AI chatbot implementatie", "RAG systeem")

    Args:
        name: Volledige naam van de klant
        email: Email adres van de klant
        company: Bedrijfsnaam (optioneel, mag lege string zijn)
        preferred_time: Voorkeurstijd voor het gesprek
        topic: Onderwerp/doel van het gesprek

    Returns:
        Bevestiging dat de meeting request is verstuurd
    """
    try:
        # Validate email format (basic check)
        if not email or '@' not in email:
            return "Ongeldig email adres. Vraag de klant om een geldig email adres."

        meeting_summary = f"Gesprek aanvraag - Onderwerp: {topic}. Voorkeurstijd: {preferred_time}"

        # 1. Insert into contact_submissions with meeting type
        await ctx.deps.supabase.from_('contact_submissions').insert({
            'name': name,
            'email': email,
            'company': company or None,
            'message': meeting_summary,
            'source': 'chatbot-meeting'
        }).execute()

        # 2. Upsert into clients
        await ctx.deps.supabase.from_('clients').upsert(
            {
                'email': email,
                'name': name,
                'company': company or None,
                'source': 'chatbot'
            },
            on_conflict='email'
        ).execute()

        # 3. Trigger email via Edge Function (reuse send-contact-email)
        try:
            await ctx.deps.supabase.functions.invoke(
                'send-contact-email',
                invoke_options={
                    'body': {
                        'name': name,
                        'email': email,
                        'company': company,
                        'message': f"📅 GESPREK AANVRAAG\n\nOnderwerp: {topic}\nVoorkeurstijd: {preferred_time}"
                    }
                }
            )
        except Exception:
            # Edge function may not exist yet, that's okay
            pass

        return f"""Gesprek aanvraag succesvol verstuurd!

We nemen zo snel mogelijk contact op met {name} via {email} om een moment in te plannen.

**Aanvraag details:**
- Onderwerp: {topic}
- Voorkeurstijd: {preferred_time}

Je ontvangt binnen 24 uur een bevestiging met een concrete datum en tijd."""

    except Exception as e:
        return f"Er ging iets mis bij het inplannen: {str(e)}. Probeer het opnieuw of neem direct contact op via info@llmsolution.nl"
