import requests


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
import os

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}

def agent(ticket):
    # Try AI first
    try:
        prompt = f"Classify this ticket and decide action: {ticket}"

        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        text = response.json()[0]["generated_text"].lower()

        # If model gives meaningful response, try extracting
        if "billing" in text:
            return {"issue": "billing", "action": "refund", "reply": "We will process your refund."}

        elif "product" in text or "damaged" in text or "broken" in text:
            return {"issue": "product", "action": "replace", "reply": "We will replace your product."}

        elif "shipping" in text or "delivery" in text:
            return {"issue": "shipping", "action": "escalate", "reply": "We will look into the delivery issue."}

    except:
        pass

    # Fallback (RULE-BASED — ensures correctness)
    ticket = ticket.lower()

    if "damaged" in ticket or "broken" in ticket or "defective" in ticket:
        return {"issue": "product", "action": "replace", "reply": "We will replace your product."}

    elif "delayed" in ticket or "late" in ticket or "not delivered" in ticket:
        return {"issue": "shipping", "action": "escalate", "reply": "We will investigate the delay."}

    elif "charged" in ticket or "payment" in ticket or "deducted" in ticket:
        return {"issue": "billing", "action": "refund", "reply": "We will process your refund."}

    else:
        return {"issue": "shipping", "action": "escalate", "reply": "We will look into your issue."}
import random

responses = [
    "We will resolve your issue.",
    "Our team is looking into it.",
    "We apologize and will fix this soon."
]

reply = random.choice(responses)