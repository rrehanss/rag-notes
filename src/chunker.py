from src.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str, filename: str, page: int, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP) ->list[dict]:
    chunks = []

    if len(text) <= chunk_size:
        return [{
            "text": text,
            "filename": filename,
            "page": page, 
            "chunk_id": 0
        }]
    chunk_step = chunk_size - chunk_overlap

    if chunk_step <= 0:
        raise ValueError("Chunks Size is supposed to be greater than chunk overlap")

    chunk_id = 0
    chunk_start = 0
    total_length = len(text)

    while chunk_start < total_length:
        chunk_end = chunk_start + chunk_size
        chunk_slice = text[chunk_start:chunk_end].strip()
        if chunk_slice: 
            chunks.append({
                "text": chunk_slice,
                "filename": filename,
                "page": page, 
                "chunk_id": chunk_id
            })
            chunk_id+= 1
        if chunk_end >= total_length: 
            break
        chunk_start += chunk_step 

    return chunks