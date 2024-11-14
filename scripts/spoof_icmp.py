from scapy.all import *

def spoof_icmp(pkt):
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:  # ICMP Echo Request
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        icmp = ICMP(type=0)  # Echo Reply
        reply = ip / icmp / pkt[Raw].load
        send(reply)

sniff(filter="icmp", prn=spoof_icmp)

