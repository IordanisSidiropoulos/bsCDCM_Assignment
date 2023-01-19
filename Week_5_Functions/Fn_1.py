"""
#
# File            : Fn_1.py
# Created          : 19/01/2023 7:56 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Functions
#
"""


def print_hi(stu_name):
    """"Print hi to person"""
    # Use a breakpoint in the code line below to debug your script
    # Press ctrl + F8 to toggle the break point
    # print(f"Hello {stu_name}")  # Formatted string example
    print("Hello {}".format(stu_name))


if __name__ == "__main__":
    stu_name = "Dian"
    print_hi(stu_name)
    print("Dian")
