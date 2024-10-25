#!/usr/bin/env python3

import random


def make_4_digit_code():
    code = ['_'] * 4
    numbers = ['1', '2', '3', '4', '5', '6']
    random.shuffle(numbers)
    code[0] = numbers.pop()
    code[1] = numbers.pop()
    code[2] = numbers.pop()
    code[3] = numbers.pop()
    return code


def how_many_correct(guess, code):
    correct = 0

    for i in range(4):
        if (guess[i] == code[i]): correct = correct + 1

    return correct


def how_many_part_correct(guess, code):
    part_correct = 0

    if guess[0] == code[1] or guess[0] == code[2] or guess[0] == code[3]: part_correct = part_correct + 1
    if guess[1] == code[0] or guess[1] == code[2] or guess[1] == code[3]: part_correct = part_correct + 1
    if guess[2] == code[0] or guess[2] == code[1] or guess[2] == code[3]: part_correct = part_correct + 1
    if guess[3] == code[0] or guess[3] == code[1] or guess[3] == code[2]: part_correct = part_correct + 1

    return part_correct


if __name__ == '__main__':
    print('Game Starting. Can you crack the code? \nYou have 10 Turns. \n')

    code_cracked = False
    turn = 1
    correct = 0
    part_correct = 0

    code = make_4_digit_code()

    while code_cracked == False:
        print('This is turn ' + str(turn) + '\n')
        guess = input('Please enter your 4 digit code: ')

        correct = how_many_correct(guess, code)
        part_correct = how_many_part_correct(guess, code)

        turn = turn + 1
        print('You have ' + str(correct) + ' in the right place and ' + str(part_correct) + ' in the wrong place \n')

        if correct == 4: code_cracked = True
        if turn == 11: break

    if code_cracked == True:
        print('Well Done')
    else:
        print('Loser: Code was' + str(code))
