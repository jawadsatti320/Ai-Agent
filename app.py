from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Load Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://qlvhtlhvkysdwklfcdjc.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsdmh0bGh2a3lzZHdrbGZjZGpjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM5NDQ1MDIsImV4cCI6MjA2OTUyMDUwMn0.Ls75z-btEDx5e--W6ZBFLAjGrg73q1ZkzfCa9n_YsaY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    data = request.json
    content = data.get("content", "")
    sender_id = data.get("sender", {}).get("id")

    if not content or not sender_id:
        return jsonify({"error": "Invalid request, missing sender or content"}), 400

    # Basic keyword AI logic
    if any(keyword in content.lower() for keyword in ["hi", "hello", "price", "help"]):
        return jsonify({"content": "Hello! How can I help you today?"})

    # If message doesn't match known logic → store in Supabase
    try:
        supabase.table("fallback_messages").insert({
            "user_id": sender_id,
            "message": content
        }).execute()
    except Exception as e:
        print(f"Error saving to Supabase: {e}")
        return jsonify({"content": "Something went wrong. Please try again later."}), 500

    return jsonify({"content": "Thanks! We’ve saved your message and will respond soon."})

if __name__ == "__main__":
    app.run(port=5000)
