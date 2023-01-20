"""
#
# File            : Fn_7_Return_multiply.py
# Created          : 20/01/2023 12:20 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Return- Multiple tuple
#
"""

import time

def multi_sample(num_1, num_2=10):
    num_1 = num_1 * 2
    num_2 = 123   # Perhaps reassign a value
    str_1 = "something"
    return num_1,num_2, str_1  # Return a tuple with two values

def list_rtn_sample():
    ages = [19, 21, 20]
    return ages  # Return a list

def list_rtn_sample2(list):
    time.sleep(3)  # add a time delay to the function
    list1 = list1 *2
    return list1


if __name__ == "__main__":
    val_1, val_2, val_3 = multi_sample(4,6)
    # Or assign to tuple, and use one at a time
    print(f"value_1:{val_1} and value_2 is {val_2} and value_3 is {val_3}")
    print("\nfull return was: {}".format(multi_sample(12, 14)))
    print("\nList example {}".format(list_rtn_sample()))
    print("\n")
    print(list_rtn_sample2([1, 2, 3]))