# agents/router.py

from knowledge_base.vector_store import qdrant
from agents.llama3_fallback import llama3_fallback

THRESHOLD = 0.75

def answer_query(query: str) -> str:
    results = qdrant.similarity_search_with_score(query, k=1)
    print("Retrieved Results:", results)

    if results:
        doc, score = results[0]
        print(f"⚠️ Similarity Score: {score}")
        if score >= THRESHOLD:
            return (
                f"✅ Answer: {doc.metadata.get('answer', 'No answer found.')}\n\n"
                f"📝 Explanation: {doc.page_content}"
            )
        else:
            print("⚠️ Low similarity score. Falling back to LLaMA-3...")

    return f"💡 Answer (from LLaMA-3):\n{llama3_fallback(query)}"
