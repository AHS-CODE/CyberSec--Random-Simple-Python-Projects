import socket # Import the socket library to create network connections

host = "127.0.0.1"  # The server will listen on localhost (127.0.0.1), meaning only local connections
port = int(input("Enter the server port: "))  # Prompt user to enter the port number for the server

# Create a TCP/IP socket (SOCK_STREAM means a TCP connection)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) # Bind the socket to the address (host and port)
s.listen(1) # Start listening for incoming connections (1 means only one connection can be queued)
print(" >> Server Started.\n >> Waiting for connection ...")

# Accept a new connection when a client connects
conn, addr = s.accept()
print(" >> Connected by", addr)

# Send a thank you message to the connected client
message = f'Thank you for connecting {addr}'
conn.send(message.encode("ascii"))
conn.close()# Close the connection once the message is sent
