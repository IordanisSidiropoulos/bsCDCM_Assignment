"""
#
# File            : PDF_3_Loops_Selection.py
# Created          : 19/01/2023 12:54 a.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Home work for loops andSelection process.
#
"""
# Question 1
if __name__ == "__main__":
#    text = ""
#    while 1:
#        print("Guess the number: ")
#        number = input()
#        number = int(number)
#        if number == 5:
#            break
#        print("Guess again")
#    print("Bravoo!")

# Question 2
    harry_Potter_1 = "10"
    title1 = "Harry Potter A"
    harry_Potter_2 = "10"
    title2 = "Harry Potter B"
    harry_Potter_3 = "10"
    title3 = "Harry Potter C"
    harry_Potter_4 = "10"
    title4 = "Harry Potter D"
    harry_Potter_5 = "10"
    title5 = "Harry Potter E"
    total = float(harry_Potter_1) #+ float(harry_Potter_2) + float(harry_Potter_3) + float(harry_Potter_4) + float(harry_Potter_5)
    print("Title: '{0}' / Cost: {1}€ / Running Total: {2}€"
          .format(title1, harry_Potter_1, float(harry_Potter_1)), "\n"
          "Title: '{0}' / Cost: {1}€ / Running Total: {2}€"
          .format(title2, harry_Potter_2, float(harry_Potter_1) + float(harry_Potter_2)), "\n"
          "Title: '{0}' / Cost: {1}€ / Running Total: {2}€"
          .format(title3, harry_Potter_3, float(harry_Potter_1) + float(harry_Potter_2) + float(harry_Potter_3)), "\n"
          "Title: '{0}' / Cost: {1}€ / Running Total: {2}€"
          .format(title4, harry_Potter_4, float(harry_Potter_1) + float(harry_Potter_2) + float(harry_Potter_3)
                  + float(harry_Potter_4)), "\n"
          "Title: '{0}' / Cost: {1}€ / Running Total: {2}€"
          .format(title5, harry_Potter_5, float(harry_Potter_1) + float(harry_Potter_2) + float(harry_Potter_3)
                  + float(harry_Potter_4) + float(harry_Potter_5)))









