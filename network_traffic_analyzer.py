import pyshark
INTERFACE = "Wi-Fi"

def packet_callback(packet):
    try:
        print(f"[+] Pacchetto catturato: {packet.highest_layer}")
        print(f"    - Protocollo: {packet.transport_layer}")
        print(f"    - Sorgente: {packet.ip.src} -> Destinazione: {packet.ip.dst}")
        print(f"    - Porta sorgente: {packet[packet.transport_layer].srcport} -> Porta destinazione: {packet[packet.transport_layer].dstport}")
        print("-" * 50)
    except AttributeError:
        pass  # Alcuni pacchetti potrebbero non avere tutti i campi, li ignoriamo

def start_sniffing():
    print(f"[*] Avvio cattura pacchetti su {INTERFACE}...")
    capture = pyshark.LiveCapture(interface=INTERFACE)
    capture.apply_on_packets(packet_callback, packet_count=10)  # Limita a 10 pacchetti per test

if __name__ == "__main__":
    start_sniffing()