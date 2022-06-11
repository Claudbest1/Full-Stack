# inport a python module called random
import random

while True:
    choices = ["R", "P", "S"]  # list of choices

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P, or S?: ").upper()  # the upper helps to convert all input to upper case
        if player not in choices:
            print("Wrong choice!")
        else:

            # when there is a Tie
            if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("Tie!")

            elif player == "R":
                if computer == "P":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Computer Win!")
                if computer == "S":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Player win!")

            elif player == "S":
                if computer == "R":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Computer Win!")
                if computer == "P":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Player win!")

            elif player == "P":
                if computer == "S":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Computer Win!")
                if computer == "R":
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Player win!")

            # If the player wants to play again
            play_again = input("Play again? (yes/no): ").lower()

            if play_again != "yes":
                break
print("Bye!")
