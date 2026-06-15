#!/usr/bin/env python3
"""
Real Estate Tour / Showing Booking Agent Sample

Handles scheduling logic and confirmation.
In production: Integrates with Calendly, Google Calendar, or the agent's MLS/CRM booking system.
"""

def handle_tour_request(lead_info: dict, requested_time: str) -> dict:
    """
    Example logic for confirming a tour.
    """
    # Mock availability check + booking
    return {
        "status": "confirmed",
        "tour_time": requested_time,
        "address": "123 Main St, Anytown",
        "confirmation_message": f"Great! Your private showing for 123 Main St is confirmed for {requested_time}. I'll text you the lockbox code and parking instructions 30 min before.",
        "follow_up": "Send prep guide + similar homes 2 days before the tour."
    }

# Extend with actual calendar API calls for client projects.