

# Script: Ops 401 Class 01 Part two of lab 01
# Author: Andrew P.
# Date of lastest revision: 04/17/2023
# Purpose: 

import os
import datetime
import time



# Ping an ip address with ICMP every two seconds.
ip_address = "8.8.8.8" 
interval = 2 



while True:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
    status = "Network Active" if response == 0 else "Network Error"
    print(f"{timestamp} {status} to {ip_address}")
    time.sleep(interval)




