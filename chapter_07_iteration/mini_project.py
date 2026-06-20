"""
Chapter 7: Mini Project - Iterative Number Guesser
A CLI game demonstrating while loops, state tracking, and breaking conditions.
"""

import random


def play_game(max_range: int = 100) -> None:
    """
    Main game loop. Tracks attempts and guides the user.
    """
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"=== Guess the Number (1 to {max_range}) ===")

    while True:
        user_input = input("Enter your guess (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            print(f"The secret number was {secret_number}. Better luck next time!")
            break

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("Run this file directly to play the game.")
    # play_game()
