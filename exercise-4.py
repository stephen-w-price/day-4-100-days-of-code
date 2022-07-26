import random
# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
mylist = ["rock", "paper", "scissors"]

my_choice = mylist[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]

their_choice = random.choice(mylist)

if my_choice == their_choice:
    print(f"You and the computer both choose {my_choice}. It's a tie.")
elif my_choice == "rock" and their_choice == "paper":
    print("You choose rock and lost to paper")
elif my_choice == "rock" and their_choice == "scissors":
    print("You choose rock and beat paper")
elif my_choice == "paper" and their_choice == "rock":
    print("You choose paper and beat rock")
elif my_choice == "scissors" and their_choice == "paper":
    print("You choose scissors and beat paper")
elif my_choice == "scissors" and their_choice == "rock":
    print("You choose scissors and lost to rock")
else:
    print("You choose paper and lost to scissors")
    