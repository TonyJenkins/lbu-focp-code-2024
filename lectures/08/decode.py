#!/usr/bin/env python3

import sys


def read_key(the_key_file):
    return the_key_file.readline()[:-1]


def build_lookup(the_key):
    from string import ascii_letters as letters

    return dict(zip(the_key, letters))


def decode_and_print(the_encoded_message, the_key):
    from string import ascii_letters as letters

    code_book = build_lookup(the_key)

    for character in the_encoded_message:
        if character in letters:
            print(code_book[character], end='')
        else:
            print(character, end='')


if __name__ == '__main__':

    try:
        with open(sys.argv[2], 'r') as key_file:
            key = read_key(key_file)

    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[2]}".')
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument for key file.')

    else:
        try:
            with open(sys.argv[1], 'r') as encoded_file:
                encoded_message = encoded_file.read()

        except FileNotFoundError:
            print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}".')
        except IndexError:
            print(f'{sys.argv[0]}: Missing required argument for encoded message file.')

        else:
            decode_and_print(encoded_message, key)
