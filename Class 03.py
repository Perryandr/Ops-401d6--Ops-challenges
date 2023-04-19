#!/usr/bin/env python3


# Script: Ops 401 Class 02 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/19/2023
# Purpose: Adding on to Class 02 code, add new features to your uptime sensor tool.




import os
import datetime
import time


import smtplib
import socket
import time
from datetime import datetime




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


# set the initial status of the host to "up"
host_status = "up"

# ask the user for email credentials
email = input("Enter your email address: ")
password = input("Enter your email password: ")

# specify the email details
sender = email
receiver = email
subject = "Host status change notification"

# connect to the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(email, password)

while True:
    # get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # try to connect to the host
    try:
        socket.create_connection(("www.google.com", 80))
        new_status = "up"
    except OSError:
        new_status = "down"

    # check if the status has changed
    if new_status != host_status:
        message = f"Host status changed from {host_status} to {new_status} at {current_time}"
        host_status = new_status

        # create the email message and send it to the administrator
        email_message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{message}"
        smtp_connection.sendmail(sender, receiver, email_message)

    # wait for 5 seconds before checking again
    time.sleep(5)

# close the SMTP connection
smtp_connection.quit()
