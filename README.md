# 🤖 Llama 3 Business Intelligence Agent 
**A Privacy-First, Local AI Proof-of-Concept for Management Insights.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Llama 3](https://img.shields.io/badge/LLM-Llama%203-red.svg)](https://ollama.com/library/llama3)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)

This project demonstrates a local "Business Analyst" agent that allows users to query structured sales data using natural language. By combining **Llama 3** (via Ollama), **LangChain**, and **Streamlit**, it translates human questions from non-data analyst management into executable SQL without sending any data to the cloud.

---

## 🚀 Key Features
* **Management-Ready:** Designed for non-technical users to get instant insights without needing to know SQL or Python.
* **Natural Language to SQL:** Bridge the gap between management questions and database records.
* **100% Private:** Entirely local execution ensures business-sensitive data stays on the local network.
* **Dynamic Visuals:** Integrated sidebar charts showing real-time revenue performance.

## 🛠️ Tech Stack
* **LLM Engine:** Llama 3 (Ollama)
* **Framework:** LangChain (SQLDatabaseChain)
* **Frontend:** Streamlit
* **Database:** SQLite
* **Data Science:** Pandas & Plotly

Recommended Hardware for Management-Speed Responses:
GPU: NVIDIA RTX 30 series or higher with 12GB+ VRAM.
RAM: 32GB (DDR5 preferred).
Storage: NVMe SSD for fast model loading.
Apple Silicon: M-series chip with 16GB+ Unified Memory.

This Hardware Guide for Llama 3 is relevant because it breaks down exactly how much Video RAM you need for different versions of the model, helping you decide if you need to upgrade for larger datasets.

## 📂 Project Structure
```
Llama3_Business_Analyst/
├── app.py              # Streamlit Frontend & UI Logic
├── engine.py           # AI Logic & LangChain Connection
├── data/
│   └── business.db     # SQLite Database (Excluded from Git)
├── requirements.txt    # Python Dependencies
└── .gitignore          # Environment & Data Protection
