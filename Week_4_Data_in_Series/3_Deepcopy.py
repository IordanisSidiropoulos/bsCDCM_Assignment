"""
#
# File            : 3_Deepcopy.py
# Created          : 19/01/2023 2:09 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Deepcopy
#
"""

from copy import deepcopy #important

if __name__ == "__main__":
    student1_details = [20, "Michael Brennan", 77.5]  # variety of data types
    student2_details = [30, "Giorgos Alexiou", 65]

    # copy type 3 - Deepcopy - created a new unique ID fo new object
    student4_details = deepcopy(student1_details)
    print("Student 4: {}".format(student4_details))

    print("\n")
    student4_details[0] = 66  # The change occurs only in student 4
    print("Student 1: {}".format(student1_details))
    print("Student 4: {}".format(student4_details))

    # Use the ID function to prove that they point to the same object
    print("Student 1 details: {0} with an ID: {1}"
          .format(student1_details, id(student1_details)))
    print("Student 4 details: {0} with an ID: {1}"
          .format(student4_details, id(student4_details)))