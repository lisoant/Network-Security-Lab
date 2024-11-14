import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5) 

print("TCP server is listening...")

while True:
    # Accept a connection from a client (Host 2)
    connection, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            # Receive data from the client
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                # Send a response back to the client
                connection.sendall(b"Hello from Host 1")
            else:
                break
    finally:
        connection.close()
        print(f"Connection closed with {client_address}")


