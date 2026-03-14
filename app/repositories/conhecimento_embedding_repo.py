import json
from sqlalchemy.orm import Session
from app.models.conhecimento_embedding import ConhecimentoEmbedding


class ConhecimentoEmbeddingRepository:

    def __init__(self, db: Session):
        self.db = db

    
    def criar(self, entidade, entidade_id, conteudo, vetor):

        embedding_json = json.dumps(vetor)

        registro = ConhecimentoEmbedding(
            entidade=entidade,
            entidade_id=entidade_id,
            conteudo=conteudo,
            embedding=embedding_json
        )

        self.db.add(registro)
        
        return registro
    

    def listar_por_entidade(self, entidade, entidade_id):
        return (
            self.db.query(ConhecimentoEmbedding).filter(
                ConhecimentoEmbedding.entidade == entidade,
                ConhecimentoEmbedding.entidade_id == entidade_id
            )
            .all()
        )