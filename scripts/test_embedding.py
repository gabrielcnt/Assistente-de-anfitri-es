from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

vector = service.generate_embedding(
    "apartamento com wifi e varanda com vista para o mar"
)

print(type(vector))

print(len(vector))
