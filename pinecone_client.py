import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load .env variables
load_dotenv()

# Get API key and region from environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_REGION = os.getenv("PINECONE_REGION")

# Initialize Pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# Index name and embedding dimension
INDEX_NAME = "smartcity-policies"
EMBEDDING_DIM = 384  # Adjust this if using a different embedding model

# Create index if not exists
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=EMBEDDING_DIM,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_REGION
        )
    )

# Connect to the index
index = pc.Index(INDEX_NAME)


# Semantic search function
def semantic_search(query_vector: list, top_k: int = 5):
    response = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    return response
