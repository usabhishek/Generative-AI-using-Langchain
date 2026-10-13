
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnablePassthrough,
    RunnableBranch
)

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, RunnableSequence(summary_prompt, model, parser)),  # If the report is longer than 300 words, summarize it
    RunnablePassthrough() 

    #Syntax: if condition is in () and default is in RunnablePassthrough
)

final_chain = report_gen_chain | branch_chain

print(final_chain.invoke({"topic": "Russia vs Ukraine"}))
