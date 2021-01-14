import re


def get_input(filename, mode='numbers'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())
    return data


data = get_input('input5', 'string')

# Definitions
F = '0'
B = '1'

R = '1'
L = '0'


def transform_to_binary(string):
    res = ''
    res = string.replace('F', F)
    res = res.replace('B', B)

    return res


def transform_to_binary_2(string):
    res = ''
    res = string.replace('R', R)
    res = res.replace('L', L)

    return res


def calculate_seat_id(seat_code):
    row = int(transform_to_binary(line[:7]), 2)
    column = int(transform_to_binary_2(line[-3:]), 2)
    return row * 8 + column


def calc_seat_id(row, col):
    return row * 8 + col


def get_seat(seat_code):
    row = int(transform_to_binary(line[:7]), 2)
    column = int(transform_to_binary_2(line[-3:]), 2)
    return row, column


# data = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']

max_id = 0

for line in data:
    seat_id = calculate_seat_id(line)
    if (seat_id > max_id):
        max_id = seat_id

print('Part1:', max_id)

# Part 2
seating_plan = dict()

for i in range(128):
    seating_plan[i] = [j for j in range(8)]

# print(seating_plan)
ids = []

for line in data:
    (row, column) = get_seat(line)
    seating_plan[row].remove(column)
    ids.append(calculate_seat_id(line))

ids.sort()
# print(ids)

print(seating_plan)

candidates = [(key, value) for key, value in seating_plan.items() if len(value) == 1]
print(candidates)
for (row, cols) in candidates:
    for col in cols:
        print(calc_seat_id(row, col))
