from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserSchemaResponse

import secrets


def seed_user(db: Session):

    usuarios = [
        {"username": "devadmin", "email": "gabrieladmin@email.com", "role": "admin"},
        {"username": "user1", "email": "user1@email.com", "role": "user"},
    ]

    for dados in usuarios:
        usuario_existente = db.query(User).filter(User.email == dados["email"]).first()

        if not usuario_existente:
            
            user = User(
                username=dados["username"],
                email=dados["email"],
                role=dados["role"],
                senha_hash=secrets.token_urlsafe(8)
            )

            db.add(user)

    db.commit()
    
    return UserSchemaResponse.model_validate(user)

