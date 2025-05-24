from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        return None

def encrypt_note(note, key):
    f = Fernet(key)
    return f.encrypt(note.encode()).decode()

def decrypt_note(encrypted_note, key):
    f = Fernet(key)
    return f.decrypt(encrypted_note.encode()).decode()
