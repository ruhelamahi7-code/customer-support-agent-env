# EASY TASK (basic classification)
easy_tasks = [
    {"ticket": "I received a damaged product", "issue": "product", "action": "replace"},
    {"ticket": "The item is defective", "issue": "product", "action": "replace"},
    {"ticket": "My order hasn't arrived yet", "issue": "shipping", "action": "escalate"},
    {"ticket": "Delivery is taking too long", "issue": "shipping", "action": "escalate"},
    {"ticket": "I was charged twice for my order", "issue": "billing", "action": "refund"},
    {"ticket": "Payment failed but money was deducted", "issue": "billing", "action": "refund"},
]

# MEDIUM TASK (slightly complex cases)
medium_tasks = [
    {"ticket": "The product is not working properly", "issue": "product", "action": "replace"},
    {"ticket": "I received the wrong item", "issue": "product", "action": "replace"},
    {"ticket": "My order is delayed by 7 days", "issue": "shipping", "action": "refund"},
    {"ticket": "My order is delayed by 10 days", "issue": "shipping", "action": "refund"},
    {"ticket": "Refund has not been processed yet", "issue": "billing", "action": "escalate"},
    {"ticket": "I want a refund for my order", "issue": "billing", "action": "refund"},
]

# HARD TASK (real-world edge cases)
hard_tasks = [
    {"ticket": "Money deducted but order not placed", "issue": "billing", "action": "refund"},
    {"ticket": "I was overcharged for my purchase", "issue": "billing", "action": "refund"},
    {"ticket": "Shipment is stuck for many days", "issue": "shipping", "action": "escalate"},
    {"ticket": "Why is my delivery so late?", "issue": "shipping", "action": "escalate"},
    {"ticket": "The product arrived in bad condition", "issue": "product", "action": "replace"},
    {"ticket": "Product quality is very poor", "issue": "product", "action": "replace"},
    {"ticket": "The delivery guy never showed up", "issue": "shipping", "action": "escalate"},
    {"ticket": "Order status is not updating", "issue": "shipping", "action": "escalate"},
]

# COMBINED DATASET (used by env)
dataset = easy_tasks + medium_tasks + hard_tasks