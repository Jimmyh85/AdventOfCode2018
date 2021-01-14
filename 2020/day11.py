import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input11','string')



width = len(data[0])
height = len(data)

for i in range(height):
    print(i, data[i])

# Definitions
OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'

def get_adjacent_fields(map, pos=(0, 0)):
    width = len(map[0])
    height = len(map)

    fields = []
    for row in [-1, 0, 1]:
        for column in [-1, 0, 1]:
            if row == column == 0:
                continue
            # check valid index
            if 0 <= pos[1] + row < width and 0 <= pos[0] + column < height:
                # print((node[0]+i, node[1]+j))
                fields.append((pos[0]+column, pos[1]+row))
    return fields

def get_adjacent_fields_2(map, pos=(0, 0)):
    R = len(map)
    C = len(map[0])
    r = pos[0]
    c = pos[1]
    fields = []
    for vr in [-1, 0, 1]:
        for vc in [-1, 0, 1]:
            if vr == vc == 0:
                continue
            # check valid index
            rr = r + vr
            cc = c + vc
            while 0 <= rr < R and 0 <= cc < C and map[rr][cc] == FLOOR:
                rr += vr
                cc += vc
            if 0 <= rr < R and 0 <= cc < C:
                # print((node[0]+i, node[1]+j))
                fields.append((rr, cc))
    return fields

def get_adjacent_fields_part2(map, pos=(0, 0)):
    width = len(map[0])
    height = len(map)

    x = pos[1]
    y = pos[0]

    fields = []
    #LEFT
    for row in range(x):
        new_x = x - row - 1
        if map[y][new_x] != FLOOR:
            fields.append((y, new_x))
            break
    #RIGHT
    for row in range(width - x - 1):
        new_x = x + row + 1
        if map[y][new_x] != FLOOR:
            fields.append((y, new_x))
            break
    #TOP
    for col in range(y):
        new_y = y - col - 1
        if map[new_y][x] != FLOOR:
            fields.append((new_y, x))
            break
    #BUTTOM
    for col in range(height - y -1):
        new_y = y + col + 1
        if map[new_y][x] != FLOOR:
            fields.append((new_y, x))
            break
    #LEFT-TOP
    max_diagonale_length = min(y, x)
    for i in range(max_diagonale_length):
        new_x = x - i - 1
        new_y = y - i - 1
        if map[new_y][new_x] != FLOOR:
            fields.append((new_y, new_x))
            break
    #RIGHT-TOP
    max_diagonale_length = min(y, width - x -1)
    for i in range(max_diagonale_length):
        new_x = x + i + 1
        new_y = y - i - 1
        if map[new_y][new_x] != FLOOR:
            fields.append((new_y, new_x))
            break

    #LEFT-BUTTOM
    max_diagonale_length = min(x, height - y -1)
    for i in range(max_diagonale_length):
        new_x = x - i - 1
        new_y = y + i + 1
        if map[new_y][new_x] != FLOOR:
            fields.append((new_y, new_x))
            break

    #RIGHT-BUTTOM
    max_diagonale_length = min(height - y -1 , width - x -1)
    for i in range(max_diagonale_length):
        new_x = x + i + 1
        new_y = y + i + 1
        if map[new_y][new_x] != FLOOR:
            fields.append((new_y, new_x))
            break

    return fields

def get_items(map, positions):
    items = []
    for pos in positions:
        items.append(map[pos[0]][pos[1]])
    return items    

def apply_rules(map, pos):
    curr = map[pos[0]][pos[1]]
    adjacent = get_items(map, get_adjacent_fields(map, pos))
    if curr == EMPTY and adjacent.count(OCCUPIED) == 0:
        return OCCUPIED
    if curr == OCCUPIED and adjacent.count(OCCUPIED) >= 4:
        return EMPTY
    
    return curr        

def apply_rules_part2(map, pos):
    curr = map[pos[0]][pos[1]]
    adjacent = get_items(map, get_adjacent_fields_2(map, pos))
    if curr == EMPTY and adjacent.count(OCCUPIED) == 0:
        return OCCUPIED
    if curr == OCCUPIED and adjacent.count(OCCUPIED) >= 5:
        return EMPTY
    
    return curr        

def next_generation(map):
    width = len(map[0])
    height = len(map)
    new_map = []
    for i in range(height):
        new_line = ''
        for j in range(width):
            new_line += apply_rules(map,(i,j))
        new_map.append(new_line)
    return new_map        

def next_generation_part2(map):
    width = len(map[0])
    height = len(map)
    new_map = []
    for i in range(height):
        new_line = ''
        for j in range(width):
            new_line += apply_rules_part2(map,(i,j))
        new_map.append(new_line)
    return new_map

def count_occupied_seats(map):
    seats = 0
    for line in map:
        seats += line.count(OCCUPIED)
    
    return seats    

t = get_adjacent_fields(data,(92,0))
print(t)
print(get_items(data, t)) 

while True:
    curr_seats = count_occupied_seats(data)
    data = next_generation_part2(data)    
    next_seats = count_occupied_seats(data)
    print(curr_seats)
    if curr_seats == next_seats:
        print(curr_seats)
        break

