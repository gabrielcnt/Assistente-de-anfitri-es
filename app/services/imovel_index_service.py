from app.services.embedding_service import EmbeddingService
from app.repositories.conhecimento_embedding_repo import ConhecimentoEmbeddingRepository
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class ImovelIndexService:

    def __init__(
            self,
            embedding_service: EmbeddingService,
            conhecimento_embedding_repo: ConhecimentoEmbeddingRepository,
            db: Session
    ):
        self.embedding_service = embedding_service
        self.repository = conhecimento_embedding_repo
        self.db = db

    
    def indexar_imovel(self, imovel):
        try:
            textos = [
                imovel.regras,
                imovel.checkin_info,
                imovel.checkout_info
            ]

            for texto in textos:
                if not texto:
                    return

                vetor = self.embedding_service.gerar_embedding(texto)

                registro = self.repository.criar(
                    entidade="imovel",
                    entidade_id=imovel.id,
                    conteudo=texto,
                    vetor=vetor
                )

            self.db.commit()
            self.db.refresh(registro)

            return registro
        
        except SQLAlchemyError:
            self.db.rollback()
            raise

    