from passlib.hash import pbkdf2_sha256

# hashing the password
def password_hack(password):
    hash = pbkdf2_sha256.hash(password)
    return hash

# password decrypting
def password_decrypt(password,hashed_password):
    return pbkdf2_sha256.verify(password,hashed_password)
