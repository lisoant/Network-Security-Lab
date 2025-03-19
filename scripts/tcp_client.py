import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.0.0.1', 12345)
print(f"Connecting to {server_address}")
client_socket.connect(server_address)

try:
    # Send a message to the server
    message = b"Hello from Host 2"
    print(f"Sending: {message}")
    client_socket.sendall(message)

    # Receive a response from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

finally:
    time.sleep(0.5)
    client_socket.close()

