#!/usr/bin/env python3


# Script: Ops 401 Class 16 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/08/2023
# Purpose: Building an automated bruteforce attack.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.

# Import libraries
import getpass
import os
import time

# Define Variables
def iterator(): 

    filepath = input("Enter your dictionary filepath:\n")

    file = open(filepath)
    line = file.readline
    print(line)
    
    
    while line:
        word =line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close
    
    
# Mode 2 :Defensive; Password recognized.
def check_password():


user_password = input()

dictionary_path =input()
# Accept a user input string.




# accepts a user input word list file path.




# Seatch the word list for the user input string.
# Print to the screen whether the string appeared in the word list.


iterator()
