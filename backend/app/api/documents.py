from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import *
from app.services.embedding_service import generate_embeddings
from app.services.retrieval_service import store_chunks
from app.models.document import DocumentUploadResponse  
router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)

# 1. Custom UploadFile class to force Swagger UI to show "Choose File"
class SwaggerUploadFile(UploadFile):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return {"type": "string", "format": "binary"}

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_documents(
    files: list[SwaggerUploadFile] = File(...)
):
    extracted_documents = []
    try:
        for file in files:
            # Check that each file is a PDF
            if not file.filename.lower().endswith(".pdf"):
                raise HTTPException(
                    status_code=400,
                    detail=f"File '{file.filename}' is not supported. Only PDF files are allowed."
                )

            # 1. Read & Extract Text
            content = await file.read()
            extracted_text = extract_text_from_pdf(content)

            # 2. Chunk Text
            chunks = chunk_text(extracted_text)
            
            if chunks:
                # 3. Generate Embeddings & Store in ChromaDB
                embeddings = generate_embeddings(chunks)
                stored_count = store_chunks(chunks=chunks, embeddings=embeddings)
            else:
                stored_count = 0

            extracted_documents.append({
                "filename": file.filename,
                "size": len(content),
                "text_length": len(extracted_text),
                "total_chunks": len(chunks),
                "chunks_stored": stored_count,
                "first_chunk_preview": chunks[0] if chunks else None
            })

        return {
            "total_files": len(files),
            "documents": extracted_documents,
            "message": f"Successfully processed and indexed {len(files)} document(s)."
        }

    except HTTPException as http_ex:
        # Re-raise HTTP exceptions like 400 bad request
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the documents: {str(e)}"
        )