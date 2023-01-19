"""
#
# File            : 4_Tuples.py
# Created          : 19/01/2023 2:28 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Tuples introduction - Protected lists
#
"""

# Almost same function as a list with few differences.
# instead of [list] there is a parenthesis (tuple)

empty_tuple = ()  # Create an empty list
ages = (19, 21, 20)

student1_details = (20, "Michael Brennan", 77.5)
student2_details = (30, "Giorgos Alexiou", 65)

class_of_students = (student1_details, student2_details, "module title", [2, 3, 4], ("a", "b"))
group_of_students = student1_details + student2_details

'''Printing tuples examples'''
print(" {}".format(ages[1]))
print("{0} \t\t{1} \t{2} "
      .format(student1_details[0], student1_details[1], student1_details[2]))
print(" {}".format(student1_details))
print(" {}".format(class_of_students))
print(" {}".format(class_of_students[0][1]))
# print(" {}".format(class_of_students[4][0])) # out of range - error

'''Is item in Tuple'''
print("Is Michael in list? {}".format(group_of_students))
print("Michael" in group_of_students)  # false
print("Michael" in group_of_students[1])  # true
# Why though:
print("group_of_students:     {}".format(group_of_students))  # this might be wrong
print("group_of_students[1]:  {}".format(group_of_students[1]))

'''Repeating tuples'''
grades = (1, 2, 3)
new_grades = (grades) * 2
print("\nValue of my New_grades:  {}".format(new_grades))

# new_grades[0][0] = 6 --- ERROR: List is protected
# print("Repeated List after change {}".format(new_grades))