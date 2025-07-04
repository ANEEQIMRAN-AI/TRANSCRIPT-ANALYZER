import fitz  # PyMuPDF

def extract_text_from_file(input_dict: dict) -> dict:
    file_path = input_dict.get("file_path")

    if file_path.endswith(".pdf"):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return {"transcript_text": text}

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return {"transcript_text": f.read()}

    else:
        raise ValueError("Unsupported file format. Please upload .pdf or .txt only.")
