# -------------------------------
# IMPORTS
# -------------------------------

# Connect to local LLM
from langchain_ollama import OllamaLLM

# PDF loader
from langchain_community.document_loaders import PyPDFLoader

# Text splitter (chunking system)
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embedding model (turns text into numbers)
from langchain_huggingface import HuggingFaceEmbeddings


# Vector database
from langchain_community.vectorstores import FAISS

# Prompt builder
from langchain_core.prompts import PromptTemplate

import os

# -------------------------------
# SETTINGS
# -------------------------------

PDF_PATH = "docs"   # Folder containing PDFs
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

print("\n📄 PDF AI System Starting...\n")

# -------------------------------
# LOAD ALL PDFS
# -------------------------------

documents = []

for file in os.listdir(PDF_PATH):
    if file.endswith(".pdf"):
        print(f"Loading: {file}")
        loader = PyPDFLoader(os.path.join(PDF_PATH, file))
        documents.extend(loader.load())

print(f"\nTotal pages loaded: {len(documents)}")

# -------------------------------
# SPLIT INTO CHUNKS
# -------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# -------------------------------
# EMBEDDINGS (NUMERICAL BRAIN)
# -------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL
)

# -------------------------------
# VECTOR STORE (KNOWLEDGE BASE)
# -------------------------------

vector_db = FAISS.from_documents(chunks, embeddings)

print("\n🧠 Knowledge base built and ready!\n")

# -------------------------------
# AI BRAIN
# -------------------------------

llm = OllamaLLM(model="llama3")

# -------------------------------
# PROMPT TEMPLATE
# -------------------------------

rag_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI assistant.

Use the context below as your source of facts.
If the question requires calculation, comparison, or reasoning,
first extract the relevant facts from the context,
then perform the necessary logic step-by-step.

If the answer truly cannot be found or derived from the context, say:
"I could not find or calculate this information from the document."

Context:
{context}

Question:
{question}

Follow this format:
1. Facts found in document:
2. Reasoning / Calculation:
3. Final Answer:
"""
)


# -------------------------------
# CHAT LOOP
# -------------------------------

while True:
    question = input("📘 Ask a question about your PDF (or type 'exit'): ")

    if question.lower() == "exit":
        print("\n👋 Goodbye! Your document AI is shutting down.")
        break

    # Search for relevant chunks
    results = vector_db.similarity_search(question, k=3)

    # Combine found chunks into context
    context = "\n\n".join([doc.page_content for doc in results])

    # Build final prompt
    final_prompt = rag_prompt.format(
        context=context,
        question=question
    )

    # Ask AI
    answer = llm.invoke(final_prompt)

    print("\n🤖 Answer:\n")
    print(answer)
    print("\n" + "-"*50 + "\n")