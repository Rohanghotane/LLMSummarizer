# LLMSummarizer
Document Summarizer using LLM is an AI-powered tool that automatically generates concise and meaningful summaries from long documents using state-of-the-art Large Language Models (LLMs). It supports various input formats such as plain text and text file, helping users quickly understand the core content without reading the entire file

# 📝 Document Summarizer Using Groq + Streamlit

A lightweight web app built with Streamlit that uses the [Groq API](https://groq.com/) and open-source LLMs to summarize text documents in different styles.

---

## 🔧 Features

- 📄 Summarize text via:
  - Pasted text
  - Uploaded `.txt` files
- 🧠 Summarization styles:
  - Brief
  - Detailed
  - Bullet Points
- ✅ Powered by Groq's high-speed inference

---

## 🚀 Setup & Run Locally

```bash
Pip install -r requirements.txt

streamlit run summarizer_V1.py (Uses openAI API)
streamlit run summarizer_V2.py ((Uses groq API)

Upload .TXT file or write paragraph

Select Summarization Style and hit generate summary button
