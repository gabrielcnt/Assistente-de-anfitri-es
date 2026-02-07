from app.core.config import db

from app.models.agente import Agente
from app.models.imoveis import Imovel
from app.models.dicas_lugares import DicaLugar
from app.models.conversas import Conversa
from app.models.mensagens import Mensagem
from app.models.user import User

def init_db():
    db.base.metadata.create_all(bind=db.engine)