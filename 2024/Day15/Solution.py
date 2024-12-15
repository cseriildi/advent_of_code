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
	
	def parse_data(self):
		with open(self.filename, 'r') as infile:
			content = infile.read()
	
		self.map, self.path = content.split("\n\n")
		if self.part == 2:
			self.map = self.map.replace("O", "[]").replace(".", "..").replace("#", "##").replace("@", "@.")
		self.map = np.array([list(row) for row in self.map.splitlines()])
		self.player = [i[0] for i in np.where(self.map == "@")]
		self.path = [DIRECTIONS[step] for step in self.path.replace("\n", "")]

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0
	
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = {">": RIGHT, "<": LEFT, "^": UP, "v": DOWN}

#####################
## PART 1 SOLUTION ##
#####################

def get_next(point, dir):
	return (point[0] + dir[0], point[1] + dir[1])

def get_prev(point, dir):
	return (point[0] - dir[0], point[1] - dir[1])

def get_map_value(map, point):
	return map[point[0], point[1]]

def set_map_value(map, point, value):
	map[point[0], point[1]] = value

def find_spot(input, step):

	i = 0
	plan = input.player
	while True:
		i += 1
		plan = get_next(plan, step)
		match get_map_value(input.map, plan):
			case "#":
				return 0
			case ".":
				return i
		
def move_ahead(input, step, place):
	goal = get_next(input.player, (step[0] * place, step[1] * place))
	plan = get_next(input.player, step)

	while goal != plan:
		prev = get_prev(goal, step)
		set_map_value(input.map, goal, get_map_value(input.map, prev))
		goal = prev

	set_map_value(input.map, input.player, ".")
	input.player = plan

def part1(input):

	for step in input.path:
		place = find_spot(input, step)
		if place: move_ahead(input, step, place)

	input.result = sum(x * 100  + y for x, y in zip(*np.where(input.map == "O")))
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def look_ahead(input, step, current):

	next = get_next(current, step)
	match get_map_value(input.map, next):
		case "#":
			return False
		case ".":
			return True
		case "[":
			pair = get_next(next, RIGHT)
			is_pushable = look_ahead(input, step, next)
			if pair != current:
				is_pushable &= look_ahead(input, step, pair)
			return is_pushable
		case "]":
			pair = get_next(next, LEFT)
			is_pushable = look_ahead(input, step, next)
			if pair != current:
				is_pushable &= look_ahead(input, step, pair)
			return is_pushable
	
def get_boxes(input, step):

	to_move = {tuple(input.player)}
	to_check = {tuple(input.player)}

	while to_check:
		current = to_check.pop()
		next = get_next(current, step)
		next_char = get_map_value(input.map, next)
		if next_char in "[]":
			if next not in to_move:
				to_check.add(next)
				to_move.add(next)
			if next_char == "[":
				pair = get_next(next, RIGHT)
			else:
				pair = get_next(next, LEFT)
			if pair != current and pair not in to_move:
				to_check.add(pair)
				to_move.add(pair)

	return to_move

def move_ahead2(input, step):
	to_move = get_boxes(input, step)
	all_to_move = copy.deepcopy(to_move)
	map = copy.deepcopy(input.map)

	while to_move:
		position = to_move.pop()
		plan = get_next(position, step)
		if get_prev(position, step) not in all_to_move:
			set_map_value(map, position, ".")
		set_map_value(map, plan, get_map_value(input.map, position))
	
	input.map = map
	input.player = get_next(input.player, step)
	
def part2(input):
	input.part = 2
	input.parse_data()

	for step in input.path:
		if look_ahead(input, step, input.player):
			move_ahead2(input, step)

	input.result = sum(x * 100  + y for x, y in zip(*np.where(input.map == "[")))
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
