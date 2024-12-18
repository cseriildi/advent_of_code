from os import path
import sys
import numpy as np
from heapq import heappush, heappop

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
		self.result = ""
		self.start = (0, 0)
		if filename == EXAMPLE_FILE_NAME:
			self.end = (6, 6)
			self.firstx = 12
		else:
			self.end = (70, 70)
			self.firstx = 1024
		self.parse_data()
		self.grid = np.full((self.end[1] + 1, self.end[0] + 1), ".", dtype="<U1")
		self.grid[tuple(zip(*self.drops[:self.firstx]))] = "#"
		self.rows, self.cols = self.grid.shape
		self.total_drop_count = len(self.drops)

	def parse_data(self):
		with open(self.filename, 'r') as infile:
			content = infile.read()
		self.drops = [tuple(map(int, row.split(","))) for row in content.splitlines()]


	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = ""
	
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

#####################
## PART 1 SOLUTION ##
#####################

def path_finder(input, min_price):
	def on_board(point):
		return 0 <= point[0] < input.rows and 0 <= point[1] < input.cols

	def move(point, dir):
		return (point[0] + dir[0], point[1] + dir[1])

	def is_obstacle(point):
		return input.grid[point] == "#"


	def save_neighbours():
		for direction in DIRECTIONS:
			new_point = move(point, direction)
			if new_point not in visited and on_board(new_point) and not is_obstacle(new_point):
				heappush(to_check, (price, new_point))
		
	to_check = [(0, input.start)]
	visited = set()

	while to_check:
		price, point = heappop(to_check)
		state = point
		if state in visited:
			continue
		visited.add(state)

		if point == input.end:
			min_price = min(price, min_price)
			if input.part == 2:
				return price
		else:
			price += 1
			save_neighbours()

	return min_price

def part1(input):

	input.result = str(path_finder(input, input.end[0] * input.end[1]))
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	input.part = 2

	def place_new_drop(drop_count):
		drop_x, drop_y = input.drops[drop_count]
		input.grid[drop_x][drop_y] = "#"
		return drop_count + 1

	drop_count = input.firstx
	place_new_drop(drop_count)
	min_price = input.end[0] * input.end[1]
	while drop_count < input.total_drop_count and path_finder(input, min_price) < min_price:
		drop_count = place_new_drop(drop_count)

	input.result = ','.join(map(str, input.drops[drop_count - 1]))
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
