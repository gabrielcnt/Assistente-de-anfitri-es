from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, hash_password
from app.core.jwt_token import create_access_token
from app.models.user import User

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session



class CredencialInvalida(Exception):
    pass

class SenhaAtualIncorreta(Exception):
    pass

class SenhasDiferentesError(Exception):
    pass


class AuthService:

    def __init__(self, user_repository: UserRepository, db: Session):
        self.user_repository = user_repository
        self.db = db



    def login(self, email: str, password: str):
        
        user = self.user_repository.get_by_email(email)

        if not user:
            raise CredencialInvalida("Credencial inválida")
        
        if not verify_password(password, user.senha_hash):
            raise CredencialInvalida("Credencial inválida")
        
        role = "password_change_required" if user.is_first_login else "user"
        

        token = create_access_token(
            data={
                "sub": str(user.id),
                "role": role
                }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "first_login": user.is_first_login
        }
    


    def change_password(self, user: User, current_password: str, new_password: str, confirm_password: str):

        try:
            if not verify_password(current_password, user.senha_hash):
                raise SenhaAtualIncorreta("Senha atual incorreta")
            
            if confirm_password != new_password:
                raise SenhasDiferentesError("Confirme a senha corretamente")

            hashed = hash_password(new_password)
            
            
            user.senha_hash = hashed
            user.is_first_login = False

            self.user_repository.save(user)
            self.db.commit()
            self.db.refresh(user)

            token = create_access_token(
                data={
                    "sub": str(user.id),
                    "role": "user"
                }
            )

            return token
        
        except SQLAlchemyError:
            self.db.rollback()
            raise

    
