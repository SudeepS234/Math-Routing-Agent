# agents/router.py

import re
from knowledge_base.vector_store import qdrant
from agents.llama3_fallback import llama3_fallback

THRESHOLD = 0.75

def is_math_query(query: str) -> bool:
    math_keywords = [
        "solve", "calculate", "equation", "integral", "derivative", "sum", "product",
        "factor", "expand", "simplify", "limit", "probability", "mean", "median", "mode",
        "matrix", "vector", "algebra", "geometry", "theorem", "proof", "function", "graph"
    ]
    if any(word in query.lower() for word in math_keywords):
        return True
    if re.search(r"[\d\+\-\*/\^=<>]", query):
        return True
    return False

def answer_query(query: str) -> str:
    if not is_math_query(query):
        return "Sorry, I can only answer math-related questions."

    results = qdrant.similarity_search_with_score(query, k=1)
    print("Retrieved Results:", results)

    if results:
        doc, score = results[0]
        print(f"⚠️ Similarity Score: {score}")
        if score >= THRESHOLD:
            return (
                f"Answer: {doc.metadata.get('answer', 'No answer found.')}\n\n"
                f"Explanation: {doc.page_content}"
            )
        else:
            print("⚠️ Low similarity score. Falling back to LLaMA-3...")

    # Step 2: Fallback
    fallback = llama3_fallback(query)
    return f"Answer (from LLaMA-3):\n{fallback}"
