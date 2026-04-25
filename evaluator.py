
def evaluate(output, correct, difficulty="hard"):
    score = 0

    if difficulty == "easy":
        if output["issue"] == correct["issue"]:
            score = 1.0
        return score

    if difficulty == "medium":
        if output["issue"] == correct["issue"]:
            score += 0.5
        if output["action"] == correct["action"]:
            score += 0.5
        return score

    # hard — 4 components
    if output["issue"] == correct["issue"]:
        score += 0.25
    if output["action"] == correct["action"]:
        score += 0.25
    if len(output.get("reply", "")) > 30:
        score += 0.25
    if output["action"] in output.get("reply", "").lower():
        score += 0.25

    return max(0.0, min(score, 1.0))