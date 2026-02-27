from sqlalchemy.orm import Session
from app.models.user import User

def seed_user(db: Session):
    usuario_existente = db.query(User).first()

    if usuario_existente:
        return usuario_existente
    
    user = User(
        username="Admin",
        email="admin@email.com",
        senha_hash="12r56v8y7u"
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user