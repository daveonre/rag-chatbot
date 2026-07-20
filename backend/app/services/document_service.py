from io import BytesIO
from pypdf import PdfReader


def extract_text_from_pdf(file: BytesIO | bytes) -> str:
    """
    Extracts text from a PDF file.
    """
    if isinstance(file, bytes):
        file = BytesIO(file)

    file.seek(0)

    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:  # Prevents TypeError if page.extract_text() returns None
            text += extracted + "\n"

    return text.strip()


def chunk_text(
    text: str, 
    chunk_size: int = 500, 
    overlap_percentage: float = 0.25
) -> list[str]:
    """
    Splits text into chunks of fixed character length with percentage-based overlap.
    """
    if not text:
        return []

    # Ensure chunk_size is always at least 100 to avoid zero-step infinite loops
    chunk_size = max(100, chunk_size)
    chunk_overlap = int(chunk_size * overlap_percentage)
    
    step = chunk_size - chunk_overlap

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Guarantees forward movement on every iteration
        start += step

    return [c.strip() for c in chunks if c.strip()]