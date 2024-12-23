import os
import sys
import time
import threading
from cryptography.fernet import Fernet, InvalidToken

# Spinner for command-line loading feedback
class Spinner:
    def __init__(self, message="Processing"):
        self.message = message
        self.done = False
        self.spinner = threading.Thread(target=self._spin, daemon=True)

    def _spin(self):
        spinner_chars = "|/-\\"
        idx = 0
        while not self.done:
            sys.stdout.write(f"\r{self.message}... {spinner_chars[idx]}")
            sys.stdout.flush()
            idx = (idx + 1) % len(spinner_chars)
            time.sleep(0.1)
        sys.stdout.write("\r" + " " * (len(self.message) + 15) + "\r")

    def start(self):
        self.spinner.start()

    def stop(self):
        self.done = True
        self.spinner.join()


# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated: key.key")


# Load encryption key
def load_key():
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found! Please generate a key using the 'generate_key' command.")
    with open("key.key", "rb") as key_file:
        return key_file.read()


# Encrypt a file in chunks
def encrypt_file(file_path, fernet, chunk_size=64 * 1024):
    temp_file_path = file_path + ".temp"
    with open(file_path, "rb") as file, open(temp_file_path, "wb") as temp_file:
        while chunk := file.read(chunk_size):
            encrypted_chunk = fernet.encrypt(chunk)
            temp_file.write(encrypted_chunk)
    os.replace(temp_file_path, file_path)  # Replace original file with encrypted file



# Decrypt a file in chunks
def decrypt_file(file_path, fernet, chunk_size=64 * 1024):
    temp_file_path = file_path + ".temp"
    with open(file_path, "rb") as file, open(temp_file_path, "wb") as temp_file:
        while chunk := file.read(chunk_size):
            decrypted_chunk = fernet.decrypt(chunk)
            temp_file.write(decrypted_chunk)
    os.replace(temp_file_path, file_path)  # Replace original file with decrypted file



# Process a directory
def process_directory(directory, fernet, operation, spinner):
    allowed_extensions = {".txt", ".pdf", ".jpg", ".png"}  # Example allowed extensions
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.splitext(file_name)[1].lower() in allowed_extensions:
                try:
                    if operation == "encrypt":
                        encrypt_file(file_path, fernet)
                    elif operation == "decrypt":
                        decrypt_file(file_path, fernet)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    spinner.stop()
    print(f"{operation.capitalize()}ion completed for directory: {directory}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using Fernet encryption.")
    parser.add_argument("command", choices=["generate_key", "encrypt", "decrypt"], help="Command to run.")
    parser.add_argument("path", nargs="?", help="File or directory path.")
    args = parser.parse_args()

    try:
        if args.command == "generate_key":
            generate_key()

        elif args.command in ["encrypt", "decrypt"]:
            if not args.path:
                raise ValueError("You must provide a file or directory path.")

            key = load_key()
            fernet = Fernet(key)
            spinner = Spinner(f"{args.command.capitalize()}ing")

            # Handle KeyboardInterrupt (Ctrl+C) for cancellation
            try:
                spinner.start()
                if os.path.isfile(args.path):
                    if args.command == "encrypt":
                        encrypt_file(args.path, fernet)
                    elif args.command == "decrypt":
                        decrypt_file(args.path, fernet)
                    print(f"\n{args.command.capitalize()}ion completed for file: {args.path}")
                elif os.path.isdir(args.path):
                    process_directory(args.path, fernet, args.command, spinner)
                else:
                    raise FileNotFoundError(f"Path not found: {args.path}")
            except KeyboardInterrupt:
                spinner.stop()
                print("\nOperation canceled by the user.")
            finally:
                spinner.stop()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
