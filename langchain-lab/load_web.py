from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer

# Only extract the main Wikipedia article content
only_content = SoupStrainer(id="mw-content-text")

loader = WebBaseLoader(
    "https://en.wikipedia.org/wiki/United_States_Department_of_State",
    bs_kwargs={
        "parse_only": only_content
    }
)

docs = loader.load()

print(f"Total documents loaded: {len(docs)}\n")

for i, doc in enumerate(docs):
    print(f"----- DOCUMENT {i + 1} -----")
    print(doc.page_content[:1000])
    print("Metadata:", doc.metadata)
    print()
