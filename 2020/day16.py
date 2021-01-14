import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input16', 'plain')
data_parts = str(data).strip().split('\n\n')
# print(data_parts)
fields_data = data_parts[0].split('\n')
my_ticket = data_parts[1].split('\n')[-1].split(',')
other_tickets = data_parts[2].split('\n')[1:]
# print(other_tickets)


def parse_fields(fields_data):
    fields = {}
    for line in fields_data:
        (field_name, field_value_data) = line.split(': ')
        field_values = field_value_data.split(' or ')
        v = []
        for value in field_values:
            low, high = value.split('-')
            v.append((int(low), int(high)))
        fields[field_name] = v
    return fields


parsed_fields_data = parse_fields(fields_data)


def parse_other_tickets(other_tickets_data):
    tickets = []
    for line in other_tickets_data:
        tickets.append(line.split(','))
    return tickets


parsed_other_tickets = parse_other_tickets(other_tickets)
# print(parsed_other_tickets)


def calculate_valid_field_range(ranges):
    valid_numbers = set()
    for num_range in ranges:
        for i in range(num_range[0], num_range[1]):
            valid_numbers.add(i)
    return valid_numbers


fields_values = aoc_helper.flatten_list(parsed_fields_data.values())
# print(fields_values)

valid_fields = calculate_valid_field_range(fields_values)

valid_tickets = []
invalid_fields = []
for ticket in parsed_other_tickets:
    # print(ticket)
    valid = True
    for ticket_field in ticket:
        if not int(ticket_field) in valid_fields:
            invalid_fields.append(int(ticket_field))
            valid = False
    if valid:
        valid_tickets.append(ticket)

# print(invalid_fields)
sum = 0
for f in invalid_fields:
    sum += f
print('Part1:', sum)
# print(valid_tickets)
# print('My ticket:', my_ticket)

# Part 2
product = 1
columns = set(range(len(parsed_fields_data)))
for _ in range(len(parsed_fields_data)):
    for i, (field_name, fields_values) in enumerate(parsed_fields_data.items()):
        a, b = fields_values[0]
        c, d = fields_values[1]
        # print(field_name, fields_values)
        # print(a, b, c, d)
        candidates = [
            col
            for col in columns
            if all(
                a <= int(ticket[col]) <= b or c <= int(ticket[col]) <= d for ticket in valid_tickets
            )
        ]
        if len(candidates) == 1:
            parsed_fields_data.pop(field_name, None)
            columns.remove(candidates[0])
            if field_name.startswith("departure"):
                product *= int(my_ticket[candidates[0]])
            break

print('Part2: ', product)
