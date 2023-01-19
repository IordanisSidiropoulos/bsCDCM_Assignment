"""
#
# File            : PDF_2.3_String_Manipulation.py
# Created          : 18/01/2023 8:58 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Home work for Python improvement.
#
"""

# Question 1
python_mission = "\n-The mission of the Python Software Foundation is to promote, protect,\n" \
                 "and advance the Python programming language, and to support and facilitate\n " \
                 "the growth of a diverse and international community of Python programmers"
print(python_mission)

# Count the number of appearances of the letter "s".
s = python_mission.count("s")
print("\n-The letter 's' appears {0} times within the Python_Mission Statement".format(s))

# Find the second instance of the word Python which occurs somewhere after position 25.
# Selection structures and loops should not be used. Your answer should only use string methods.
print(python_mission[-18:-12])

# What value is returned from the statement:
# print(“The word returned is: {}”.format(python_mission[25:34]))
print("The word returned is: >{}<".format(python_mission[25:34]))

# Find out if the word ‘diverse’ is in the mission statement
# using two different methods.
diverse = python_mission.find("diverse")
print(diverse)  # 1) If the word is not in the script, thn we get a -1 instead
# If the word exists, then we get its position number
print("diverse" in python_mission)  # This query gives us True or False
print("diverse" not in python_mission)  # This query returns True of False again.
# I used three ways to find the word "diverse" within Python_mission

# Check if the string 12345 is a number
value = "12345"
print("\n", value.isnumeric())

# Print out the following directory structure as a string
# C:\users\ndarby\python3\python-3.5.1\bin


# Question 2
print(python_mission[-18:-12])

# Question 3
suffix_no = 1122
