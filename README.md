# Nova — Voice Assistant 🎙️

A real-time voice assistant built with:
- **STT** — Browser Web Speech API (SpeechRecognition)
- **AI Brain** — Claude API via Python Flask backend
- **TTS** — Browser SpeechSynthesis API

---

## Project Structure

```
nova_assistant/
├── app.py              ← Flask backend (talks to Claude API)
├── static/
│   └── index.html      ← Frontend UI (STT + TTS + chat UI)
├── .env                ← Your API key (never commit this!)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup & Run

### 1. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Anthropic API key
Edit the `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```
Get your key at: https://console.anthropic.com/settings/keys

### 4. Run the server
```bash
python app.py
```

### 5. Open in Chrome
Go to: **http://localhost:5000**

> ⚠️ Must use Chrome — Firefox does not support Web Speech API for STT.

---

## How It Works

```
[You speak] → SpeechRecognition (STT)
           → POST /chat → Flask → Claude API
           → Response text → SpeechSynthesis (TTS)
           → Nova speaks back
```

---

## GitHub Submission

1. Push this folder to a **public** GitHub repo
2. Make sure `.env` is in `.gitignore` (already done!)
3. Record a demo video and upload to YouTube
4. Share GitHub + YouTube links on LinkedIn and tag Uneeq Interns
