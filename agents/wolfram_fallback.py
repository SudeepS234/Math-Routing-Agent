import os
import requests

WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")

def wolfram_fallback(query: str) -> str:
    if not WOLFRAM_APP_ID:
        return "WolframAlpha App ID not set."
    url = "https://api.wolframalpha.com/v1/result"
    params = {
        "i": query,
        "appid": WOLFRAM_APP_ID
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("⚠️ WolframAlpha API Error:", e)
        return "I couldn't get an answer from WolframAlpha."