"""
#
# File            : 2_Copy_Lists.py
# Created          : 19/01/2023 1:48 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    student1_details = [20, "Michael Brennan", 77.5]  # variety of data types
    student2_details = [30, "Giorgos Alexiou", 65]

    # copy type 1 - Same ID
    student3_details = student1_details
    print("Student 3 details: {}".format(student3_details))

    student3_details[0] = 55  # the change occurs in both
    print("Student 1: {}".format(student1_details))
    print("Student 3: {}".format(student3_details))

    # Use the ID function to prove that they point to the same object
    print("Student 1 details: {0} with an ID: {1}"
          .format(student1_details, id(student1_details)))
    print("Student 3 details: {0} with an ID: {1}"
          .format(student3_details, id(student3_details)))  # same ID

    # copy type 2 - different ID
    student3_details = student1_details[:]  # this [:] symbol creates different IDs
    print("Student 3 details: {}".format(student3_details))
    student3_details[0] = 88  # The change does not occur in both
    print("Student 1: {}".format(student1_details))
    print("Student 3: {}".format(student3_details))

    # Use the ID function to prove that they point to a different object
    print("Student 1 details: {0} with an ID: {1}"
          .format(student1_details, id(student1_details)))
    print("Student 3 details: {0} with an ID: {1}"
          .format(student3_details, id(student3_details)))

