"""
#
# File            : TESTING_Loops.py
# Created          : 21/01/2023 2:21 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Testing Loops
#
"""


def money_in_Bank():
    total = 0
    for i in range(1, 6):
        month = input("Enter month payed: ".format(i))
        amount_saved = input("Enter amount saved: ".format(i))
        amount_saved = float(amount_saved)
        total += amount_saved
        print("Month: {0} / Money Saved: {1} / Total Savings: {2}".format(month, amount_saved, total))
    print("The sum of your savings are: {}".format(total))


if __name__ == "__main__":
    money_in_Bank()


