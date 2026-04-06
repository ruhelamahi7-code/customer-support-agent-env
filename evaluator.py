def evaluate(output, correct, difficulty="hard"):
    score = 0

    # Easy: only grade issue classification
    if difficulty == "easy":
        if output["issue"] == correct["issue"]:
            score = 1.0
        return score

    # Medium: grade issue + action
    if difficulty == "medium":
        if output["issue"] == correct["issue"]:
            score += 0.5
        if output["action"] == correct["action"]:
            score += 0.5
        return score

    # Hard: grade all three components
    if output["issue"] == correct["issue"]:
        score += 0.25
    if output["action"] == correct["action"]:
        score += 0.25
    if len(output["reply"]) > 30:
        score += 0.25
    if output["action"] in output["reply"].lower():
        score += 0.25

    return score
    
