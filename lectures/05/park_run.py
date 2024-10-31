#!/usr/bin/env python3


def parse_line(data_line):
    this_runner, this_time = data_line.split('::')

    return this_runner, int(this_time)


def print_statistics(final_times, best_runner):

    from statistics import mean

    print()
    print(f'Number of Runners: {len(final_times)}.')
    print()
    print(f'Fastest Time:      {min(final_times)}.')
    print(f'Slowest Time:      {max(final_times)}.')
    print(f'Average Time:      {round(mean(final_times))}.')
    print()
    print(f'Fastest Time by Runner #{best_runner}.')
    print()


if __name__ == '__main__':

    times = []
    top_runner = ''

    while True:

        next_line = input('> ')

        if next_line == 'END':
            break
        else:
            runner, current_time = parse_line(next_line)

            if times:
                top_runner = runner if current_time < min(times) else top_runner
            else:
                top_runner = runner

            times.append(current_time)

    if times:
        print_statistics(times, top_runner)
    else:
        print('No data entered. Nothing to do.')
