from src.config import DOCUMENTS_DIR
from src.document_loader import load_documents
from src.chunker import chunk_document

sections = load_documents(DOCUMENTS_DIR)
chunks = chunk_document(sections)

print("Sections loaded:", len(sections))
print("Chunks created:", len(chunks))

lengths = [len(c["text"]) for c in chunks]
print("Longest chunk:", max(lengths))
print("Shortest chunk:", min(lengths))

for c in chunks[:3]:
    print("\n---", c["filename"], "page", c["page"], "chunk", c["chunk_id"], "global", c["global_chunk_id"], "---")
    print(c["text"][:200])