#!/usr/bin/env python3


# Script: Ops 401 Class 33 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/30/2023
# Thanks to instructor Marco for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.
# Also thank you to Alex and Sierra for helping me with python3.




# Encode it to bytes using UTF-8 encoding
message = "Some Text to hash.".encode()

# Hash with MD5
print ("MD5:", haslib.md5(message).hexdigest())

# Hash with SHA-2
print("SHA-256",
hashlib.sha256(message).hexdigest())
