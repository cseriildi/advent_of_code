###################
## INPUT PARSING ##
###################

def parse():
	with open("input.txt", 'r') as infile:
		return infile.read().splitlines()

def split_columns(input):
	left = []
	right = []
	for row in input:
		a, b = row.split()
		left.append(int(a))
		right.append(int(b))
	
	return left, right

#####################
## PART 1 SOLUTION ##
#####################

def part1(input):
	left, right = split_columns(input)
	left.sort()
	right.sort()

	return sum(abs(left[i] - right[i]) for i in range(len(left)))

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	left, right = split_columns(input)

	return sum(num * right.count(num) for num in left)


if __name__ == "__main__":
	input = parse()
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Solution: ", part2(input))
