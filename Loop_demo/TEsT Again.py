"""
#
# File            : TEsT Again.py
# Created          : 22/01/2023 1:39 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Trying to exit loops with combining functions
#
"""
import sys

print("\nWelcome to our Numbers Game Pro!\n")
print("You will be asked to guess the right number!")


def game():
    # if __name__ == "__main__":
    while 1:
        print("\nAre YOU Ready Player?!! :-D :-)")
        number = input("Enter a number: ")
        number = int(number)
        if number == 5:
            print("Well Done YOU!!!")
            while 2:
                continue_game = input("Continue playing? [y/n]]")
                continue_game = str(continue_game.lower())
                if continue_game == "n".format(continue_game.lower()):
                    sys.exit("Thank you for playing!\nSee you again! Goodbye!\n:-))))")

                elif continue_game == "y".format(continue_game.lower()):
                    print("Perfect!\nLet's do this!")
                    game()
                else:
                    print("Wrong input! Enter only 'n' or 'y' please!")
        elif number > 10 or number < 0:
            print("Out of range\nGuess within 0 to 10 range please!")
        else:
            print("Sorry, wrong number....")
            while 2:
                continue_game = input("Continue playing? [y/n]]")
                continue_game = str(continue_game.lower())
                if continue_game == "n".format(continue_game.lower()):
                    sys.exit("Thank you for playing!\nSee you again! Goodbye!\n:-))))")
                elif continue_game == "y".format(continue_game.lower()):
                    print("Perfect!\nLet's do this!")
                    game()
                else:
                    print("Wrong input! Enter only 'n' or 'y' please!")


if __name__ == "__main__":
    game()
