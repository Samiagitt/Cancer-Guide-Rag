# Cancer-Guide-Rag
CancerGuide RAG: Source-Grounded Cancer Education Assistant

CancerGuide RAG is a Retrieval-Augmented Generation project that answers general cancer education questions using a local knowledge base of cancer-related documents.

This project was built to understand the complete RAG workflow: document loading, chunking, embeddings, vector storage, retrieval, prompt augmentation, and LLM-based answer generation. The assistant retrieves relevant cancer education content from stored documents and uses that context to generate safer, more grounded responses.

Medical Safety Note: This project is for educational purposes only. It does not diagnose cancer, prescribe treatment, recommend medical decisions, or replace a qualified healthcare professional.

Project Motivation

Large language models can answer many health-related questions, but they may hallucinate or provide information without showing where it came from. In health education, this can be risky.

The goal of this project is to make the assistant answer from a specific set of stored cancer education documents instead of relying only on the model’s general knowledge.

This project focuses on:

source-grounded answering
retrieved context usage
safer medical education responses
transparent retrieval results
building a strong foundation for advanced RAG methods such as CRAG, Self-RAG, and Agentic RAG
What This Project Does

The user asks a cancer education question, such as:

What is cancer in simple words?
What are common cancer risk factors?
What is chemotherapy?
What is cancer screening?
What are common side effects of cancer treatment?
What should someone do first after a cancer diagnosis?

The system then:

Loads cancer education documents
Splits them into smaller text chunks
Converts chunks into embeddings
Stores embeddings in ChromaDB
Retrieves the most relevant chunks using MMR retrieval
Sends the retrieved context to the LLM
Generates an answer using only the retrieved information
Displays the retrieved sources/metadata for transparency
Tech Stack
Python
LangChain
OpenAI Embeddings
OpenAI Chat Model
ChromaDB
RecursiveCharacterTextSplitter
MMR Retriever
python-dotenv
RAG Pipeline
Cancer Documents
      ↓
TextLoader
      ↓
RecursiveCharacterTextSplitter
      ↓
OpenAI Embeddings
      ↓
Chroma Vector Database
      ↓
Retriever
      ↓
Prompt Augmentation
      ↓
LLM Answer
Retrieval Strategy

I experimented with different retrieval styles while building this project.

At first, I used basic similarity search. It worked, but sometimes the retrieved chunks were too similar to each other and did not give enough variety in the context.

Then I tested MMR retrieval. MMR stands for Maximal Marginal Relevance. It tries to balance:

relevance to the user question
diversity among retrieved chunks

For this project, MMR worked better because cancer education questions often need information from slightly different parts of the documents. For example, a question about cancer risk may need context about genetics, lifestyle, infections, and screening.

The current retriever uses:

retriever = vs.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

This retrieves 5 final chunks after considering 20 possible candidate chunks.

Prompting Strategy

The prompt is designed to reduce hallucination by forcing the model to answer only from the retrieved context.

The assistant is instructed to:

answer only using the provided context
say when information is not available
avoid diagnosis
avoid treatment prescription
encourage professional medical care for personal questions

Example rule from the prompt:

Answer the question using ONLY the context below.
If the answer is not in the context, say:
"I could not find this information in the stored information."
Medical Safety Guardrails

Because this project uses cancer-related information, safety is important.

The assistant should not:

diagnose cancer
say whether someone has or does not have cancer
prescribe medicine
choose a treatment for a patient
replace a doctor
answer emergency medical situations as if it is a normal chatbot

The assistant should:

give general education only
encourage users to talk to a qualified healthcare professional
admit when the stored context does not contain enough information
use simple and careful language
Dataset / Documents

The project uses local .txt cancer education documents. The documents are organized by topic, such as:

data/
  cancer_docs/
    general_cancer/
    prevention_risk/
    screening/
    breast_cancer/
    cervical_cancer/
    colorectal_cancer/
    lung_cancer/
    treatment/
    side_effects/
    nutrition/
    support/
    survivorship/
    advanced_cancer/

What I Learned

Through this project, I practiced:

building a complete RAG pipeline
loading multiple local documents
adding metadata to documents
splitting text into chunks
generating embeddings
storing vectors in ChromaDB
retrieving relevant context
comparing retrieval strategies
using MMR to improve retrieval diversity
designing safer prompts for medical education
grounding LLM answers in retrieved documents
handling cases where the answer is not found in the context
Current Limitations
The project currently runs in the terminal only.
It does not have a Streamlit or web UI yet.
The vector database may contain duplicate chunks if the same documents are ingested repeatedly.
It does not yet include formal RAG evaluation.
It does not provide real medical diagnosis or treatment advice.
It only answers based on the local documents provided.
Future Improvements

Planned improvements include:

separate ingestion and query files
better source citation formatting
metadata filtering by cancer topic
duplicate document checking before adding to ChromaDB
RAG evaluation using RAGAS
query rewriting for better retrieval
CRAG to grade retrieved documents before answering
Self-RAG to check whether the answer is grounded
Agentic RAG using LangGraph
optional Streamlit UI after improving the core pipeline
Why This Project Matters

This project is a foundation for more advanced RAG systems. A basic chatbot can answer from the model’s memory, but a RAG system can answer from a specific knowledge base.

For health education topics, this is especially important because answers should be grounded, careful, and transparent.

CancerGuide RAG demonstrates how retrieval, embeddings, vector databases, prompt engineering, and safety-aware response generation can work together in a practical AI application.

Disclaimer

This project is for educational and portfolio purposes only.

It is not a medical device, not a diagnosis system, and not a replacement for professional healthcare. Users should always contact a qualified healthcare professional for personal medical advice, diagnosis, or treatment.
