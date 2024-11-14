import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.0.0.2', 12345)

try:
    # Send a message to Host 2
    message = b'Hello from Host 1'
    print(f'Sending: {message}')
    udp_client.sendto(message, server_address)

    # Receive a response from Host 2
    data, server = udp_client.recvfrom(4096)
    print(f'Received: {data.decode()}')

finally:
    udp_client.close()
