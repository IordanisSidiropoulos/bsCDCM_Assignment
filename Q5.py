"""
#
# File            : Q5.py
# Created          : 21/05/2023 4:00 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : This is the code of the question 5 from the OOPR assignment.
#
"""

import paramiko

def ssh_connection(host, username, password, command):

    try:
        # Creating an SSH client
        ssh_client = paramiko.SSHClient()

        # Automatically adding the host key
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connecting to the remote server
        ssh_client.connect(host, username=username, password=password)

        # Opening a SSH session
        ssh_session = ssh_client.get_transport().open_session()

        # Running the command
        ssh_session.exec_command(command)

        # Getting the output of the command
        output = ssh_session.recv(4096).decode()

        # Printing the output
        print(output)

        # Closing the SSH session and the connection
        ssh_session.close()
        ssh_client.close()

    except Exception as e:
        print("Connection Failed: ", e)

# Specifying the host, username, password, and command
host = "192.168.167.131"
username = "iordanis"
password = "P@s$w0rd"
command = "sudo apt-get update\nsudo apt-get install curl -y\n" \
          "mkdir LabsA\nmkdir LabsA/lab1\nmkdir LabsA/lab2\ncd LabsA && ls\n" \
          "ls -l --time=atime ~/"

# Calling the ssh_connect function
ssh_connection(host, username, password, command)