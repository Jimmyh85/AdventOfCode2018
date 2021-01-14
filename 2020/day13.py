
import aoc_helper
from functools import reduce

data = aoc_helper.get_input('input13', 'string')

timestamp = int(data[0])
bus_ids = [int(id) for id in data[1].split(',') if id != 'x']

print(timestamp)
print(bus_ids)

result = {}
for bus in bus_ids:
    i = 1
    while bus * i <= timestamp:
        i += 1
    result[bus] = bus*i

print(result)
min_tuple = (0, 999999999999)
for key, value in result.items():
    if value < min_tuple[1]:
        min_tuple = (key, value)

print(min_tuple[0]*(min_tuple[1]-timestamp))

# Part2


def egcd(a, b):
    """
    Compute the Extended Euclidean Algorithm (EEA) and return (g, x, y) a*x + b*y = gcd(x, y)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


#data[1] = '17,x,13,19'
#data[1] = '67,7,59,61'
bus_ids_with_pos = data[1].split(',')
print(bus_ids_with_pos)

AiMi = []
M = 1
for ai, mi in enumerate(bus_ids_with_pos):
    if mi != 'x':
        AiMi.append(((int(ai) * -1) % int(mi), int(mi)))
        M *= int(mi)
print(AiMi)

# Solve with Chinese Remainder Theorem
res = 0
for i in AiMi:
    ai = i[0]
    mi = i[1]
    MI = M // mi
    print(ai, mi, MI)
    (g, ri, si) = egcd(mi, MI)
    ei = si * MI
    res += i[0]*ei

res = res % M
print(res)
