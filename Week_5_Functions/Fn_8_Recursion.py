"""
#
# File            : Fn_8_Recursion.py
# Created          : 20/01/2023 12:51 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Recursion
#
"""
import time


def recursion_demo(count):
    time.sleep(2)

    if count < 10:
        count = count + 1
        print("Iteration: {}".format(count))
        recursion_demo(count)


if __name__ == "__main__":
    count = 0
    recursion_demo(count)
