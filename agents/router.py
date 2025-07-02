from agents.wolfram_fallback import wolfram_fallback
import re

def is_math_query(query: str) -> bool:
    # Simple heuristic: look for math keywords, numbers, or math symbols
    math_keywords = [
        "solve", "calculate", "equation", "integral", "derivative", "sum", "product",
        "factor", "expand", "simplify", "limit", "probability", "mean", "median", "mode",
        "matrix", "vector", "algebra", "geometry", "theorem", "proof", "function", "graph"
    ]
    if any(word in query.lower() for word in math_keywords):
        return True
    # Look for numbers and common math symbols
    if re.search(r"[\d\+\-\*/\^=<>]", query):
        return True
    return False

def answer_query(query: str) -> str:
    if not is_math_query(query):
        return "Sorry, I can only answer math-related questions."

    from knowledge_base.vector_store import qdrant

    # Use score-based retrieval
    results = qdrant.similarity_search_with_score(query, k=1)
    print("Retrieved Results:", results)

    THRESHOLD = 0.75

    if results:
        doc, score = results[0]
        print(f"⚠️ Similarity Score: {score}")

        if score >= THRESHOLD:
            return (
                f"Answer: {doc.metadata.get('answer', 'No answer found.')}\n\n"
                f"Explanation: {doc.page_content}"
            )
        else:
            print("⚠️ Low similarity score. Falling back to WolframAlpha.")

    # If no results or low similarity
    fallback = wolfram_fallback(query)
    return f"Answer (from WolframAlpha): {fallback}"