#!/bin/bash


# Script: Ops 401 Class 01 Part two of lab 01
# Author: Andrew P.
# Date of lastest revision: 04/17/2023
# Purpose: Give myself an objective for shell script from 
# Automatic screen lock
# or Antivirus installed and scanning 
# or automatic OS updates enabled.


# Site used for reference/aid is https://techdirectarchive.com/2020/03/24/how-to-orchestrate-windows-update-with-powershell-and-task-scheduler/


# Assignment: Automatic OS updates enabled.

# Enable automatic OS updates

# installs everything (newest version) along with required modules.
Install-Module PSWindowsUpdate -Force

# Will ensure that updates are downloaded, installed completely and then restarted.
Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot



