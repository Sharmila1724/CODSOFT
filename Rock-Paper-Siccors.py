
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Wow..! You won!")
    elif player == "paper" and computer == "rock":
        print("Wow..! You won!")
    elif player == "scissors" and computer == "paper":
        print("Wow..! You won!")
    else:
        print("Ohh..! You lose!")

    if not input("Want to Play again? (yes/no): ").lower() == "yes":
        running = False

print("Thank you for playing!")