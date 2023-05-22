"""
#
# File            : Q4.py
# Created          : 22/05/2023 9:39 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : This is the code of the question 4 from the OOPR assignment.
#
"""


import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    # Clearing the screen
    subprocess.call("cls", shell=True)

    # Asking for input
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Printing server information on a clean banner
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Checking the time that scan was started
    t1 = datetime.now()

    # Range function for specifying the ports
    # to be scanned (here from 1 to 100)
    # Some error handling code was also put
    try:
        for port in range(1, 100):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                service = ""
                if port == 22:
                    service = "SSH"
                elif port == 80:
                    service = "HTTP"
                print("Port {}: {} is Open".format(port, service))

            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctr+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname coud not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn´t connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculating the time difference
    # to see how long it took to finish scanning
    total = t2 - t1

    # Printing the information
    print("Scanning completed in: ", total)

if __name__ == "__main__":
    port_scan()
