###################
## INPUT PARSING ##
###################

def parse():
	with open("input.txt", 'r') as infile:
		input = infile.read().split()
		return input

#####################
## PART 1 SOLUTION ##
#####################

def	check_xmas(input, row, col):\

	if input[row][col] != 'X':
		return 0
	max_x = len(input[0])
	max_y = len(input)
	xmas = ['X', 'M', 'A', 'S']

	count = 0
	if row >= 3:
		count += [input[row - i][col] for i in range(4)] == xmas
	if row <= max_y - 4:
		count += [input[row + i][col] for i in range(4)] == xmas
	if col >= 3:
		count += [input[row][col - i] for i in range(4)] == xmas
	if col <= max_x - 4:
		count += [input[row][col + i] for i in range(4)] == xmas
	if row >= 3 and col >= 3:
		count += [input[row - i][col - i] for i in range(4)] == xmas
	if row <= max_y - 4 and col <= max_x - 4:
		count += [input[row + i][col + i] for i in range(4)] == xmas
	if row >= 3 and col <= max_x - 4:
		count += [input[row - i][col + i] for i in range(4)] == xmas
	if row <= max_y - 4 and col >= 3:
		count += [input[row + i][col - i] for i in range(4)] == xmas
	return count

def part1(input):

	max_x = len(input[0])
	max_y = len(input)

	return sum(check_xmas(input, row, column) for row in range(max_y) for column in range(max_x))

#####################
## PART 2 SOLUTION ##
#####################

def is_xmas(input, row, col):

	if input[row][col] != 'A':
		return False
	
	a = input[row - 1][col - 1]
	b = input[row + 1][col + 1]
	c = input[row + 1][col - 1]
	d = input[row - 1][col + 1]

	return a + b in ("MS", "SM") and c + d in ("MS", "SM")

def part2(input):

	max_x = len(input[0])
	max_y = len(input)

	return sum(is_xmas(input, row, col) for row in range(1, max_x - 1) for col in range(1, max_y - 1))

if __name__ == "__main__":
	input = parse()
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Solution: ", part2(input))
