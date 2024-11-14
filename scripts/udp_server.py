import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 12345)
udp_server.bind(server_address)

print("UDP server is listening...")

while True:
    # Receive a message from Host 1
    data, address = udp_server.recvfrom(4096)
    print(f'Received: {data.decode()} from {address}')

    # Send a response back to Host 1
    response = b'Hello from Host 2'
    udp_server.sendto(response, address)



