import itertools
from functools import reduce

def get_input(filename, mode='numbers'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())    
    return data

data = get_input('input2','string')

print(data)

def parse_line(line):
    parts = line.split(" ")
    (min, max) = parts[0].split("-")
    letter = parts[1][0]
    password = parts[2]
    return ((int(min), int(max), letter), password)

def is_valid_password(policy, password):
    (min, max, letter) = policy
    if (password.count(letter) <= max and password.count(letter) >= min):
        return True
    return False    

def is_valid_password_part2(policy, password):
    (pos1, pos2, letter) = policy
    if((password[pos1-1] == letter and not password[pos2-1] == letter) or (not password[pos1-1] == letter and password[pos2-1] == letter)):
        return True
    return False    

valid_pwds = 0
for d in data:
    (policy, password) = parse_line(d)
    #if(is_valid_password(policy, password)):
    if(is_valid_password_part2(policy, password)):
        valid_pwds = valid_pwds + 1
        print((policy, password))

print(valid_pwds)