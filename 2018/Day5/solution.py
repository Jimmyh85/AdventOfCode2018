
import sys


def doesReact(polymer_tuple):

    if polymer_tuple[0] == polymer_tuple[1]:
        return False
    elif polymer_tuple[0].upper() == polymer_tuple[1] or polymer_tuple[0].lower() == polymer_tuple[1]:
        return True
    else:
        return False


def part1(polymer):
    remaining = polymer
    index = 0
    while remaining:

        current_pair = remaining[index:index+2]
        if(len(current_pair) < 2):  # if we are at the end and cannot find a new pair anymore we exit the loop
            break

        if doesReact(current_pair):
            remaining = remaining[0:index] + remaining[index+2:]
            if index > 0:
                index -= 1
        else:
            index += 1

    return remaining


def part2(polymer):
    min = (sys.maxsize, '')
    for i in range(ord('a'), ord('z')+1):
        fixed_polymer = polymer.replace(chr(i), "").replace(chr(i).upper(), "")
        fixed_length = len(part1(fixed_polymer))
        if fixed_length < int(min[0]):
            min = (fixed_length, chr(i))

    return min


with open('input.txt', 'r') as f:
    polymer = f.read().strip()

print(len(part1(polymer)))
print(part2(polymer))
