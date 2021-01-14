import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input12','string')

# print(data)

def parse_line(line):
    instruction = line[0]
    num = int(line[1:])
    return instruction, num


directions = {
    0: (0,1),       # North
    90: (1,0),      # East
    -270: (1,0),      # East
    180: (0,-1),    # South
    -180: (0,-1),    # South
    270: (-1,0),     # West
    -90: (-1,0)     # West
}

x = 0
y = 0

# Part 2
wx = 10
wy = 1

curr_direction = 90

# Part 1
for line in data:
    instruction, num = parse_line(line)
    if instruction == 'N':
        y += num
    elif instruction == 'E':
        x += num
    elif instruction == 'S':
        y -= num    
    elif instruction == 'W':
        x -= num
    elif instruction == 'L':
        curr_direction = (curr_direction - num) % 360
    elif instruction == 'R':
        curr_direction = (curr_direction + num) % 360
    elif instruction == 'F':
        (vx,vy) = directions[curr_direction]
        x += num * vx
        y += num * vy

print(x, y, abs(x)+abs(y))                       


# Part 2
x = 0
y = 0

wx = 10
wy = 1

curr_direction = 90

def rotate_clockwise_90(x,y):
    return (y,-x)

def rotate_clockwise_180(x,y):
    return (-x,-y)

def rotate_clockwise_270(x,y):
    return (-y ,x)

for line in data:
    instruction, num = parse_line(line)
    if instruction == 'N':
        wy += num
    elif instruction == 'E':
        wx += num
    elif instruction == 'S':
        wy -= num    
    elif instruction == 'W':
        wx -= num
    elif instruction == 'L':
        for i in range(num // 90):
            wx, wy = -wy, wx
    elif instruction == 'R':
        for i in range(num // 90):
            wx, wy = wy, -wx
    elif instruction == 'F':
        # (vx,vy) = directions[curr_direction]
        x += num * wx
        y += num * wy

print(x, y, abs(x)+abs(y))
