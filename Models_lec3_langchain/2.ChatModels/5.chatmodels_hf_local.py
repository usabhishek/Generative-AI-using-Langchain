from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

pipe = pipeline(
    task="text-generation",
    model="Qwen/Qwen3-0.6B",
    max_new_tokens=50,
    temperature=0.4,
)

llm = HuggingFacePipeline(pipeline=pipe)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of Switzerland?")

print(response.content)