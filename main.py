from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
folder_path = Path(r"E:\RAG(_Project 1)\Cancer_docs")

docs = []

for file_path in folder_path.rglob("*.txt"):
    loader = TextLoader(str(file_path), encoding="utf-8")
    loaded_docs = loader.load()

    for doc in loaded_docs:
        doc.metadata["source_file"] = file_path.name
        doc.metadata["folder"] = file_path.parent.name

    docs.extend(loaded_docs)

print("Total documents loaded:", len(docs))
splitter=RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=150
)
chunks=splitter.split_documents(docs)
print("Total chunks:", len(chunks))

embeddings=OpenAIEmbeddings(model="text-embedding-3-small")
vs=Chroma(
    collection_name="Cancer_information",
    embedding_function=embeddings,
    persist_directory="Chroma_cancerDB"
)
import uuid
ids=[]
for i,chunk in enumerate(chunks):
    chunk_id=str(uuid.uuid4())
    chunk.metadata["chunk_id"]=chunk_id
    chunk.metadata["chunk_number"]=i
    ids.append(chunk_id)
vs.add_documents(
    documents=chunks,
    ids=ids
)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

retriever = vs.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

query = "is cancer curable?"

retrieved_docs = retriever.invoke(query)
#print(retrieved_docs)
context = "\n\n".join(
    [doc.page_content for doc in retrieved_docs]
)

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant.

    Answer the question using ONLY the context below.
    If the answer is not in the context, say:
    "I could not find this information in the stored information."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
)

rag_chain = prompt | llm | StrOutputParser()

answer = rag_chain.invoke({
    "context": context,
    "question": query
})

print(answer)