from os import path
import sys
import numpy as np

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):
		with open(filename, 'r') as infile:
			content = infile.read()
		self.grid = np.array([list(row) for row in content.splitlines()])
		self.rows, self.cols = self.grid.shape
	
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

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

#####################
## PART 1 SOLUTION ##
#####################

def is_on_grid(plot, input):
	return plot[0] in range(input.rows) and plot[1] in range(input.cols)

def is_same_plant(input, plot1, plot2):
	return is_on_grid(plot2, input) and input.grid[plot1[0]][plot1[1]] == input.grid[plot2[0]][plot2[1]]

def is_in_same_region(plot, plot2, input, region):
	return plot2 not in region and is_same_plant(input, plot, plot2)

def move(point, dir):
	return (point[0] + dir[0], point[1] + dir[1])

def is_upper_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(plant, UP))

def is_lower_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(plant, DOWN))

def is_left_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(plant, LEFT))

def is_right_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(plant, RIGHT))

def is_upper_left_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(move(plant, UP), LEFT))

def is_upper_right_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(move(plant, UP), RIGHT))

def is_lower_left_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(move(plant, DOWN), LEFT))

def is_lower_right_not_in_region(input, plant):
	return not is_same_plant(input, plant, move(move(plant, DOWN), RIGHT))

def find_region(input, plant):

	""" Find all plants in the same region as the given plant"""

	region = {plant}
	to_check = {plant}
	while to_check:
		plot = to_check.pop()
		for dir in DIRECTIONS:
			plot2 = move(plot, dir)
			if is_in_same_region(plot, plot2, input, region):
				region.add(plot2)
				to_check.add(plot2)

	return region

def get_region_price(region, input):

	""" Calculate the price of the fence around a region of plants
	In part1, the fence price is the count of the fence units multiplied by the number of plants in the region
	In part2, the fence price is the count of (in one direction) continous fences multiplied by the number of plants in the region"""

	count = 0
	fence = 0
	for plant in region:
		count += 1
		if input.part == 1:
			fence += is_upper_not_in_region(input, plant)
			fence += is_lower_not_in_region(input, plant)
			fence += is_left_not_in_region(input, plant)
			fence += is_right_not_in_region(input, plant)
		else:
			fence += is_upper_not_in_region(input, plant) and is_left_not_in_region(input, plant) == is_upper_left_not_in_region(input, plant)
			fence += is_lower_not_in_region(input, plant) and is_left_not_in_region(input, plant) == is_lower_left_not_in_region(input, plant)
			fence += is_left_not_in_region(input, plant) and is_upper_not_in_region(input, plant) == is_upper_left_not_in_region(input, plant)
			fence += is_right_not_in_region(input, plant) and is_upper_not_in_region(input, plant) == is_upper_right_not_in_region(input, plant)
	return count * fence

def part1(input):

	""" Find all regions of plants and calculate the price of the fence around each region
	A region is a group of plants that are connected to each other by sharing a side and have the same plant type"""

	to_check = {(i, j) for i in range(input.rows) for j in range(input.cols)}

	while to_check:
		plant = to_check.pop()
		region = find_region(input, plant)
		to_check -= region
		input.result += get_region_price(region, input)

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
