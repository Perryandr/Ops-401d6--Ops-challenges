#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/24/2023
# Purpose: Encrypting and decrypting a file with python.

# Import
pip3 install cryptography

from cryptography.Fernet import Fernet



# Define key
def write_key():

    key = Fernet.generate.key()
    with open("key.key", "wb") as key_file
    key.file.write(key)



# Function to Load Key
def load_key():
    
    return open("key.key", "rb")


# Main Part

write_key()

load_key

# Encrypt
message = "The princess is in another castle."


print("Plain text is " + str(message))

print()

