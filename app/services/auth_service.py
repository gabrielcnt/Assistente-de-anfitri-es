from app.repositories.user_repo import UserRepository
from app.core.security import verify_password
from app.core.jwt_token import create_access_token

class CredencialInvalida(Exception):
    pass


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, email: str, password: str):
        
        user = self.user_repository.get_by_email(email)

        if not user:
            raise CredencialInvalida("Credencial inválida")
        
        if not verify_password(password, user.senha_hash):
            raise CredencialInvalida("Credencial inválida")
        
        token = create_access_token(
            data={
                "sub": str(user.id),
                "role": user.role
                }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "first_login": user.is_first_login
        }