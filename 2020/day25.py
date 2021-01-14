public_key_door = 11404017
public_key_card = 13768789

hash = {}


def transform(x, sz):
    return pow(x, sz, 20201227)


def transform_subjectnumber(subject_number, loopsize):
    if (subject_number, loopsize) in hash:
        return hash[(subject_number, loopsize)]
    else:
        value = 1
        for _ in range(loopsize):
            value *= subject_number
            value = value % 20201227
        hash[(subject_number, loopsize)] = value
        return value


def find_loopsize(public_key, subject_number):
    loopsize = 1
    while not transform(subject_number, loopsize) == public_key:
        loopsize += 1
        # print(loopsize)
    return loopsize


print(find_loopsize(5764801, 7))
print(find_loopsize(17807724, 7))

loopsize_door = find_loopsize(public_key_door, 7)
loopsize_card = find_loopsize(public_key_card, 7)
print(loopsize_card)
print(loopsize_door)
encryption = transform(public_key_door, loopsize_card)
encryption2 = transform(public_key_card, loopsize_door)
print("Part 1:", encryption, encryption2)
