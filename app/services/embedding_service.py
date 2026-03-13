from app.core.openai_client import client

class EmbeddingService:

    def gerar_embedding(texto: str):
        
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=texto
        )

        vetor = response.data[0].embedding
        
        return vetor
    
    