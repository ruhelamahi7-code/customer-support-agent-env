---
title: Customer Support Agent Env
emoji: 📊
colorFrom: green
colorTo: indigo
sdk: docker
pinned: false
---

# Customer Support Agent Environment

An OpenEnv-compatible environment where an AI agent handles customer support tickets by classifying issues, deciding actions, and writing replies.

## Environment Description

The agent receives a customer support ticket (plain text) and must output three things: the issue type, the correct action, and a reply to the customer. Performance is scored against ground-truth labels.

## Observation Space

| Field  | Type   | Description                        |
|--------|--------|------------------------------------|
| ticket | string | Raw customer support message       |

## Action Space

| Field  | Type   | Description                                        |
|--------|--------|----------------------------------------------------|
| issue  | string | Issue category: `billing`, `shipping`, or `product`|
| action | string | Action to take: `refund`, `replace`, or `escalate` |
| reply  | string | Response message to the customer                   |

## Reward

Scores range from 0.0 to 1.0. Each component contributes 0.25:
- Correct issue classification → +0.25
- Correct action decision → +0.25
- Reply length > 30 characters → +0.25
- Action keyword present in reply → +0.25

## Tasks

| Level  | Description                              |
|--------|------------------------------------------|
| Easy   | Classify issue type from clear tickets   |
| Medium | Classify issue and decide correct action |
| Hard   | Full pipeline: classify + action + reply |

## Setup
```bash
git clone https://huggingface.co/spaces/xyzzzz21122/customer-support-agent-env
cd customer-support-agent-env
pip install -r requirements.txt
```

Set environment variables:
```bash
export OPENAI_API_KEY=your_key
export API_BASE_URL=https://api.openai.com/v1
export MODEL_NAME=gpt-3.5-turbo
```

Run inference:
```bash
python inference.py
```

## Files

| File            | Purpose                          |
|-----------------|----------------------------------|
| env.py          | Main environment (step/reset/state) |
| models.py       | Typed State and Action dataclasses |
| evaluator.py    | Reward/scoring function          |
| dataset.py      | Easy/medium/hard task data       |
| agent.py        | Baseline LLM agent               |
| inference.py    | Runs full evaluation loop        |
| openenv.yaml    | OpenEnv spec declaration         |
