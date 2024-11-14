from scapy.all import *

def icmp_monitor(pkt):
    if pkt.haslayer(ICMP):
        print(f"ICMP packet: {pkt.summary()}")


sniff(iface="h1-eth0", filter="icmp", prn=icmp_monitor, store=0)


