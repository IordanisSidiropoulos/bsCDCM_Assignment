"""
#
# File            : Loop_ex7_WhileTrue.py
# Created          : 18/01/2023 5:13 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    # While true sample
    text = ""
    while 1:
        print("Enter name")
        username = input()
        username = username.lower()   # For any lower or upper case input
        if username == "pat":       # in code: name has to be typed with lower case letter
            break
        print("\nSorry, try again! \n")
    print("Finished")