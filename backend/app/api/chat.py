from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse  # Adjust import based on your setup
from app.services.embedding_service import generate_embeddings
from app.services.retrieval_service import search_similar_chunks
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/api/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def ask_question(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    try:
        # 1. Generate query embedding
        query_vector = generate_embeddings([request.question])[0]
        
        # 2. Retrieve top chunks from ChromaDB
        retrieved_chunks = search_similar_chunks(
            query_embedding=query_vector, 
            top_k=request.top_k
        )
        
        # 3. Generate answer via LLM
        answer = generate_answer(
            query=request.question, 
            context_chunks=retrieved_chunks
        )
        
        return ChatResponse(
            answer=answer,
            sources=retrieved_chunks
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))