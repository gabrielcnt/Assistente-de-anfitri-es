from app.core.security import hash_password, verify_password


def test_hash_password():
    password = "12345"
    hash = hash_password(password)

    assert hash != password
    assert len(hash) > 0


def test_verify_password():
    password = "12345"
    hash = hash_password(password)

    assert verify_password(password, hash) == True
    assert verify_password("senha incorreta", hash) == False
