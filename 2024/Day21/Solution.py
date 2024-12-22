from os import path
import sys
from functools import cache
import re

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

UP, DOWN, LEFT, RIGHT = "^", "v", "<", ">"

DIRECTIONS = {DOWN: (1, 0), UP: (-1, 0), LEFT: (0, -1), RIGHT: (0, 1)}

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

PAD_N = {v: k for k, v in NUMERICAL_PAD.items()}
PAD_D = {v: k for k, v in DIRECTIONAL_PAD.items()}

@cache
def move(point, dir):
	return (point[0] + dir[0], point[1] + dir[1])

@cache
def get_delta(point1, point2):
	return point2[0] - point1[0], point2[1] - point1[1]

@cache
def get_horizontal(point, d_col, numeric):
	
	direction = RIGHT if d_col > 0 else LEFT
	p = point
	for _ in range(abs(d_col)):
		p = move(p, DIRECTIONS[direction])
		if (numeric and PAD_N[p] == "X") or (not numeric and PAD_D[p] == "X"):
			return "X"
	return direction * abs(d_col)

@cache
def get_vertical(point, d_row, numeric):
	direction = DOWN if d_row > 0 else UP
	p = point
	for _ in range(abs(d_row)):
		p = move(p, DIRECTIONS[direction])
		if numeric and PAD_N[p] == "X" or not numeric and PAD_D[p] == "X":
			return "X"
	return direction * abs(d_row)

@cache
def calculate_movements(curr, next, numeric):

	point1 = NUMERICAL_PAD[curr] if numeric else DIRECTIONAL_PAD[curr]
	point2 = NUMERICAL_PAD[next] if numeric else DIRECTIONAL_PAD[next]

	d_row, d_col = get_delta(point1, point2)
	option1 = get_horizontal(point1, d_col, numeric) + get_vertical(move(point1, (0, d_col)), d_row, numeric) + "A"
	option2 = get_vertical(point1, d_row, numeric) + get_horizontal(move(point1, (d_row, 0)), d_col, numeric) + "A"

	movements = []
	if "X" not in option1:
			movements.append(option1)
	if option1 != option2 and "X" not in option2:
			movements.append(option2)
	return movements

@cache
def path_finder(code, prev, numeric):
	paths = set()
	length = len(code)
	to_check = [[0, prev, ""]]
	while to_check:
		i, curr, path = to_check.pop()
		if i == length:
			paths.add(path)
			continue
		for step in calculate_movements(curr, code[i], numeric):
			to_check.append([i + 1, code[i], path + step])
	return paths

@cache
def find_shortest_path(codes, number_of_robots, numeric):
	prev = "A"
	res = 0
	for code in codes:
		for c in code:
			new_code = path_finder(c, prev, numeric)
			if number_of_robots == 0:
				res += min([len(code) for code in new_code])
			else:
				res += min(find_shortest_path(code, number_of_robots - 1, numeric=False) for code in new_code)
			prev = c
	return res

def get_number(code):
	return int(re.findall(r'\d+', code)[0])

def part1(input):
	for code in input.codes:
		input.result += find_shortest_path(code, number_of_robots=2, numeric=True) * get_number(code)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	for code in input.codes:
		input.result += find_shortest_path(code,number_of_robots=25, numeric=True) * get_number(code)
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
	if example: part2(example)
	part2(input)
