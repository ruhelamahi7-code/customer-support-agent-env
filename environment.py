from dataset import dataset
from agent import agent
from evaluator import evaluate

def run_environment():
    total_score = 0

    for i, data in enumerate(dataset):
        print(f"\n--- Test Case {i+1} ---")
        print("Ticket:", data["ticket"])

        output = agent(data["ticket"])
        print("Agent Output:")
        print("Issue:", output["issue"])
        print("Action:", output["action"])
        print("Reply:", output["reply"])

        score = evaluate(output, data)
        print("Score for this case:", score)

        total_score += score

    final_score = total_score / len(dataset)
    print("\n====================")
    print("Final Average Score:", final_score)

if __name__ == "__main__":
    run_environment()