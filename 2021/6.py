import aoc_helper
from collections import defaultdict

data = aoc_helper.get_input("6", "plain")
current_gen = [int(entry) for entry in data.split(",")]

print(current_gen)


# Example data
# current_gen = [3, 4, 3, 1, 2]

days = 1

# dict with key = 'fish with age x', value = 'number of fish with that age'
fish_population = defaultdict(int)
for fish in current_gen:
    fish_population[fish] += 1

print(fish_population)
while days <= 256:
    next_population = defaultdict(int)
    for fish, num in fish_population.items():
        if fish == 0:
            next_population[8] += num
            next_population[6] += num
        else:
            next_population[fish - 1] += num
    fish_population = next_population
    # print(fish_population)
    # print("After ", days, " day(s): ", current_gen)
    if days == 80:
        print("Part 1", sum(fish_population.values()))

    days += 1

print("Part 2", sum(fish_population.values()))
