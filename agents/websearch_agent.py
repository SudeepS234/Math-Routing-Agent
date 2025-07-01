import os
import requests
from dotenv import load_dotenv
load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_KEY")

def fallback_web_answer(query):
    if not SERP_API_KEY:
        return None

    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google",
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json()
        snippets = [s.get("snippet") for s in results.get("organic_results", []) if "snippet" in s]

        if snippets:
            return {
                "answer": snippets[0],
                "explanation": "This answer was retrieved from a web search. Accuracy not guaranteed."
            }

    except Exception as e:
        print("Web search failed:", e)

    return None
