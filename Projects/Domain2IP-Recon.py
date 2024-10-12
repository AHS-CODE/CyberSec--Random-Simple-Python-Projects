import sys  # Importing the sys module for handling command-line arguments
import requests  # Importing requests to make HTTP requests
import socket  # Importing socket to resolve domain names to IP addresses
import re  # Importing re for regular expressions (used to validate the domain)
import json  # Importing json to format and handle JSON data


# Check if the script has exactly one argument (the domain)
if len(sys.argv) != 2:
    print(f'Usage: python {sys.argv[0]} <domain> ')
    sys.exit(1)

# Store the domain name passed as an argument
target = sys.argv[1]

# Regular expression pattern to validate domain names
domain_regex = r'^(?!\-)([A-Za-z0-9\-]{1,63})(?<!\-)\.([A-Za-z]{2,6})(\.[A-Za-z]{2,6})?$'

# Check if the target matches the domain regex and make a GET request to the domain over HTTPS
if re.match(domain_regex, target):
    req1 = requests.get(f'https://{target}/')
    print(f"Status Code: {req1.status_code}")
    print("Headers:")
    print(json.dumps(dict(req1.headers), indent=4))
    print()
# If the target is not a valid domain, print an error message and exit
else:
    print('>> Only domains are accepted ')
    print(f'>> Usage: python {sys.argv[0]} <domain> ')
    sys.exit(1)

# Resolve the domain name to its IP address using socket.gethostbyname
target_ip = socket.gethostbyname(target)
print(f'{target_ip} -> {target}')

# Make a GET request to the ipinfo.io API to get information about the IP address in JSON format
req2 = requests.get(f'https://ipinfo.io/{target_ip}/json')
resp = json.loads(req2.text)
print(f'Location: {resp["loc"]}')
print(f'Region: {resp["region"]}')
print(f'Country: {resp["country"]}')
print(f'City: {resp["city"]}')
print(f'Postal Code: {resp["postal"]}')
print(f'Organization: {resp["org"]}')

