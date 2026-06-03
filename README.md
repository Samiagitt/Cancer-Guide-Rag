# 🩺 CancerGuide RAG

A source-grounded **Cancer Education Assistant** built with **LangChain, OpenAI Embeddings, ChromaDB, and MMR Retrieval**.

This project answers general cancer education questions using stored cancer documents instead of relying only on the LLM’s memory.

> ⚠️ **Disclaimer:** This project is for educational purposes only. It does not diagnose cancer, prescribe treatment, or replace a healthcare professional.

---

## ✨ What It Does

CancerGuide RAG can answer questions like:

* 🧬 What is cancer in simple words?
* 🚬 What are common cancer risk factors?
* 🧪 What is chemotherapy?
* 🔬 What is cancer screening?
* ⚕️ What are common side effects of cancer treatment?
* 🏥 What should someone do first after a cancer diagnosis?

The assistant retrieves relevant information from stored documents and then generates an answer using only that retrieved context.

---

## 🚀 Key Features

* 📄 Loads local cancer education documents
* ✂️ Splits documents into smaller chunks
* 🧠 Creates embeddings using OpenAI Embeddings
* 🗂️ Stores vectors in ChromaDB
* 🔎 Retrieves relevant chunks using **MMR Retrieval**
* 🧾 Shows retrieved source metadata
* 🛡️ Uses safety-aware prompting for medical education
* ❌ Refuses to answer when information is not found in the stored context

---

## 🧠 How It Works

```text
Cancer Documents
      ↓
Text Splitting
      ↓
OpenAI Embeddings
      ↓
ChromaDB Vector Store
      ↓
MMR Retriever
      ↓
Prompt + Retrieved Context
      ↓
LLM Answer
```

---

## 🔎 Why MMR Retrieval?

I tested different retrieval approaches while building this project.

Basic similarity search worked, but sometimes it returned chunks that were too similar to each other. For cancer education questions, the answer often needs information from different parts of the documents, such as risk factors, screening, treatment, and safety notes.

That is why I used **MMR Retrieval**.

MMR helps balance:

* 🎯 relevance to the question
* 🌐 diversity among retrieved chunks

This made the retrieved context more useful and less repetitive.

```python
retriever = vs.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)
```

---

## 🛡️ Safety-Aware Design

Because this project uses cancer-related information, the assistant is designed to be careful.

It does **not**:

* ❌ diagnose cancer
* ❌ prescribe medicine
* ❌ recommend treatment decisions
* ❌ replace a doctor

It does:

* ✅ answer from stored documents
* ✅ use simple educational language
* ✅ encourage users to talk to a healthcare professional
* ✅ say when the answer is not found in the stored context

---

## 🧪 Example Question

```text
What guidelines to follow to prevent cancer?
```

## ✅ Example Answer

```text
Important cancer prevention steps include avoiding tobacco, limiting alcohol, protecting skin from ultraviolet radiation, staying physically active, maintaining a healthy weight, eating a nutritious diet, getting recommended vaccines, and completing recommended screening tests.
```

---

## 🛠️ Tech Stack

* 🐍 Python
* 🔗 LangChain
* 🧠 OpenAI Embeddings
* 💬 OpenAI Chat Model
* 🗂️ ChromaDB
* ✂️ RecursiveCharacterTextSplitter
* 🔎 MMR Retriever
* 🔐 python-dotenv

---

## 📌 What I Learned

Through this project, I practiced:

* building a complete RAG pipeline
* loading and chunking documents
* creating embeddings
* storing vectors in ChromaDB
* using retrievers
* comparing similarity search and MMR retrieval
* grounding LLM answers with retrieved context
* adding source metadata
* designing safer prompts for medical education

---

## 🔮 Future Improvements

* 🧾 Better source citation formatting
* 🧪 RAG evaluation with RAGAS
* 🔍 Query rewriting for better retrieval
* 🧠 CRAG for retrieved document grading
* 🔁 Self-RAG for answer self-checking
* 🤖 Agentic RAG with LangGraph
* 🌐 Optional Streamlit UI later

---


