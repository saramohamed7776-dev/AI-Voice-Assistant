from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder="static")
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Nova, a helpful real-time voice assistant.
Keep responses short and conversational — 1 to 3 sentences max unless the user asks for detail.
Do not use markdown, bullet points, or special characters — your response will be spoken aloud.
Be warm, clear, and helpful."""


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        response = client.chat.completions.create(
           model="llama-3.3-70b-versatile",
            max_tokens=1000,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    key = os.getenv("GROQ_API_KEY")
    if not key:
        print("\n⚠️  WARNING: GROQ_API_KEY not set in .env file!")
        print("   Get a free key at: https://console.groq.com\n")
    else:
        print(f"\n✅ Groq API key loaded: {key[:12]}...")
    print("🚀 Nova Voice Assistant running at http://localhost:5000\n")
    app.run(debug=True, port=5000)
