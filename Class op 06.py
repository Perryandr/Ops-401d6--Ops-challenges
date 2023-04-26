#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/24/2023
# Purpose: Encrypting and decrypting a file with python.

# Import
pip3 install cryptography

from cryptography.Fernet import Fernet
Import os


# Define key
def write_key():

    key = Fernet.generate.key()
    with open("key.key", "wb") as key_file
    key.file.write(key)



# Function to Load Key
def load_key():
    
    return open("key.key", "rb")


# Encrypt
f = Fernet(key)
with open(filename, "rb") as file:
    file_data = file.read()
    # encrypts file
    encrypted_data = f.encrypt(file_data)
    

with open(filename, "wb") as file:
    file.write(encrypted_data)
    
    
    
# Encrypt a message    
def encrypt_message(message, key):    
    Encrypts a message
    
    f = Fernet(key)
    
    
# prints the encrypted message
print(f"Encrypted message(message, key)"):    
    









# Main Part

write_key()

load_key









# Encrypt
message = "The princess is in another castle."


print("Plain text is " + str(message))

print()

