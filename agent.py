import requests
import os
import random

# Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}


def agent(ticket):
    # Response variations (for randomness)
    responses = {
        "billing": [
            "We will process your refund.",
            "Your refund is being initiated.",
            "We are issuing your refund shortly."
        ],
        "product": [
            "We will replace your product.",
            "A replacement will be sent soon.",
            "We are arranging a replacement for you."
        ],
        "shipping": [
            "We will investigate the delivery issue.",
            "Our team is checking the delay.",
            "We are looking into your shipment issue."
        ]
    }

    # Try AI first
    try:
        prompt = f"Classify this ticket into billing, shipping, or product and suggest action: {ticket}"

        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )

        result = response.json()

        # Safe check (sometimes API gives different format)
        if isinstance(result, list) and "generated_text" in result[0]:
            text = result[0]["generated_text"].lower()

            if "billing" in text:
                return {
                    "issue": "billing",
                    "action": "refund",
                    "reply": random.choice(responses["billing"])
                }

            elif "product" in text or "damaged" in text or "broken" in text:
                return {
                    "issue": "product",
                    "action": "replace",
                    "reply": random.choice(responses["product"])
                }

            elif "shipping" in text or "delivery" in text:
                return {
                    "issue": "shipping",
                    "action": "escalate",
                    "reply": random.choice(responses["shipping"])
                }

    except Exception as e:
        # If API fails, fallback will handle
        pass

    # 🔁 RULE-BASED FALLBACK (ensures correctness)
    ticket = ticket.lower()

    if "damaged" in ticket or "broken" in ticket or "defective" in ticket:
        return {
            "issue": "product",
            "action": "replace",
            "reply": random.choice(responses["product"])
        }

    elif "delayed" in ticket or "late" in ticket or "not delivered" in ticket:
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": random.choice(responses["shipping"])
        }

    elif "charged" in ticket or "payment" in ticket or "deducted" in ticket:
        return {
            "issue": "billing",
            "action": "refund",
            "reply": random.choice(responses["billing"])
        }

    else:
        return {
            "issue": "shipping",
            "action": "escalate",
            "reply": random.choice(responses["shipping"])
        }