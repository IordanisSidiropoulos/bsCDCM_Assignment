"""
#
# File            : File_eg_2.py
# Created          : 20/01/2023 4:06 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""


def file_processing(file_name):
    """Open a file with a list of students and print their details"""
    file_obj = open(file_name, "r+")
    # lines.sort()  #this method can be used to sort a file

    for line in file_obj:
        print(line.rstrip())  # remove o strip the white space at the end of line when printing

    file_obj.write("\nTony Martin, 7898, Vocal training")
    file_obj.seek(0)  # rewind the file to the beginning start at position 0

    print("\nAfter new student was added: ")
    all_file_contents = file_obj.read()  # another way to read the file
    print(all_file_contents)  # Print contents now that new line is added
    file_obj.close()


if __name__ == "__main__":
    file_processing("sample.txt")
