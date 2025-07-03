# 🧠 Math Routing Agent

A smart math question-answering agent designed for JEE-level problem solving using an **Agentic-RAG (Retrieval-Augmented Generation)** architecture. The agent integrates knowledge base retrieval, web search fallback, LLM reasoning, and human-in-the-loop feedback with guardrails to ensure safe, accurate responses.

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![LLM](https://img.shields.io/badge/LLM-LLaMA--3-yellow)
![Search](https://img.shields.io/badge/Fallback-WebSearch-critical)
![Benchmark](https://img.shields.io/badge/Benchmarked-JEEBench-blue)

---

## 🔍 Features

- 📚 **Vector Search**: Retrieves from a curated math QA knowledge base using vector similarity.
- 🌐 **Web Search Fallback**: Scrapes Cymath or uses LLM if no close KB match is found.
- 🧠 **LLM Reasoning**: Uses LLaMA-3 (via Hugging Face Novita router) for fallback solutions.
- 🔁 **Human-in-the-loop Feedback**: Supports DSPy-based feedback learning.
- 🛡️ **Guardrails AI**: Validates both question and answer formats.
- 📈 **Benchmarking**: Measures performance using the JEE Bench dataset (via Hugging Face).

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
