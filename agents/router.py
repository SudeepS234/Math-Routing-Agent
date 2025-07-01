from agents.knowledge_agent import search_kb
from agents.mcp_fallback import mistral_fallback

def answer_query(query: str) -> str:
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
            print("⚠️ Low similarity score. Falling back to Mistral.")

    # If no results or low similarity
    fallback = mistral_fallback(query)
    return f"Answer (from Mistral): {fallback}"
