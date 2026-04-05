import random
import os

def get_random_reply():
    responses = [
        "We will resolve your issue.",
        "Our team is looking into it.",
        "We apologize and will fix this soon.",
        "Thank you for your patience, we are handling this.",
        "We’re sorry for the inconvenience caused."
    ]
    return random.choice(responses)

def agent(ticket):
    ticket = ticket.lower()

    # PRODUCT ISSUES
    if any(word in ticket for word in ["damaged", "broken", "defective", "not working", "bad condition", "poor quality", "wrong item"]):
        return {
            "issue": "product",
            "action": "replace",
            "reply": get_random_reply()
        }

    # BILLING ISSUES
    elif any(word in ticket for word in ["charged", "payment", "deducted", "refund", "overcharged"]):
        return {
            "issue": "billing",
            "action": "refund",
            "reply": get_random_reply()
        }

    # SHIPPING ISSUES
    elif any(word in ticket for word in ["delayed", "delivery", "not arrived", "shipment", "late", "not delivered", "status"]):
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": get_random_reply()
        }

    # DEFAULT
    else:
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": get_random_reply()
        }