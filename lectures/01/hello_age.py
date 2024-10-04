#!/usr/bin/env python3

if __name__ == "__main__":

    name = input('What is your name? ')

    if name:
        try:
            year_now = int(input('What is the current year? '))
            year_born = int(input('What year were you born? '))

            if year_born > year_now:
                print('Invalid input. You cannot be born in the future.')
            else:
                age = year_now - year_born

                print()
                print(f'Hello, {name.title()}! It is good to meet you.')
                print(f'This year you will be {age} years old.')

        except ValueError:
            print('Invalid input. Please enter a number.')

    else:
        print('Invalid input. Please enter a name.')
