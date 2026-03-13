from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password


def seed_user(db: Session):

    usuarios = [
        {"username": "admin", "email": "admin@email.com", "role": "admin"},
        {"username": "user1", "email": "user1@email.com", "role": "user"},
    ]

    for dados in usuarios:
        usuario_existente = db.query(User).filter(User.email == dados["email"]).first()

        if not usuario_existente:
            
            user = User(
                username=dados["username"],
                email=dados["email"],
                role=dados["role"],
                senha_hash=hash_password("12345")
            )

            db.add(user)

    db.commit()
    
