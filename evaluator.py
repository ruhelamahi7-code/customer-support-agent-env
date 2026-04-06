def evaluate(output, correct):
    score = 0

    # Issue check
    if output["issue"] == correct["issue"]:
        score += 0.25
    else:
        score -= 0.25

    # Action check
    if output["action"] == correct["action"]:
        score += 0.25
    else:
        score -= 0.25

    # Reply length check
    if len(output["reply"]) > 30:
        score += 0.25
    else:
        score -= 0.25

    # Action mentioned in reply
    if output["action"] in output["reply"].lower():
        score += 0.25
    else:
        score -= 0.25

    return  max(score, 0)
    
