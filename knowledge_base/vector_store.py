from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "math_kb")

# Ensure collection exists
if COLLECTION_NAME not in [c.name for c in qdrant_client.get_collections().collections]:
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=len(embeddings.embed_query("test")),
            distance=Distance.COSINE
        )
    )

qdrant = Qdrant(
    client=qdrant_client,
    collection_name=COLLECTION_NAME,
    embeddings=embeddings
)
