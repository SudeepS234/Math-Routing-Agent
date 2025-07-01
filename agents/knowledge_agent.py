from knowledge_base.vector_store import qdrant

def search_kb(query):
    results = qdrant.similarity_search(query, k=1)
    if results:
        return results[0].metadata.get("answer")
    return None
