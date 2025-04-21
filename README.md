# 🛒 Swiggy Voice Grocery Extractor 🎙️

Say goodbye to the hassle of adding grocery items one by one on Swiggy Instamart! With this smart AI-powered tool, just **speak your entire shopping list**, and it extracts all items with quantities — instantly.

---

## ✨ Problem Statement

Ever been asked to order groceries and handed a long list?  
Now you’re stuck adding them manually on Instamart one-by-one.  
What if you could just read the list aloud and have everything show up?

> **"Mom: Order this list, okay?"  
> Son: *deep sigh while typing each item manually into search...*  
> 🤯**

---

## 🚀 Solution

With this tool:
- Speak your grocery list in one go using a mic or type it in.
- AI transcribes and parses your list intelligently.
- Automatically extracts item names and quantities.
- Returns a structured format that can be directly used for product matching on Swiggy.

---

## 🛠️ How It Works

🔊 **Input**: Voice or text input  
🧠 **Processing**:
- Whisper (or any voice-to-text model) transcribes the speech.
- A small language model (like T5 or Teapot) extracts item names and quantities.
- Regex to extract items and their respective quantities.

📦 **Output**: A clean JSON list like:

```json
[
  {"item": "Amul butter", "quantity": null},
  {"item": "Lady's finger", "quantity": "100gms"},
  {"item": "Cheese", "quantity": "250gms"}
]
```

## 🎯 Features
- 🎤 Voice & Text input supported via Gradio

- 🧠 Smart AI understanding of item names (even with brands)

- 🔍 Scalable to plug into Swiggy or similar grocery platforms

- ⚡ Lightweight (works under ~1.5GB RAM)

## 📷 UI Preview
![Grocery Extractor UI](./assets/![demo_screenshot](https://github.com/user-attachments/assets/fd1f0c90-7de9-46a5-a453-189155117336))

🔧 Setup
Install dependencies:

```bash
pip install -r requirements.txt
```
Make sure ffmpeg is installed and available in your system path.

Run the app:

```bash
python app.py
```

📫 Contact
Crafted with ❤️ by Sai Adhithya
