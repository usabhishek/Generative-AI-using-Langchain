from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader # PDF Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter # Text Splitter
from langchain_huggingface import HuggingFaceEmbeddings # Embeddings
from langchain_community.vectorstores import FAISS # Vector Database

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# PDF LOADER
loader = PyPDFLoader("Resume.pdf")
documents = loader.load()


print("Number of pages:", len(documents))


# TEXT SPLITTER
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)


print("Number of chunks:", len(chunks))

# EMBEDDINGS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# FAISS VECTOR DATABASE

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("FAISS vector database created.")

# RETRIEVER

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the question using ONLY the context provided below.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}
"""
)


# OUTPUT PARSER
parser = StrOutputParser()

question = "Give me the email and phone number of the person in the resume."


retrieved_docs = retriever.invoke(question)


context = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)

# RAG CHAIN
chain = prompt | llm | parser


# GENERATE ANSWER

answer = chain.invoke({
    "context": context,
    "question": question
})


print("\n Answer:")
print(answer)

# This is a demo project that shows how to use LangChain with Google Gemini 2.5 and FAISS vector database to build a simple RAG (Retrieval-Augmented Generation) application. The application loads a PDF resume, splits it into chunks, creates embeddings, stores them in a FAISS vector database, and then retrieves relevant information based on a user query.

#We will cover each topic in seperate lectures. In this lecture, we will see the cover Runnables part: 1