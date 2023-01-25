"""
#
# File            : Q2.1_2.2.py
# Created          : 24/01/2023 9:06 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Q 2.1 & 2.2
#
"""


# Q 2.1
# What are the headers?


# Q 2.2
# Count word Apache in the Text
# This is the best I could do
def countWords(file_name, listwords):
    try:
        file = open(file_name, "r")
        read = file.readlines()
        file.close()
        for word in listwords:
            lower = word.lower()
            count = 0
            for sentence in read:
                line = sentence.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("*,`|/   --|134567890#</ul></li><li>_><!.,;%&/\
                    =><()¨´´?[]{}:</tt></b><pre><tt>")
                    if lower == line2:
                        count += 1
            print(lower, "exists:", count, "times in the text.")
    except FileExistsError:
        print("The file is not there")


countWords("Website.html", ["Apache2"])

# if __name__ == "__main__":
#   countWords("Website.html")
