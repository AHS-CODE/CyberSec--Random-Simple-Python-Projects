import requests  # Import the requests library to make HTTP requests
import sys  # Import the sys library to access command-line arguments

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print('Invalid arguments')
    print(f' >> Usage: python3 {sys.argv[0]} <domain>')
    exit()

# Store the target domain from the command-line argument
target = sys.argv[1]
sub_list = input("Enter the subdomains list: ") # Ask the user to input the filename that contains a list of subdomains

# Open the file containing the subdomains list
with open(sub_list) as subs:
    # Loop through each subdomain in the file
    for sub in subs:
        sub = sub.strip()# Remove any leading or trailing whitespace (such as newlines)
        url = f'https://{sub}.{target}'# Construct the URL by appending the subdomain and target domain
        try:
            req = requests.get(url)  # Make an HTTP GET request to the constructed URL
        except requests.exceptions.ConnectionError: # If a connection error occurs (e.g., invalid subdomain), ignore and move to the next
            pass
        else:
            # If no exception occurs, the subdomain is valid and reachable
            print(f'>> Valid Subdomain: {sub}.{target}')
