from itertools import combinations
import math

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):

		with open(filename, 'r') as infile:
			content = infile.read()

		self.grid = [list(row) for row in content.splitlines()]
		self.rows = len(self.grid)
		self.cols = len(self.grid[0])
		self.antenna_types = {char for char in content if char not in {'.', '\n'}}
		self.part = 1

#####################
## PART 1 SOLUTION ##
#####################

def get_distance(p1, p2, normalize):
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]

	if normalize:
		greatest_common_divisor = math.gcd(abs(dx), abs(dy))
		dx //= greatest_common_divisor
		dy //= greatest_common_divisor

	return dx, dy

def	is_on_grid(p, rows, cols):
	return p[0] in range(rows) and p[1] in range(cols)

def next_point(p, dx, dy):
	return (p[0] + dx, p[1] + dy)

def find_antinodes(input, antennas):

	rows, cols = input.rows, input.cols
	antinodes = set()

	for a1, a2 in combinations(antennas, 2):

		dx, dy = get_distance(a1, a2, input.part)

		if input.part == 1:
			if is_on_grid(next_point(a1, dx, dy), rows, cols):
				antinodes.add(next_point(a1, dx, dy))
			if is_on_grid(next_point(a2, -dx, -dy), rows, cols):
				antinodes.add(next_point(a2, -dx, -dy))

		if input.part == 2:
			antinodes.add(a1)
			while is_on_grid(next_point(a1, dx, dy), rows, cols):
				a1 = next_point(a1, dx, dy)
				antinodes.add(a1)

			while is_on_grid(next_point(a1, -dx, -dy), rows, cols):
				a1 = next_point(a1, -dx, -dy)
				antinodes.add(a1)

	return antinodes

def find_matching_antennas(input, type):

	rows, cols = input.rows, input.cols
	grid = input.grid

	return {(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == type}

def part1(input):

	antinodes = set()

	for type in input.antenna_types:

		antennas = find_matching_antennas(input, type)
		antinodes |= find_antinodes(input, antennas)

	return len(antinodes)

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	return part1(input)

if __name__ == "__main__":
	from os import path
	dirname = path.dirname(__file__)

	example = Data(path.join(dirname, "example.txt"))
	input = Data(path.join(dirname, "input.txt"))

	print("Part", example.part, "Example: ", part1(example))
	print("Part", input.part, "Solution: ", part1(input))

	example.part = 2
	input.part = 2
	print("Part", example.part, "Example: ", part2(example))
	print("Part", input.part, "Solution: ", part2(input))
