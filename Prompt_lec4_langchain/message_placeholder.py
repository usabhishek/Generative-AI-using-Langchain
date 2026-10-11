# A message placeholder is a special placeholder used inside a Chat Prompt Template to dynamically insert chat history or a list of messgaes at runtime

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat Template
chat_template = ChatPromptTemplate.from_messages([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt) 