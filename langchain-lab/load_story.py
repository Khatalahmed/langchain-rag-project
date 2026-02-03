from langchain_community.document_loaders import TextLoader

# Load plain text file (no unstructured needed)
loader = TextLoader("data/story.txt", encoding="utf-8")

# Load documents
docs = loader.load()

# Print content and metadata
for doc in docs:
    print("----- CONTENT -----")
    print(doc.page_content)
    print("----- METADATA -----")
    print(doc.metadata)
