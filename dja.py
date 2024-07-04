from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# Function to generate a key from a password
def generate_key(password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key, salt

# Function to encrypt an image file
def encrypt_image(filename, password):
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return
    
    # Generate key and salt
    key, salt = generate_key(password)

    # Read image data
    with open(filename, "rb") as file:
        image_data = file.read()

    # Add padding to the data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    # Generate initialization vector
    iv = os.urandom(16)

    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Write encrypted data to file
    encrypted_filename = filename + ".encrypted"
    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(salt)
        encrypted_file.write(iv)
        encrypted_file.write(encrypted_data)

    print(f"Encryption successful. Encrypted file: {encrypted_filename}")

# Example usage
if __name__ == "__main__":
    image_path = input("Enter path of image file to encrypt: ").strip()
    password = input("Enter encryption password: ").strip()

    # Encrypt the image
    encrypt_image(image_path, password)
