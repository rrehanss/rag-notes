from pathlib import Path

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



    