#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/26/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.


# Import
import os
import shutil
from cryptography.fernet import Fernet


# Create a Fernet with key
fernet = Fernet(key)

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







