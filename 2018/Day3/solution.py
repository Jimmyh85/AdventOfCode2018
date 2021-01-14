# Open the file with read only permit
import re
from collections import defaultdict
with open('input.txt', "r") as f:
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    claims = []

    for line in f:
        claims.append(line)

# Solve by counting the overlaps


def part1(claim_list):

    # parse the input to a list with (claim_index, start_x, start_y, width, height)
    claims = list(map(lambda s:
                      list(map(int, re.findall(r'-?\d+', s))), claim_list))

    overlaps = {}
    fabrics = defaultdict(list)
    for (claim_index, start_x, start_y, width, height) in claims:
        overlaps[claim_index] = set()
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                if fabrics[(i, j)]:
                    for number in fabrics[(i, j)]:
                        overlaps[number].add(claim_index)
                        overlaps[claim_index].add(number)
                fabrics[(i, j)].append(claim_index)

    duplicate_inches = len([k for k in fabrics if len(fabrics[k]) > 1])
    return duplicate_inches


def part2(claim_list):
    claims = list(
        map(lambda s: list(map(int, re.findall(r'-?\d+', s))), claim_list))

    overlaps = {}
    fabrics = defaultdict(list)
    for (claim_index, start_x, start_y, width, height) in claims:
        overlaps[claim_index] = set()
        for i in range(start_x, start_x + width):
            for j in range(start_y, start_y + height):
                if fabrics[(i, j)]:
                    for number in fabrics[(i, j)]:
                        overlaps[number].add(claim_index)
                        overlaps[claim_index].add(number)
                fabrics[(i, j)].append(claim_index)

    claim_no_overlap = [k for k in overlaps if len(overlaps[k]) == 0][0]
    return claim_no_overlap

# Solve with the help of a 2d array


def part1_old(claim_list):

    WIDTH = 1000
    HEIGHT = 1000

    field = [["."] * WIDTH for i in range(HEIGHT)]

    # dupliate inches
    duplicate_inches = 0

    regex = re.compile("[#@:]")
    for claim in claim_list:
        claim = re.sub(regex, "", claim)
        # claim reformatted to [id;;left,top;widthxheigth]
        claim = claim.split(" ")

        # Draw the claim on the field
        id = int(claim[0])
        pos_left = int(claim[2].split(",")[1])
        pos_top = int(claim[2].split(",")[0])
        dim_w = int(claim[3].split("x")[0])
        dim_h = int(claim[3].split("x")[1])

        for w in range(dim_w):
            for h in range(dim_h):
                if field[pos_left + h][pos_top + w] == ".":
                    field[pos_left + h][pos_top + w] = id
                elif field[pos_left + h][pos_top + w] == "#":
                    continue
                else:
                    duplicate_inches = duplicate_inches + 1
                    field[pos_left + h][pos_top + w] = "#"

    return duplicate_inches


# print(part1(claims))
print(part2(claims))
