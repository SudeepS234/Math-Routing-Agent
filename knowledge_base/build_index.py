from langchain.docstore.document import Document
from knowledge_base.vector_store import qdrant

sample_data = [
    ("What is 2+2?", "2+2 equals 4."),
    ("What is the derivative of x^2?", "The derivative of x^2 is 2x."),
    ("Integrate x dx", "The integral of x dx is (1/2)x^2 + C.")
]

docs = [Document(page_content=q, metadata={"answer": a}) for q, a in sample_data]
qdrant.add_documents(documents=docs)
print("Vector store indexed.")
