#!/usr/bin/env python3


# Script: Ops 401 Class 27 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 05/23/2023
# Thanks to instructor Marco for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.



import logging
import os
import datetime
import logging.handlers as handlers
import time

target = "8.8.8.8"

# Create logging object
logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='w')

# Create object
loggerV = logging.getLogger("app")

# Setting the threshold
loggerV.setLevel(logging.INFO)  # Use logging.INFO constant or "INFO" string

# Create log file handlers
loghandler = handlers.RotatingFileHandler("Demo.log", maxBytes=500, backupCount=2)
loghandler.setLevel(logging.INFO)  # Use logging.INFO constant or "INFO" string

loggerV.addHandler(loghandler)

def ping_Status(target):
    try:
        # Intentionally raise an exception to simulate an error
        raise ValueError("An intentional error occurred")

        # Evaluate the response and assign success or failure to the status variable
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "success"
            print(f"{target} is up!")
        else:
            status = "failure"
            print(f"{target} is down!")

        # Get the current timestamp and print the status and timestamp
        currenttime = datetime.datetime.now()
        print(f"{currenttime} - Status: {status}")
        return status
    except Exception as e:
        loggerV.exception("An error occurred")
        raise e

while True:
    try:
        # Transmit a single ICMP ping packet to the target
        ping_Status(target)
        # Wait for 2 seconds before transmitting another ping packet
        time.sleep(2)
    except KeyboardInterrupt:
        # Stop the program if the user interrupts it
        break
    except Exception as e:
        loggerV.exception("An error occurred")
