#!/usr/bin/env python3
"""
Real Estate Follow-up & Nurturing Agent Sample

Keeps leads warm with personalized sequences.
"""

def generate_follow_up(lead: dict, days_since_contact: int, event_type: str = "new_lead") -> str:
    if event_type == "new_lead":
        return "Thanks for reaching out about the property on Main St. Quick question - are you working with a lender yet? I have a couple great options if you need intros."
    elif event_type == "open_house":
        return "Loved meeting you at the open house yesterday! Here's a quick video walkthrough of the home + 3 similar properties that just hit the market in the same price range."
    # Extend with more triggers: price drop, new listing, just listed alerts, etc.
    return "Personalized follow-up message here."

# Real version would run on a schedule or triggered by CRM events.