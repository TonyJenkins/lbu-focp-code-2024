#!/usr/bin/env python3

import sys


KEY_FILE = 'key.txt'


def generate_key():
    from random import shuffle
    from string import ascii_letters as letters

    letter_list = list(letters)
    shuffle(letter_list)

    new_key = ''.join(letter_list)

    return new_key


def save_key(key_to_save, keyfile=KEY_FILE):
    with open(keyfile, 'w') as out_file:
        out_file.write(key_to_save + '\n')


def encode_message(this_key, this_message):
    from string import ascii_letters as letters

    encoded_message = ''
    for character in this_message:
        if character in letters:
            position = letters.find(character)
            encoded_message += this_key[position]
        else:
            encoded_message += character

    return encoded_message


def save_message(message_to_save, original_file_name):
    out_file = f'{original_file_name}.encoded'

    with open(out_file, 'w') as of:
        of.write(message_to_save)


if __name__ == '__main__':

    try:
        with open(sys.argv[1], 'r') as message_file:
            message = message_file.read()

    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}".')
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')

    else:

        key = generate_key()
        save_key(key)

        new_message = encode_message(key, message)
        save_message(new_message, sys.argv[1])
