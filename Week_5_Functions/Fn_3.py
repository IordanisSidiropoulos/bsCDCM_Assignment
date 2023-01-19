"""
#
# File            : Fn_3.py
# Created          : 19/01/2023 9:26 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""


def print_lnum(lnum):
    """Prints a welcome message"""
    print(f'Hi, {lnum}')
    return


def print_name(student_name):
    fname, lname = str(student_name).split(" ")
    print(f'Hi {fname} {lname}, welcome to LYIT')
    return


if __name__ == '__main__':
    print_name("Iordanis Sidiropoulos")

if __name__ == "__main__":
    print_lnum("mr.1053")


def company(companyName):
    part1, part2 = str(companyName).split(" ")
    print(f"I work as a Cabin Crew for {part1} {part2}")


if __name__ == "__main__":
    company("Ryan Air")
