from pexpect import pxssh
# It is recommended to use a Linux system; Windows systems may encounter issues

def Login(server, uname, passwd):
    try:
        s = pxssh.pxssh()
        s.login(server, uname, passwd)
        print("yes")
    except:
        print("no")


def main():
    Login("ssh IP address", "username", "password")
    pass

if __name__ == "__main__":
    main()