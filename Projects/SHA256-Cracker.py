from pwn import *  # Importing Pwntools library for logging and utility functions
import sys         # Importing sys to handle command-line arguments
import os          # Importing os to check file existence
import hashlib     # Importing hashlib for hashing functionality

# Checking if the script was provided with the correct number of arguments (1 argument for hash)
if len(sys.argv) != 2:
    print('Invalid arguments')
    print(f' >> Usage: python3 {sys.argv[0]} <sha256sum>')
    exit()

# Storing the target hash (the SHA-256 hash we want to crack)
target_hash = sys.argv[1]
attempts = 0
# Asking the user for the password file to use in the brute force attack
password_file = input('Enter password file: ')

# Checking if the password file exists
if not os.path.exists(password_file):
    print("File not found. Please check the path.")
else:
    print("File found. Initiating Brute Force")

# Function to calculate SHA-256 hash of a given password
def sha256sumhex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('latin-1'))
    return sha256.hexdigest()


# Logging progress of the brute force process
with log.progress(f'Attempting to crack: {target_hash}') as progress:
    # Open the password file in 'latin-1' encoding to handle special characters
    with open(password_file, 'r', encoding='latin-1') as password_list:
        # Loop through each password in the password file
        for password in password_list:
            password = password.strip("\n")  # Remove any trailing newlines from the password
            password_hash = sha256sumhex(password)  # Compute the SHA-256 hash of the password
            # Update the progress log with the current attempt and hashed password
            progress.status(f'{attempts}, {password} == {password_hash}')
            # Check if the hashed password matches the target hash
            if password_hash == target_hash:
                # If a match is found, log success and exit the script
                progress.success(f'Password hash found after {attempts} attempts! The hash {target_hash} cracked is {password}')
                exit()  # Exit the script after finding the correct password
            attempts += 1  # Increment the attempt counter for each password tried

        # If no password matches the target hash after trying all passwords, log failure
        progress.failure("Password not found")
