"""
#
# File            : IF_sample2.py
# Created          : 18/01/2023 3:49 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""
if __name__ == "__main__":
    grade = 80
    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print("You are the best! You earned a distinction!")
    elif grade >= 60:
        print("You did very well! You got an M.1.")
    elif grade >= 50:
        print("You have earned an M.2.")
    elif grade >= 40:
        print("You passed!")
    else:
        print("Please try again.")


