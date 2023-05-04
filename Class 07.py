#!/usr/bin/env python3


# Script: Ops 401 Class 07 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/03/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.


# Import
import os
import shutil
from cryptography.fernet import Fernet



# Define key
def write_key():

    key = Fernet.generate.key()
    with open("key.key", "wb") as key_file:
     key.file.write(key)
     
key = Fernet.generate_key()

# Fernet def
fernet = Fernet(key)

# Encryption
def encrypt_file(key, filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    os.remove(filepath)
    with open(filepath, 'wb') as f:
        f.write(encrypted)

def encrypt_string(key, plaintext):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext.encode())
    print(encrypted.decode())

# Decryption
def decrypt_file(key, filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    os.remove(filepath)
    with open(filepath, 'wb') as f:
        f.write(decrypted)


def decrypt_string(key, ciphertext):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(ciphertext.encode())
    print(decrypted.decode())


# Encrypt the messages.
encrypted_message = fernet.encrypt(message.encode())
message ="The Princess is in another castle."

# Write the encrypted message to a file
with open("encrypted_message.txt", "wb") as f:
    f.write(encrypted_message)

# Read the encrypted message from the file
with open("encrypted_message.txt", "rb") as f:
    encrypted_message = f.read()

# Decrypt the message
decrypted_message = fernet.decrypt(encrypted_message)

## main Part


def main():
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    mode = int(input("Enter mode: "))
    key = Fernet.generate_key()

    if mode == 1:
        filepath = input("Enter filepath: ")
        encrypt_file(key, filepath)
    elif mode == 2:
        filepath = input("Enter filepath: ")
        decrypt_file(key, filepath)
    elif mode == 3:
        plaintext = input("Enter plaintext: ")
        encrypt_string(key, plaintext)
    elif mode == 4:
        ciphertext = input("Enter ciphertext: ")
        decrypt_string(key, ciphertext)
    else:
        print("Invalid mode selected.")


# Folder walkthrough for recursive
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
    

    # Read the file
    with open(file_path, "rb") as f:
        file_contents = f.read()
        
    #encrypt file
    encrypted_contents = fernet.encrypt(file_contents)



# Decrypt folders and files
def decrypt_folder(folder_path, key):
    # Create a Fernet instance with the key
    fernet = Fernet(key)

    # Walk through the folder tree recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Read the contents of the file
            with open(file_path, "rb") as f:
                file_contents = f.read()

            # Decrypt the file contents
            decrypted_contents = fernet.decrypt(file_contents)

            # Write the decrypted contents back to the file
            with open(file_path, "wb") as f:
                f.write(decrypted_contents)



if __name__ == "__main__":
    # Generate a key
    key = Fernet.generate_key()

    # Encrypt a folder and its contents
    encrypt_folder("/path/to/folder", key)

    # Decrypt the encrypted folder and its contents
    decrypt_folder("/path/to/folder", key)







