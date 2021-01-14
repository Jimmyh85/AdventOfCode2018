# Open the file with read only permit
with open('input.txt', "r") as f:
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    frequencies = []
    
    for line in f:
        frequencies.append(int(line))


def part1(frequencies):
    sum = 0
    
    for f in frequencies:
        sum += f
    
    return sum        
           

from itertools import cycle
def part2(frequencies):
    
   # frequencies = [7,7,-2,-7,-4]
    cycled_list = cycle(frequencies)
    
    found = False
    seen = [0]
    sum = 0

    while not found:
        sum += next(cycled_list)
        if sum in seen:
            found = True
        else:
            seen.append(sum)

    return sum

#print(part1(frequencies))
#print(part2(frequencies))