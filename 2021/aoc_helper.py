# Module with helper functions for Advent of Code challenge

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


def flatten_list(original_list):
    flat_list = []
    for nested_list in original_list:
        for item in nested_list:
            flat_list.append(item)
    return flat_list

