import aoc_helper

data = aoc_helper.get_input('input8', 'string')

# print(data)


def extract_instruction(instruction):
    operator = instruction.split(' ')[0]
    argument = int(instruction.split(' ')[1])
    return operator, argument


def execute_instructions(instructions):
    valid_operators = ['nop', 'acc', 'jmp']
    seen_lines = set()

    curr_pos = 0
    accumulator_value = 0

    while True:
        next_instruction = instructions[curr_pos]
        operator, argument = extract_instruction(next_instruction)

        if curr_pos in seen_lines:
            #print('Part1', accumulator_value)
            break
        else:
            seen_lines.add(curr_pos)

        assert operator in valid_operators

        if operator == 'nop':
            curr_pos += 1
        if operator == 'acc':
            accumulator_value += argument
            curr_pos += 1
        if operator == 'jmp':
            curr_pos += argument

        # Terminate condition
        if curr_pos == len(instructions):
            print('Part2', accumulator_value)
            break


for i in range(len(data)):
    data_try = data.copy()
    if data[i].startswith('nop'):
        data_try[i] = data_try[i].replace('nop', 'jmp')
    if data[i].startswith('jmp'):
        data_try[i] = data_try[i].replace('jmp', 'nop')
    execute_instructions(data_try)

