"""Response validator to ensure chatbot only uses RAG and never general knowledge."""

from typing import Optional
import re


class ResponseValidator:
    """Validates chatbot responses to ensure they follow RAG-only rules."""

    # Keywords that indicate meeting/lead actions (allowed without tool usage)
    ACTION_KEYWORDS = [
        'gesprek', 'inplannen', 'contact', 'meeting', 'afspraak',
        'bellen', 'email', 'naam', 'bedrijf'
    ]

    # Common general knowledge indicators that should NEVER appear
    FORBIDDEN_PATTERNS = [
        # Sports/celebrities
        r'voetballer|voetbal|sport|atleet|speler',
        r'geboren op|geboren in',
        r'carrière|speelde voor|club',

        # General knowledge
        r'hoofdstad van|president van|koning van',
        r'definitie van|betekent dat|is een term',
        r'geschiedenis van|uitgevonden door',

        # Math/science (unless from docs)
        r'\d+\s*\+\s*\d+\s*=\s*\d+',  # Simple math like "2+2=4"
        r'formule voor|volgens de wet van',

        # Generic explanations
        r'is een proces waarbij|is een systeem dat',
        r'algemeen bekend|iedereen weet',
    ]

    @staticmethod
    def validate_response(
        response_text: str,
        user_message: str,
        tool_calls_made: list[str]
    ) -> tuple[bool, Optional[str]]:
        """
        Validate if a response follows RAG-only rules.

        Args:
            response_text: The agent's response text
            user_message: The original user message
            tool_calls_made: List of tool names that were called

        Returns:
            (is_valid, error_message) tuple
        """
        # Check if action tools were called (schedule_meeting or submit_lead)
        # These are ALWAYS valid, even without keywords in user message
        # (user might be providing info in follow-up: "jesse lamm jesselamm@icloud.com...")
        action_tools_called = any(
            tool in tool_calls_made
            for tool in ['schedule_meeting', 'submit_lead']
        )

        # If action tools were called, validate and allow
        if action_tools_called:
            # Still check for forbidden patterns (shouldn't happen with action tools)
            response_lower = response_text.lower()
            for pattern in ResponseValidator.FORBIDDEN_PATTERNS:
                if re.search(pattern, response_lower):
                    return False, (
                        f"VALIDATOR BLOCKED: Algemene kennis gedetecteerd in response. "
                        f"Pattern: {pattern}. De chatbot mag ALLEEN documentatie gebruiken."
                    )
            return True, None  # Action tool calls are always valid

        # Check if this is an action request by keywords
        is_action_request = any(
            keyword in user_message.lower()
            for keyword in ResponseValidator.ACTION_KEYWORDS
        )

        # If not an action request, retrieve_relevant_documents MUST have been called
        if not is_action_request:
            if 'retrieve_relevant_documents' not in tool_calls_made:
                return False, (
                    "VALIDATOR BLOCKED: Informatievraag zonder tool gebruik gedetecteerd. "
                    "retrieve_relevant_documents moet altijd worden aangeroepen voor informatievragen."
                )

        # Check for forbidden general knowledge patterns
        response_lower = response_text.lower()
        for pattern in ResponseValidator.FORBIDDEN_PATTERNS:
            if re.search(pattern, response_lower):
                return False, (
                    f"VALIDATOR BLOCKED: Algemene kennis gedetecteerd in response. "
                    f"Pattern: {pattern}. De chatbot mag ALLEEN documentatie gebruiken."
                )

        # Check for suspicious signs of general knowledge
        # If response is long but no tool was used for info questions
        if (
            len(response_text) > 100
            and not is_action_request
            and 'retrieve_relevant_documents' not in tool_calls_made
        ):
            return False, (
                "VALIDATOR BLOCKED: Lange response zonder RAG tool gebruik. "
                "Dit duidt op gebruik van algemene kennis."
            )

        return True, None

    @staticmethod
    def get_fallback_response(user_message: str) -> str:
        """
        Get a safe fallback response when validation fails.

        Args:
            user_message: The original user message

        Returns:
            Safe fallback response
        """
        return (
            "Ik heb daar geen informatie over in onze documentatie. "
            "Ik kan alleen vragen beantwoorden over LLM Solution's AI-diensten en oplossingen. "
            "Heb je vragen daarover, of wil je een gesprek inplannen met het team?"
        )
