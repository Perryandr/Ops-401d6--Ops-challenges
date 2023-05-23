#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/26/2023
# Purpose: Encrypting and decrypting a file with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.



# Import
from cryptography.fernet import Fernet
import os


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


# Encrypt the message
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

if __name__ == "__main__":
    main()