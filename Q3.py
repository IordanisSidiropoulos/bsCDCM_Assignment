"""
#
# File            : Q3.py
# Created          : 22/05/2023 2:03 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : This is the code of the question 3 from the OOPR assignment.
#
"""

import paramiko
import time
import re


# Opening SSH connection to the device
def ssh_connection(ip):
    try:
        username = "iordanis" # Automation script- reading dta from file
        password = "P@s$w0rd" # never hard code

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")  # unix command to list
        # directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection("192.168.167.131")