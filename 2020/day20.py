import math
import aoc_helper
import regex as re
import numpy as np

data = aoc_helper.get_input("input20", "plain").strip()
# print(data)

# print(data.split("\n\n"))


def rotate90degrees(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


def flip_horizontally(array_2d):
    result = []
    for line in array_2d:
        result.append(line[::-1])
    return result


def flip_vertically(array_2d):
    # return rotate90degrees(rotate90degrees(rotate90degrees(flip_horizontally(rotate90degrees(array_2d)))))
    list_of_tuples = zip(*array_2d)
    list_of_tuples = [list(elem[::-1]) for elem in list_of_tuples]
    return [list(elem) for elem in zip(*list_of_tuples)]


class Tile:
    def __init__(self, data):
        self.pixel = []
        for line in data.split("\n"):
            m = re.match("Tile (\d+)", line)
            if m != None:
                self.tile_id = int(m.group(1))
            else:
                # print(line)
                self.pixel.append(list(line))

    def get_transformation(self):
        rotate90 = rotate90degrees(self.pixel)
        rotate180 = rotate90degrees(rotate90)
        rotate270 = rotate90degrees(rotate180)

        transformations = [
            self.pixel,
            rotate90,
            rotate180,
            rotate270,
            flip_horizontally(self.pixel),
            flip_horizontally(rotate90),
            flip_horizontally(rotate180),
            flip_horizontally(rotate270),
        ]
        return transformations

    @staticmethod
    def pretty_print_tile(tile):
        return "\n".join("".join(map(str, sl)) for sl in tile)

    def __repr__(self):
        return str(self.tile_id) + "\n" + self.pretty_print_tile(self.pixel)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.tile_id == other.tile_id
        return False


tiles = []
for tiles_data in data.split("\n\n"):
    tiles.append(Tile(tiles_data))

tile_width = 10
length = len(tiles)
width = height = int(math.sqrt(length))
# print(length, width, height)

# Backtracking algorithm


def solve(values, safe_up_to, size):
    """Finds a solution to a backtracking problem.

    values     -- a sequence of values to try, in order. For a map coloring
                  problem, this may be a list of colors, such as ['red',
                  'green', 'yellow', 'purple']
    safe_up_to -- a function with two arguments, solution and position, that
                  returns whether the values assigned to slots 0..pos in
                  the solution list, satisfy the problem constraints.
    size       -- the total number of “slots” you are trying to fill

    Return the solution as a list of values.
    """
    solution = [None] * size
    remaining = values.copy()

    def extend_solution(position, remaining):
        for tile in remaining:
            # print('Trying ', tile.tile_id)
            for tile_transform in tile.get_transformation():
                solution[position] = (tile_transform, tile.tile_id)
                if safe_up_to(solution, position):
                    remain = remaining.copy()
                    remain.remove(tile)
                    if position >= size - 1 or extend_solution(position + 1, remain):
                        return solution
        return None

    return extend_solution(0, remaining)


# Check constraints => here: borders must match


def matching_borders(board, position):
    row = position // width
    column = position % width
    # print(position, row, column)

    tile = board[position][0]
    # print(tile)
    # check matching left borders
    if column != 0:
        # get the tile to compare against
        other_tile = board[position - 1][0]
        for i in range(tile_width):
            if other_tile[i][tile_width - 1] != tile[i][0]:
                return False

    # check matching top borders
    if row != 0:
        # get the tile to compare against
        other_tile = board[position - width][0]
        for i in range(tile_width):
            if other_tile[tile_width - 1][i] != tile[0][i]:
                return False

    # When all checks have succeeded, return True
    return True


# print(length)
solution = solve(tiles, matching_borders, length)
# print(solution)
# print(Tile.pretty_print_tile(solution[0][0]))
# print("---")
# print(Tile.pretty_print_tile(solution[1][0]))
# print("---")
# print(Tile.pretty_print_tile(solution[12][0]))
# print("---")
# print(Tile.pretty_print_tile(solution[13][0]))

corners = (
    solution[0][1],
    solution[width - 1][1],
    solution[length - width][1],
    solution[length - 1][1],
)
# print(corners)

ans = 1
for corner in corners:
    ans *= corner

print("Part 1:", ans)

# Part 2

# Remove the borders from a given 2d array
def remove_borders(tile):
    tile_width = len(tile)
    tile_height = len(tile[0])
    new_tile = []
    for i, row in enumerate(tile):
        if i == 0 or i == tile_width - 1:
            continue
        else:
            new_row = []
            for j, column in enumerate(row):
                if j == 0 or j == tile_height - 1:
                    continue
                else:
                    new_row.append(column)
            new_tile.append(new_row)

    return new_tile


# test_tile = solution[13][0]
# print(test_tile)
# print(Tile.pretty_print_tile(remove_borders(test_tile)))

# create one big "solution" tile
def transform_tile_array(tile_array, rows, columns):
    count = 0
    tile_height = len(tile_array[0])
    tile_width = len(tile_array[0][0])
    # print(tile_height, tile_width)
    new_tile = [
        [0 for i in range(tile_width * columns)] for j in range(tile_height * rows)
    ]

    for i, tile in enumerate(tile_array):
        row_offset = (i // rows) * tile_height
        column_offset = (i % columns) * tile_width
        # print(i, tile)
        for j, tile_row in enumerate(tile):
            for k, tile_column in enumerate(tile_row):
                # print(j, k, j + row_offset, k + column_offset, tile_column)
                new_tile[j + row_offset][k + column_offset] = tile_column
                if tile_column == "#":
                    count += 1
    return new_tile, count


solution_array = list(map(lambda x: x[0], solution))
solution_tile, count = transform_tile_array(
    list(map(lambda x: remove_borders(x), solution_array)), 12, 12
)
# print(solution_tile, count)

# Find sea monsters
k = len(solution_tile[0])
# print(k)

rotate90 = rotate90degrees(solution_tile)
rotate180 = rotate90degrees(rotate90)
rotate270 = rotate90degrees(rotate180)

solution_transformations = [
    solution_tile,
    rotate90,
    rotate180,
    rotate270,
    flip_horizontally(solution_tile),
    flip_horizontally(rotate90),
    flip_horizontally(rotate180),
    flip_horizontally(rotate270),
]
for tile in solution_transformations:
    solution_tile_string = Tile.pretty_print_tile(tile)
    # print(solution_tile_string)
    monsters = len(
        re.findall(
            "(?=(#..{"
            + str(k - 19)
            + "}#.{4}##.{4}##.{4}###.{"
            + str(k - 19)
            + "}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}))",
            solution_tile_string,
            re.DOTALL,
            overlapped=True,
        )
    )
    # print(monsters)
    if monsters > 0:
        print("Part 2:", count - monsters * 15)
