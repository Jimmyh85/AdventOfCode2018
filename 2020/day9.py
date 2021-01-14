import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input9')

# print(data)

# Definitions
PREAMBLE_SIZE = 25

def is_valid_number(number, preamble):
    numbers = set(preamble)
    for num in preamble:
        if number - num in numbers:
            return True
    return False

part1_idx = 0

for i in range(len(data) - PREAMBLE_SIZE):
    check_number = data[i+PREAMBLE_SIZE]
    preamble = data[:i+PREAMBLE_SIZE]
    if not is_valid_number(check_number, preamble):
        part1_idx = i + PREAMBLE_SIZE
        print("Part1:", data[part1_idx])
        break
# Part 2:
result = data[part1_idx]
found = False

for set_length in range(2, part1_idx + 1):
    if found == True:
        break
    for i in range(part1_idx):
        test_set = data[i:i+set_length]
        test_set_sum = reduce(lambda x, y : x + y, test_set)
        #print(test_set, test_set_sum)
        if test_set_sum == result:
            print("Part2:", max(test_set) + min(test_set))
            found = True
            break
        if test_set_sum > result:
            break