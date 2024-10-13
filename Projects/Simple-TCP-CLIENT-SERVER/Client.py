import socket

host = input("Enter the host: ")# Prompt user to enter the server's host (IP address)
port = int(input("Enter the port: "))# Prompt user to enter the server's port number

# Create a TCP/IP socket (SOCK_STREAM means a TCP connection)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server using the provided host and port
s.connect((host, port))

# Receive a message from the server (buffer size of 1024 bytes)
msg = s.recv(1024)

# Close the socket after receiving the message
s.close()

# Print the received message, decoding it from ASCII
print(msg.decode("ascii"))
