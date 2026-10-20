from src.config import DOCUMENTS_DIR
from src.document_loader import load_single_document

print(load_single_document(DOCUMENTS_DIR/"sample.txt"))
