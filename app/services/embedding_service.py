from app.core.openai_client import client


class EmbeddingService:
    def generate_embedding(self, text: str):

        response = client.embeddings.create(model="text-embedding-3-small", input=text)

        vector = response.data[0].embedding

        return vector
