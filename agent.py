import requests


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
import os

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}

def agent(ticket):
    ticket = ticket.lower()

    # PRODUCT ISSUES
    if any(word in ticket for word in ["damaged", "broken", "defective", "not working", "bad condition", "poor quality", "wrong item"]):
        return {
            "issue": "product",
            "action": "replace",
            "reply": "We will replace your product."
        }

    # BILLING ISSUES
    elif any(word in ticket for word in ["charged", "payment", "deducted", "refund", "overcharged"]):
        return {
            "issue": "billing",
            "action": "refund",
            "reply": "We will process your refund."
        }

    # SHIPPING ISSUES
    elif any(word in ticket for word in ["delayed", "delivery", "not arrived", "shipment", "late", "not delivered", "status"]):
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": "We will investigate the delay."
        }

    # DEFAULT
    else:
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": "We will look into your issue."
        }

responses = [
    "We will resolve your issue.",
    "Our team is looking into it.",
    "We apologize and will fix this soon."
]

reply = random.choice(responses)