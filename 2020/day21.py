import math
import aoc_helper
import re
from collections import defaultdict

data = aoc_helper.get_input("input21", "string")
# data = aoc_helper.get_input("input21_sample", "string")
# print(data)

foods = {}
counts = defaultdict(int)

all_allergens = set()
all_ingredients = set()
for line in data:
    (food, allergen_list) = line.split(" (contains ")
    allergen_list = allergen_list.replace(")", "").split(", ")
    ingredient_list = food.split(" ")
    # print(food)
    # print(allergen_list)
    foods[food] = allergen_list
    for ingredient in ingredient_list:
        all_ingredients.add(ingredient)
    for allergen in allergen_list:
        all_allergens.add(allergen)

print(all_allergens)
print(all_ingredients)

ingredient_allergen_candidates = {i: set(all_allergens) for i in all_ingredients}

for food, allergens in foods.items():
    food_ingredients = food.split(" ")
    for ingredient in food_ingredients:
        counts[ingredient] += 1

    for allergen in allergens:
        for ingredient in all_ingredients:
            if ingredient not in food_ingredients:
                ingredient_allergen_candidates[ingredient].discard(allergen)

# print(counts)
# print(ingredient_allergen_candidates)

# Part 1
ans = 0
for ingredient in all_ingredients:
    if ingredient_allergen_candidates[ingredient]:
        print(ingredient, ingredient_allergen_candidates[ingredient])
    else:
        ans += counts[ingredient]

print("Part 1:", ans)

# Part 2

Ingredient_to_Allergen = {}
USED = set()

while len(Ingredient_to_Allergen) < len(all_allergens):
    for ingredient in all_ingredients:
        candidates = [
            allergen
            for allergen in ingredient_allergen_candidates[ingredient]
            if allergen not in USED
        ]
        if len(candidates) == 1:
            # print(ingredient, candidates, USED)
            Ingredient_to_Allergen[ingredient] = candidates[0]
            USED.add(candidates[0])

print(Ingredient_to_Allergen)
sorted_mapping = {
    k: v for k, v in sorted(Ingredient_to_Allergen.items(), key=lambda item: item[1])
}
ans_part2 = ",".join(sorted_mapping.keys())
print("Part 2:", ans_part2)
