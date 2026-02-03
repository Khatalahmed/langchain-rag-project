# ============================================================
# STEP 1: Import OCR-based loader
# ============================================================

from langchain_community.document_loaders import PyPDFLoader
import pytesseract
from pdf2image import convert_from_path


# ============================================================
# STEP 2: Convert PDF pages to images
# ============================================================

pdf_path = "data/Actinsoft_OfferLetter_KhatalAhmed_Signed (3).pdf"

images = convert_from_path(pdf_path)

documents = []

# ============================================================
# STEP 3: Run OCR on each page
# ============================================================

for page_number, image in enumerate(images):
    text = pytesseract.image_to_string(image)

    documents.append({
        "page": page_number + 1,
        "content": text
    })


# ============================================================
# STEP 4: Print OCR text
# ============================================================

for doc in documents:
    print(f"----- PAGE {doc['page']} -----")
    print(doc["content"])
    print()
