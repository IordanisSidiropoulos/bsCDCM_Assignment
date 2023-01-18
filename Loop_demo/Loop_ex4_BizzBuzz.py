"""
#
# File            : Loop_ex4_BizzBuzz.py
# Created          : 18/01/2023 4:42 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    for i in range(1, 20):
        if i == 5:                     #Simple number
            print("Buzz")
        print("Bizz", end="")

    print("\n")

    for i in range(1, 20):
        if (i % 5) == 0:
            print("Buzz")
        print("Bizz", end="")