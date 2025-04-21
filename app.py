from formatter import re_formatter
from llm_extractor import extract_using_llm
from voice_to_text import transcribe_text


import gradio as gr

# Master function: handles audio or text
def handle_input(audio, text):
    items = None 
    if audio is not None:
        text = transcribe_text(audio)
    extract_llm = extract_using_llm(text)
    items = re_formatter(extract_llm)
    return text, items

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🗣️ Grocery Extractor using Whisper")
    gr.Markdown("Speak or type your grocery list, and get structured items with quantities.")

    with gr.Row():
        text_input = gr.Textbox(label="Or type your list")
        audio_input = gr.Audio(type="numpy", format="wav", label="Record your list (WAV only)")


    btn = gr.Button("Extract")
    output_text = gr.Textbox(label="Transcribed Text")
    output_json = gr.JSON(label="Extracted Items")

    btn.click(fn=handle_input, inputs=[audio_input, text_input], outputs=[output_text, output_json])

demo.launch()
