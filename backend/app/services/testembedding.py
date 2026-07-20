import os
from app.services.embedding_service import generate_embeddings

# 1. Test chunks
sample_chunks = [
    "FastAPI is a modern Python web framework.",
    "OpenAI embeddings convert text into numerical vectors."
]

# 2. Call your function
try:
    vectors = generate_embeddings(sample_chunks)
    
    print(f"✅ Generated {len(vectors)} embeddings.")
    print(f"📊 Vector 1 dimension count: {len(vectors[0])}")
    print(f"🔍 Sample numbers from Vector 1: {vectors[0][:5]}...")

except Exception as e:
    print(f"❌ Error generating embeddings: {e}")