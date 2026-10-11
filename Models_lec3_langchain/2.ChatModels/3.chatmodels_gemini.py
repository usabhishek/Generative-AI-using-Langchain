from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke("What is the capital of France?")
# print(result) # It will show the content and the keyword arguments used in the model invocation.
print(result.content) # It will show the content of the model invocation only.