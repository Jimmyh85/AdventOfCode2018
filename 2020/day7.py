import re

def get_input(filename, mode='numbers'):
    with open(filename, 'r') as f:
        if (mode == 'plain'):
            return f.read()
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())
    return data


data = get_input('input7', 'string')
#print(data)

# Definitions
OUR_BAG = 'shiny gold'

bag_rules = dict()

for line in data:
    rule = line.split(" contain ")
    left = rule[0].replace('bags','')
    left = left.replace('bag', '')
    left = left.strip()
    right = rule[1].replace('bags','')
    right = right.replace('bag','')
    right = right.replace('.','')

    bag_rules[left] = list(map(lambda x: x.strip(), right.split(',')))

containing_bags = []

def find_containing_bags(list_of_bags, parent_bags):
    if len(list_of_bags) == 0:
        return parent_bags
    else:
        # find new containing bags
        new_containing_bags = []
        for new_bag in list_of_bags:
            for key, value in bag_rules.items():
                for bag in value:
                    if new_bag in bag:
                        new_containing_bags.append(key)
        if len(new_containing_bags) > 0:
            parent_bags.update(new_containing_bags)
        return find_containing_bags(new_containing_bags, parent_bags)

def get_bags_in_bag(bag):
    children = []
    if bag in bag_rules:
        print('get_bib->', bag, bag_rules[bag])
        for child in bag_rules[bag]:
            # print('Child', child)
            if child == "no other":
                continue
            else:
                bag_count, bag_color = re.search('^(\d+)(.*)$', child).groups()
                children.append((bag_count, bag_color.strip()))
        print(children)
    return children


def count_included_bags(list_of_bags):
    print('f->', list_of_bags)
    res = 1
    new_children = []
    for new_bag in list_of_bags:
        new_children += get_bags_in_bag(new_bag)

    print(new_children)

    if len(new_children) == 0:
        return 1
    else:
        # find new children
        for count, nbag in new_children:
            print(count, nbag)
            res = res + (int(count) * count_included_bags([nbag]))
            print(res)
        return res

print(bag_rules)

l = find_containing_bags([OUR_BAG], set())

print('Part1', len(l))

#print(get_bags_in_bag('shiny gold'))
l2 = count_included_bags([OUR_BAG])
print(l2)