#!/usr/bin/env python3


# Script: Ops 401 Class 12 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/24/2023
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.


import ipaddress
from scapy.all import IP, ICMP, sr1, TCP
import socket

# Define the function to perform the ICMP ping sweep
def sweep(network):
    # Create an IPv4Network object from the CIDR block
    network = ipaddress.IPv4Network(network)
    # Loop through all IP addresses in the network
    for ip in network.hosts():
        # Send an ICMP echo request packet and wait for a response
        response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
        # Check if a response was received
        if response: 
            if response[ICMP].code == 3:
                # Display a message indicating that the network is blocking ICMP traffic
                print(f"{ip}: Network is actively blocking ICMP traffic")
            else:
                # Display the IP address and ICMP code
                print(f"{ip}: {response[ICMP].code}")
                print("Network address of the network: ", network.network_address)
                print("Network mask: ", network.netmask)
                print("Total number of hosts under the network: ", network.num_addresses)
                print(f"({network}) is up")
                # Create an IPv4Network object from the CIDR block
                ip_network = ipaddress.IPv4Network(network)
                # Display the network mask from the IP address
                print("Network mask from IP address: ", ip_network.netmask)
                break
        else:
            print(f"No response from {ip}")


# Define the function to perform the ICMP ping sweep
def IPsweep(ip):
    # Create an IPv4Address object from the IP address
    ipA = ipaddress.IPv4Address(ip)
    # Send an ICMP echo request packet and wait for a response
    response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
    # Check if a response was received
    if response:
        if response[ICMP].code == 3:
        # Display a message indicating that the network is blocking ICMP traffic
            print(f"{ip}: Network is actively blocking ICMP traffic")
        # Display the IP address and ICMP code
        else:
            print(f"{ipA}: {response[ICMP].code}")
            print(f"({ipA}) is up")
            ip_network = ipaddress.ip_network(ipA)
            network_mask = ip_network.netmask
            print("The network mask IP is: ", network_mask)
        
    else:
        print(f"No response from {ip}")

# Define the function to perform the ICMP ping sweep
def Hostsweep(host):
    # Get the IP address of the host
    ip_address = socket.gethostbyname(host)
    ip_network = ipaddress.ip_network(ip_address)
    network_mask = ip_network.netmask
    # Send an ICMP echo request packet and wait for a response
    response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
    # Check if a response was received
    if response:
        # Display the IP address and ICMP code
        if response[ICMP].code == 3:
            # Display a message indicating that the network is blocking ICMP traffic
            print(f"{ip}: Network is actively blocking ICMP traffic")
        else:
            print(f"{ip}: {response[ICMP].code}")
            print("The network mask is: " , network_mask)
    else:
        print(f"No response from {ip}")




# User Menu
while True:
    user = input("Please pick on of the following: PortScan or ICMP or Exit ")
    # Port Scanner
    # Port Scanner
    if user == "Portscan":
        # Define host IP
        IP_add = input("Please type in an IP address: ")
        # Define port range or specific set of ports to scan
        port_range = [22, 23, 80, 443, 3389]
        # IP address '45.33.32.156' - test IP
        source_port = int(input("Enter source port number: "))
        for dst_port in port_range:
            response = sr1(IP(dst=IP_add) / TCP(sport=source_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
            if response is not None:
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    print(f"Port {dst_port} is open")
                elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                    print(f"Port {dst_port} is closed")
                else:
                    print(f"No response received from {IP_add}")
            else:
                print(f"No response received from {IP_add}")

        if user == "Exit":
            break    
    
    # ICMP sweep    
    if user == "ICMP":
        # Choices
        reply = input("IP, Host or Network? ")
        # IP - IP of the place you want to scan
        if reply == "IP":
            ip = input("Please type an IP address: ")
            IPsweep(ip)
        # Host - Host name
        if reply == "Host":
            host = input("Write host name: ")
            Hostsweep(host)
        # Nework - CIDR Block  
        if reply == "Network": 
            IPnetwork = input("Type a CIDR block: ")
            sweep(IPnetwork)