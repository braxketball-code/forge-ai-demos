#!/usr/bin/env python3
"""
Simple Lead Qualifier Agent Example
For demo / client delivery reference.

This is a starting template. In real projects we integrate with the client's website/IG/SMS platform
and use their preferred LLM or tools.

Usage: Adapt the system prompt and scoring logic for the specific niche.
"""

import os

def qualify_lead(lead_message: str, niche: str = "general") -> dict:
    """
    Basic lead qualification logic.
    In production: call your LLM (Grok, Claude, GPT, etc.) with a strong system prompt.
    """
    system_prompt = f"""
You are an expert {niche} sales assistant AI.

Your job is to qualify incoming leads quickly and helpfully.

For every lead message, return a JSON with:
- score: 1-10 (how sales-ready)
- intent: one of ["ready_to_buy", "browsing", "price_sensitive", "just_questions", "not_qualified"]
- next_action: suggested response or booking prompt
- notes: any key details

Be friendly, concise, and focused on moving the conversation forward.
"""

    # Placeholder for real LLM call
    # In real delivery we use the client's API key or our wrapper
    print(f"[DEMO] Would call LLM with system prompt for niche: {niche}")
    print(f"[DEMO] Lead message: {lead_message}")

    # Mock response for demo purposes
    return {
        "score": 7,
        "intent": "browsing",
        "next_action": "Reply with value + soft booking link",
        "notes": "Mentioned timeline interest"
    }


if __name__ == "__main__":
    example = "Hi, I'm looking at 3-bed homes in downtown. Do you have any open this weekend?"
    result = qualify_lead(example, niche="real estate")
    print(result)

# Real projects usually wrap this in a webhook, ManyChat/Botpress flow, or simple FastAPI endpoint.