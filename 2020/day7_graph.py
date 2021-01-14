data = open('input7', 'r').read().split('\n')

m = {}

for line in data:
	line = line.replace('bags', '').replace('bag', '').strip('.')
	line = line.split('contain')
	m[line[0].strip()] = line[1].strip().split(',')

def get_bags(bag_col):

	if 'no other' in m[bag_col]:
		return 1

	total = 1
	for col in m[bag_col]:
		x = col.split()
		total += int(x[0]) * get_bags(' '.join(x[1:]))

	return total

print(get_bags('shiny gold')-1)