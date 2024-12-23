# HarshCrypto

HarshCrypto is a Python library that provides simple and secure file encryption and decryption using the Fernet symmetric encryption scheme from the `cryptography` library. It supports individual files and directory

## Features

- Encrypt individual files securely.
- Decrypt encrypted files.
- Process entire directories recursively.
- Ensures files are only encrypted or decrypted once.
- Lightweight and easy to integrate.
---

## Installation

Install the package via pip:

```bash
pip install harshCrypto
```

---
# Quick Start
## Generating a Key
Before encrypting or decrypting files, generate an encryption key:
```python
Copy code
from harshcrypto import generate_key
```
## Generate a key and save it as key.key
```python
generate_key()
```
This creates a key.key file in the current directory.

## Loading the Key
Load the key when needed for encryption or decryption:

```python
from harshcrypto import load_key

key = load_key("key.key")
```

## Encrypting a File
Encrypt a single file using the loaded key:

```python
from harshcrypto import encrypt_file, load_key

key = load_key("key.key")
encrypt_file("example.txt", key)
```

## Decrypting a File
Decrypt a previously encrypted file:

```python
from harshCrypto import decrypt_file, load_key

key = load_key("key.key")
decrypt_file("example.txt", key)
```

## Encrypting or Decrypting an Entire Directory
Encrypt or decrypt all files in a directory recursively:

```python
from harshCrypto import process_directory, load_key

key = load_key("key.key")

# Encrypt all files in the directory
process_directory("path/to/directory", key, operation="encrypt")

# Decrypt all files in the directory
process_directory("path/to/directory", key, operation="decrypt")
```

# Requirements
- Python 3.6 or higher
- Dependencies : `cryptography` 

*__Install the required dependencies using pip:__*

```bash
pip install cryptography
```

# Security Considerations
- **Key Storage:** Ensure the key.key file is stored securely. If lost, the encrypted files cannot be decrypted.
- **Backup Files:** Always backup your files before encryption in case of unforeseen issues.
- **Encryption Scheme:** Uses Fernet, which provides authenticated encryption (AES in CBC mode with PKCS7 padding and HMAC for authentication).

# Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


# License
This project is licensed under the MIT License. See the [LICENSE]() file for details.

# Support
If you encounter any issues or have questions, feel free to open an issue in the [GitHub](https://github.com/Geeta-Tech/windows-files-locker) repository.