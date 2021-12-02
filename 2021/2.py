import aoc_helper

directions_data = aoc_helper.get_input("2", "string")

# Part 1
x = 0
y = 0
for line in directions_data:
    v_x = 0
    v_y = 0
    (direction, steps) = line.split(" ")
    assert direction in ["forward", "down", "up"]
    if direction == "forward":
        v_x = int(steps)
    if direction == "down":
        v_y = int(steps) 
    if direction == "up":
        v_y = int(steps) * -1
    x = x + v_x
    y = y + v_y
    # print(direction, steps, x, y)

# print(x,y)
print("Part 1", x*y)

# Part 2
x = y = aim = 0

for line in directions_data:
    v_x = v_y = v_aim = 0
    (direction, steps) = line.split(" ")
    assert direction in ["forward", "down", "up"]
    if direction == "forward":
        v_x = int(steps)
        v_y = int(steps) * aim
    if direction == "down":
        v_aim = int(steps) 
    if direction == "up":
        v_aim = int(steps) * -1
    # print(x, y)
    x = x + v_x
    y = y + v_y
    aim = aim + v_aim
    # print(direction, steps, x, y, aim)

print("Part 2", x*y)
