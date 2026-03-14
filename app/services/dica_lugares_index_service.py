from app.services.embedding_service import EmbeddingService
from app.repositories.conhecimento_embedding_repo import ConhecimentoEmbeddingRepository
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError



class DicasIndexService:
    
    def __init__(
            self,
            embedding_service: EmbeddingService,
            repository: ConhecimentoEmbeddingRepository,
            db: Session
    ):
        self.embedding_service = embedding_service
        self.repository = repository
        self.db = db



    def indexar_dicas(self, dica):
        
        try:
            descricao = dica.descricao or ""

            texto = f"""
            Lugar: {dica.nome}
            Tipo: {dica.tipo}
            Descrição: {descricao}
            """

            vetor = self.embedding_service.gerar_embedding(texto)

            registro = self.repository.criar(
                entidade="dica_lugar",
                entidade_id=dica.id,
                conteudo=texto,
                vetor=vetor
            )

            self.db.commit()
            self.db.refresh(registro)

            return registro
        
        except SQLAlchemyError:
            self.db.rollback()
            raise