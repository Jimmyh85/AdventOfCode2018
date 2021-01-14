
import aoc_helper
from functools import reduce
from itertools import product
from collections import defaultdict

data = aoc_helper.get_input('input17', 'string')
print(data)


def get_neighbors(*position):
    for diff in product([-1, 0, 1], repeat=len(position)):
        # Skip position itself
        if diff == (0,) * len(position):
            continue
        neighbor = tuple(pos + diff[i] for i, pos in enumerate(position))
        yield neighbor
        # print('D:', diff)
        # print('N:', neighbor)


def play_game(initial_state, dimensions, rounds):
    space = defaultdict(lambda: '.')
    padding = (0,) * (dimensions - 2)
    print(padding)
    for x, line in enumerate(initial_state):
        for y, state in enumerate(line):
            cube = (x, y) + padding
            space[cube] = state

    # print(space)
    for _ in range(rounds):
        cube_to_active_count = defaultdict(int)

        for cube in space:
            if space[cube] == '.':
                continue
            for n in get_neighbors(*cube):
                # print(n != cube and space[cube] == '#')
                # cube_to_active_count[n] += n != cube and space[cube] == '#'
                if space[cube] == '#':
                    cube_to_active_count[n] += 1
                else:
                    cube_to_active_count[n] += 0
                # cube_to_active_count[n] += space[cube] == '#'
            # Add the cube itself
            cube_to_active_count[cube] += 0
            # print(cube_to_active_count)
        for n, count in cube_to_active_count.items():
            if space[n] == '#':
                if count in [2, 3]:
                    space[n] = '#'
                else:
                    space[n] = '.'
            elif space[n] == '.':
                if count == 3:
                    space[n] = '#'

    return sum(state == '#' for state in space.values())


# print(get_neighbors(1, 1, 1))
print('Part 1:', play_game(data, 3, 6))
print('Part 2:', play_game(data, 4, 6))
