from cryptography.fernet import Fernet
from datetime import datetime

# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

# Load existing key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt text
def encrypt_text(text, key):
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    log_action("Encrypted")
    return encrypted.decode()

# Decrypt text
def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_text.encode())
    log_action("Decrypted")
    return decrypted.decode()

# Log activity
def log_action(action):
    with open("log.txt", "a") as log:
        log.write(f"{datetime.now()} - {action}\n")

