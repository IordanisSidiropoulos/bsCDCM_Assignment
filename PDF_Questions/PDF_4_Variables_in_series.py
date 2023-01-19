"""
#
# File            : PDF_4_Variables_in_series.py
# Created          : 19/01/2023 5:30 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Questions in lists, tuplesand dictionaries

#  NOT FINISHED
"""

# Question 1
l_number1 = "L12345"  # Creating tuples for students
l_number2 = "L66666"
l_numbers_all = l_number1 + l_number2  # All students together
print("\n-Student L Numbers: {0} / {1}".format(l_number1, l_number2))

module1 = ["java_programming"]
module2 = ["python_scripting"]
modules_list = module1 + module2
print("-Modules List Data: a) {0} / b) {1}".format(module1[0], module2[0]))
java_grades = {l_number1: 20, l_number2: 30}
python_grade2 = {l_number1: 50, l_number2: 60}
print("Java Grades:    {}".format(java_grades))
print("Python Grades:  {}".format(python_grade2))

# Question 2
# week 1
Lotto_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
week1_players = ["Joe", "John", "Jane", "Mick", "Mary",
                 "Ann", "Rick", "John", "Aine", "Brenda"]
numbers_players1 = {"Joe": 2, "John": 19, "Jane": 12, "Mick": 9, "Mary": 5,
                    "Ann": 7, "Rick": 10, "John": 13, "Aine": 5, "Brenda": 16}
week2_players = ["Jack", "Mary", "Phil", "John", "Pat",
                 "Joe", "Luke", "Bill", "Ben", "Nathan"]
numbers_players2 = {"Jack": 3, "Mary": 5, "Phil": 8, "John": 2, "Pat": 1,
                    "Joe": 7, "Luke": 5, "Bill": 2, "Ben": 7, "Nathan": 7}
print("Joe played / Week 1: {} times / Week 2:  {} times"
      .format(week1_players.count("Joe"), week2_players.count("Joe")))
print("John played / Week 1: {} times / Week 2:  {} times"
      .format(week1_players.count("John"), week2_players.count("John")))
print("Jane played / Week 1: {} times / Week 2: {} times"
      .format(week1_players.count("Jane"), week2_players.count("Jane")))

