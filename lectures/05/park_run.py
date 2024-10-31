#!/usr/bin/env python3

def time_as_string(seconds):
    mins = seconds // 60
    secs = seconds % 60

    return f'{mins} minute{"" if mins == 1 else "s"}, {secs} second{"" if secs == 1 else "s"}'


def parse_line(data_line):
    this_runner, this_time = data_line.split('::')

    if not this_runner:
        raise ValueError('Invalid data on line. Probably missing runner number')

    return this_runner, int(this_time)


def print_statistics(final_times, best_runner):

    from statistics import mean

    print()
    print(f'Number of Runners: {len(final_times)}.')
    print()
    print(f'Fastest Time:      {time_as_string(min(final_times))}.')
    print(f'Slowest Time:      {time_as_string(max(final_times))}.')
    print(f'Average Time:      {time_as_string(round(mean(final_times)))}.')
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
            try:
                runner, current_time = parse_line(next_line)

                if times:
                    top_runner = runner if current_time < min(times) else top_runner
                else:
                    top_runner = runner

                times.append(current_time)
            except ValueError:
                print('Invalid data. Will ignore.')

    if times:
        print_statistics(times, top_runner)
    else:
        print('No data entered. Nothing to do.')
