from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Accenture_2026_DSA_100_Questions_Java_Annotated.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

print(len(texts))  # Number of chunks
print(texts[0].page_content)  # Content of the first chunk
print(texts[0].metadata)  # Metadata of the first chunk