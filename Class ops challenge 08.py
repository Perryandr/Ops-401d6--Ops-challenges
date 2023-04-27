#!/usr/bin/env python3


# Script: Ops 401 Class 05 Ops challenge
# Author: Andrew P.
# Date of lastest revision: 04/26/2023
# Purpose: Encrypting and decrypting a file with python.
# Thanks to classmate Alex, instructor Alex for his demo and the introduction 
# to python help tools and practice sites, and chat.gpt to help me fix any 
# I messed up.



#     ------ START ------

from cryptography.fernet import Fernet
import os, math, time, datetime, getpass, os.path
import urllib.request
import ctypes
import pyautogui
from appscript import app, mactypes


# Requirements
# Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message

# Method 1: change_desktop_background
def change_desktop_background():
  # Need an imageURl
    # imageUrl = 'https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg'
  # Need a path to save Image too
  # Tool: urllib request the image url and saves it to the path
    # urllib.request.urlretrieve(imageUrl, path)
  
  # ----- WINDOWS OS -----
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    # Tool: ctypes => allow us to change the background
    # Need to set SPI_SETDESKWALLPAPER = 20 so access Desktop functionality
      # ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

  # ----- Linux OS -----
  # Using the os package to access the gnome shell and passing it a file. This will change the desktop
    # os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/user/Pictures/wallpapers/picture_name")

  # ----- MAC OS -----
  # need to install `appscript` through python
    # python3 -m pip install appscript
  # pathToImg = '/Users/InstructorWhtie/Desktop/caged.avif'
  # app('Finder').desktop_picture.set(mactypes.File(pathToImg))




# Method 2: pop_up
def pop_up():
  # pyautogiu => sends alerts! All OS's can use this, installed through python
    # pyautogui.alert("YO- you been 'Caged'!", "RANSOMWARE ALERT!!!!", button='WHAT!?!')


# Method 3: ransomeware
def ransomeware():
  # Encrypt directory contents()
  # change_desktop_background()
  # time.sleep(10)
  # pop_up()


# Method 4: ransomeware_restore
def ransomeware_restore():
  #   # Decrypt the dir contents()
  #   # restore background()

# Method 5: restore background
def restore_background():
  # Utilize the backgorund tool depending on your OS to provide it a default/original background

# NEED USER INPUT!
# what mode? 7=>ransomeware, 8=> restore
# provide a dir to ransome or set a default directory

#     ------ END ------










