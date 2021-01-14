import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input14', 'string')
print(data)


def apply_mask(mask, value):
    new_value = 0
    print(mask, value)
    for i, bit in enumerate(reversed(mask)):
        vbit = value & (2**i)
        if bit == 'X':
            new_value += vbit
        if bit == '1':
            new_value += 2**i

    return new_value


mem = {}
mask = ''
for line in data:
    if line.startswith('mask'):
        mask = line.split()[-1]
        print(mask)
    else:
        value = int(line.split()[-1])
        mem_idx = line.split()[0].split('[')[1][:-1]
#:        print(mem_idx, value)
        new_value = apply_mask(mask, value)
        print(new_value)
        mem[mem_idx] = new_value

sum = 0
for value in mem.values():
    sum += int(value)

print(sum)
