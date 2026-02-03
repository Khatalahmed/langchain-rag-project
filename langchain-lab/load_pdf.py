from langchain_community.document_loaders import PyPDFLoader

# Load TEXT-based PDF
loader = PyPDFLoader("data/large_text.pdf")
docs = loader.load()

print(f"Total pages loaded: {len(docs)}\n")

for i, doc in enumerate(docs):
    print(f"----- PAGE {i + 1} -----")
    print(doc.page_content[:800])  # preview
    print("Metadata:", doc.metadata)
    print()
