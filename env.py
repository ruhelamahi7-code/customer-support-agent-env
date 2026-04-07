from dataset import dataset, easy_tasks, medium_tasks
from agent import agent
from evaluator import evaluate

class CustomerSupportEnv:
    def __init__(self):
        self.index = 0
        self.data = dataset
        self.current_ticket = None
        self.easy_ids = list(range(len(easy_tasks)))
        self.medium_ids = list(range(len(easy_tasks), len(easy_tasks) + len(medium_tasks)))

    def _get_difficulty(self, idx):
        if idx in self.easy_ids:
            return "easy"
        elif idx in self.medium_ids:
            return "medium"
        return "hard"

    def reset(self):
        self.index = 0
        self.current_ticket = self.data[self.index]["ticket"]
        from models import State
        return State(ticket=self.current_ticket)

    def step(self, action=None):
        output = action if action else agent(self.current_ticket)

        correct = self.data[self.index]
        difficulty = self._get_difficulty(self.index)
        reward = evaluate(output, correct, difficulty)

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