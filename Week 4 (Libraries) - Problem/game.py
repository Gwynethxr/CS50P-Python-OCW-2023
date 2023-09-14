"""
1. Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
2. Randomly generates an integer between 1 and inclusive, using the RANDOM module.
3.Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

If the guess is smaller than that integer, the program should output Too small! and prompt the user again.

If the guess is larger than that integer, the program should output Too large! and prompt the user again.

If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level <= 0 :
        continue

    num = random.randint(1, level)

    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess == num :
        print("just right!")
        break
    elif guess < num :
        print("Too small!")
    elif guess > num:
        print("Too large!")
