from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

vetor = service.gerar_embedding(
    "apartamento com wifi e varanda com vista para o mar"
)

print(type(vetor))

print(len(vetor))
