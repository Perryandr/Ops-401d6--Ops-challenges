#!/usr/bin/env python3


# Script: Ops 401 Class 02 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/18/2023
# Purpose: Ping an IP every few seconds.

import os
import datetime
import time



# Ping an ip address with ICMP every two seconds.
ip_address = "8.8.8.8" 
interval = 2 




while True:
    # ping the IP and capture the return code
    ret_code = os.system(f"ping -c 1 {ip_address} ")
    
    # evaluate the return code and assign status
    if ret_code == 0:
        status = 'Success'
    else:
        status = 'Failure'
        
    # print the status along with timestamp and destination IP
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{timestamp} {status} to {ip_address}")
    
    time.sleep(2)  # wait for 2 seconds before next ping



