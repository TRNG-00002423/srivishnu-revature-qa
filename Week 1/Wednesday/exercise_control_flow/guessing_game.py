"""
Task 3: Number Guessing Game
Guess a random number between 1 and 100 in 7 attempts.
"""

import random


def guessing_game():
    answer = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        attempts += 1

        if guess == answer:
            print(f"\nCongratulations! You guessed it in {attempts} attempt(s)!")
            break
        elif guess < answer:
            print("Too low!\n")
        else:
            print("Too high!\n")
    else:
        print(f"\nOut of attempts! The answer was {answer}.")


if __name__ == "__main__":
    guessing_game()
