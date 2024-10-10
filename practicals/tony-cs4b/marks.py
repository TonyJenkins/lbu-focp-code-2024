#!/usr/bin/env python3

from statistics import mean


if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    marks_list = []

    for counter in range(NUMBER_OF_MARKS):
        while True:
            try:
                mark = int(input('Enter Mark: '))
                if 0 <= mark <= 100:
                    marks_list.append(mark)
                    break
                else:
                    print('Invalid Mark')
            except ValueError:
                print('Invalid Mark')

    max_mark = max(marks_list)
    min_mark = min(marks_list)
    average = mean(marks_list)

    print()
    print(f'The average is {average:.2f}.')
    print(f'The maximum mark is {max_mark}.')
    print(f'The minimum mark is {min_mark}.')
