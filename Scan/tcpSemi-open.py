
from scapy import *
from random import randint

def main():
    ip = input("please input ip like this:127.0.0.1")
    port = 80
    pocket = IP(dst=ip) / TCP(sport=12345, dport=port, flags="S")  # Send a SYN packet
    resp = sr1(pocket, timeout=10)
    if (str(type(resp)) == "<'type NoneType'>"):
        print("%s is closed" % (port))
    elif (resp.haslayer(TCP)):
        if (resp.getlayer(TCP).flags == 0x12):
            # Actually, we can confirm it here
            send_rst = sr1(IP(dst=ip) / TCP(sport=12345, dport=port, flags="R"), timeout=10)  # No ACK packet is sent, only an R is transmitted, which prevents the three-way handshake from being established, This means that the scan will not be recorded by the firewall.
            print("port %s is open" % (port))
        elif (resp.getlayer(TCP).flags == 0x14):
            # If it is 0x14, it means the other party refused the connection
            print("port %s is down" % (port))

    pass
if __name__ == "__main__":
    main()