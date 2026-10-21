from pathlib import Path
import pymupdf

SUPPORTED_EXTENSIONS = { ".pdf", ".txt", ".md"}

def load_single_document(file_path: Path) -> list[dict]:
    ext = file_path.suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)

    if ext in {".md", ".txt"}:
        try:
            text = file_path.read_text(encoding = "utf-8").strip()
            if text:
                return [{
                    "filename": file_path.name, 
                    "text": text, 
                    "page": 1,
                    "total_pages": 1
                }]
        except Exception as e:
            print(f"Failed to read the text from file '{file_path.name}':{e}")
    return []

def extract_text_from_pdf(file_path: Path) -> list[dict]:
    pages_data = []
    try:
        doc = pymupdf.open(file_path)
        num_pages = len(doc)
        for page_index in range(num_pages):
            page = doc[page_index]
            page_text = (page.get_text() or "").strip()

            if page_text:
                pages_data.append({
                    "filename": file_path.name, 
                    "text": page_text, 
                    "page": page_index + 1, 
                    "total_pages" : num_pages
                })
    except Exception as e:
        print(f"Warning: Failed to extract text from PDF '{file_path.name}':{e}")

    return pages_data


def load_documents(directory_path: Path) -> list[dict]:
    if not directory_path.exists():
        directory_path.mkdir(parents = True, exist_ok = True)
        return []
    
    all_sections : list[dict] = []
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            print(f"Skipping FOLDER: {file_path.name}")
            continue
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            print(f"Skipping unsupported file {file_path.name}")
            continue
        doc_section = load_single_document(file_path)
        all_sections.extend(doc_section)

    return all_sections
                    

    