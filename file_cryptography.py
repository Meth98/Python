import sys, os, shutil
from cryptography.fernet import Fernet

# to generate a key and save it in a file
def generate_key():
        key = Fernet.generate_key()

        with open("key.key", "wb") as key_file:         # file opened also in binary mode
                key_file.write(key)

        return key


# to encrypt the specified file
def encrypt_file(key, file_to_encrypt):
        fernet = Fernet(key)

        with open(file_to_encrypt, "rb") as f:
                file_data = f.read()

        encrypted_data = fernet.encrypt(file_data)      # to encrypt the file data

        with open(file_to_encrypt, "wb") as f:
                f.write(encrypted_data)                 # to write the encrypted data back to the file


# to load an existing key from a file
def load_key():
        with open("key.key", "rb") as key_file:
                key = key_file.read()

        return key


# to decrypt the same file (using the same key)
def decrypt_file(key, file_decrypted):
        fernet = Fernet(key)

        with open(file_decrypted, "rb") as f:
                encrypted_data = f.read()

        decrypted_data = fernet.decrypt(encrypted_data)  # to decrypt the data

        with open(file_decrypted, "wb") as f:
                f.write(decrypted_data)                 # to write the decrypted data back to the file


# ------------------
# ------ MAIN ------
# ------------------

if __name__ == "__main__":
        file_name = "original_file.txt"
        file_to_encrypt = "encrypted_file.txt"
        file_decrypted = "decrypted_file.txt"

        if len(sys.argv) == 2:
                if os.path.isfile(file_name):
                        if sys.argv[1] == "encrypt":
                                key = generate_key()                      # to generate a new key for encryption
                                shutil.copy2(file_name, file_to_encrypt)  # to copy original to encrypted file
                                encrypt_file(key, file_to_encrypt)
                                print(f"File '{file_to_encrypt}' encrypted successfully!")
                        elif sys.argv[1] == "decrypt":
                                if not os.path.isfile(file_decrypted):
                                        if os.path.isfile(file_to_encrypt):
                                                key = load_key()                               # to load the existing key for decryption
                                                shutil.copy2(file_to_encrypt, file_decrypted)  # to copy encrypted to decrypted file
                                                decrypt_file(key, file_decrypted)
                                                print(f"File '{file_decrypted}' decrypted successfully!")
                                        else:
                                                print(f"Error!! The encrypted file {file_to_encrypt} doesn't exist!")
                                else:
                                        print(f"Error!! The file {file_name} has already been decrypted!")
                                        print(f"File produced: {file_decrypted}")
                        else:
                                print("Error!! You can only type 'encrypt' or 'decrypt'!")
                else:
                        print(f"Error!! Create a file called {file_name} and populate it!")
        else:
                print(f"Error!! Usage: {sys.argv[0]} encrypt/decrypt")
                print(f"  encrypt = to encrypt the file {file_name}")
                print(f"  decrypt = to decrypt the file {file_name}")