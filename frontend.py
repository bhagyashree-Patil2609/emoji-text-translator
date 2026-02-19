import gradio as gr

custom_css = """
/* Animated Gradient Background */
body {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
}

/* Animation Keyframes */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Make all text black and bold */
* {
    color: black !important;
    font-weight: bold !important;
}

/* Buttons Styling */
.gr-button {
    background-color: #6c5ce7 !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 12px !important;
    transition: 0.3s ease-in-out;
}

.gr-button:hover {
    background-color: #a29bfe !important;
    transform: scale(1.05);
}

/* Textboxes */
textarea, input {
    border-radius: 12px !important;
    border: 2px solid #6c5ce7 !important;
    font-weight: bold !important;
}
"""

def create_app(emoji_to_name, name_to_emoji):

    with gr.Blocks(css=custom_css) as app:

        gr.Markdown("# 🌈 Emoji ↔ Name Translator")

        with gr.Tab("😊 Emoji ➝ Name"):
            e_input = gr.Textbox(label="Enter Emoji(s)")
            e_output = gr.Textbox(label="Result", lines=5)
            e_btn = gr.Button("Translate")
            e_btn.click(emoji_to_name, inputs=e_input, outputs=e_output)

        with gr.Tab("🔎 Name ➝ Emoji"):
            n_input = gr.Textbox(label="Enter Word (Example: dog, india)")
            n_output = gr.Textbox(label="Matching Emojis", lines=8)
            n_btn = gr.Button("Search")
            n_btn.click(name_to_emoji, inputs=n_input, outputs=n_output)

    return app
