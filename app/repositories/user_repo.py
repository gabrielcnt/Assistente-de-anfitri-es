from app.models.user import User

from sqlalchemy.orm import Session

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_id(self, user_id: int):
        return self.db.get(User, user_id)
    
    def update_password(self, user: User, nova_senha_hash: str):
        user.senha_hash = nova_senha_hash
        user.is_first_login = False
        return user

    def created_user(self, email: int, senha_hash: str, role: str = "user"):
        user = User(
            email=email,
            senha_hash=senha_hash,
            role=role
        )

        self.db.add(user)

        return user
    
    def exstis_by_email(self, email: str):
        return (
            self.db.query(User).filter(User.email == email).first()
            is not None
        )