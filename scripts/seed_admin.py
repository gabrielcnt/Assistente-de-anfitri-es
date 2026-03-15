from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User


def seed_user(db: Session):

    users = [
        {"username": "admin", "email": "admin@email.com", "role": "admin"},
        {"username": "user1", "email": "user1@email.com", "role": "user"},
    ]

    for dados in users:
        existing_users = db.query(User).filter(User.email == dados["email"]).first()

        if not existing_users:
            user = User(
                username=dados["username"],
                email=dados["email"],
                role=dados["role"],
                password_hash=hash_password("123456789"),
            )

            db.add(user)

    db.commit()
