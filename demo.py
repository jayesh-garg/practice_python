import os
import socket
import sys
import time
import argparse

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-p", "--pwd", help="this will show path for present working directory", action="store_true")
    parser.add_argument("-H", "--Hostname", help="this will display hostname", action="store_true")
    parser.add_argument("-i", "--ipaddress", help="provide ip address", action="store_true")
    args=parser.parse_args()
    if args.pwd:
        print (os.getcwd())
    elif args.Hostname:
        print ("host name is: {}".format(socket.gethostname()))
    elif args.ipaddress:
        print ("ip address is: {}".format(socket.gethostbyname(socket.gethostname())))
    else:
        pass

if __name__ == '__main__':
    Main()
    time.sleep(1)
    sys.exit()