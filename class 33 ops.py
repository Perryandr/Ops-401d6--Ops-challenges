#!/usr/bin/env python3


# Script: Ops 401 Class 33 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/30/2023
# Thanks to instructor Marco for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.
# Also thank you to Alex and Sierra for helping me with python3.

# Imports

import os
import platform
import hashlib
from datetime import datetime
import subprocess



# Encode it to bytes using UTF-8 encoding
message = "Some Text to hash.".encode()

# Hash with MD5
print ("MD5:", haslib.md5(message).hexdigest())

# Hash with SHA-2
print("SHA-256",
hashlib.sha256(message).hexdigest())


# Prompt the user for a directory to search in
path = input("Please enter the directory to search in: ")
# Add a time stamp
dt = datetime.now()

# Search each file and folder recursively in the directory
def find_all(path):
    result = []
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            result.append(os.path.join(root, directory))
        for file in files:
            result.append(os.path.join(root, file))
    return result

def hash(file):
    # Hash object
    hasher = hashlib.md5()
    try:
        # Open file
        with open(file, 'rb') as file_obj:
            # Loop through the file content
            chunk = file_obj.read(1024)
            while chunk:
                hasher.update(chunk)
                chunk = file_obj.read(1024)
    # If no
    except FileNotFoundError:
        return None  
    return hasher.hexdigest()

# Recursive function to search for files
def search_files(path):
    search_result = []
    if os.path.isfile(path):
        search_result.append(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                search_result.append(os.path.join(root, file))
    return search_result

# Call the function to search for the files
search_result = search_files(path)

# Display the search result
if search_result:
    file_hash = hash(search_result[0])
    if file_hash is not None:
        print("This Operating system is: ", platform.system())
        print("Number of files searched:", len(search_result))
        print("Number of hits found:", len(search_result))
        print("File found in the following locations:")
        for file_path in search_result:
            print("Location:", file_path)
            print("Hash: ", file_hash)
            print("Timestamp: ", dt)
            print('---------------')
        print("Now passing to Virus-total: ")
    else:
        print("Error in hash for files")
else:
    print("No items found in the specified directory.")


# Pass hashes to Virus-Total
# Set your environment variable before proceeding.
apikey = input("Please put you API Key here: ")
# apikey = os.getenv('API')
path = r'C:\Users\maldo\OneDrive\Documents\Github\Ops-401\Code\virustotal-search.py'
# Construct the command to call the script
command = ['python3', path, '-k', apikey, '-m', file_hash]

# Execute the command
subprocess.call(command)