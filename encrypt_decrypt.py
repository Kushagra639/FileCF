import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import InvalidToken

def generate_key(password, salt):

    password = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(password)
    )

    return key

def encrypt_file(filename, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)
    
    with open(filename, 'rb') as f:
        original = f.read()
    
    encrypted = fernet.encrypt(original)

    with open(filename+".encrypted", 'wb') as fn:
        fn.write(salt)
        fn.write(encrypted)

    print("Encryption successful.\nEncrypted file saved as: " + filename + ".encrypted")

def decrypt_file(filename, password):
    with open(filename, 'rb') as f:
        salt = f.read(16)
        encrypted = f.read()
    
    key = generate_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted)

        with open(filename.replace(".encrypted", ""), 'wb') as fn:
            fn.write(decrypted)

        print("Decryption successful.\nFile saved as: " + filename.replace(".encrypted", ""))
    except InvalidToken:
        print("Decryption failed. Incorrect password.")
    
    except Exception as e:
        print("Decryption failed. Check your password and try again.")
        print(f"Error: {e}")
