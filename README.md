---
title: Customer Support Agent Env
emoji: 🎫
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
tags:
  - openenv
pinned: false
---

# Customer Support Agent Environment

An OpenEnv-compatible RL environment where an AI agent handles
customer support tickets end-to-end — classifying issues,
deciding resolution actions, and drafting professional replies.

## What the agent does

1. Reads a customer ticket: "I was charged twice for my order"
2. Classifies the issue: billing / shipping / product
3. Decides the action: refund / replace / escalate / resolve
4. Writes a professional reply to the customer
5. Gets a reward score (0.0 – 1.0) based on accuracy

## Tasks

| Task | Difficulty | What is graded |
|------|------------|----------------|
| easy | Easy | Issue classification only (1.0 if correct) |
| medium | Medium | Issue + Action (0.5 each) |
| hard | Hard | Issue + Action + Reply length + Action in reply (0.25 each) |

## Reward function

| Component | Points | Rule |
|-----------|--------|------|
| Issue correct | +0.25 | Exact match |
| Action correct | +0.25 | Exact match |
| Reply length | +0.25 | More than 30 characters |
| Action in reply | +0.25 | Action word appears in reply |
| **Total** | **1.0** | Clamped to [0.0, 1.0] |

## Dataset

20 labelled tickets: 6 easy + 6 medium + 8 hard
Issues covered: billing, shipping, product

## Observation space

```
State:
  ticket: str        # The raw customer support ticket
  difficulty: str    # easy | medium | hard
  reward: float      # Score from last step (0.0–1.0)
  done: bool         # Is the episode complete?
```

## Action space

```
Action:
  issue:  billing | shipping | product
  action: refund | replace | escalate | resolve
  reply:  str  (professional reply to the customer)
```

## Run locally

```bash
git clone https://huggingface.co/spaces/xyzzzz21122/customer-support-agent-env
cd customer-support-agent-env
pip install -r requirements.txt
python app.py
```

## Run with Docker

```bash
docker build -t customer-support-env .
docker run -p 7860:7860 customer-support-env
```

## Run inference (baseline benchmark)

```bash
python inference.py
```

## Baseline scores (rule-based keyword agent)

| Difficulty | Avg Score |
|------------|-----------|
| Easy | 1.00 |
| Medium | 0.75 |
| Hard | 0.50 |
| **Overall** | **0.72** |

## Files

```
app.py          Gradio UI
env.py          CustomerSupportEnv — reset() / step() / state()
evaluator.py    Difficulty-aware reward function
agent.py        Keyword-based baseline agent
dataset.py      20 labelled support tickets
models.py       State and Action dataclasses
inference.py    Benchmark script
openenv.yaml    OpenEnv manifest
Dockerfile      Container setup
```
