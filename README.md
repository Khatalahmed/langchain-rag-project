# 🦜🔗 LangChain RAG Project

> Build powerful AI applications locally with LangChain + Ollama — No cloud, no API costs, complete privacy.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.4-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-7C3AED?style=for-the-badge&logo=llama&logoColor=white)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🌟 Highlights

🔒 **100% Local** — Your data never leaves your machine  
💰 **Zero Cost** — No API keys or cloud subscriptions needed  
⚡ **Fast** — No network latency, instant responses  
📚 **Educational** — Learn RAG, memory, routing & more  

---

## 📂 Project Overview

| Category | Files | Description |
|----------|-------|-------------|
| **🚀 Getting Started** | [main.py](cci:7://file:///d:/langchain-lab/main.py:0:0-0:0) | Basic Ollama LLM test |
| **🔗 Chains** | [chain.py](cci:7://file:///d:/langchain-lab/chain.py:0:0-0:0), [cook_pipeline.py](cci:7://file:///d:/langchain-lab/cook_pipeline.py:0:0-0:0) | Prompt chaining & LCEL pipelines |
| **📄 Document Loaders** | [load_pdf.py](cci:7://file:///d:/langchain-lab/load_pdf.py:0:0-0:0), [load_pdf_ocr.py](cci:7://file:///d:/langchain-lab/load_pdf_ocr.py:0:0-0:0), [load_story.py](cci:7://file:///d:/langchain-lab/load_story.py:0:0-0:0), [load_web.py](cci:7://file:///d:/langchain-lab/load_web.py:0:0-0:0) | Load PDFs, text files & web pages |
| **🧠 RAG Pipeline** | [pdf_ai.py](cci:7://file:///d:/langchain-lab/pdf_ai.py:0:0-0:0) | Complete Retrieval-Augmented Generation |
| **💬 Memory** | [memory_chat.py](cci:7://file:///d:/langchain-lab/memory_chat.py:0:0-0:0) | Chatbot with conversation history |
| **🎯 Routing** | [prompt_router.py](cci:7://file:///d:/langchain-lab/prompt_router.py:0:0-0:0), [router_with_memory.py](cci:7://file:///d:/langchain-lab/router_with_memory.py:0:0-0:0), [router_memory_confidence.py](cci:7://file:///d:/langchain-lab/router_memory_confidence.py:0:0-0:0) | Intent-based routing with confidence scoring |
| **📊 Structured Output** | [structured_output.py](cci:7://file:///d:/langchain-lab/structured_output.py:0:0-0:0) | JSON output with self-repair mechanism |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Installation |
|-------------|---------|--------------|
| Python | 3.10+ | [python.org](https://python.org) |
| Ollama | Latest | [ollama.ai](https://ollama.ai) |

### Step 1: Clone Repository

git clone https://github.com/Khatalahmed/langchain-rag-project.git
cd langchain-rag-project

### Step 2: Setup Environment

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

### Step 3: Setup Ollama

ollama pull llama3.2

### Step 4: Run Examples

# Test basic LLM connection
python main.py

# Run full RAG pipeline
python pdf_ai.py

---

## 🏗️ Architecture

langchain-rag-project/
│
├── 📁 data/                      # Sample input documents
│   ├── large_text.pdf
│   └── story.txt
│
├── 📁 docs/                      # Additional documents for RAG
│
├── 📁 outputs/                   # Generated outputs
│
├── 🐍 Core Scripts
│   ├── main.py                   # LLM connection test
│   ├── chain.py                  # Prompt chaining
│   ├── cook_pipeline.py          # LCEL pipeline demo
│   └── pdf_ai.py                 # 🔥 Complete RAG pipeline
│
├── 📄 Document Loaders
│   ├── load_pdf.py               # PDF loader
│   ├── load_pdf_ocr.py           # OCR-based PDF
│   ├── load_story.py             # Text file loader
│   └── load_web.py               # Web scraper
│
├── 🧠 Advanced Features
│   ├── memory_chat.py            # Conversation memory
│   ├── prompt_router.py          # Intent routing
│   ├── router_with_memory.py     # Router + memory
│   ├── router_memory_confidence.py # Confidence scoring
│   └── structured_output.py      # JSON output
│
├── requirements.txt              # Dependencies
└── README.md                     # You are here!

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangChain** | LLM application framework |
| **LangGraph** | Stateful agent workflows |
| **Ollama** | Local LLM runtime |
| **FAISS** | Vector similarity search |
| **Sentence Transformers** | Local text embeddings |
| **PyPDF / Tesseract** | Document processing |

---

## 📚 Concepts Covered

### Core LangChain
- ✅ LLM Integration with Ollama
- ✅ Prompt Templates
- ✅ LCEL (LangChain Expression Language)
- ✅ Chain composition

### RAG Pipeline
- ✅ Document Loading (PDF, Text, Web)
- ✅ Text Splitting & Chunking
- ✅ Embeddings (Sentence Transformers)
- ✅ Vector Stores (FAISS)
- ✅ Retrieval & Generation

### Advanced Patterns
- ✅ Conversation Memory
- ✅ Intent-based Routing
- ✅ Confidence Scoring
- ✅ Structured Output Parsing
- ✅ Self-repair Mechanisms

---

## 💡 Why This Stack?

| Feature | Benefit |
|---------|---------|
| 🏠 **Ollama** | Run LLMs locally — Llama 3.2, Mistral, Phi & more |
| 🔐 **Privacy First** | Sensitive data stays on your machine |
| 💸 **Cost Effective** | No per-token charges or rate limits |
| 🎓 **Learning Friendly** | Experiment freely without API costs |
| ⚡ **Low Latency** | No network round-trips |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔀 Submit pull requests

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## ⭐ Support

If you found this helpful, please give it a ⭐ star!

---

Built with ❤️ while learning LangChain for real-world AI applications.
