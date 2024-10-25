#!/usr/bin/env python3
#A python program for a simple number guessing game

import random

if __name__ == '__main__':
    level = int(input("Please enter the maximum value for the guessing game: "))
    cpu_guess = random.randint(1, level)
    print(cpu_guess)
    turns = 0
    while True:
        turns += 1
        player_guess = int(input("Please guess a number between 1 and 10: "))

        if player_guess == cpu_guess:
            print("Well Done! You guessed correctly")
            break
        elif player_guess > cpu_guess:
            print("You guessed higher")
        else:
            print("You guessed lower")

    print(f"Thank you for playing! You guessed in {turns} turns ")



