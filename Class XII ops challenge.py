#!/usr/bin/env python3


# Script: Ops 401 Class 12 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/02/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.


import sys
from scapy.all import *

def tcp_port_scan(ip, start_port, end_port):
    # TODO: Implement TCP Port Range Scanner
    pass

def icmp_ping_sweep(network):
    # TODO: Implement ICMP Ping Sweep
    pass

if __name__ == '__main__':
    print("Select mode: ")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    mode = int(input("Enter choice: "))

    if mode == 1:
        ip = input("Enter host IP: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        tcp_port_scan(ip, start_port, end_port)

    elif mode == 2:
        network = input("Enter network address (CIDR notation): ")
        icmp_ping_sweep(network)

    else:
        print("Invalid choice.")








import sys
from scapy.all import *

def tcp_port_scan(ip, start_port, end_port):
    open_ports = []
    closed_ports = []
    filtered_ports = []

    for port in range(start_port, end_port+1):
        print("Scanning port {}".format(port))
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
        
        if response is None:
            filtered_ports.append(port)
            print("Port {} is filtered".format(port))
        
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            send(IP(dst=ip)/TCP(dport=port, flags="AR"), verbose=0)
            open_ports.append(port)
            print("Port {} is open".format(port))
        
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            closed_ports.append(port)
            print("Port {} is closed".format(port))

    print("Open ports: ", open_ports)
    print("Closed ports: ", closed_ports)
    print("Filtered ports: ", filtered_ports)

def icmp_ping_sweep(network):
    # TODO: Implement ICMP Ping Sweep
    pass

if __name__ == '__main__':
    print("Select mode: ")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    mode = int(input("Enter choice: "))

    if mode == 1:
        ip = input("Enter host IP: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        tcp_port_scan(ip, start_port, end_port)

    elif mode == 2:
        network = input("Enter network address (CIDR notation): ")
        icmp_ping_sweep(network
