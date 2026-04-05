import os
from env import CustomerSupportEnv
from agent import agent

def run_inference():
    print("[START] Running inference")

    env = CustomerSupportEnv()
    state = env.reset()

    total_reward = 0
    steps = 0

    done = False

    while not done:
        print(f"[STEP] Ticket: {state.ticket}")

        action = agent(state.ticket)

        state, reward, done, info = env.step(action)

        print(f"[STEP] Issue: {action['issue']}")
        print(f"[STEP] Action: {action['action']}")
        print(f"[STEP] Reward: {reward}")

        total_reward += reward
        steps += 1

    final_score = total_reward / steps

    print(f"[END] Final Score: {final_score}")


if __name__ == "__main__":
    run_inference()