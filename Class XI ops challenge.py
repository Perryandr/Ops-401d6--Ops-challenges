#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/26/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.










import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # to suppress warning messages from scapy

from scapy.all import *

# Define the host IP and port range to scan
host = "192.168.1.1"
ports = range(1, 1000) # replace with specific ports if desired

# Define function to test each port in the range
def scan_port(port):
    src_port = RandShort() # generate a random source port
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"), timeout=1, verbose=0) # send SYN packet and wait for response

    if response is not None:
        if response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12: # SYN-ACK flag
                send(IP(dst=host)/TCP(sport=src_port,dport=port,flags="AR"), verbose=0) # send RST packet to gracefully close the connection
                print(f"Port {port} is open")
            elif response.getlayer(TCP).flags == 0x14: # RST flag
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered (silently dropped)")
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]: # ICMP unreachable types
                print(f"Port {port} is filtered (ICMP unreachable)")
        else:
            print(f"Port {port} is filtered (no response)")
    else:
        print(f"Port {port} is filtered (no response)")

# Loop through each port in the range and call scan_port function
for port in ports:
    scan_port(port)






