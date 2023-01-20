"""
#
# File            : Fn_5.py
# Created          : 20/01/2023 12:01 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Scope
#
"""

def overloading_sample(num_1, num_2=10):
    # global total - <<Not recommended method>>
    #total = 0  # Local scope variable (inside function)
    # Local take priority over global
    total = num_1 + num_2
    print("Inside function total is: {}".format(total))
    return

total = 0  # Global scope (out of function)

if __name__ == "__main__":
    overloading_sample(99, 1000)
    overloading_sample(50)
    print("In main, total is: {}".format(total))