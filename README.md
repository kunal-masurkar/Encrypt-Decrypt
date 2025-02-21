# File Encryption and Decryption

A Python-based utility for encrypting and decrypting files using the **Fernet** symmetric encryption method from the `cryptography` library.

## Features
- Generate a secure encryption key
- Encrypt any file with a `.enc` extension
- Decrypt encrypted files back to their original state
- Uses **Fernet** symmetric encryption for security

## Technologies Used
- **Python**
- **Cryptography (Fernet)**

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kunal-masurkar/file-encryption-tool.git
   cd file-encryption-tool
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python encryptor.py
   ```

## Usage

### Generate an Encryption Key
If you don’t have a key, generate one by running the script and selecting `yes` when prompted. The key will be saved as `encryption_key.key`.

### Encrypt a File
1. Run the script.
2. Select `encrypt`.
3. Provide the file path.
4. The encrypted file will be saved with a `.enc` extension.

### Decrypt a File
1. Run the script.
2. Select `decrypt`.
3. Provide the path to the encrypted file (`.enc`).
4. The original file will be restored.

## License
This project is licensed under the MIT License.

## Author
[Kunal Masurkar](https://github.com/kunal-masurkar)
