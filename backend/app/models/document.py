from pydantic import BaseModel
from typing import Optional

class DocumentSummary(BaseModel):
    filename: str
    size: int
    text_length: int
    total_chunks: int
    chunks_stored: int
    first_chunk_preview: Optional[str] = None

class DocumentUploadResponse(BaseModel):
    total_files: int
    documents: list[DocumentSummary]
    message: str