#!/usr/bin/env python3


import sys


def banner(s):
    print()
    print('=' * len(s))
    print(s)
    print('=' * len(s))
    print()


def parse_dog_line(line):
    return line.split(',')[0], float(line.split(',')[1])


def update_times(dog_dict, new_name, new_time):
    if new_name in dog_dict:
        dog_dict[new_name].append(new_time)
    else:
        dog_dict[new_name] = [new_time,]


def print_averages(dog_dict):
    from statistics import mean

    for dog in dog_dict:
        print(f'{dog:12}: {mean(dog_dict[dog]):.2f}')


def get_fastest_average(dog_dict):
    from statistics import mean

    return min([mean(dog_dict[dog]) for dog in dog_dict])


def get_fastest_dog(dog_dict):
    from statistics import mean

    fastest_average = get_fastest_average(dog_dict)

    for dog in dog_dict:
        if mean(dog_dict[dog]) == fastest_average:
            return dog


if __name__ == '__main__':

    dog_details = {}

    try:
        with open(sys.argv[1], 'r') as dog_file:
            for dog_line in dog_file:
                try:
                    name, time = parse_dog_line(dog_line)
                    update_times(dog_details, name, time)
                except IndexError:
                    print(f'Error found on line "{dog_line.strip()}". Will ignore.')

    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open "{sys.argv[1]}".')
    except IndexError:
        print(f'{sys.argv[0]}: Missing required argument.')

    else:
        if dog_details:
            banner('Dog Leaderboard')
            print_averages(dog_details)
            print()
            print(f'Fastest Dog is {get_fastest_dog(dog_details)}')
        else:
            print(f'{sys.argv[0]}: Corrupt Data file?')
