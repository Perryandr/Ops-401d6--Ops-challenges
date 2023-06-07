#!/usr/bin/env python3


# Script: Ops 401 Class 33 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 06/07/2023
# Thanks to instructor Marco for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.
# Also thank you to Alex and Sierra for helping me with python3 challenge, I struggle dearly.

# Import Libraries.
import os, sys, time, telnetlib, signal
import subprocess, socket
import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

print("Target site is " + targetsite)
print(cookie)


# - Send the cookie back to the site and receive a HTTP response
new_response = requests.get(targetsite, cookies=cookie)

# - Generate a .html file to capture the contents of the HTTP response
page = new_response.text
with open(r'C:\Users\deadl\OneDrive\Documents\Github\Ops-401\Code\cookie.html', 'w') as file:
    file.write(page)
    
# - Open it with Firefox
webbrowser.get('firefox').open('cookie.html')