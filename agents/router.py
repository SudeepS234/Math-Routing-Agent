from agents.knowledge_agent import search_kb
from agents.websearch_agent import fallback_web_answer

def answer_query(query: str) -> str:
    from knowledge_base.vector_store import qdrant

    # similarity_search_with_score returns List[Tuple[Document, float]]
    results = qdrant.similarity_search_with_score(query, k=5)
    print("Retrieved Results:", results)

    if results:
        doc, score = results[0]
        return (
            f"Answer: {doc.metadata.get('answer', 'No answer found.')}\n\n"
            f"Explanation: {doc.page_content or doc.metadata.get('explanation', 'No explanation available.')}"
        )

    # Optional fallback
    # web_answer = fallback_web_answer(query)
    # return f"Answer (from Web): {web_answer}"

    return "Answer: Sorry, I couldn't find an accurate answer to this question.\n\nExplanation: Not available."
