import gradio as gr
from env import CustomerSupportEnv

def run_env():
    env = CustomerSupportEnv()
    state = env.reset()

    output_text = "Starting Environment...\n\n"
    total_reward = 0
    count = 0

    done = False

    while not done:
        output_text += f"Ticket: {state.ticket}\n"

        state, reward, done, action = env.step()

        total_reward += reward
        count += 1

        output_text += f"Issue: {action['action'].issue}\n"
        output_text += f"Action: {action['action'].action}\n"
        output_text += f"Reply: {action['action'].reply}\n"
        output_text += f"Reward: {reward}\n"
        output_text += "\n-------------------\n\n"

    final_score = total_reward / count
    output_text += f"\nFINAL SCORE: {final_score}\n"

    return output_text


iface = gr.Interface(
    fn=run_env,
    inputs=[],
    outputs="text",
    title="Customer Support Agent Environment",
    description="Simulates an AI agent handling customer support tickets",
    allow_flagging="never"
)

iface.launch(server_name="0.0.0.0", server_port=7860)