from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.2)

result = llm.invoke("What is the capital of France?")
print(result)


#An LLM (Large Language Model) is the AI model itself.
# Its only job is:
# Take text as input → Generate text as output.

# That's it.

# It doesn't have:

# ❌ Memory
# ❌ Chat history
# ❌ UI
# ❌ File upload
# ❌ Internet
# ❌ Tools
# ❌ User accounts


# Chat Model

# A Chat Model is designed for conversations. Instead of plain text, it works with messages.

# System Message
# Human Message
# AI Message
# Tool Message
#       |
#       ▼

#    Chat Model

#         │

#         ▼

#    AI Message