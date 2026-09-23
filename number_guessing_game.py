# Number guessing game
import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < 1 or guess >100:
        print("Invalid number! Enter a number between 1 and 100.")

    elif guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! 🎉")
        print("You guessed the number in", attempts, "attempts.")
        break