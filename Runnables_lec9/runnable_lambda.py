# Workflow of Application :

# RunnableSequence(prompt -> llm -> output_parser) --RunableParallel(
# {joke: RunnablePassthrough},
# {word count: Runnablelambda},
# {explanation: RunnableSequence(prompt2, llm, output_parser)})

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain me the joke: {joke}',
    input_variables=['joke']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = (
    f"{result['joke']}\n"
    f"Word count: {result['word_count']}\n"
    f"Explanation: {result['explanation']}"
)

print(final_result)
                                                
