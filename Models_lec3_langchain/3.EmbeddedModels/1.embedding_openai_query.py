# We use embedding models to convert text into numerical vectors that can be used for various machine learning tasks, such as semantic search, clustering, and classification. In this example, we will demonstrate how to use OpenAI's embedding model to generate embeddings for a given query. We use embeddig models so that that vector have contextual understanding of the text, which allows for better performance in downstream tasks.


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

openai_embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 32
)

result = openai_embeddings.embed_query("Hello, how are you doing today?")

print(str(result))
print("Length of the embedding vector:", len(result))
print("Dimension of the embedding vector:", openai_embeddings.dimensions)
