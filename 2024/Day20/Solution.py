from os import path
import sys
import numpy as np

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
		self.grid = np.array([list(row) for row in content.splitlines()])
		self.start = tuple(np.argwhere(self.grid == "S")[0])
		self.end = tuple(np.argwhere(self.grid == "E")[0])
		
	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

NEXT = {
	UP: {UP, LEFT, RIGHT},
	DOWN: {DOWN, LEFT, RIGHT},
	LEFT: {LEFT, UP, DOWN},
	RIGHT: {RIGHT, UP, DOWN},
	None: {UP, DOWN, LEFT, RIGHT}
}

#####################
## PART 1 SOLUTION ##
#####################

def path_finder(input):

	def move(point, dir):
		return (point[0] + dir[0], point[1] + dir[1])

	def find_next_step(point, direction):
		for dir in NEXT[direction]:
			new_point = move(point, dir)
			if input.grid[new_point[0]][new_point[1]] == "#":
				continue
			return new_point, dir
		return None, None
	
	path = []
	point = input.start
	price = 0
	direction = find_next_step(point, None)[1]
	while point != input.end:
		path.append([point, price])
		point, direction = find_next_step(point, direction)
		price += 1

	return path + [[input.end, price]]

def get_distance(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_points_within_radius(path, point1, radius):
	return {(point2, time2) for point2, time2 in path if get_distance(point1, point2) <= radius}

def cheat(path, benchmark_time, allowed_cheats):
	count = 0
	for index, (point1, time1) in enumerate(path):
		for point2, time2 in find_points_within_radius(path[index + 1:], point1, allowed_cheats):
			if time2 - time1 - get_distance(point1, point2) >= benchmark_time:
				count += 1
	return count

def part1(input):
	path = path_finder(input)

	if input.type == "Example":
		input.result = cheat(path, benchmark_time=1, allowed_cheats=2)
	else:
		input.result = cheat(path, benchmark_time=100, allowed_cheats=2)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	path = path_finder(input)

	if input.type == "Example":
		input.result = cheat(path, benchmark_time=50, allowed_cheats=20)
	else:
		input.result = cheat(path, benchmark_time=100, allowed_cheats=20)
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
		print("\033[1;91mSave puzzle input to",  INPUT_FILE_NAME, "\033[0m", file=sys.stderr)
		exit(1)
	
	if example: part1(example)
	part1(input)
	if example: part2(example)
	part2(input)
