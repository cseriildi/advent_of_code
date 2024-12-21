from os import path
import sys
import numpy as np
from functools import lru_cache

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename, puzzle_type):
		self.filename = filename
		self.part = 1
		self.result = 0
		self.type = puzzle_type
		self.parse_data()

	def parse_data(self):
		with open(self.filename, 'r') as infile:
			content = infile.read()
		self.codes = content.splitlines()

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

# Define constants for directions
UP, DOWN, LEFT, RIGHT = "^", "v", "<", ">"

# Define the numerical pad and directional pads
NUMERICAL_PAD = {
	"7": (0, 0), "8": (0, 1), "9": (0, 2),
	"4": (1, 0), "5": (1, 1), "6": (1, 2),
	"1": (2, 0), "2": (2, 1), "3": (2, 2),
	"X": (3, 0), "0": (3, 1), "A": (3, 2)
}

DIRECTIONAL_PAD = {
	"X": (0, 0), UP: (0, 1), "A": (0, 2),
	LEFT: (1, 0), DOWN: (1, 1), RIGHT: (1, 2)
}

PAD1 = {v: k for k, v in NUMERICAL_PAD.items()}
PAD2 = {v: k for k, v in DIRECTIONAL_PAD.items()}

@lru_cache
def move(point, dir):
	return (point[0] + dir[0], point[1] + dir[1])

@lru_cache
def get_horizontal(point, d_col, numeric):
	str = ""
	right = d_col > 0
	p = point
	for _ in range(abs(d_col)):
		p = move(p, (0, 1 if right else -1))
		if numeric and PAD1[p] == "X":
			return "X"
		if not numeric and PAD2[p] == "X":
			return "X"
		if right:
			str += RIGHT
		else:
			str += LEFT
	return str

@lru_cache
def get_vertical(point, d_row, numeric):
	str = ""
	down = d_row > 0
	p = point
	for _ in range(abs(d_row)):
		p = move(p, (1 if down else -1, 0))
		if numeric and PAD1[p] == "X":
			return "X"
		if not numeric and PAD2[p] == "X":
			return "X"
		if down:
			str += DOWN
		else:
			str += UP
	return str


@lru_cache
def calculate_movements(curr, next, numeric):
		
	movements = []
	if numeric:
		point1 = NUMERICAL_PAD[curr]
		point2 = NUMERICAL_PAD[next]
	else:
		point1 = DIRECTIONAL_PAD[curr]
		point2 = DIRECTIONAL_PAD[next]

	d_row = point2[0] - point1[0]
	d_col = point2[1] - point1[1]

	hor1 = get_horizontal(point1, d_col, numeric)
	hor2 = get_horizontal(move(point1, (d_row, 0)), d_col, numeric)
	ver1 = get_vertical(point1, d_row, numeric)
	ver2 = get_vertical(move(point1, (0, d_col)), d_row, numeric)

	if hor1 != "X" and ver2 != "X":
			movements.append(hor1 + ver2 + "A")
	if hor2 != "X" and ver1 != "X" and hor1 + ver2 != ver1 + hor2:
			movements.append(ver1 + hor2 + "A")
	return movements

import heapq

@lru_cache
def path_finder(code, prev, numeric):
	paths = set()
	length = len(code)
	to_check = [(0, 0, prev, [])]
	heapq.heapify(to_check)
	while to_check:
		priority, i, curr, path = heapq.heappop(to_check)
		if i == length:
			if path:
				paths.add("".join(path))
			continue
		for step in calculate_movements(curr, code[i], numeric):
			heapq.heappush(to_check, (priority + len(step), i + 1, code[i], path + [step]))
		
	return paths

""" def decoder(code):
	def move_backwards(point, dir):
		return (point[0] - dir[0], point[1] - dir[1])

	previous_code = ""
	position = DIRECTIONAL_PAD["A"]
	for step in code.split("A")[:-1]:
		for c in step:
			if c == UP:
				position = move_backwards(position, (1, 0))
			elif c == DOWN:
				position = move_backwards(position, (-1, 0))
			elif c == LEFT:
				position = move_backwards(position, (0, 1))
			elif c == RIGHT:
				position = move_backwards(position, (0, -1))
		previous_code += PAD2[position]

	return previous_code """

def find_shortest_path(code, prev, number_of_robots=2):

	current_paths = path_finder(code, prev, True)
	for i in range(number_of_robots):
		next_paths = set()
		for path in current_paths:
			next_paths.update(path_finder(path, "A", False))
		current_paths = next_paths
	return min([len(path) for path in current_paths])

import re
def get_number(code):
	return int(re.findall(r'\d+', code)[0])

def part1(input):
	for code in input.codes:
		shortest = 0
		prev = "A"
		for c in code:
			shortest += find_shortest_path(c, prev, 2)
			prev = c
		input.result += shortest * get_number(code)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	for code in input.codes:
		shortest = 0
		prev = "A"
		for c in code:
			shortest += find_shortest_path(c, prev, 25)
			prev = c
		input.result += shortest * get_number(code)
	input.print_solution()

##########
## MAIN ##
##########

dirname = path.dirname(__file__)
EXAMPLE_FILE_NAME = path.join(dirname, "example.txt")
INPUT_FILE_NAME = path.join(dirname, "input.txt")

if __name__ == "__main__":
	try:
		example = Data(EXAMPLE_FILE_NAME, "Example")
	except:
		example = False
		print("\033[1;91mSave puzzle example to", EXAMPLE_FILE_NAME, "\033[0m", file=sys.stderr)

	try:
		input = Data(INPUT_FILE_NAME, "Solution")
	except:
		print("\033[1;91mSave puzzle input to", INPUT_FILE_NAME, "\033[0m", file=sys.stderr)
		sys.exit(1)

	if example: part1(example)
	part1(input)
	#if example: part2(example)
	part2(input)
