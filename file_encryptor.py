from cryptography.fernet import Fernet
import os

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as encryption_key.key")

# Function to load the encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_path + ".enc", "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    print(f"File {file_path} encrypted successfully as {file_path}.enc")

# Function to decrypt a file
def decrypt_file(encrypted_file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    original_file_path = encrypted_file_path.replace(".enc", "")
    
    with open(original_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"File {encrypted_file_path} decrypted successfully as {original_file_path}")

# Example usage
if __name__ == "__main__":
    choice = input("Do you want to generate a new key? (yes/no): ").strip().lower()
    if choice == "yes":
        generate_key()
    
    action = input("Do you want to encrypt or decrypt a file? (encrypt/decrypt): ").strip().lower()
    file_path = input("Enter the file path: ").strip()
    
    if action == "encrypt":
        encrypt_file(file_path)
    elif action == "decrypt":
        decrypt_file(file_path)
    else:
        print("Invalid choice! Use 'encrypt' or 'decrypt'.")