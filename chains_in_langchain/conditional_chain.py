from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch, RunnableLambda

from typing import Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

# -------------------- Output Schema --------------------

# We want the model to return ONLY positive or negative that's why we are using pydantic output parser.
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")

# Converts model output into Feedback object
feedback_parser = PydanticOutputParser(
    pydantic_object=Feedback
)

# -------------------- Prompt for Classification --------------------

classifier_prompt = PromptTemplate(
    template="""
Classify the following feedback as either positive or negative.

Feedback:
{feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={"format_instructions": feedback_parser.get_format_instructions()}
)

# Prompt -> Gemini -> Feedback Object
classifier_chain = classifier_prompt | model | feedback_parser

# -------------------- Why RunnablePassthrough? --------------------

# classifier_chain returns ONLY Feedback(sentiment="positive"). The original feedback text is LOST.We still need the feedback later to generate the response. RunnablePassthrough keeps the original input and adds one more key called "sentiment".

chain_with_sentiment = RunnablePassthrough.assign(
    sentiment=classifier_chain
)

# Output becomes
# {
#     "feedback": "This is a beautiful phone",
#     "sentiment": Feedback(sentiment="positive")
# }

# -------------------- Response Prompts --------------------

positive_prompt = PromptTemplate.from_template(
    "Write a polite thank-you response.\n\nFeedback:\n{feedback}"
)

negative_prompt = PromptTemplate.from_template(
    "Write a polite apology response.\n\nFeedback:\n{feedback}"
)

# -------------------- RunnableBranch --------------------

# RunnableBranch works exactly like
#
# if sentiment == positive:
#       positive_chain
# else:
#       negative_chain

branch_chain = RunnableBranch(

    # ---------------- Positive ----------------
    (
        lambda x: x["sentiment"].sentiment == "positive",

        # RunnableLambda is simply a Python function converted into a Runnable. It convert lambda into runnable lambda
        
        # Here we only keep the feedback because PromptTemplate needs only {feedback}

        RunnableLambda(
            lambda x: {
                "feedback": x["feedback"]
            }
        )
        | positive_prompt
        | model
        | parser
    ),

    # ---------------- Negative ----------------
    (
        lambda x: x["sentiment"].sentiment == "negative",

        RunnableLambda(
            lambda x: {
                "feedback": x["feedback"]
            }
        )
        | negative_prompt
        | model
        | parser
    ),

    # Default case
    # "_" means "I receive an input but I don't use it."

    RunnableLambda(
        lambda _: "Could not determine sentiment."
    )
)

# -------------------- Complete Chain --------------------

chain = chain_with_sentiment | branch_chain

# -------------------- Run --------------------

result = chain.invoke(
    {
        "feedback": "This is a beautiful phone."
    }
)

print(result)

# Visualize the chain
chain.get_graph().print_ascii()