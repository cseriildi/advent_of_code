from itertools import combinations
import math

###################
## INPUT PARSING ##
###################

def parse(filename):
	with open(filename, 'r') as infile:
		input = infile.read()
		grid = [list(row) for row in input.splitlines()]
		antenna_types = {char for char in input if char not in ('.', '\n')}
		rows = len(grid)
		cols = len(grid[0])

		return {"grid" : grid, "grid_size" : (rows, cols), "antenna_types": antenna_types}

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

def find_antinodes(input, antennas, part2 = False):

	(rows, cols) = input["grid_size"]
	antinodes = set()

	for a1, a2 in combinations(antennas, 2):

		dx, dy = get_distance(a1, a2, part2)

		if not part2:
			if is_on_grid(next_point(a1, dx, dy), rows, cols):
				antinodes.add(next_point(a1, dx, dy))
			if is_on_grid(next_point(a2, -dx, -dy), rows, cols):
				antinodes.add(next_point(a2, -dx, -dy))

		if part2:
			antinodes.add(a1)
			while is_on_grid(next_point(a1, dx, dy), rows, cols):
				a1 = next_point(a1, dx, dy)
				antinodes.add(a1)

			while is_on_grid(next_point(a1, -dx, -dy), rows, cols):
				a1 = next_point(a1, -dx, -dy)
				antinodes.add(a1)

	return antinodes

def find_matching_antennas(input, type):

	(rows, cols) = input["grid_size"]
	grid = input["grid"]

	return {(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == type}

def part1(input):

	antinodes = set()

	for type in input["antenna_types"]:

		antennas = find_matching_antennas(input, type)
		antinodes |= find_antinodes(input, antennas)

	return len(antinodes)

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	antinodes = set()

	for type in input["antenna_types"]:

		antennas = find_matching_antennas(input, type)
		antinodes |= find_antinodes(input, antennas, True)

	return len(antinodes)

if __name__ == "__main__":
	from os import path
	dirname = path.dirname(__file__)

	input = parse(dirname + "/input.txt")
	example = parse(dirname + "/example.txt")
	print("Part 1 Example: ", part1(example))
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Example: ", part2(example))
	print("Part 2 Solution: ", part2(input))
