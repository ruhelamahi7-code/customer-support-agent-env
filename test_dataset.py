from dataset import dataset

for data in dataset:
    print("Ticket:", data["ticket"])
    print("Issue:", data["issue"])
    print("Action:", data["action"])
    print("------")