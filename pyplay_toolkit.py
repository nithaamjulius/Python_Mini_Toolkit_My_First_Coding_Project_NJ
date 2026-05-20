# pyplay_toolkit.py
# This file contains the 3 mini tools for the PyPlay system.

import random

# Geography Quiz Game
def geography_quiz():
    print("\n=== Geography Quiz ===")
    score = 0

    # List of question and answer pairs
    questions = [
        ("What is the capital of South Africa?", "pretoria"),
        ("What is the largest ocean on Earth?", "pacific"),
        ("Which continent is Egypt in?", "africa")
    ]

    # Loop through each question
    for question, answer in questions:
        # Get the user's answer and clean it up
        user_answer = input(question + " ").strip().lower()

        # Check if the answer is correct
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {answer.title()}.")

    # Show the final score
    print(f"\nYour final score is {score}/{len(questions)}")


# Number Guessing Game
def number_guessing_game():
    print("\n=== Number Guessing Game ===")

    # Pick a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Number of chances the player gets
    attempts = 3

    print("I am thinking of a number between 1 and 10.")
    print("You have 3 tries.")

    # Loop while the player still has attempts left
    while attempts > 0:
        try:
            # Cast the input to an integer
            guess = int(input("Enter your guess: "))

            # Check that the guess is within the valid range
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

        except ValueError:
            # Handle invalid input that is not a number
            print("Invalid input. Please enter a whole number.")
            continue

        # Compare the guess to the secret number
        if guess == secret_number:
            print("Well done! You guessed the number.")
            return
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        # Reduce attempts after each wrong guess
        attempts -= 1
        print(f"Attempts left: {attempts}")

    # Show the correct answer if the player runs out of tries
    print(f"Game over. The number was {secret_number}.")


# Even or Odd Checker
def even_or_odd_checker():
    print("\n=== Even or Odd Checker ===")

    try:
        # Cast the user input to an integer
        number = int(input("Enter a number: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a whole number.")
        return

    # Check whether the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
