#!/usr/bin/env python3


from wonderwords import RandomWord


if __name__ == "__main__":

    rw = RandomWord()

    try:
        number_to_generate = int(input('How many passwords: '))

        if 0 < number_to_generate <= 20:
            print()

            for counter in range(number_to_generate):
                password = rw.word() + rw.word() + rw.word()
                print(f'{counter + 1}: {password}')

        else:
            print('Please enter a number between 1 and 20.')

    except ValueError:
        print('Invalid input')
