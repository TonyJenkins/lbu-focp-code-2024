#!/usr/bin/env python3


def clean_string(s):
    return ''.join([c for c in s if c.isalpha()])


def get_surname(data_line):
    return clean_string(data_line[9:].split(',')[0].lower())


def get_initials(data_line):
    name = data_line[9:].split(',')[1].strip()

    return '.'.join([c.lower() for c in name if c.isupper()])


def four_random_digits():
    from random import choice
    from string import digits

    return ''.join([choice(digits) for _ in range(4)])


def build_email(data_line, domain="poppleton.ac.uk"):
    initials = get_initials(data_line)
    surname = get_surname(data_line)

    return f'{initials}.{surname}{four_random_digits()}@{domain}'


if __name__ == '__main__':

    try:
        student_line = input('Enter student data: ')

        print(build_email(student_line))

    except IndexError:
        print('Incorrect format entered.')
