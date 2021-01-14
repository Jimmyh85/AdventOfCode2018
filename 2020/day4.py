from functools import reduce
import re

def get_input(filename, mode='numbers'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            if (mode == 'numbers'):
                data.append(int(line.strip()))
            if (mode == 'string'):
                data.append(line.strip())    
    return data

data = get_input('input4','string')

#print(data)

# Definitions
# (field_name: validation_pattern)
required_fields = [
    ('byr','^(19[2-8][0-9]|199[0-9])|(200[0-2])$'),
    ('iyr','^201[0-9]|2020$'),
    ('eyr','^202[0-9]|2030$'),
    ('hgt','^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$'),
    ('hcl','^#[0-9a-f]{6}$'),
    ('ecl','^(amb|blu|brn|gry|grn|hzl|oth)$'),
    ('pid','^[0-9]{9}$')
]

def extract_passports(data):
    passports = []
    passport = ''
    for line in data:
        if(line == ''):
            passports.append(passport.strip())
            passport = ''
        else:
            passport += line + ' '
    # append last line
    passports.append(passport.strip())        
    return passports

def is_valid_passport_part1(passport_data):
    for field, pattern in required_fields:
        if(not field in passport_data):
            return False
    return True        

def is_valid_passport_part2(passport_data):
    for field, pattern in required_fields:
        fields_to_check = list(map(lambda x: x.split(':'), passport_data.split(' ')))
        passport = dict(fields_to_check) 
        
        if(not field in passport):
            return False
        else:
            if(not re.match(pattern, passport[field])):
                return False
    return True

valid_1 = 0
valid_2 = 0

for passport in extract_passports(data):
    if(is_valid_passport_part1(passport)):
        valid_1 += 1
    if(is_valid_passport_part2(passport)):
        valid_2 += 1    
        #print(password)
        #print("---")    
    #else:
        #print(password)
        #print("---")    

#print(extract_passwords(data))            
print('Part1', valid_1)
print('Part2', valid_2)
