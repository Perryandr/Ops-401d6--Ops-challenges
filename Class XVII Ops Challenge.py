#!/usr/bin/env python3


# Script: Ops 401 Class 17 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/09/2023
# Purpose: Building an automated bruteforce attack.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.


# Add to your Python brute force tool the capability to:
#Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
#   Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.

import paramiko
import sys, os
import socket
import getpass
import time
    
def mode1():
    # Search the word list for the user input string.
    word_list_path = input("Please enter the path to the word list file: ")
    with open(word_list_path) as f:
        for word in f:
            word = word.strip()
            print(word)
            time.sleep(0.2)
            

# Mode 2 :Defensive- Do we recognize the password.           
            
def mode2():
    # Accept a user input string.
     filepath = input("Enter the filepath to desired directory:\n")
    with open(filepath) as file:
      # Requirement: Accepts a user input word list file path
       word_list_path = input("Enter the path to the word list file: ")
        password_list = [line.strip() for line in file]
        
        # Print to the screen whether the string appeared in the word list.
        while True:
            password = input("Create your new password: \n")
            if password in password_list:
                print("Error with password, try again")
            else:
                print("Password is acceptable.")
                break

def mode3():
        # 
        





while True:
    answer = input("Mode 1 or Mode 2: ")
    if answer == "Mode 1":
        mode1()
    if answer == "Mode 2":
        mode2()
    if answer == "Mode 3""
        mode3()
    else:
        break







# Set up SSH client
sshConnection. = paramiko.SSHClient()

# Auto add host-key policy
sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Create SSh connection with info : host, port, username, and password
sshConnection.connect(host, port, username, "password")


# Define variables
host = raw_input(*[*] Enter Target Host Address: *)
username = raw_input(*[*] Enter SSH Username: *)
input_file = raw_input(*[*] Enter SSH password file: *)

    if os.path.exists(input_file) == False
        print "\n[*] File Path Does Not Exist !!!"
        sys.exit(4)
except KeyboardInterrupt:
        print "\n\n[*] User Requested An Interrupt"
        sys.exit(3)
    


# end










