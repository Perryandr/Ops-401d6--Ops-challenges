#!/usr/bin/env python3


# Script: Ops 401 Class 13 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/09/2023
# Purpose: Encrypting and decrypting a file and folders in a path with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools, and chat.gpt to help me fix and replace anything 
# I messed up.

import scapy.all
import IP,ICMP, sr1, TCP
import ipaddress


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







import ipaddress
from scapy.all import IP, ICMP, sr1, TCP

# Define the function to perform the ICMP ping sweep
def IP4sweep(ip):
    # Create an IPv4Address object from the IP address
    ipA = ipaddress.IPv4Address(ip)
    # Send an ICMP echo request packet and wait for a response
    response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
   # Verify IP address in an IP address
    try:
        ipaddress.ip_address(ip)
        print(f"{ip} Valid IP address")
    except ValueError:
        print(f"{ip} Invalid IP address")
    # Check if a response was received and if Code is in list
    list = (1, 2, 3, 9, 10, 13)
    if response:
        if response[ICMP].code == list:
        # Display a message indicating that the network is blocking ICMP traffic
            print(f"{ip}: Network is blocking ICMP traffic")
        # Display the IP info and run port scanner
        else:
            # print code number
            print(f"{ipA}: {response[ICMP].code}")
            # print if ip is up
            print(f"({ipA}) is up")
            # print netmask
            ip_network = ipaddress.ip_network(ipA)
            network_mask = ip_network.netmask
            print("The network mask IP is: ", network_mask)
            # run port scanner
            scanner(ip)
        
    else:
        print(f"No response from {ip}")
        
def scanner(ip):
    port_range = [22, 23, 80, 443, 3389]
    source_port = 1025
    for dsp_port in port_range:
        response = sr1(IP(dst=ip)/TCP(sport=source_port, dport=dsp_port, flags="S"), timeout=1, verbose=0)
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
            answer = (f"No response from {ip}")
            print(f"Port {dsp_port} is {answer}")
            
while True:
    ip = input("Select an IP address: ")
    if not ip:
        # If empty runs this IP automaticly
        IP4sweep('45.33.32.156') 
    # breaks the loop 
    elif ip == "Exit":
        break