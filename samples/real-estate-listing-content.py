#!/usr/bin/env python3
"""
Real Estate Listing Content Generator Sample

Generates SEO-friendly descriptions, social posts, and email blasts from property details.
"""

def generate_listing_content(property_details: dict) -> dict:
    """
    property_details example:
    {
        "address": "...",
        "beds": 3,
        "baths": 2,
        "sqft": 1850,
        "price": 475000,
        "key_features": ["updated kitchen", "large backyard", "near park"],
        "neighborhood": "..."
    }
    """
    # In production: LLM call with strong real estate copywriting prompt
    return {
        "description": "Charming 3 bed, 2 bath single family in the heart of [neighborhood]. Updated kitchen, spacious backyard perfect for entertaining, walking distance to the park. Priced at $475,000.",
        "instagram_caption": "Just listed! 3bd/2ba with modern updates and a yard that dreams are made of 🏡 Link in bio for details or to schedule a private tour.",
        "email_blast_subject": "New Listing: 3 Bed Home Near the Park - $475k",
        "follow_up_sequence": ["Day 1: Tour invite", "Day 3: Market stats for the area", "Day 7: Similar homes"]
    }

# Use this as base for Premium package content agents.