#!/usr/bin/env python3


import sys


def clean_string(s):
    return ''.join([c.lower() for c in s if c.isalpha()])


def create_dictionary():
    from string import ascii_lowercase as letters

    the_dict = {}
    for letter in letters:
        the_dict[letter] = 0

    return the_dict


def make_counts(the_dict, the_letters):
    for letter in the_letters:
        the_dict[letter] += 1

    return the_dict


def top_letter_count(the_dict):
    return max(the_dict.values())


def find_top_letters(the_dict):
    from string import ascii_lowercase as letters

    top_count = top_letter_count(the_dict)

    letter_list = [letter for letter in letters if the_dict[letter] == top_count]
    letter_list.sort()

    return ''.join(letter_list)


if __name__ == '__main__':

    letter_frequencies = create_dictionary()

    try:
        with open(sys.argv[1], 'r') as in_file:
            raw_file = in_file.read()

    except FileNotFoundError:
        print(f'{sys.argv[0][2:]}: Cannot open "{sys.argv[1]}".')
    except IndexError:
        print(f'{sys.argv[0][2:]}: Missing required argument.')

    else:
        letter_string = clean_string(raw_file)

        if letter_string:
            letter_frequencies = make_counts(letter_frequencies, letter_string)

            top_letters = find_top_letters(letter_frequencies)

            if len(top_letters) == 1:
                print(f'Unique Most Common Letter: {top_letters}.')
            else:
                print(f'Multiple Most Common Letter: {top_letters}.')

        else:
            print('Nothing to count. Probably an empty file.')
