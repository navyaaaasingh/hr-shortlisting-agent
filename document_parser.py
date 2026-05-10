import fitz
import pdfplumber
from docx import Document

def parse_pdf(file_path):

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()

    return text

def parse_docx(file_path):

    doc = Document(file_path)

    return "\n".join(
        [para.text for para in doc.paragraphs]
    )

def parse_resume(file_path):

    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)

    elif file_path.endswith(".docx"):
        return parse_docx(file_path)

    return ""
