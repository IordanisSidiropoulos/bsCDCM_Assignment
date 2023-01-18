"""
#
# File            : Loop_ex3.py
# Created          : 18/01/2023 4:26 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == "__main__":
    # letters
    from string import ascii_lowercase

    manifesto = """individuals and interactionsover processes and tools
        working software over comprehensive documentation
        Customer collaboration over contract negotiation
        Responding to change over following a plan"""
    for i in ascii_lowercase:
        # print(i)              #Κάθετα
        # print(i, end="")      #Οριζόντια
        print(i, end=":")  # Οριζόντια με χαρακτήρες στη μέση

        print("\n")        # Κενή γραμμή

    for i in manifesto:
        if i != "o":       # Αφαιρούμε συγκεκριμένους χαρακτήρες από το αποτέλεσμα
            print(i, end="")
