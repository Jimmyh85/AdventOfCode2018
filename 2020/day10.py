import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input10')

#print(data)

jolts = data

device_builtin_joltage = max(jolts) + 3
charging_outlet_joltage = 0

jolts.append(charging_outlet_joltage)
jolts.append(device_builtin_joltage)

jolts.sort()
print(jolts)

one_jolt_difference = 0
three_jolt_difference = 0

for i in range(len(jolts)-1):
    diff = jolts[i+1] - jolts[i]
    if diff == 1:
        one_jolt_difference += 1
    elif diff == 3:
        three_jolt_difference += 1
    else:
        print(diff)

print(one_jolt_difference * three_jolt_difference)        

# Part 2
cache = {}

def count_arrangements(pos):
    if pos == len(jolts) - 1:
        return 1
    if pos in cache:
        return cache[pos]
    ans = 0
    for j in range(pos+1, min(pos+4, len(jolts))):
        if jolts[j] - jolts[pos] <= 3:
            ans += count_arrangements(j)
    cache[pos] = ans
    return ans               

print(count_arrangements(0))

