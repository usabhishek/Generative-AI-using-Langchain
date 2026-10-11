#This is thr code for string parsing by LLM using LangChain and HuggingFace. Now we move tos tring output parsing
from dotenv import load_dotenv

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)

from langchain_core.prompts import PromptTemplate

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
{text}
""",
    input_variables=["text"]
)

prompt1 = template1.invoke(
    {
        "topic": "Artificial Intelligence"
    }
)

result = model.invoke(prompt1)

prompt2 = template2.invoke(
    {
        "text": result.content
    }
)

result2 = model.invoke(prompt2)

print("Detailed Report:\n")
print(result.content)

print("\nSummary:\n")
print(result2.content)