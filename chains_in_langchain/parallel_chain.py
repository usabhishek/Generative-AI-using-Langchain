from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# ---------------- Models ----------------

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:fastest",
    task="text-generation"
)

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

model2 = ChatHuggingFace(
    llm=llm
)

# ---------------- Prompts ----------------

notes_prompt = PromptTemplate(
    template="""
Generate concise study notes from the following text.

{text}
""",
    input_variables=["text"]
)

quiz_prompt = PromptTemplate(
    template="""
Generate 5 interview-style quiz questions with answers from the following text.

{text}
""",
    input_variables=["text"]
)

merge_prompt = PromptTemplate(
    template="""
You are an AI study assistant.

Combine the following Notes and Quiz into a well-formatted study guide.

## Notes
{notes}

## Quiz
{quiz}

Format the output using headings and bullet points.
""",
    input_variables=["notes", "quiz"]
)

# ---------------- Parser ----------------

parser = StrOutputParser()

# ---------------- Parallel Chain ----------------

parallel_chain = RunnableParallel(
    notes=notes_prompt | model1 | parser,
    quiz=quiz_prompt | model2 | parser
)

# ---------------- Merge Chain ----------------

merge_chain = merge_prompt | model1 | parser

# ---------------- Complete Chain ----------------

chain = parallel_chain | merge_chain

# ---------------- Input ----------------

text = """
A Support Vector Machine (SVM) is a supervised machine learning algorithm used for
classification and regression.

It works by finding an optimal boundary, called a hyperplane,
that best separates different data classes.

Core Concepts:

Hyperplane:
The decision boundary separating classes.

Support Vectors:
The closest data points to the hyperplane.

Margin:
Distance between the hyperplane and support vectors.

Kernel Trick:
Transforms non-linear data into higher-dimensional space.

Types:

Linear SVM

Non-linear SVM

Implemented in scikit-learn using SVC and LinearSVC.
"""

# ---------------- Run ----------------

result = chain.invoke(
    {
        "text": text
    }
)

print(result)

# ---------------- Graph ----------------

chain.get_graph().print_ascii()