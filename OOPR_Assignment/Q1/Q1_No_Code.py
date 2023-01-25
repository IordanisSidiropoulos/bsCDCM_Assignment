"""
#
# File            : Q1_No_Code.py
# Created          : 24/01/2023 5:55 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Question 1 - No Code Required - Word File Submitted
#
"""

print("""Question 1
 
 (Preparation: Not code_Word document submitted_Screenshots inluded): 
 Install apache2 on the vm. 5 marks 
The first command installs the web server. The second allows the server through the firewall 
– _if this was a production machine, I would not do it this way! 
The next command reboots the vm to allow the changes to take effect. 
Next, start the server and then test that it is running. 

sudo apt-get install apache2 
sudo ufw allow 'Apache Full' 
sudo init 6 
sudo systemctl start apache 
sudo systemctl status apache 

Open a browser on your own host machine (not the vm) 
and point it to the IP address of the VM. 
It should show a default web page. Use screenshots to demonstrate that this worked. 
Save them to a file named L0012345_Q1_File_1 where L0012345 is replaced by your own L number. 
""")