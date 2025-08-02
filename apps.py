from flask import Flask, request, jsonify
import os
import requests
from supabase import create_client, Client

# === Flask app setup ===
app = Flask(__name__)

# === Chatwoot API Config ===
CHATWOOT_ACCOUNT_ID = "127826"  # Change if different
CHATWOOT_API_KEY = "MPL7JgHwh138i5SQJHn5i2DM"  # 🔁 Replace with your actual key
CHATWOOT_BASE_URL = "https://app.chatwoot.com"  # No trailing slash

# Load Supabase credentials from environment variables
SUPABASE_URL=( "https://qlvhtlhvkysdwklfcdjc.supabase.co")
SUPABASE_KEY=("JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsdmh0bGh2a3lzZHdrbGZjZGpjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM5NDQ1MDIsImV4cCI6MjA2OTUyMDUwMn0.Ls75z-btEDx5e--W6ZBFLAjGrg73q1ZkzfCa9n_YsaY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# === Dummy AI Response Logic ===
def get_bot_reply(message):
    if message.strip() == "":
        return None
    return f"Echo: {message}"  # Replace this with OpenAI/your model

# === Webhook endpoint for Chatwoot ===
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("✅ Received data:", data)

    if "content" in data and "inbox" in data:
        message = data["content"]
        contact_id = data["sender"]["id"]
        conversation_id = data["conversation"]["id"]

        print("📩 Incoming message:", message)
        reply = get_bot_reply(message)
        print("🤖 Bot reply:", reply)

        if reply:
            # Send reply back to Chatwoot
            send_chatwoot_reply(conversation_id, reply)
        else:
            # Save fallback to Supabase
            save_fallback_message(message, "Telegram", contact_id)

    return jsonify({"status": "ok"}), 200
@app.route("/test", methods=["GET"])
def test_supabase():
    try:
        response = supabase.table("messages").select("*").limit(1).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Chatwoot send message ===
def send_chatwoot_reply(conversation_id, message):
    url = f"{CHATWOOT_BASE_URL}/api/v1/accounts/{CHATWOOT_ACCOUNT_ID}/conversations/{conversation_id}/messages"

    headers = {
        "Content-Type": "application/json",
        "api_access_token": CHATWOOT_API_KEY
    }

    payload = {
        "content": message,
        "message_type": "outgoing"
    }

    response = requests.post(url, headers=headers, json=payload)
    print("📤 Chatwoot response:", response.status_code, response.text)

# === Supabase fallback save ===
def save_fallback_message(message, platform, user_id):
    print("💾 Saving fallback to Supabase...")
    try:
        result = supabase.table("fallback_messages").insert({
            "platform": platform,
            "message": message,
            "user_id": user_id
        }).execute()
        print("✅ Fallback saved:", result)
    except Exception as e:
        print("❌ Supabase error:", str(e))
        

# === Start server ===
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
