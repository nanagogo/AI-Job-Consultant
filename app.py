import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com",
)

SYSTEM_PROMPT = (
    "你是一个毒舌但专业的求职顾问。"
    "你必须保持专业、准确、可执行，不做无依据的断言。"
    "你的回复必须简短且犀利：优先用 1-3 句短句，直击问题核心，不寒暄，不废话。"
    "可以尖锐指出问题，但不能做人身攻击或使用低俗辱骂。"
    "当用户询问求职相关问题时，先指出关键短板，再给出可立即执行的改进建议。"
)


def create_message_state():
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def chat(user_input, message_state, ui_history):
    user_input = (user_input or "").strip()
    if not user_input:
        return "", ui_history, message_state, ui_history

    if message_state is None:
        message_state = create_message_state()
    if ui_history is None:
        ui_history = []

    message_state.append({"role": "user", "content": user_input})
    ui_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=message_state,
            stream=False,
        )
        assistant_reply = (response.choices[0].message.content or "").strip()
    except Exception as e:
        assistant_reply = f"请求失败：{e}"

    message_state.append({"role": "assistant", "content": assistant_reply})
    ui_history.append({"role": "assistant", "content": assistant_reply})
    return "", ui_history, message_state, ui_history


def clear_chat():
    return [], create_message_state(), []


with gr.Blocks(title="毒舌求职顾问") as demo:
    gr.Markdown("# 毒舌求职顾问")

    message_state = gr.State(create_message_state())
    ui_history = gr.State([])

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="对话",
                height=560,
            )
        with gr.Column(scale=2):
            user_input = gr.Textbox(
                label="输入你的问题",
                placeholder="比如：我的简历投了 100 份还没面试，问题在哪？",
                lines=8,
            )
            send_btn = gr.Button("发送", variant="primary")
            clear_btn = gr.Button("清空对话")

    send_btn.click(
        fn=chat,
        inputs=[user_input, message_state, ui_history],
        outputs=[user_input, chatbot, message_state, ui_history],
    )
    user_input.submit(
        fn=chat,
        inputs=[user_input, message_state, ui_history],
        outputs=[user_input, chatbot, message_state, ui_history],
    )
    clear_btn.click(
        fn=clear_chat,
        inputs=[],
        outputs=[chatbot, message_state, ui_history],
    )


if __name__ == "__main__":
    demo.launch()