"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

random_number = random.randint(1, 20)
print("=== SIMPLE GUESSING GAME ===")
print("Guess my number between 1 and 20!")
print("You have 6 attempts.")

attempts = 0
while attempts < 6:
    guess = input(f"Attempt {attempts+1}/6 - Enter your guess: ")
   
    guess = int(guess)
    attempts += 1
    if guess == random_number:
        print(f"Congratulations! You won in {attempts} attempts!")
        break
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
else:
    print(f"Sorry, you lost! The correct number was: {random_number}")