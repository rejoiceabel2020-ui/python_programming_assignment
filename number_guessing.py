import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    attempts += 1
    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct! You guessed the number in", attempts, "attempts.")
        break