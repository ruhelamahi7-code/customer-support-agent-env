iimport gradio as gr
from env import CustomerSupportEnv

def run_env():
    env = CustomerSupportEnv()
    state = env.reset()

    output_text = "Starting Environment...\n\n"
    total_reward = 0
    count = 0
    easy_scores, medium_scores, hard_scores = [], [], []

    done = False

    while not done:
        difficulty = env._get_difficulty(env.index)

        output_text += f"Ticket     : {state.ticket}\n"
        output_text += f"Difficulty : {difficulty}\n"

        state, reward, done, info = env.step()

        output_text += f"Issue      : {info['action'].issue}\n"
        output_text += f"Action     : {info['action'].action}\n"
        output_text += f"Reply      : {info['action'].reply}\n"
        output_text += f"Reward     : {reward:.2f}\n"
        output_text += "-" * 40 + "\n\n"

        total_reward += reward
        count += 1

        if difficulty == "easy":
            easy_scores.append(reward)
        elif difficulty == "medium":
            medium_scores.append(reward)
        else:
            hard_scores.append(reward)

    final_score = total_reward / count

    output_text += f"\n===== RESULTS =====\n"
    output_text += f"Easy   avg : {sum(easy_scores)/len(easy_scores):.2f}  ({len(easy_scores)} tickets)\n"
    output_text += f"Medium avg : {sum(medium_scores)/len(medium_scores):.2f}  ({len(medium_scores)} tickets)\n"
    output_text += f"Hard   avg : {sum(hard_scores)/len(hard_scores):.2f}  ({len(hard_scores)} tickets)\n"
    output_text += f"Overall    : {final_score:.2f}  ({count} tickets)\n"

    return output_text


iface = gr.Interface(
    fn=run_env,
    inputs=[],
    outputs="text",
    title="Customer Support Agent Environment",
    description="Simulates an AI agent handling customer support tickets and evaluates performance using rewards.",
    allow_flagging="never",
    submit_btn="Run Simulation"
)

iface.launch(server_name="0.0.0.0", server_port=7860)