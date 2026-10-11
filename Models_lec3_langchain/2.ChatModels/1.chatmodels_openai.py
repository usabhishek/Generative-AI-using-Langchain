from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")
result = model.invoke("What is the capital of France?")

print(result) # It will show the content and the keyword arguments used in the model invocation.
print(result.content) # It will show the content of the model invocation only.


#This are the chatmodels that are available in the langchain library. You can use any of these models to build your own chat applications.
# they all are closed source models and you need to have an API key to use them. You can get the API key from the respective model providers.

#An LLM accepts a plain text prompt and generates plain text, whereas a Chat Model accepts structured chat messages (such as System, Human, and AI messages) and generates an AI message, making it suitable for conversational AI applications.