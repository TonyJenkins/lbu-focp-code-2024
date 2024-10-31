#!/usr/bin/env python3


def parse_line(data_line):
    this_runner, this_time = data_line.split('::')

    return this_runner, int(this_time)


def print_statistics(final_times):

    from statistics import mean

    print()
    print(f'Number of Runners: {len(final_times)}.')
    print(f'Fastest Time:      {min(final_times)}.')
    print(f'Slowest Time:      {max(final_times)}.')
    print(f'Average Time:      {round(mean(final_times))}.')


if __name__ == '__main__':

    times = []

    while True:

        next_line = input('> ')

        if next_line == 'END':
            break
        else:
            runner, current_time = parse_line(next_line)
            times.append(current_time)

    print_statistics(times)
