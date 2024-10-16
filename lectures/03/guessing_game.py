#!/usr/bin/env python3


from game_utils import generate_secret_number, get_integer_from_user


if __name__ == '__main__':

    DEBUG = False

    secret_number = generate_secret_number()

    if DEBUG:
        print(secret_number)

    guesses = 0

    print()
    print('I am thinking of a number between 0 and 100.')
    print('Can you guess what it is?')
    print()

    while True:
        next_guess = get_integer_from_user(0, 100, 'Enter your guess: ')
        guesses += 1

        if secret_number < next_guess:
            print('Lower!')
        elif secret_number > next_guess:
            print('Higher!')
        elif secret_number == next_guess:
            print()
            print('You got it!')
            print(f'You made {guesses} {"guesses" if guesses > 1 else "guess"}.')
            break

        if guesses == 10:
            print()
            print('You are out of guesses!')
            print(f'The number was {secret_number}.')
            break
