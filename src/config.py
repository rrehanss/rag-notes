"""
This module centralizes all configurable parameters for the RAG pipeline.
Centralizing configuration ensures we do not hardcode model names,
paths, or hyperparameters across multiple files.
"""

from pathlib import Path

# OLLAMA And Model Config 

# Default local server
OLLAMA_HOST = "http://127.0.0.1:11434"
# Converts textual content to vectors
EMBEDDING_MODEL = "nomic-embed-text"
# Generates final answer from the retrieved context
LLM_MODEL = "qwen2.5:7b"


# CHUNK Parameters 

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200 

# Top K Chunks 

TOP_K = 4 

# Storage and Directory Path 

# Its a full path to our main directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
# Its a full path to the documents
DOCUMENTS_DIR = BASE_DIR / "documents"
# Its a full path to the data
DATA_DIR = BASE_DIR / "data"

# Similar to this, FAISS, metadata(json)
# Since they live in data, it goes under it 

# FAISS index binary file
FAISS_INDEX_PATH = DATA_DIR / "faiss.index"
# Metadata JSON file (maps FAISS vector ID -> chunk text & source document)
METADATA_PATH = DATA_DIR / "metadata.json"




