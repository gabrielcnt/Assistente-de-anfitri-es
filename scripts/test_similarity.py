from app.services.embedding_service import EmbeddingService
from app.utils.vector_similarity import cosine_similarity

service = EmbeddingService()

v1 = service.generate_embedding("tem restaurante perto?")
v2 = service.generate_embedding("algum restaurante próximo?")
v3 = service.generate_embedding("qual horário do checkout?")

print(cosine_similarity(v1, v2))
print(cosine_similarity(v1, v3))