import itertools
from functools import reduce

def get_input(mode='numbers'):
    with open('input1', 'r') as f:
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())    
    return data

print(get_input())            

data = get_input()

# Part 1 
# num_tuples = 2

# Part 2
num_tuples = 3
target_sum = 2020

for items in itertools.combinations(data,num_tuples):
    if (sum(items) == target_sum):
        print(items)
        print(reduce(lambda x, y: x * y, items))
