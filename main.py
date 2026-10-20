from src.config import DOCUMENTS_DIR
from src.document_loader import load_documents

docs = load_documents(DOCUMENTS_DIR)
print(len(docs))
for doc in docs:
    print(doc["filename"], "-", doc["text"][:50])
