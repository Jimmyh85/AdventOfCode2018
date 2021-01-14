from functools import reduce

def get_input(filename, mode='numbers'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())    
    return data

data = get_input('input3','string')

# print(data)


# Definitions
map_width = len(data[0])
map_height = len(data)
TREE = '#'
SQUARE = '.'

# Starting position
x = 0
y = 0

# Slopes defined by its velocity (vx, vy)
# Part 1
#slopes = [(3,1)]

#Part 2
slopes = [(1,1), (3,1), (5,1),(7,1),(1,2)]

print(map_width)
print(len(data))

trees = []
squares = []

for slope in slopes:
    (vx, vy) = slope
    x = 0
    y = 0
    seen_trees = 0
    seen_squares = 0 
    while y < map_height - 1:
        x = (x + vx) % map_width
        y += vy
        # print(x, y)
        pos = data[y][x]
        if (pos == TREE):
            seen_trees += 1
        if (pos == SQUARE):
            seen_squares += 1
    trees.append(seen_trees)
    squares.append(seen_squares)        

print(trees)                
print(reduce(lambda x, y: x * y, trees))