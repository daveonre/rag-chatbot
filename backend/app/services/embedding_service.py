import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
#initialize OpenAI API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_embeddings(chunks: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """
    Generates embeddings for the given list of texts using OpenAI's API.

    Args:
        chunks (list[str]): The list of texts to generate embeddings for.
        model (str): The model to use for generating the embeddings. Default is "text-embedding-3-small".

    Returns:
        list[list[float]]: A list of vector embeddings, one for each input chunk.
    """

    if not chunks:
        return []
    
    response = client.embeddings.create(
        input=chunks,
        model=model
    )
    # Extract the vector list from the response objects
    embeddings = [item.embedding for item in response.data]
    return embeddings