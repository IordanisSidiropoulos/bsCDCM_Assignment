"""
#
# File            : Fn_4.py
# Created          : 19/01/2023 10:10 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""

num = 3
inc_by = 2


# Function to increase a number (3) by a value (2) = 5

def increase_value(original_value, increment_by):
    print("Inside Method")
    print("Original_value {0}, ID: {1}".format(original_value, id(original_value)))
    print("Increment by {0}, Increment by ID: {1}".format(original_value, id(original_value)))
    original_value += increment_by
    print("Updated version: Original_value {0}  (new)ID: {1}\n"
          .format(original_value, id(original_value)))


if __name__ == "__main__":
    print("Called in main")
    print("num {0} numid {1}".format(num, id(num)))
    print("inc_by {0} inc_by ID: {1}".format(inc_by, id(inc_by)))
    increase_value(num, inc_by)  # Function is called
    print("Called in main after Funcion")
    print("num {0} num id {1}".format(num, id(num)))
    print("inc_by {0}, inc_by ID: {1}".format(inc_by, id(inc_by)))
