"""
#
# File            : TEST.py
# Created          : 19/01/2023 9:13 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""


def learn(lessons):
    print(f"I will learn {lessons}!")


if __name__ == "__main__":
    learn("ALL THE LESSONS")


def graduate(university):
    print(f"I will graduate a Level 7 degree from {university}")


if __name__ == "__main__":
    graduate("LetterKenny University")


def whoisthebest(person):
    print(f"The best human in the world is {person}.")


if __name__ == "__main__":
    whoisthebest("Η μικρή Ελένη")

if __name__ == "__main__":
    your_guess = ""

    while 1:
        your_guess = input("Enter your guess: ")
        your_guess = int(your_guess)
        if your_guess == 5:
            break
        print("Again")
    print("congrats")

while 1:
    print("NEW GAME")
    i = input("Enter a NEW number: ")
    i = int(i)
    if i == 6:
        print("Well done MANNN!!!")
        noanswer = input("Play again?? [y/n]:\n")
        noanswer = str(noanswer.lower())
        if noanswer == "n":
            print("Thank you! Goodbye!")
            break
        else:
            print("Alright! Let's do this again!")
    else:
        print("Wrong answer...")
        noanswer = input("Play again?? [y/n]:\n")
        if noanswer == "n":
            print("Thank you! Goodbye!")
            break
        else:
            print("Alright! Let's do this again!")



