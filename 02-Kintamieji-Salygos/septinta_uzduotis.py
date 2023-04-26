import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess > number:
        print("Too high, try again.")
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Congratulations! You guessed the number.")