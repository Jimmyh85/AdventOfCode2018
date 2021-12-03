import aoc_helper

lines = aoc_helper.get_input("3", "string")

DATA_LENGTH = len(lines[0])

def get_ones_and_zeros(lines):

    ones = [0 for _ in range(DATA_LENGTH)]
    zeros = [0 for _ in range(DATA_LENGTH)]

# Part 1
    for line in lines:
        i = 0
        for char in line:
            # print(char)
            if int(char) == 1:  
                ones[i] += 1
            else:
                zeros[i] += 1
            i += 1
    return (ones, zeros)

(ones, zeros) = get_ones_and_zeros(lines)

# print(ones, zeros)
gamma = ""
epsilon = ""
for i in range(DATA_LENGTH):
    if ones[i] > zeros[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Part 1", int(gamma, 2) * int(epsilon, 2))

# Part 2
pos = 0
filtered_oxygen = lines

while len(filtered_oxygen) > 1 and pos < DATA_LENGTH:
    ones, zeros = get_ones_and_zeros(filtered_oxygen)
    if ones[pos] >= zeros[pos]:
        filtered_oxygen = [line for line in filtered_oxygen if line[pos] == "1"]
    else:
        filtered_oxygen = [line for line in filtered_oxygen if line[pos] == "0"]
    pos += 1

# print(filtered_oxygen)
                
pos = 0
filtered_co2 = lines

while len(filtered_co2) > 1 and pos < DATA_LENGTH:
    ones, zeros = get_ones_and_zeros(filtered_co2)
    if zeros[pos] <= ones[pos]:
        filtered_co2 = [line for line in filtered_co2 if line[pos] == "0"]
    else:
        filtered_co2 = [line for line in filtered_co2 if line[pos] == "1"]
    pos += 1

# print(filtered_co2)

print("Part 2", int(filtered_oxygen[0], 2) * int(filtered_co2[0], 2))
        



