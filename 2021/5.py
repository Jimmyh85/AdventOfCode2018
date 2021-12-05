import aoc_helper
from collections import defaultdict 

data = aoc_helper.get_input("5", "string")

paths = defaultdict(int)

for line in data:
    points = line.split(" -> ")
    x1, y1 = points[0].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2, y2 = points[1].split(",")
    x2 = int(x2)
    y2 = int(y2)
    # only vertical and horizontal lines
    if x1 != x2 and y1 != y2:
        continue
    v_x = x2 - x1
    if v_x > 0:
        v_x = 1
    if v_x < 0:
        v_x = -1

    v_y = y2 - y1
    if v_y > 0:
        v_y = 1
    if v_y < 0:
        v_y = -1    
    paths[(x1,y1)] += 1    
    while not (x1 == x2 and y1 == y2):
        x1 += v_x
        y1 += v_y
        paths[(x1,y1)] += 1

# Part 1
print("Part 1", len([point for point in paths.values() if point > 1]))

# Part 2
paths = defaultdict(int)
for line in data:
    points = line.split(" -> ")
    x1, y1 = points[0].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2, y2 = points[1].split(",")
    x2 = int(x2)
    y2 = int(y2)
   
    v_x = x2 - x1
    if v_x > 0:
        v_x = 1
    if v_x < 0:
        v_x = -1

    v_y = y2 - y1
    if v_y > 0:
        v_y = 1
    if v_y < 0:
        v_y = -1    
    paths[(x1,y1)] += 1    
    while not (x1 == x2 and y1 == y2):
        x1 += v_x
        y1 += v_y
        paths[(x1,y1)] += 1

# Part 1
print("Part 2", len([point for point in paths.values() if point > 1]))

    

