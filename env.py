from dataset import dataset
from agent import agent
from evaluator import evaluate

class CustomerSupportEnv:
    def __init__(self):
        self.index = 0
        self.data = dataset
        self.current_ticket = None

    def reset(self):
        self.index = 0
        self.current_ticket = self.data[self.index]["ticket"]
        from models import State
        return State(ticket=self.current_ticket)

    def step(self, action=None):
        output = action if action else agent(self.current_ticket)

        correct = self.data[self.index]
        reward = evaluate(output, correct)

        self.index += 1
        done = self.index >= len(self.data)

        if not done:
            next_ticket = self.data[self.index]["ticket"]
            self.current_ticket = next_ticket
        else:
            next_ticket = None

        from models import Action, State

        action_obj = Action(
            issue=output["issue"],
            action=output["action"],
            reply=output["reply"]
        )

        next_state = State(ticket=next_ticket) if next_ticket else None

        return next_state, reward, done, {"action": action_obj}

    def state(self):
        from models import State
        return State(ticket=self.current_ticket)