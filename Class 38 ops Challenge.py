#!/usr/bin/env python3


# Script: Ops 401 Class 33 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 06/07/2023
# Thanks to instructor Alex for his demo and the introduction 
# to python help tools and Replit.com, and chat.gpt to help me fix any errors 
# I created.
# Also thank you to Alexander and Sierra for helping me with python3 challenge, I struggle dearly.

# Import Libraries.
import os, sys, time, telnetlib, signal
import subprocess, socket
import webbrowser
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
### Takes input from user and retrives all the HTML forms then returns a list of form elements
def get_all_forms(url):
    #Send a GET request to the URL. .content us used to access the raw content of the response
    # Bs creates an object soup which is parsed HTML
    soup = bs(requests.get(url).content, "html.parser")
    # Returns a list of all the form elements found in the HTML
    return soup.find_all("form")

### TODO: Add function explanation here ###
### This function extracts details form the 'form' variable. This returns a dictionary containing these form details
def get_form_details(form):
    # Empty dictionary to store form details
    details = {}
    # Saves the elements attributes or 'attrs'. The 'get' is used to access the form. 
    # 'lower' converts the data to lowercase
    action = form.attrs.get("action").lower()
    # Retrives the value of the method from the form element list, if no method the defaults to get.
    # also coverts data to lowercase
    method = form.attrs.get("method", "get").lower()
    # Starts a new empty list to store data
    inputs = []
    # Iterates over all input tags
    for input_tag in form.find_all("input"):
        # Retrieves the value of the type of data, if no type then defaults to text
        input_type = input_tag.attrs.get("type", "text")
        # Retrieves the value of the name of the data
        input_name = input_tag.attrs.get("name")
        # Creates the dicionary with the input type and name and appends it to 'inputs'
        inputs.append({"type": input_type, "name": input_name})
    # Stores the action URL in a dictionary
    details["action"] = action
    # Stores the method ie GET or POST in a dictionary
    details["method"] = method
    # Stores the input in a dictionary
    details["inputs"] = inputs
    # Return details as a variable 
    return details

### TODO: Add function explanation here ###
# This function constructs the form submission URL and populates the form fields with the provided data
# Either Through GET or POST
def submit_form(form_details, url, value):
    # This uses urljoin to join the base URL with the value of the action arribute
    target_url = urljoin(url, form_details["action"])
    # Retrieves the list of input fields from form_details and assgins to new Var
    inputs = form_details["inputs"]
    #  New empty Dictionary
    data = {}
    # Iterates of each input in inputs
    for input in inputs:
        # Checks if the input is Text or Search
        if input["type"] == "text" or input["type"] == "search":
            # Assigns the proved value to the value attribute. injects the value into the input field
            input["value"] = value
        # Gets the value of name. 
        input_name = input.get("name")
        # gets the value of value.
        input_value = input.get("value")
        # if both input name and input value are not noe then the script continues
        if input_name and input_value:
            # Adds assigns the name with the corresponding value in the data dictionary
            data[input_name] = input_value
    # Checks if the method is post. This line sends a POST request to the URL with data included.
    if form_details["method"] == "post":
        # returns the response of the POST request
        return requests.post(target_url, data=data)
    else:
        # If the form is not POST
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
# Main function that preforms the XSS scan. 
# Takes URL and scans for potential XSS vulnerabilites. 
# returns True or False
def scan_xss(url):
    # Calls the function from earlier, and assigns it a variable
    forms = get_all_forms(url)
    # Prints a message indication the number of forms detected. 
    print(f"[+] Detected {len(forms)} forms on {url}.")
    # Assigns a JavaScript payloda to a variable. Triggers an alert
    js_script = "<script>alert('XSS Vulnerability');</script>"
    # This line initializes a boolean variable. To track whether there are any threats found
    is_vulnerable = False
    # Loop that iterates over each form in forms list
    for form in forms:
        # Calls a function from eariler to retrieve the details of the current forms. 
        # Returns data as a new variable as Form_details
        form_details = get_form_details(form)
        #Calls submit_form and its details are turned into the variable content
        content = submit_form(form_details, url, js_script).content.decode()
        # Checks is the payload (js_script) is present in the content string. If found, the script continues
        if js_script in content:
            # Prints message indicationg that a XSS has been detected
            print(f"[+] XSS Detected on {url}")
            # Prints a string before details
            print(f"[*] Form details:")
            # Prints the details pprint = pretty print 
            pprint(form_details)
            # Indicates that an XSS vulnerablitiy was found
            is_vulnerable = True
    # Returns the variable. If one was found the True otherwise False
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
# Prompts user to enter URL and calls Scan_Xss to test vulnerabilites.
if __name__ == "__main__":
    # this prompts the user to enter URL
    url = input("Enter a URL to test for XSS:") 
    # Calls the scan_xss function, passing the url as an argument 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection