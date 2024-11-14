from scapy.all import *

def sniff_tcp_session(pkt):
    if pkt.haslayer(TCP):
        tcp_layer = pkt.getlayer(TCP)
        print(f"Source: {pkt[IP].src} --> Destination: {pkt[IP].dst}")
        print(f"SEQ: {tcp_layer.seq} | ACK: {tcp_layer.ack}")

# Sniff TCP packets on Host 3
sniff(iface="h3-eth0", filter="tcp", prn=sniff_tcp_session)
