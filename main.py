from src.config import DOCUMENTS_DIR
from src.document_loader import load_documents
from src.chunker import chunk_documents
from src.embeddings import embed_documents

sections = load_documents(DOCUMENTS_DIR)
chunks = chunk_documents(sections)
vectors = embed_documents(chunks)

print("Chunks:", len(chunks))
print("Vectors shape:", vectors.shape)
print("Type:", vectors.dtype)