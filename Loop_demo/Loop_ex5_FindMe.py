"""
#
# File            : Loop_ex5_FindMe.py
# Created          : 18/01/2023 4:50 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    # Stop when you find a 6
    # Break statement stops the loop
    for i in range(1, 10):
        if i == 6:
            print("Found")
            break
        print("not yet")
    print ("it was found at {}".format(i))