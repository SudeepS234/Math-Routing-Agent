# 🧠 Math Routing Agent

A smart math question-answering agent designed for step by step math problem solving using an **Agentic-RAG (Retrieval-Augmented Generation)** architecture. The agent integrates knowledge base retrieval, web search fallback, LLM reasoning, and human-in-the-loop feedback with guardrails to ensure safe, accurate responses.

![Frontend](https://img.shields.io/badge/Frontend-Streamlit-orange)
![RAG](https://img.shields.io/badge/Architecture-RAG-brightgreen)
![Fallback](https://img.shields.io/badge/LLM-LLaMA--3-yellow)

---

## 🔍 Features

- 📚 **Vector Search**: Retrieves from a curated math QA knowledge base using vector similarity.
- 🧠 **LLM Reasoning**: Uses LLaMA-3 (via Hugging Face Novita router) for fallback solutions.
- 🔁 **Human-in-the-loop Feedback**: Supports Human-in-the-loop feedback and collects the message.
- 🛡️ **Guardrails AI**: Validates both question and answer formats.
- 📈 **Benchmarking**: Measures performance using the JEE Bench dataset.

---

## 📦 Installation

### Requirements

- Python 3.10+
- Git, pip
- Hugging Face account (for API access)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/SudeepS234/Math-Routing-Agent.git
cd Math-Routing-Agent
```

2. **Install Docker(if not yet installed) and run this in cmd:**
```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

3. **Add these keys(freely available) in a .env file in the root folder:**
```bash
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=math_kb
QDRANT_API_KEY= {Get your key by creating a free cluster}
HF_API_TOKEN= {your huggingface token}
```

4. **Create a virtual environment:**
```bash
python -m venv env
```

5. **In the virtual environment install the requirements:**
```bash
pip install -r requirements.txt
```

6. **Run the app:**
```bash
streamlit run app/main.py
```
