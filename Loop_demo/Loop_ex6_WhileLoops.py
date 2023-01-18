"""
#
# File            : Loop_ex6_WhileLoops.py
# Created          : 18/01/2023 4:56 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    # sample while loop
    max_books = 5
    counter = 0
    book_price = 0
    while counter <= max_books:
        book_price += 9.99   # book price
        counter += 1         # count of books is incremented by 1
    print("The final books price is: {0:5.2f}".format(book_price))