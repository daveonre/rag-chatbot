import uuid
import chromadb

# Initialize local persistent storage in the 'chroma_db' folder
client = chromadb.PersistentClient(path="./chroma_db")
# Get or create a collection named 'pdf_documents'
collection = client.get_or_create_collection(name="pdf_documents")

print(f"📊 Document Count: {collection.count()}")
print("🔍 Peek items:", collection.peek(limit=5))


def store_chunks(chunks: list[str], embeddings: list[list[float]], doc_name: str = "default_doc") -> int:
    """
    Stores text chunks and their corresponding embeddings into ChromaDB.
    """
    if not chunks or not embeddings:
        return 0

    ids = [str(uuid.uuid4()) for _ in chunks]
    metadatas = [{"source": doc_name, "chunk_index": i} for i in range(len(chunks))]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )

    return len(chunks)


def search_similar_chunks(query_embedding: list[float], top_k: int = 3) -> list[str]:
    """
    Finds top_k text chunks most semantically similar to the query vector.
    """
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    if results and "documents" in results and results["documents"]:
        return results["documents"][0]

    return []