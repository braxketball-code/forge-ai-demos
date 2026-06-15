#!/usr/bin/env python3
"""
Real Estate Lead Qualifier Agent - Sample Template

Use as starting point for client deliveries.

Qualifies buyer/seller leads from website forms, IG/FB DMs, Zillow inquiries, etc.
Returns score, intent, recommended next action, and key details to extract.

In real projects: Connect to your client's lead source via webhook, ManyChat, Botpress, or custom endpoint.
Integrate with their calendar for auto-booking.
"""

def qualify_real_estate_lead(lead_message: str, lead_source: str = "website") -> dict:
    """
    Real estate specific qualification.
    """
    system_prompt = """
You are a top-performing real estate buyer's and seller's agent AI assistant.

Extract and score the lead from the message.

Return ONLY valid JSON:
{
  "score": 1-10 (10 = ready to tour/book now),
  "intent": "buyer_ready" | "seller_ready" | "browsing" | "price_sensitive" | "just_info" | "not_qualified",
  "lead_type": "buyer" | "seller" | "investor" | "unknown",
  "key_details": {
    "price_range": "string or null",
    "timeline": "string or null",
    "location": "string or null",
    "property_type": "string or null",
    "pre_approved": "yes|no|unknown",
    "must_haves": "string or null"
  },
  "next_action": "string (specific suggested reply or booking prompt)",
  "notes": "any other insights"
}

Be professional, helpful, and focused on moving the lead to a showing or consultation.
"""

    # In production: call LLM here with the system_prompt + lead_message
    print(f"[DEMO] Real estate lead from {lead_source}: {lead_message[:100]}...")

    # Mock realistic output for demo
    return {
        "score": 8,
        "intent": "buyer_ready",
        "lead_type": "buyer",
        "key_details": {
            "price_range": "$450k-$550k",
            "timeline": "within 60 days",
            "location": "downtown / near park",
            "property_type": "single family",
            "pre_approved": "yes",
            "must_haves": "3+ beds, yard"
        },
        "next_action": "Reply with 2-3 matching listings + offer to book a tour this weekend. Include Calendly link.",
        "notes": "Motivated buyer, pre-approved, specific must-haves"
    }


if __name__ == "__main__":
    example = "Hi, saw your listing on Zillow. Looking for a 3 bed house under 500k, moving in the next month. Are you the listing agent?"
    result = qualify_real_estate_lead(example, lead_source="Zillow")
    print(result)

# Real delivery: Hook this into the agent's actual lead channels and calendar tool.