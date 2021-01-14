import math
import aoc_helper
import re
from collections import defaultdict

data = aoc_helper.get_input("input24", "string")
# data = aoc_helper.get_input("input24_sample", "string")
# print(data)

black_tiles = set()

for line in data:
    (x, y, z) = (0, 0, 0)
    while line:
        # Start at the center point
        if line.startswith("e"):
            x += 1
            y -= 1
            line = line[1:]
        elif line.startswith("se"):
            z += 1
            y -= 1
            line = line[2:]
        elif line.startswith("sw"):
            x -= 1
            z += 1
            line = line[2:]
        elif line.startswith("w"):
            x -= 1
            y += 1
            line = line[1:]
        elif line.startswith("nw"):
            y += 1
            z -= 1
            line = line[2:]
        elif line.startswith("ne"):
            x += 1
            z -= 1
            line = line[2:]
        else:
            assert False

    # Flip to white if tile is already black
    # print(x, y, z)
    if (x, y, z) in black_tiles:
        black_tiles.discard((x, y, z))
    else:
        black_tiles.add((x, y, z))

# print(black_tiles)
print("Part 1:", len(black_tiles))

# Part 2
days = 100

for _ in range(days):
    black_tiles_next_generation = set()
    tiles_to_check = set()
    for tile in black_tiles:
        tiles_to_check.add(tile)
        for (vx, vy, vz) in [
            (1, -1, 0),
            (0, -1, 1),
            (-1, 0, 1),
            (-1, 1, 0),
            (0, 1, -1),
            (1, 0, -1),
        ]:
            x, y, z = tile
            tiles_to_check.add((x + vx, y + vy, z + vz))
    for tile in tiles_to_check:
        black_neighbors = 0
        for (vx, vy, vz) in [
            (1, -1, 0),
            (0, -1, 1),
            (-1, 0, 1),
            (-1, 1, 0),
            (0, 1, -1),
            (1, 0, -1),
        ]:
            x, y, z = tile
            if (x + vx, y + vy, z + vz) in black_tiles:
                black_neighbors += 1
        # Negate rule for black tiles to figure out which ones to take over to the next generation
        if tile in black_tiles and not (black_neighbors == 0 or black_neighbors > 2):
            black_tiles_next_generation.add(tile)
        # Rules for white tiles
        if tile not in black_tiles and (black_neighbors == 2):
            black_tiles_next_generation.add(tile)
    black_tiles = black_tiles_next_generation
    # print(len(black_tiles))
print("Part 2:", len(black_tiles))
