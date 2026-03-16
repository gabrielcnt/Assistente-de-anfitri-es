from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: int):
        return self.db.get(User, user_id)

    def update_password(self, user: User, new_password_hash: str):
        user.password_hash = new_password_hash
        user.is_first_login = False
        return user

    def created_user(self, email: str, password_hash: str, role: str = "user"):
        user = User(email=email, password_hash=password_hash, role=role)

        self.db.add(user)

        return user

    def exists_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first() is not None

    def save(self, user: User):
        self.db.add(user)
        return user
