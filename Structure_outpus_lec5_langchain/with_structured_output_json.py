from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

review_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "description": "Write down all the key themes discussed in the review in a list",
            "items": {
                "type": "string"
            }
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "description": "Return sentiment of the review either positive, negative or neutral",
            "enum": ["positive", "negative", "neutral"]
        },
        "pros": {
            "type": ["array", "null"],
            "description": "Write down all the pros inside a list",
            "items": {
                "type": "string"
            }
        },
        "cons": {
            "type": ["array", "null"],
            "description": "Write down all the cons inside a list",
            "items": {
                "type": "string"
            }
        },
        "name": {
            "type": ["string", "null"],
            "description": "Give me the name of the reviewer, if present. Do not give me the name of the product mentioned in the review",
            "default": None
        }
    },
    "required": [
        "key_themes",
        "summary",
        "sentiment",
        "pros",
        "cons"
    ]
}

structured_model = model.with_structured_output(review_schema)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast.
The 5000mAh battery lasts all day.
The camera is amazing.

Pros:
- Fast processor
- Great camera
- Long battery life

Review by Abhishek Kashyap
"""

result = structured_model.invoke(review)

print(type(result)) #By default, json schema return dictionary
print(result)

print(result["name"])
print(result["summary"])