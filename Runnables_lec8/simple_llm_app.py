from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short poem about {topic}."
)

topic = "Sunrise and exile of the soul"

formatted_prompt = prompt.format(topic=topic)

poem = llm.invoke(formatted_prompt)

print(poem)