# agents/llama3_fallback.py

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

def llama3_fallback(query: str) -> str:
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful and accurate math solver. Solve the following step by step."},
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ LLaMA-3 fallback error:", e)
        return "Sorry, I couldn't process this question right now."
