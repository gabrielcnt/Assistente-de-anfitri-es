import pytest
from app.core.security import hash_password, verify_password


def test_hash_password():
    senha = "12345"
    hash_da_senha = hash_password(senha)

    assert hash_da_senha != senha
    assert len(hash_da_senha) > 0

def test_verify_password():
    senha = "12345"
    hash_da_senha = hash_password(senha)

    assert verify_password(senha, hash_da_senha) == True
    assert verify_password("senha incorreta", hash_da_senha) == False