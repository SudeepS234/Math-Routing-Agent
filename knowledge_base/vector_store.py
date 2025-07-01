from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.config import QDRANT_URL, QDRANT_COLLECTION_NAME

# Initialize embeddings
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Initialize Qdrant client
client = QdrantClient(QDRANT_URL)

# ✅ Create collection if not exists
if not client.collection_exists(collection_name=QDRANT_COLLECTION_NAME):
    print(f"Creating collection `{QDRANT_COLLECTION_NAME}` in Qdrant...")
    client.recreate_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,  # embedding size of all-MiniLM-L6-v2
            distance=Distance.COSINE,
        ),
    )

# Create LangChain Qdrant wrapper
qdrant = Qdrant(
    client=client,
    collection_name=QDRANT_COLLECTION_NAME,
    embeddings=embeddings
)
