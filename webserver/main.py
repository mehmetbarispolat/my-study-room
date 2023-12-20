import socket

# Define socket host and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6161

# Create socket
# AF_INET	IPv4 Internet protocols
# SOCK_STREAM: Provides sequenced, reliable, two-way, connection-based byte streams.
#              An out-of-band data transmission mechanism may be supported.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"Listening on port {SERVER_PORT} ...")

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse endpoint in HTTP headers
    headers = request.split("\n")
    endpoint = headers[0].split()[1]
    print(endpoint)

    # Send HTTP response
    response = "HTTP/1.0 200 OK\n\nHello World"
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
