import aoc_helper
from functools import reduce
from itertools import product
from collections import defaultdict
import re

data = aoc_helper.get_input('input19', 'plain').strip()
# print(data)

rules_data = data.split('\n\n')[0].split('\n')
messages = data.split('\n\n')[1].split('\n')

# print(rules_data)
# print(messages)


def parse_rules(rules_data):
    rules = {}
    for line in rules_data:
        line_split = line.split(': ')
        rule_id = line_split[0]
        line_split_values = line_split[1].split(' | ')
        sub_rules = []
        for v in line_split_values:
            if v not in ['\"a\"', '\"b\"']:
                values = v.split(' ')
            else:
                values = v.replace('"', '')
            sub_rules.append(values)
        rules[rule_id] = sub_rules
    return rules


rules = parse_rules(rules_data)
print(rules)


def gen_rule_regexp(rules, rule_id, depth=0):
    # Do not run forever...
    if depth > 20:
        return ''

    rule = rules[rule_id]
    if rule[0][0] in 'ab':
        return rule[0][0]

    reg_exp = '('
    if len(rule) == 1:
        for r in rule[0]:
            reg_exp += gen_rule_regexp(rules, r, depth+1)
    else:
        for i, or_rules in enumerate(rule):
            for r in or_rules:
                reg_exp += gen_rule_regexp(rules, r, depth+1)
            if i < len(rule) - 1:
                reg_exp += '|'
    reg_exp += ')'
    return reg_exp


print(gen_rule_regexp(rules, '0'))

my_regex = f"^{gen_rule_regexp(rules, '0')}$"
counter_p1 = 0
for this_message in messages:
    if re.match(my_regex, this_message):
        counter_p1 += 1

print('Part 1:', counter_p1)

# Part 2

# New rules
rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]

my_regex_2 = f"^{gen_rule_regexp(rules, '0')}$"
counter_p2 = 0
for this_message in messages:
    if re.match(my_regex_2, this_message):
        counter_p2 += 1

print('Part 2:', counter_p2)

