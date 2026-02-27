def test_hashing():
    from app.security import hash_password, verify_password
    password = "test123"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
