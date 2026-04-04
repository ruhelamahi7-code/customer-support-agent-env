from dataset import dataset
from agent import agent
from evaluator import evaluate

class CustomerSupportEnv:
    def __init__(self):
        self.index = 0
        self.data = dataset
        self.current_ticket = None

    # Reset environment (start from beginning)
    def reset(self):
        self.index = 0
        self.current_ticket = self.data[self.index]["ticket"]
        from models import State
        return State(ticket=self.current_ticket)

    # Step function (one interaction)
    def step(self):
        # Agent processes ticket
        output = agent(self.current_ticket)

        # Get correct answer
        correct = self.data[self.index]

        # Evaluate
        reward = evaluate(output, correct)

        # Move to next ticket
        self.index += 1

        done = False
        if self.index >= len(self.data):
            done = True
            next_state = None
        else:
            next_state = self.data[self.index]["ticket"]
            self.current_ticket = next_state

        from models import Action, State

        action_obj = Action(
        issue=output["issue"],
        action=output["action"],
        reply=output["reply"]
        )

        if next_state:
            next_state = State(ticket=next_state)

        return next_state, reward, done, action_obj

    # State (current ticket)
   
    def state(self):
        from models import State
        return State(ticket=self.current_ticket)