from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import *

router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)

# 1. Custom UploadFile class to force Swagger UI to show "Choose File"
class SwaggerUploadFile(UploadFile):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return {"type": "string", "format": "binary"}

@router.post("/upload")
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

            content = await file.read()
            extracted_text = extract_text_from_pdf(content)

            chunks = chunk_text(extracted_text)
            extracted_documents.append({
                "filename": file.filename,
                "size": len(content),
                "text_length": len(extracted_text),
                "text_preview": extracted_text[:500],
                "total_chunks": len(chunks),
                "first_chunk_preview": chunks[0] if chunks else None
            })
        return {
            "total_files": len(files),
            "documents": extracted_documents,
            "message": f"Successfully processed {len(files)} document(s)."
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the documents: {str(e)}"
        )