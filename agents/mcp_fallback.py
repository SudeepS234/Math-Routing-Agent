# agents/mcp_fallback.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def mistral_fallback(query: str) -> str:
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a math tutor. Answer the user's question step by step."},
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("⚠️ MCP (Hugging Face Mistral) Error:", e)
        return "I couldn't get an answer from the fallback model (Mistral)."
