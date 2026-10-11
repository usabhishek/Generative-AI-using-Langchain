from dotenv import load_dotenv

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:fastest",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on the following topic:\n{topic}",
    input_variables=["topic"]
)

# Summary
template2 = PromptTemplate(
    template="""
Summarize the following report in exactly 5 lines.

Report:
{topic}
""",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "Black Holes"})

print(result)