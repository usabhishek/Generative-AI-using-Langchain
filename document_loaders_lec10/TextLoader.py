from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("document_loaders_lec10/cricket.txt", encoding="utf-8")
documents = loader.load()


# print(type(documents))  # List[Document]
print(documents[0].page_content)  # Actual text
print(documents[0].metadata)     # Source information

chain = RunnableSequence(prompt, model, parser)
print(chain.invoke({'poem':documents[0].page_content}))