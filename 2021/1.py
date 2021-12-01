import aoc_helper

data = aoc_helper.get_input("1")
print(data)
print(len(data))

diffs = 0
for i in range(len(data) - 1):
    # print(i)
    if data[i+1] > data[i]:
        diffs = diffs + 1

# Part 1
print("Part 1", diffs)

# Part 2
diffs = 0
for i in range(len(data) - 3):
    # print(i)
    if sum(data[i+1:i+4]) > sum(data[i:i+3]):
        diffs = diffs + 1

print("Part 2", diffs)
