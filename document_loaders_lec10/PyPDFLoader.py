from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document_loaders_lec10/Accenture_2026_DSA_100_Questions_Java_Annotated.pdf")
document = loader.load()

print(type(document))  # List[Document]
print(len(document))  # Number of pages
print(document[0].page_content)  # Actual text