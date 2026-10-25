"""
This file contains embeddings function. 
Converts human text to dnese nermical vectors
Text which has similar meaning gets mapped to vectors that point in a similar direction

Nomic-Embed text
Wants a small label in front of every text telling it what kinda text it is 
for eg:
query_prefix: "search question"
document_prefix: "search document"

WHY?
With Labels, it places questions near the chunks that answer them, so search gets accurate
"""

import numpy as np
import ollama
from src.config import EMBEDDING_MODEL, OLLAMA_HOST

def get_ollama_client() -> ollama.Client:
    return ollama.Client(host = OLLAMA_HOST)

def embed_text(text: str, model: str = EMBEDDING_MODEL, is_query: bool= False) -> np.ndarray:
    client = get_ollama_client()

    if "nomic" in model.lower():
        if is_query:
            text = "search_query: " + text
        else:
            text = "search_document: " + text

    try:
        response = client.embeddings(model = model, prompt = text)
        vector = response["embedding"]
        return np.array(vector, dtype = np.float32)
    except Exception as e:
        raise RuntimeError(
            f"Failed to generate embedding with model '{model}'. "
            f"Ensure Ollama is running and run 'ollama pull {model}'.\nError: {e}"
        )

