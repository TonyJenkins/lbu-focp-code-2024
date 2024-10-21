#!/usr/bin/env python3

from statistics import mean, median


if __name__ == '__main__':

    marks_list = []

    while True:
        mark = input('Enter Mark: ')

        if not mark:
            break
        else:
            try:
                if 0 <= int(mark) <= 100:
                    marks_list.append(int(mark))
                else:
                    print('Invalid Mark')

            except ValueError:
                print('Invalid Mark')

    if marks_list:
        max_mark = max(marks_list)
        min_mark = min(marks_list)
        average = mean(marks_list)

        print()
        print(f'The average is {average:.2f}.')
        print(f'The maximum mark is {max_mark}.')
        print(f'The minimum mark is {min_mark}.')
        print(f'The median mark is {median(marks_list):.2f}.')
    else:
        print('No marks entered. Nothing to do.')
