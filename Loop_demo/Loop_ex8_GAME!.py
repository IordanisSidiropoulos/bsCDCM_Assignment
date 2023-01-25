"""
#
# File            : Loop_ex8_GAME!.py
# Created          : 20/01/2023 1:25 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Game
#
"""

if __name__ == "__main__":
    # While true sample
    text = ""
    while 1:
        print("Enter number: ")
        number = input()
        number = int(number)   # For any lower or upper case input
        if number == 5:       # in code: name has to be typed with lower case letter
            print("Congrats!!")
            break
        elif number < 5 or number > 5:
            machine_answer = "Sorry, try again?"
            print(machine_answer)
            player_answer = input("[y/n]: ")
            player_answer = str(player_answer)
            player_answer = player_answer[0]
            player_answer = str(player_answer[0].lower())
            if player_answer == "n":
                print("Thank you, goodbye!")
                break
            if player_answer == "y":
                print("One more try then!")
            else:
                print("Only 'y' and 'n' allowed!")
                print("Try again?")
                player_answer = input("[y/n]: ")
                player_answer = str(player_answer)
                player_answer = player_answer[0]
                player_answer = str(player_answer[0].lower())
                if player_answer == "n":
                    print("Thank you, goodbye!")
                    break
                if player_answer == "y":
                    print("One more try then!")
                else:
                    print("Don't Spam! You are out!")
                    break
    print("Exited Game")
