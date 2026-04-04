from env import CustomerSupportEnv
import time

while True:
    env = CustomerSupportEnv()
    state = env.reset()

    print("Starting Environment...\n")

    done = False

    while not done:
        print("Ticket:", state.ticket)

        state, reward, done, action = env.step()

        print("Issue:", action.issue)
        print("Action:", action.action)
        print("Reply:", action.reply)
        print("Reward:", reward)
        print("\n-------------------\n")

    time.sleep(5)  # wait before restarting