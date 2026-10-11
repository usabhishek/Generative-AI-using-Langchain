from dotenv import load_dotenv

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:fastest",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template = 'Give me the name, age and city of the fictional character \n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction': JsonOutputParser().get_format_instructions()}
)

# We can also use the chain to invoke the model and parse the output in one step, but here we are doing it in two steps for clarity.
# chain = template | model | JsonOutputParser()
# result = chain.invoke({}) -- Although we are not taking input variables, we still need to pass an empty dictionary to invoke the chain.
# print(result)

prompt = template.format()
result = model.invoke(prompt)
final_result = JsonOutputParser().parse(result.content)

print(final_result)
print(type(final_result)) #Python treats the json object as a dictionary, so the type will be <class 'dict'>