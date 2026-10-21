from src.config import DOCUMENTS_DIR
from src.document_loader import load_documents
from src.chunker import chunk_text

docs = load_documents(DOCUMENTS_DIR)
"""
print(len(docs))
for doc in docs:
    print(doc["filename"], "-", doc["text"][:10])
"""

for c in chunk_text("ABCDEFGHIJ", "test", 1, chunk_size=4, chunk_overlap=1):
    print(c["chunk_id"], c["text"])