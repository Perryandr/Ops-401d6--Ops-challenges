#!/usr/bin/env python3


# Script: Ops 401 Class 27 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/23/2023
# Purpose: Building an automated bruteforce attack.
# Thanks to classmate Marco, instructor Marco for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.



# Import libraries
import logging
import logging.handlers as handler
import time
 


# Logger basic configuration
logger = logging.handler()


# Create log file handlers
logHandler = handler.RotatingFileHandler('')

# Create



# Join our logger to our loghandler
logger.addHandler(logHandler)


# Configure logging
log_file = "log_file.log"
# Maximum log file size in bytes

log_max_size = 1024  

# Create a rotating file handler
file_handler = logging.handlers.RotatingFileHandler(
    log_file,
    maxBytes=log_max_size,
    backupCount=3  # Number of backup log files to keep
)
file_handler.setLevel(logging.DEBUG)

# Create a log formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Create a logger and add the file handler
logger = logging.getLogger()
logger.addHandler(file_handler)

def divide_numbers(x, y):
    try:
        result = x / y
        logging.info(f"Division successful: {x} / {y} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error occurred.")
        raise e

# Inducing an error
try:
    divide_numbers(10, 0)
except ZeroDivisionError:
    pass

# Confirm logging
with open(log_file, "r") as log_file:
    print(log_file.read())

logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # to suppress warning messages from scapy

from scapy.all import *

# Define the host IP and port range to scan
host = "192.168.1.1"
port_range = [22, 23, 80, 443, 3389] # replace with specific ports if desired

# Define function to test each port in the range
def scan_port(port):
    # generate a random source port
    src_port = RandShort() 
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"), timeout=1, verbose=0) # send SYN packet and wait for response

    if response is not None:
        if response.haslayer(TCP):
            # SYN-ACK flag
            if response.getlayer(TCP).flags == 0x12: 
                send(IP(dst=host)/TCP(sport=src_port,dport=port,flags="AR"), verbose=0) 
                print(f"Port {port} is open")
                # RST flag
            elif response.getlayer(TCP).flags == 0x14: 
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered (silently dropped)")
                # ICMP unreachable types
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]: 
                print(f"Port {port} is filtered (ICMP unreachable)")
        else:
            print(f"Port {port} is filtered (no response)")
    else:
        print(f"Port {port} is filtered (no response)")

# Loop through each port in the range and call scan_port function
for port in ports:
    scan_port(port)

