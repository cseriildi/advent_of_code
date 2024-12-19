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
	to_check = [(0, input.start, RIGHT)]
	visited = set()
	min_price = input.rows * input.cols * 1000

	while to_check:
		price, point, last_direction = heappop(to_check)

		state = (point, last_direction)
		if state in visited:
			continue
		visited.add(state)
		if point == input.end:
			if price < min_price:
				min_price = price
			continue
		for direction in NEXT[last_direction]:
			new_point = move(point, direction)
			if not on_board(input, new_point) or input.grid[new_point[0]][new_point[1]] == "#":
				continue
			new_price = price + 1
			if last_direction != direction:
				new_price += 1000
			heappush(to_check, (new_price, new_point, direction))

	return min_price

def part1(input):
	input.result = get_min_price(input)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def remove_dead_ends(input):

	def is_dead_end(point):
		if input.grid[point] != ".":
			return False, ()
		neighbors_coords = [move(point, direction) for direction in DIRECTIONS]
		neighbors = [input.grid[coord] for coord in neighbors_coords]
		if neighbors.count(".") == 0:
			return True, ()
		elif neighbors.count(".") == 1 and "S" not in neighbors and "E" not in neighbors:
			return True, neighbors_coords[neighbors.index(".")]
		return False, ()

	def find_dead_ends():
		dead_ends = set()
		for i in range(1, input.rows - 1):
			for j in range(1, input.cols - 1):
				point = (i, j)
				dead_end, neighbor = is_dead_end(point)
				if dead_end: dead_ends.add((point, neighbor))
		return dead_ends
	
	to_check = find_dead_ends()
	while to_check:
		point, neighbor = to_check.pop()
		input.grid[point] = "x"
		if neighbor:
			dead, new = is_dead_end(neighbor)
			if dead: to_check.add((neighbor, new))

def get_min_path(input):

	def get_min_additional_price(point, direction):
		addition = 0
		v = (point[0] - input.end[0], point[1] - input.end[1])
		addition += abs(v[0]) + abs(v[1])
		if addition == 0: return 0
		if (direction == UP and v[1] != 0) or (direction == RIGHT and v[0] != 0):
			addition += 1000
		elif direction in (DOWN, LEFT):
			addition += 2000
		return addition

	def get_neighbours(point, last_direction, price):
		neighbours = []
		for direction in NEXT[last_direction]:
			new_point = move(point, direction)
			if not on_board(input, new_point) or input.grid[new_point[0]][new_point[1]] in "#x":
				continue
			new_price = price + 1
			if last_direction != direction:
				new_price += 1000
			if new_price + get_min_additional_price(new_point, direction) > min_price:
				continue
			matches = [tup[2] for tup in visited if tup[:2] == (new_point, last_direction)]
			if matches and new_price > min(matches):
				continue
			visited.add((new_point, last_direction, new_price))
			neighbours.append((new_point, direction, new_price))
		return neighbours

	to_check = [(0, input.start, set(), RIGHT)]
	min_price = get_min_price(input)
	point = input.start
	min_points = set()
	visited = set()
	while to_check:
		price, point, path, last_direction = heappop(to_check)
		path.add(point)
		directions = get_neighbours(point, last_direction, price)
		while len(directions) == 1:
			new_point, direction, new_price = directions[0]
			if new_point == input.end:
				break
			path.add(new_point)
			directions = get_neighbours(new_point, direction, new_price)
		
		for new_point, direction, new_price in directions:
			if new_point == input.end:
				if new_price == min_price:
					path.add(new_point)
					min_points |= path
				continue
			heappush(to_check, (new_price, new_point, path.copy(), direction))
	return min_points

def part2(input):

	remove_dead_ends(input)
	input.result = len(get_min_path(input))
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
	print("Part 2 takes approximately 1.15 minute to complete.")
	part2(input)
