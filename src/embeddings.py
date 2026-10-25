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

def embed_documents(chunks: list[dict], model: str = EMBEDDING_MODEL) -> np.ndarray:

    if not chunks:
        return np.empty((0,0), dtype=np.float32)
    vectors = []
    total = len(chunks)

    for idx, chunk in enumerate(chunks, start=1):
        if idx % 100 == 0 or idx == total or idx == 1:
            print(f"Generating embedding for chunk [{idx}/{total}] for '{chunk.get('filename', 'unknown')}' ")
        vec = embed_text(chunk["text"], model, is_query=False)
        vectors.append(vec)

    return np.vstack(vectors).astype(np.float32)
