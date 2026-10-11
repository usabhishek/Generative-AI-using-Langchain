from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

#Hugging face does not have a dimensions parameter, so we will use the length of the vector to determine the dimensions of the embedding vector.

vector = embeddings.embed_query("Hello, how are you?")

print(len(vector))
print(str(vector))

# It will download the model from Hugging Face and cache it locally. The first time you run this code, it may take some time to download the model. Subsequent runs will be faster as the model will be loaded from the local cache.