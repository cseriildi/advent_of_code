from os import path
import sys
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
		if filename == EXAMPLE_FILE_NAME:
			self.type = "Example"
		elif filename == INPUT_FILE_NAME:
			self.type = "Solution"
		else:
			self.type = "undefined"
		self.result = 0

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

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

	input.result = len(antinodes)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	part1(input)

##########
## MAIN ##
##########

dirname = path.dirname(__file__)
EXAMPLE_FILE_NAME = path.join(dirname, "example.txt")
INPUT_FILE_NAME = path.join(dirname, "input.txt")

if __name__ == "__main__":

	try:
		example = Data(EXAMPLE_FILE_NAME)
	except:
		example = False
		print("\033[1;91mSave puzzle example to", EXAMPLE_FILE_NAME, "\033[0m", file=sys.stderr)

	try:
		input = Data(INPUT_FILE_NAME)
	except:
		print("\033[1;91mSave puzzle input to",  INPUT_FILE_NAME, "\033[0m", file=sys.stderr)
		exit(1)
	
	if example: part1(example)
	part1(input)
	if example: part2(example)
	part2(input)
