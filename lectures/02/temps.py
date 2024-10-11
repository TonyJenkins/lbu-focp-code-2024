#!/usr/bin/env python3

if __name__ == "__main__":

    try:
        temp_1 = float(input('Enter 8am Temp:  ')[:-1])
        temp_2 = float(input('Enter 11am Temp: ')[:-1])
        temp_3 = float(input('Enter 2pm Temp:  ')[:-1])
        temp_4 = float(input('Enter 5pm Temp:  ')[:-1])
        temp_5 = float(input('Enter 8pm Temp:  ')[:-1])

    except ValueError:
        print('Invalid input')

    else:
        avg_temp = (temp_1 + temp_2 + temp_3 + temp_4 + temp_5) / 5.0
        max_temp = max(temp_1, temp_2, temp_3, temp_4, temp_5)
        min_temp = min(temp_1, temp_2, temp_3, temp_4, temp_5)

        print()
        print(f'Average Temp: {avg_temp:.2f}C')
        print(f'Max Temp:     {max_temp:.2f}C')
        print(f'Min Temp:     {min_temp:.2f}C')
        print(f'Range:        {max_temp - min_temp:.2f}C')
