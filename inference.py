import os
from env import CustomerSupportEnv

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def mock_agent(ticket):
    ticket_lower = ticket.lower()
    if any(w in ticket_lower for w in ["charge", "payment", "refund", "money", "billed", "overcharged", "deducted"]):
        issue, action = "billing", "refund"
    elif any(w in ticket_lower for w in ["ship", "deliver", "arrival", "late", "stuck", "delay", "arrived"]):
        issue, action = "shipping", "escalate"
    else:
        issue, action = "product", "replace"
    return {
        "issue": issue,
        "action": action,
        "reply": f"We are sorry for the inconvenience. We will {action} this for you shortly."
    }

def run_inference():
    print("[START] Running inference")
    print(f"[CONFIG] API key set: {bool(OPENAI_API_KEY)}")

    if OPENAI_API_KEY:
        from agent import agent
        active_agent = agent
        print("[CONFIG] Using real agent")
    else:
        active_agent = mock_agent
        print("[CONFIG] No API key found — using mock agent for reproducible baseline")

    env = CustomerSupportEnv()
    state = env.reset()

    total_reward = 0
    steps = 0
    easy_scores, medium_scores, hard_scores = [], [], []
    done = False

    while not done:
        print(f"\n[STEP {steps + 1}] Ticket: {state.ticket}")

        action = active_agent(state.ticket)
        difficulty = env._get_difficulty(env.index)

        state, reward, done, info = env.step(action)

        print(f"[STEP {steps + 1}] Difficulty : {difficulty}")
        print(f"[STEP {steps + 1}] Issue      : {action['issue']}")
        print(f"[STEP {steps + 1}] Action     : {action['action']}")
        print(f"[STEP {steps + 1}] Reply      : {action['reply']}")
        print(f"[STEP {steps + 1}] Reward     : {reward:.2f}")

        total_reward += reward
        steps += 1

        if difficulty == "easy":
            easy_scores.append(reward)
        elif difficulty == "medium":
            medium_scores.append(reward)
        else:
            hard_scores.append(reward)

    final_score = total_reward / steps

    print(f"\n[RESULTS] ----------------------------------------")
    print(f"  Easy   avg : {sum(easy_scores)/len(easy_scores):.2f}  (over {len(easy_scores)} tickets)")
    print(f"  Medium avg : {sum(medium_scores)/len(medium_scores):.2f}  (over {len(medium_scores)} tickets)")
    print(f"  Hard   avg : {sum(hard_scores)/len(hard_scores):.2f}  (over {len(hard_scores)} tickets)")
    print(f"  Overall    : {final_score:.2f}  (over {steps} tickets)")
    print(f"[END] -----------------------------------------------")

if __name__ == "__main__":
    run_inference()