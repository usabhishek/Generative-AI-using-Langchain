from langchain_text_splitters import TokenTextSplitter

text = "LangChain helps developers build applications using LLMs."

splitter = TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2
)

chunks = splitter.split_text(text)

print(chunks)