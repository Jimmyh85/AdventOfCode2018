import aoc_helper
from collections import defaultdict

data = aoc_helper.get_input("7", "plain")
input = [int(num) for num in data.split(",")]

pos_count = defaultdict(int)
for pos in input:
    pos_count[pos] += 1

# print(pos_count)
# print(input)

# print(len(input))

opt = 10000000
for i in range(min(input), max(input)):
    # calculate cost 
    cost = 0
    for key,value in pos_count.items():
        cost += abs(key - i) * value
    if cost < opt:
        opt = cost

print("Part 1", opt)

def cost_p2(num, level):
    distance = abs(num - level) 
    cost = distance * (distance + 1) // 2
    return cost 

opt = 1000000000
for i in range(min(input), max(input)):
    # calculate cost 
    cost = 0
    for key,value in pos_count.items():
        cost += cost_p2(key, i) * value
    if cost < opt:
        opt = cost

print("Part 2", opt)
