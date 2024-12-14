from os import path
import sys
import re
from time import sleep
import random

###################
## INPUT PARSING ##
###################

COLORS = ['\033[31;1m', '\033[32;1m', '\033[33;1m', '\033[34;1m', '\033[35;1m', '\033[36;1m', '\033[37;1m']

class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.reset()

	def reset(self):
		self.char = '  '
		self.color = '\033[0m'
			
class Robot:
	def __init__(self, px, py, vx, vy):
		self.px = px
		self.py = py
		self.vx = vx
		self.vy = vy
		self.color = random.choice(COLORS)
		self.char = '██'

	def move(self, size):
		self.px = (self.px + self.vx) % size[0]
		self.py = (self.py + self.vy) % size[1]

class Data:
	def __init__(self, filename):

		self.filename = filename
		self.part = 1
		if filename == EXAMPLE_FILE_NAME:
			self.type = "Example"
			self.size = [11, 7]
			self.quadrant = [5, 3]

		elif filename == INPUT_FILE_NAME:
			self.type = "Solution"
			self.size = [101, 103]
			self.quadrant = [50, 51]

		self.printed = False
		self.result = 0
		self.parse_data()
		self.nb_of_robots = len(self.robots)
		self.grid = [[Cell(x, y) for x in range(self.size[0])] for y in range(self.size[1])]

	def __str__(self):
		return '\n'.join(''.join(cell.color + cell.char for cell in row) for row in self.grid)
	
	def parse_data(self):
		with open(self.filename, 'r') as infile:
			content = infile.read()
	
		self.robots = [Robot(*map(int, re.findall(r'[+-]?\d+', line))) for line in content.splitlines()]
		self.printed = False

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0
	
	def update_grid(self):
		if VISUALIZATION:
			for row in self.grid:
				for cell in row:
					if cell.x != self.quadrant[0] and cell.y != self.quadrant[1]:
						cell.reset()

		for robot in self.robots:
			robot.move(self.size)

			if VISUALIZATION and robot.px != self.quadrant[0] and robot.py != self.quadrant[1]:
				self.grid[robot.py][robot.px].char = robot.char
				self.grid[robot.py][robot.px].color = robot.color

	def set_quadrant_lines(self):
		for i in range(self.size[0]):
			self.grid[self.quadrant[1]][i].char = '██'
			self.grid[self.quadrant[1]][i].color = '\033[90m'
			
		for row in self.grid:
			row[self.quadrant[0]].char = '██'
			row[self.quadrant[0]].color = '\033[90m'

	def print_grid(self):
		if self.printed:
			for _ in range(self.size[1]):
				print("\033[A", end="\033[0m")
		else:
			self.printed = True
			self.set_quadrant_lines()

		print(self)

#####################
## PART 1 SOLUTION ##
#####################

def count_robots(input):
	
	q1, q2, q3, q4 = 0, 0, 0, 0

	for robot in input.robots:
		if robot.px < input.quadrant[0] and robot.py < input.quadrant[1]:
			q1 += 1
		elif robot.px > input.quadrant[0] and robot.py < input.quadrant[1]:
			q2 += 1
		elif robot.px < input.quadrant[0] and robot.py > input.quadrant[1]:
			q3 += 1
		elif robot.px > input.quadrant[0] and robot.py > input.quadrant[1]:
			q4 += 1

	return q1, q2, q3, q4


def part1(input):
	
	for _ in range(100):
		input.update_grid()

		if VISUALIZATION:
			input.print_grid()

	q1, q2, q3, q4 = count_robots(input)

	input.result = q1 * q2 * q3 * q4
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def is_cristmas_tree(input):
	return max(count_robots(input)) > input.nb_of_robots * 0.5

def part2(input):

	input.parse_data()
	input.part = 2
	input.update_grid()
	input.result += 1

	while is_cristmas_tree(input) == False:
		input.result += 1
		input.update_grid()
		
		if VISUALIZATION and input.result > VISUALIZE_ABOVE:
			input.print_grid()

	input.print_solution()

##########
## MAIN ##
##########

dirname = path.dirname(__file__)
EXAMPLE_FILE_NAME = path.join(dirname, "example.txt")
INPUT_FILE_NAME = path.join(dirname, "input.txt")

VISUALIZATION = True
VISUALIZE_ABOVE = 6500

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
