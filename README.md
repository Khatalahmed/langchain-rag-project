# 🦜🔗 LangChain Lab

A hands-on learning repository demonstrating **LangChain** capabilities — from basic LLM interactions to advanced RAG pipelines using **Ollama** (100% local, no cloud required).

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.4-green?logo=chainlink)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-purple?logo=llama)

---

## 🎯 What's Inside

| File | Description |
|------|-------------|
| [main.py](cci:7://file:///d:/langchain-lab/main.py:0:0-0:0) | Basic LLM test with Ollama |
| [chain.py](cci:7://file:///d:/langchain-lab/chain.py:0:0-0:0) | Prompt chaining fundamentals |
| [cook_pipeline.py](cci:7://file:///d:/langchain-lab/cook_pipeline.py:0:0-0:0) | LCEL pipeline demo |
| [load_pdf.py](cci:7://file:///d:/langchain-lab/load_pdf.py:0:0-0:0) | PDF document loader |
| [load_pdf_ocr.py](cci:7://file:///d:/langchain-lab/load_pdf_ocr.py:0:0-0:0) | OCR-based PDF extraction |
| [load_story.py](cci:7://file:///d:/langchain-lab/load_story.py:0:0-0:0) | Text file loader |
| [load_web.py](cci:7://file:///d:/langchain-lab/load_web.py:0:0-0:0) | Web scraping with LangChain |
| [memory_chat.py](cci:7://file:///d:/langchain-lab/memory_chat.py:0:0-0:0) | Chatbot with conversation memory |
| [pdf_ai.py](cci:7://file:///d:/langchain-lab/pdf_ai.py:0:0-0:0) | **Complete RAG pipeline** 🔥 |
| [prompt_router.py](cci:7://file:///d:/langchain-lab/prompt_router.py:0:0-0:0) | Intent-based routing |
| [router_with_memory.py](cci:7://file:///d:/langchain-lab/router_with_memory.py:0:0-0:0) | Router + memory integration |
| [router_memory_confidence.py](cci:7://file:///d:/langchain-lab/router_memory_confidence.py:0:0-0:0) | Advanced router with confidence scoring |
| [structured_output.py](cci:7://file:///d:/langchain-lab/structured_output.py:0:0-0:0) | JSON output + self-repair mechanism |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) installed locally

### 1. Setup Ollama

# Install Ollama (visit ollama.ai for your OS)
# Pull a model
ollama pull llama3.2

### 2. Clone & Setup

git clone https://github.com/Khatalahmed/langchain-rag-project.git
cd langchain-rag-project

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

### 3. Run Examples

# Basic LLM test
python main.py

# Full RAG pipeline
python pdf_ai.py

---

## 📁 Project Structure

langchain-rag-project/
├── 📁 data/                  # Sample documents
│   ├── large_text.pdf        # Test PDF
│   └── story.txt             # Sample text
├── 📁 docs/                  # Additional documents
├── 📁 outputs/               # Generated outputs
├── main.py                   # Entry point
├── pdf_ai.py                 # RAG pipeline
├── requirements.txt          # Dependencies
└── README.md                 # You are here!

---

## 🛠️ Tech Stack

- **LangChain** - LLM application framework
- **LangGraph** - Stateful agent workflows
- **Ollama** - Local LLM (Llama, Mistral, etc.)
- **FAISS** - Vector similarity search
- **Sentence Transformers** - Local embeddings

---

## 📚 Key Concepts Demonstrated

- ✅ LLM Integration (Ollama - 100% Local)
- ✅ Document Loading (PDF, Text, Web)
- ✅ Text Splitting & Chunking
- ✅ Embeddings & Vector Stores
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Conversation Memory
- ✅ Prompt Templates & Chaining
- ✅ Intent Routing
- ✅ Structured Output Parsing

---

## 💡 Why Ollama?

- 🔒 **Privacy** - Data never leaves your machine
- 💰 **Free** - No API costs
- ⚡ **Fast** - No network latency
- 🎛️ **Flexible** - Use any open-source model

---

## 🤝 Connect

Built while learning LangChain for real-world AI applications.

⭐ Star this repo if you find it helpful!

---

## 📄 License

MIT License - Feel free to use and modify!
