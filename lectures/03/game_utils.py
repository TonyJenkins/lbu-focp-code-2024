#!/usr/bin/env python3

from random import randint


def generate_secret_number():
    while True:
        random_number = randint(0, 100)
        if random_number not in ['50', '25', '75']:
            return random_number


def get_integer_from_user(lower_bound=0, upper_bound=100, prompt='Enter a number: '):
    while True:
        try:
            number = int(input(prompt))
            if lower_bound <= number <= upper_bound:
                return number
            else:
                print(f'Number must be between {lower_bound} and {upper_bound}.')
        except ValueError:
            print('Please enter a number')


if __name__ == '__main__':

    for count in range(10):
        print(generate_secret_number())

    print(get_integer_from_user(1, 5, 'Enter your best guess: '))
