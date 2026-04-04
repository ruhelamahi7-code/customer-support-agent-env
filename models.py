from dataclasses import dataclass

# Input state (what agent sees)
@dataclass
class State:
    ticket: str

# Output action (what agent produces)
@dataclass
class Action:
    issue: str
    action: str
    reply: str