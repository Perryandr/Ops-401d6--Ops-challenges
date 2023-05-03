#!/usr/bin/env python3


# Script: Ops 401 Class 11 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/01/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.









import logging
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






