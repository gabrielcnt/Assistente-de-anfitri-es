import pytest
from sqlalchemy.exc import IntegrityError
from app.models.imoveis import Imovel

def test_criar_imovel_sucesso(db, agente, user):
    imovel = Imovel(
        nome="casa do morro",
        endereco="Rua 1",
        agente_id=agente.id,
        user_id=user.id
    )

    db.add(imovel)
    db.commit()
    db.refresh(imovel)

    assert imovel.id is not None
    assert imovel.agente_id == agente.id
    assert imovel.user_id == user.id



def test_criar_imovel_sem_agente_deve_falhar(db, user):
    imovel = Imovel(
        nome="casa do morro",
        endereco="rua 1",
        agente_id=999,
        user_id=user.id
    )

    db.add(imovel)
    
    with pytest.raises(IntegrityError):
        db.commit()
