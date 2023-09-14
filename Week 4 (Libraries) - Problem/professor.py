"""
Prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
digits. No need to support operations other than addition (+).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
   while True:
       user_level = input("Level : ")
       if user_level not in["1","2","3"]:
           continue
       return user_level



def generate_integer(user_level):
    score = 0 # score countdown
    for i in range(10): #score
        nyawa = 1
        if user_level == "1": #select level
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif user_level == "2":
            x = random.randint(10,99)
            y = random.randint(10,99)
        elif user_level == "3":
            x = random.randint(100,999)
            y = random.randint(100,999)

        while True:
            print(f"{x} + {y} = ", end="") #question
            answer = input()
            if answer == str(x + y ):
                score += 1
                break
            elif answer != str(x + y ) and nyawa != 3:
                print("EEE")
                nyawa += 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break
    print(f"Score: {score}")

if __name__ == "__main__":
    main()