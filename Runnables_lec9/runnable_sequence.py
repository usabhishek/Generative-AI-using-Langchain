from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write me a joke about {topic}.",
    input_variables = ["topic"],
)

model = GoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = "Explain me the joke: {joke}",
    input_variables = ["joke"],
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "chickens"}))
