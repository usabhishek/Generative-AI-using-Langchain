#This file is for dynamic message prompting on list of messages
#Just like in single messgages we have prompt template for dynamic messages but for now we have chatprompt template

from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful, {domain} assistant.'),
    ('human', 'Explain in simple terms, what is {topic}?')
])


prompt = chat_template.invoke({'domain': 'cricket expert','topic': 'Duckworth-Lewis method'})

print(prompt)

