#!/usr/bin/env python3

from statistics import mean

if __name__ == '__main__':

    NUMBER_OF_MARKS = 6

    mark_list = []

    for counter in range(NUMBER_OF_MARKS):
        while True:
            try:
                mark = int(input('Enter Next Grade: '))
                if 0 >= mark >= 100:
                    mark_list.append(mark)
                    break
            except ValueError:
                print('Please enter an integer between 0 and 100')

    max_mark = max(mark_list)
    min_mark = min(mark_list)
    avg_mark = mean(mark_list)

    print()
    print(f'Max Mark:     {max_mark}')
    print(f'Min Mark:     {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')
