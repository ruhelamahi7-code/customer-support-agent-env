fimport gradio as gr
from env import CustomerSupportEnv

def run_env():
    env = CustomerSupportEnv()
    state = env.reset()

    output_text = "Starting Environment...\n\n"

    done = False

    while not done:
        output_text += f"Ticket: {state.ticket}\n"

        state, reward, done, action = env.step()

        output_text += f"Issue: {action.issue}\n"
        output_text += f"Action: {action.action}\n"
        output_text += f"Reply: {action.reply}\n"
        output_text += f"Reward: {reward}\n"
        output_text += "\n-------------------\n\n"

    return output_text

iface = gr.Interface(
    fn=run_env,
    inputs=[],
    outputs="text",
    title="Customer Support Agent Environment",
    description="Simulates an AI agent handling customer support tickets"
)

iface.launch()