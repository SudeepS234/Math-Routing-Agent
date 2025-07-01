from agents.knowledge_agent import search_kb
from agents.websearch_agent import fallback_web_answer

def answer_query(query):
    kb_result = search_kb(query)
    if kb_result:
        return f"Answer (from KB): {kb_result}"
    web_result = fallback_web_answer(query)
    return f"Answer (from Web): {web_result}"
