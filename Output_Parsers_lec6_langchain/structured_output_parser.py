from dotenv import load_dotenv

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)

from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:fastest",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me 3 facts about {topic}. {format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

prompt = template.invoke({'topic' : "Back hole"})
result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

#With the help of structured output parser we can get our data in a structured format. But the most important disadvantage of structured output is we cannot able to have data validation.