# 🤖 AI Agent — Intelligent Webhook Chatbot with Supabase

A production-ready AI agent built with **Python (Flask)** that handles incoming webhook messages, applies intelligent keyword-based response logic, and stores unhandled queries in a **Supabase** database for follow-up. Designed for multi-channel deployment (WhatsApp, Messenger, custom chat interfaces, etc.).

---

## 🚀 Features

- **Webhook-based AI Agent** — receives messages via POST requests from any platform
- **Keyword Intent Detection** — instantly responds to greetings, pricing queries, and help requests
- **Supabase Integration** — unmatched messages are saved to a cloud database for human review
- **Modular & Extensible** — easy to plug in LLM (OpenAI, Gemini) for smarter responses
- **Lightweight REST API** — built with Flask, deployable on GCP Cloud Run, Railway, or any container platform

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | Supabase (PostgreSQL) |
| Deployment | GCP Cloud Run / Docker |
| AI Logic | Keyword NLP (extensible to LLM) |

---

## 📁 Project Structure

```
Ai-Agent/
├── app.py                              # Main Flask webhook agent
├── apps.py                             # Extended app logic
├── AI_Face_Recognition_Attendance_System_.ipynb  # Bonus: CV-based attendance AI
├── requirenmnet.txt                    # Dependencies
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/jawadsatti320/Ai-Agent.git
cd Ai-Agent
```

### 2. Install dependencies
```bash
pip install -r requirenmnet.txt
```

### 3. Set environment variables
```bash
export SUPABASE_URL="your_supabase_url"
export SUPABASE_KEY="your_supabase_anon_key"
```

### 4. Run the agent
```bash
python app.py
```

Agent will start on `http://localhost:5000`

---

## 📬 API Usage

### POST `/webhook`

Send a message to the agent:

```json
{
  "content": "Hello, I need help",
  "sender": {
    "id": "user_123"
  }
}
```

**Response (matched intent):**
```json
{
  "content": "Hello! How can I help you today?"
}
```

**Response (unmatched — saved to Supabase):**
```json
{
  "content": "Thanks! We've saved your message and will respond soon."
}
```

---

## 🧠 How It Works

```
Incoming Message (webhook)
        ↓
  Keyword Detection
   ┌────┴────┐
Matched    Not Matched
   ↓            ↓
Instant     Save to
Response   Supabase DB
```

---

## 🔮 Roadmap

- [ ] Integrate OpenAI / Gemini LLM for smarter responses
- [ ] Add Streamlit / Gradio UI for agent monitoring dashboard
- [ ] Deploy on GCP Cloud Run with CI/CD
- [ ] Add multi-language support (Urdu, Arabic)

---

## 👨‍💻 Author

**Jawad Ahmed** — AI Engineer & ML Specialist  
BS Computer Science (AI) — PMAS Rawalpindi  
Currently at DEVROLIN

> *Building intelligent systems — from AI agents and chatbots to computer vision pipelines.*

---

## 📄 License

MIT License — feel free to use, modify, and build on this project.
