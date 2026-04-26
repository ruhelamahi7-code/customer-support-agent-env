from env import CustomerSupportEnv

env = CustomerSupportEnv()

state = env.reset()

done = False

while not done:
    print("\nTicket:", state)

    state, reward, done, output = env.step()

    print("Output:", output)
    print("Reward:", reward)