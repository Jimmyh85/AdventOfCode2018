
import re
from collections import defaultdict


def parse_time(line):
    time = line.split("]")
    time = time[0]
    time = time[-2:]
    return int(time)


def solve_day4(shifts):

    guard_pattern = re.compile(r"Guard #(\d+) begins shift")

    guard_times = defaultdict(int)
    guard_minute_times = defaultdict(int)

    for line in shifts:
        match = re.search(guard_pattern, line)
        if match:
            guard = int(match.group(1))
        if 'falls asleep' in line:
            start_time = parse_time(line)
        if 'wakes up' in line:
            end_time = parse_time(line)
            for i in range(start_time, end_time):
                guard_times[guard] += 1
                guard_minute_times[(guard, i)] += 1

    # Get the guard with the maximum sleep minutes
    guard_max = max(guard_times.keys(), key=(lambda x: guard_times[x]))
    # Given the guard that slept the most minutes, calculate on which minute he slept the most
    guard_minute_max = max([k for k in guard_minute_times.keys() if guard_max in k],
                           key=(lambda x: guard_minute_times[x]))
    # Get the minute that one guard slept the most
    minute_max = max(guard_minute_times.keys(), key=(
        lambda x: guard_minute_times[x]))

    # return a the solution tuple for part1 and part2
    return guard_minute_max, minute_max


def part1(shifts):
    # part1 receives the tuple with ('guard','max_minute_of_guard')
    result = solve_day4(shifts)[0]
    return result[0] * result[1]


def part2(shifts):
    # part2 receives the tuple with ('guard, 'max_minute_overall')
    result = solve_day4(shifts)[1]
    return result[0] * result[1]


with open('input.txt', 'r') as f:
    shifts = f.readlines()

shifts.sort()
print(part1(shifts))
print(part2(shifts))
