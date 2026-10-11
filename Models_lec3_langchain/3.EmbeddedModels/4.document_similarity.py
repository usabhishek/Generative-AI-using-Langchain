# This is a kinf of document similarity model. It is used to find the most similar documents to a given query. It uses the HuggingFaceEmbeddings model to generate embeddings for the documents and the query, and then uses cosine similarity to find the most similar documents.

# because we have to pay for usage of the OpenAI API, we will use the HuggingFaceEmbeddings model to generate embeddings for the documents and the query, and then use cosine similarity to find the most similar documents.    

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting style and leadership skills. He has been the captain of the Indian national team and has numerous records to his name.",
    "Lionel Messi is an Argentine professional footballer who plays as a forward. He is widely regarded as one of the greatest football players of all time, having won multiple Ballon d'Or awards and numerous titles with FC Barcelona and Paris Saint-Germain.",
    "Serena Williams is an American professional tennis player who has won 23 Grand Slam singles titles, the most by any player in the Open Era. She is known for her powerful serve and athleticism on the court.",
    "Elon Musk is a technology entrepreneur and engineer, known for founding SpaceX and co-founding Tesla, Inc. He has been involved in various innovative projects, including the development of electric vehicles, space exploration, and renewable energy solutions.",
    "Erling Haaland is a Norwegian professional footballer who plays as a striker. He is known for his incredible goal-scoring ability, speed, and physical presence on the field. Haaland has played for clubs like Borussia Dortmund and Manchester City, and he has represented the Norwegian national team in international competitions.",
]

query = "Tell me about Elon"
# User asked about Lionel Messi, so we will find the most similar document to the query.

document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity between the query embedding and each document embedding

similarities = cosine_similarity([query_embedding], document_embeddings)
print(similarities)
# we have to make list of query_embedding because cosine_similarity expects a 2D array as input. The query_embedding is a 1D array, so we wrap it in a list to make it a 2D array and document_embeddings is already a 2D array, so we can pass it directly

best_match = np.argmax(similarities)

#Another way
# index, score = sorted(list(enumerate(similarities)), key=lambda x: x[1], reverse=True)[0]
# print(f"Most similar document index: {index}, score: {score}")


print(best_match) # index of the most similar document

print(query)
print(documents[best_match])
