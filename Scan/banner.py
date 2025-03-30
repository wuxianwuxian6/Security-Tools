# Connect attempts are usually blocked by firewalls. But if you know which ports are open and can't identify their functions, the banner can be useful.
import time
import socket

def main():
    ip = input("please input ip like this:127.0.0.1")
    port = input("please input port like 80 ")
    s = socket.socket()
    s.connect((ip, port))  # A built-in Python function to connect to the target
    s.send('haha'.encode())  # Send some random data
    banner = s.recv(1024)  # Receive the response
    s.close()
    print("banner is {}".format(banner))  # It will reply with its type
    pass
if __name__ == "__main__":
    main()