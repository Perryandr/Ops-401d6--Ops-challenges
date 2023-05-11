
# This 
# is 
# for 
# Testing
# Parts
# of
# a 
# script.

import paramiko
import sys, os
import socket
import getpass
import time

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
