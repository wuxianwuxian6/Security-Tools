from scapy.all import *
from random import randint
def main():
    ip = input("Target IP or let the user input like this: 127.0.0.1")
    ip_id = randint(1, 65535)  # Define a random number
    icmp_id = randint(1, 65535)
    icmp_seq = randint(1, 65535)
    # The random numbers above are used to confuse the firewall
    packet = IP(dst="ip", ttl=64, id=ip_id) / ICMP(id=icmp_id, seq=icmp_seq) / b'Add any characters here'  # The TTL value decreases by 1 for each router passed,by 1 for each router passed, usually not exceeding 64
    # "Packet" means the data packet
    result = sr1(packet, timeout=1, verbose=False)  # Send the packet
    if result:
        for rcv in result:
            scan_ip = rcv[IP].src  # Return who I am scanning
            print(scan_ip + ' is alive')
    else:
        print('is dead')
    pass
if __name__ == '__main__':
    main()