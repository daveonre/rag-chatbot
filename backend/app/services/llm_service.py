import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query: str, context_chunks: list[str]) -> str:
    """
    Combines retrieved chunks with a user query and asks the LLM to generate an answer.
    """
    # 1. Join retrieved context chunks into a single string
    context_text = "\n\n".join(context_chunks)
    
    # 2. Construct the system prompt (forcing the LLM to rely on provided context)
    system_prompt = (
        "You are a helpful AI assistant. Answer the user's question using ONLY "
        "the provided context below. If the answer cannot be found in the context, "
        "reply with: 'I don't have enough information in my database to answer that.'"
    )
    
    user_prompt = f"Context:\n{context_text}\n\nUser Question: {query}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast and cost-effective model for RAG
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2  # Lower temperature keeps answers grounded and factual
        )
        
        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ Error generating LLM answer: {e}")
        return "An error occurred while generating the answer."