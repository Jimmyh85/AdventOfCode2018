# Open the file with read only permit
with open('input.txt', "r") as f:
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    box_ids = []

    for line in f:
        box_ids.append(line)


def part1(box_ids):

    occurences = [0, 0]  # holds the found 2s and 3s
    for id in box_ids:
        seen2 = False
        seen3 = False
        for char in id:
            if id.count(char) == 3 and not seen3:
                occurences[1] = occurences[1] + 1
                seen3 = True
            if id.count(char) == 2 and not seen2:
                occurences[0] = occurences[0] + 1
                seen2 = True

    return occurences[0] * occurences[1]


def part2(box_ids):
    # Find two IDs that only differ in one single character
    for id1 in box_ids:
        for id2 in box_ids[1:]:
            if hamming_distance(id1, id2) == 1:  # we have found a match
                result = ""
                for c1, c2 in zip(id1, id2):
                    if c1 == c2:
                        result = result + c1

                return result

    return 0


def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


# print(part1(box_ids))
print(part2(box_ids))
