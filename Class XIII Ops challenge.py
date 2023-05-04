#!/usr/bin/env python3


# Script: Ops 401 Class 07 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/03/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools, and chat.gpt to help me fix and replace anything 
# I messed up.

import scapy.all
import IP,ICMP, sr1, TCP
import ipaddress
import socket
import subprocess


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
                print(f"{ip}: Network is blocking ICMP traffic")
            else:
                # Display the IP address and ICMP code
                print(f"{ip}: {response[ICMP].code}")
                print("Network address : ", network.network_address)
                print("Network mask is: ", network.netmask)
                print("Total number of hosts: ", network.num_addresses)
                print(f"({network}) is up")
                # Create an IPv4Network object from the CIDR block
                # Display the network mask from the IP address
                print("Network mask from IP address: ", network.netmask)
                break
        else:
            print(f"There is no response from {ip}")


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
            print(f"{ip}: Network is blocking ICMP traffic")
        # Display the IP address and ICMP code
        else:
            print(f"{ipA}: {response[ICMP].code}")
            print(f"({ipA}) is up")
            ip_network = ipaddress.ip_network(ipA)
            network_mask = ip_network.netmask
            print("The network mask IP is: ", network_mask)
        
    else:
        print(f"There is no response from {ip}")

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
            print(f"{ip}: Network is blocking ICMP traffic")
        else:
            print(f"{ip}: {response[ICMP].code}")
            print("The network mask is: " , network_mask)
    else:
        print(f"There is no response from {ip}")




# User Menu
while True:
    user = input("Please pick on of the following: PortScan or ICMP or Exit ")
    # Port Scanner
    if user.lower() == "PortScan":
        # Define host Ip
        IP_add = input("Please type in a IP address: ")
        # define port range or specific set of ports to scan
        port_range = [22, 23, 80, 443, 3389]
        # IP address ' 45.33.32.156 ' - test IP
        source_port = int(input("Enter source port number: "))
        for dsp_port in port_range:
            response = sr1(IP(dst=IP_add)/TCP(sport=source_port, dport=dsp_port, flags="S"), timeout=1, verbose=0)
        # If flag Ox12 received, send a RST packet. Se1()
            if (response.haslayer(TCP)):
                if (response.getlayer(TCP).flags == 0x12):
                    answer = ("Open")
                    print(f"Port {dsp_port} is {answer}")
                    
            # If Ox14 received, notfiy if close
            elif (response.haslayer(TCP)):
                if (response.getlayer(TCP).flags == 0x14):
                        answer = ("Closed")
                        print(f"Port {dsp_port} is {answer}")
                        
            # If no flag was received 
            else:
                answer = (f"No respose received from {IP_add}")
                print(f"Port {dsp_port} is {answer}")
    
    if user.lower() == "Exit":
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



# Define a function for the port scan
def port_scan(ip_address):
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

# Prompt the user for an IP address to target
ip_address = input("Enter an IP address to scan: ")

# Send an ICMP echo request to check if the host is responsive
ping = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
ping.wait()
if ping.returncode == 0:
    print("Host is online.")
    # Call the port scan function
    port_scan(ip_address)
else:
    print("Host is offline.")
