"""
#
# File            : Fn_6_Scope_reassign.py
# Created          : 20/01/2023 12:38 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Scope reassigned
#
"""

# num_2 is given a default value of 10 oly if
# 1 variable is passed to the method
def overloading_sample(num_1, num_2=10):
    # local variables have priority
    total_inner = num_1 + num_2
    print("Inside fn total is: {}".format(total_inner))
    # rename total in the function for the best practice
    return total_inner

if __name__ == "__main__":
    total = overloading_sample(99,1000)
    print("In main total is {}".format(total))
    total = overloading_sample(50)
