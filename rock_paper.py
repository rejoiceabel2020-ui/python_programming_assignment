import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

# Loop to allow multiple rounds
while True:

    # User input
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)

    # Display computer choice
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    # Ask user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break