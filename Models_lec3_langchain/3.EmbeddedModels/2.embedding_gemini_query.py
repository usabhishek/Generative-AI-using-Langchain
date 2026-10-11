from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

vector = embeddings.embed_query("Hello, how are you?")

print("Embedding Dimension:", len(vector))
print(str(vector))


# This is the code for embedding multiple documents using Google Generative AI Embeddings. It is commented out because it is not part of the main example, but it can be used to embed a list of documents and get their embeddings.
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="gemini-embedding-2",
#     dimensions = 256
# )

# documents = [
#     "Artificial Intelligence",
#     "Machine Learning",
#     "Deep Learning"
# ]

# vectors = embeddings.embed_documents(documents)

# print("Number of Documents:", len(vectors))
# print("Embedding Dimension:", len(vectors[0]))