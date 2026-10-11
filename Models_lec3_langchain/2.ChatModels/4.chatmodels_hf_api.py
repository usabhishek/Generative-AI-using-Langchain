from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen3.6-27B",
    task = "text-generation"

)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of switzerland?")

print(result.content) # It will show the content of the model invocation only.
