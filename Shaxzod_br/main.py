#Number Guessing Game Objectives:
from art import logo
import random

print(logo)
# Include an ASCII art logo.
actual_guess = random.randint(0, 100)
hearts = 0
is_game_over = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")
print(f"Pssst, the correct answer is {actual_guess}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    hearts += 10
elif level == "hard":
    hearts += 5
print(f"You have {hearts} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))
# Allow the player to submit a guess for a number between 1 and 100.
while not is_game_over:
    if actual_guess < guess:
        print("Too high.")
        print("Guess again.")
        hearts -= 1
        print(f"You have {hearts} attempts remaining to guess the number.")
        if hearts == 0:
            is_game_over = True
            break
        guess = int(input("Make a guess: "))
    elif actual_guess > guess:
        print("Too low.")
        print("Guess again.")
        hearts -= 1
        if hearts == 0:
            is_game_over = True
            break
        print(f"You have {hearts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    else:

        print(f"You got it! The answer was {actual_guess}.")
        is_game_over = True
