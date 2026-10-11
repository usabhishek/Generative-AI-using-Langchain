# This will be a simple example of how to use the PromptTemplate class to create a prompt template and fill in the values of the placeholders.
#This is the example of dynamic prompt using PromptTemplate class from langchain_core.prompts module.

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'Abhishek'})

result = model.invoke(prompt)

print(result.content)
