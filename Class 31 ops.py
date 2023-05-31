#!/usr/bin/env python3


# Script: Ops 401 Class 31 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/30/2023
# Thanks to instructor JB for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.
# Also thank you to Alex and Sierra for helping me with python3.


import os
import platform
# Prompt the user to type in a file name to search for
file = input("Please enter the file name to search for: ")

# Prompt the user for a directory to search in
path = input("Please enter the directory to search in: ")

# Search each file in the directory by name
def find_all(file, path):
    result = []
    for root, dirs, files in os.walk(path):
        if file in files:
            result.append(os.path.join(root, file))
    return result

# Call the function to search for the file
search_result = find_all(file, path)

# Display the search result
if search_result:
    print("This Operating system is: ", platform.system())
    print("Number of files searched:", len(search_result))
    print("Number of hits found:", len(search_result))
    print("File found in the following locations:")
    for file_path in search_result:
        print("Name:", file)
        print("Location:", file_path)
        print("------------------------")
else:
    print("Number of files searched: 0")
    print("Number of hits found: 0")
    print("File not found.")