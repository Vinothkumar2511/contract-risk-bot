import re
from docx import Document
from PyPDF2 import PdfReader

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)

    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    else:
        return file.read().decode("utf-8")

def extract_clauses(text):
    clauses = re.split(r"\n\d+\.|\n[A-Z][A-Z ]+:", text)
    return [c.strip() for c in clauses if len(c.strip()) > 50]
