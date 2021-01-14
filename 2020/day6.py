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


data = get_input('input6', 'plain')


def remove_linebreak(string):
    return string.replace('\n', '')

#Part 1
def count_unique_yes(form):
    return len(set(list(remove_linebreak(form))))

#Part 2
def count_common_yes(form):
    group_size = form.count('\n') + 1
    answers = dict()
    for char in remove_linebreak(form):
        if char in answers:
            answers[char] += 1
        else:
            answers[char] = 1

    return len([v for v in answers.values() if v == group_size])

# Definitions
forms = data.split('\n\n')

yes_count_1 = 0
yes_count_2 = 0

for form in forms:
    yes_count_1 += count_unique_yes(form)
    yes_count_2 += count_common_yes(form)

print("Part1", yes_count_1)
print("Part2", yes_count_2)
