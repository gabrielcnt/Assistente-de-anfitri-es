from app.utils.vector_similarity import cosine_similarity
from sqlalchemy.orm import Session


class RetrievalService:
    def __init__(self, embedding_service, repository, db: Session):

        self.embedding_service = embedding_service
        self.repository = repository
        self.db = db

    def search_context(self, question: str, top_k: int = 3):
        question_embedding = self.embedding_service.generate_embedding(question)

        embeddings = self.repository.get_all()

        results = []

        for item in embeddings:
            score = cosine_similarity([question_embedding], [item.vector])[0][0]
            results.append((score, item))

        results.sort(key=lambda x: x[0], reverse=True)

        top_results = results[:top_k]

        return [item for score, item in top_results]
