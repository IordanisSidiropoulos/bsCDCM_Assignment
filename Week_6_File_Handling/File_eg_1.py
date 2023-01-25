"""
#
# File            : File_eg_1.py
# Created          : 20/01/2023 3:45 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""


def file_processing(file_name):
    '''Open a file with a list of students and print their details'''

    lines = open(file_name).readlines()
    # lines.sort()  #  This method can be used to sort a file

    for line in lines:
        student, l_num, course = line.split(",")
        print("Student name: {0} \nLNumber: \t{1} \bCourse \t\t{2}\n".format(student, l_num, course))
        # Practice!!! Could I format the string in an other way???


# Press the green button in the gutter to run the script
if __name__ == "__main__":
    file_processing("sample.txt")
