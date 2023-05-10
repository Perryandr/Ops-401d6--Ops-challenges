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
    









