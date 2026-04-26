from agent import agent
from evaluator import evaluate

# sample data
correct = {
    "ticket": "I received a damaged product",
    "issue": "product",
    "action": "replace"
}

output = agent(correct["ticket"])

score = evaluate(output, correct)

print("Agent Output:", output)
print("Score:", score)