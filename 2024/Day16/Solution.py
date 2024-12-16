from os import path
import sys
import numpy as np
import copy

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):

		self.filename = filename
		self.part = 1
		if filename == EXAMPLE_FILE_NAME:
			self.type = "Example"
		elif filename == INPUT_FILE_NAME:
			self.type = "Solution"
		self.result = 0
		self.parse_data()
		self.rows, self.cols = self.grid.shape
	
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
	
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

NEXT = {
	UP: {UP, LEFT, RIGHT},
	DOWN: {DOWN, LEFT, RIGHT},
	LEFT: {LEFT, UP, DOWN},
	RIGHT: {RIGHT, UP, DOWN}
}

#####################
## PART 1 SOLUTION ##
#####################
from heapq import heappush, heappop
import copy

def on_board(input, point):
	return 0 <= point[0] < input.rows and 0 <= point[1] < input.cols

def move(point, dir):
	return (point[0] + dir[0], point[1] + dir[1])

def get_min_price(input):
	to_check = [(0, input.start, RIGHT, [])]
	visited = set()
	min_price = 10000000
	ulimate_path = []

	while to_check:
		price, point, last_direction, path = heappop(to_check)

		state = (point, last_direction)
		if state in visited:
			continue
		visited.add(state)
		path.append(point)

		if point == input.end:
			if price < min_price:
				min_price = price
			if price == min_price:
				ulimate_path = path.copy()
			continue

		for direction in NEXT[last_direction]:
			new_point = move(point, direction)
			if not on_board(input, new_point) or input.grid[new_point[0]][new_point[1]] == "#":
				continue

			new_price = price + 1
			if last_direction != direction:
				new_price += 1000

			heappush(to_check, (new_price, new_point, direction, path.copy()))
	
	""" 	for i in range(input.rows):
		for j in range(input.cols):
			if (i, j) in ulimate_path:
				print("O", end="")
			else:
				print(input.grid[i][j], end="")
		print() """

	return min_price

def part1(input):
	input.result = get_min_price(input)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def get_min_path(input):

	path_counter = 0
	to_check = [(0, input.start, [], RIGHT)]
	min_price = get_min_price(input)
	point = input.start
	while to_check:

		price, point, path, last_direction = heappop(to_check)
		path.append(point)
		for direction in DIRECTIONS:
			new_point = move(point, direction)
			if not on_board(input, new_point) or input.grid[new_point[0]][new_point[1]] in "#x":
				continue
			if new_point in path:
				continue
			new_price = price + 1
			if last_direction != direction:
				new_price += 1000
			if new_price > min_price:
				continue
			if new_point == input.end:
				if new_price == min_price:
					path.append(new_point)
					for x, y in path:
						input.grid[x][y] = "O"
					path_counter += 1
					print("Path found", path_counter)
				continue
			heappush(to_check, (new_price, new_point, path.copy(), direction))

def part2(input):

	get_min_path(input)

	for row in input.grid:
		for cell in row:
			if cell == "O":
				input.result += 1

	input.print_solution()

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
