Nova — Real-Time Voice Assistant
A real-time AI voice assistant built with Python Flask, Groq API, and browser-native Speech Recognition & Synthesis.

# About the Project
Nova is a fully functional real-time voice assistant built from scratch as part of the Uneeq Interns internship program. The task was to implement a voice assistant using Speech-to-Text (STT) and Text-to-Speech (TTS) technologies.
Nova listens to your voice through the microphone, sends it to a Python Flask backend, gets an AI-generated response from the Groq API, and speaks the answer back to you — all in real time.
# How It Works
┌─────────────┐     ┌──────────────────┐     ┌────────────────┐     ┌─────────────┐
│  You Speak  │────▶│ Web Speech API   │────▶│  Flask Backend │────▶│  Groq API   │
│  (Mic)      │     │ SpeechRecognition│     │  POST /chat    │     │ LLaMA 3.3   │
└─────────────┘     │ (STT)            │     └────────────────┘     └──────┬──────┘
                    └──────────────────┘                                   │
┌─────────────┐     ┌──────────────────┐                                   │
│ Nova Speaks │◀────│ SpeechSynthesis  │◀──────────────────────────────────┘
│ (Speaker)   │     │ (TTS)            │         AI Response Text
└─────────────┘     └──────────────────┘

# Project Structure
nova_assistant/
├── app.py                  ← Flask backend — handles /chat route & Groq API
├── static/
│   └── index.html          ← Frontend UI with STT, TTS, and chat interface
├── .env                    ← API key (never committed — gitignored)
├── .gitignore
├── requirements.txt        ← Python dependencies
└── README.md
