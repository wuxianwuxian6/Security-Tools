from scapy.all import *
import time

def main():
    while 1:
        pdst = "%i,%i,%i,%i" % (randint(1, 254), randint(1, 254), randint(1, 254), randint(1, 254))
        psrc = input("Find a non-existent ip address like this:192.192.192.192")
        send(IP(src=psrc, dst=pdst) / ICMP())
        '''
        # If this person does not exist on the public network, the packet will be sent and no response will be received.
         If this person does exist on the public network, the packet will be sent and no response will be received either. 
         Either way, the packet will go missing on one side.
        '''

        time.sleep(0.5)
        print(pdst)
    pass

if __name__ == "__main__":
    main()