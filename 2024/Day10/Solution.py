from os import path
import sys
import pprint as pp

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):
		with open(filename, 'r') as infile:
			content = infile.read()
		self.grid = [[int(num) for num in row] for row in content.splitlines()]
		self.rows = len(self.grid)
		self.cols = len(self.grid[0])
		self.trailheads = {(i, j) for i, row in enumerate(self.grid) for j, num in enumerate(row) if num == TRAIL_START}

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

TRAIL_START = 0
TRAIL_END = 9
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#####################
## PART 1 SOLUTION ##
#####################

def	is_on_grid(point, input):
	return point[0] in range(input.rows) and point[1] in range(input.cols)

def get_height(input, position):
	return input.grid[position[0]][position[1]]

def find_next_moves(input, curr_pos):

	""" Returns all vertical and horizontal neighbours that lay higher. """
	row, col = curr_pos
	moves = set()

	for x, y in DIRECTIONS:
		new_pos = (row + y, col + x)
		if is_on_grid(new_pos, input) and get_height(input, new_pos) == get_height(input, curr_pos) + 1:
			moves.add(new_pos)
	
	return moves

def find_trail(input, head):
	""" Following a trail from the head, on the way saving possible other trail options.
	 	Once a trail end is found or the trail doesn't lead to a trail end
		the other possibilities are discovered from their last position. 
		
		For Part1 the number of distinct trailends is returned.
		For Part2 the number of distinct trails is returned. """
	
	trail_ends = set()
	routes = 0

	trails_to_discover = [head]
	while trails_to_discover:
		last_pos = trails_to_discover.pop()
		while get_height(input, last_pos) != TRAIL_END:
			moves = find_next_moves(input, last_pos)
			if len(moves) == 0:
				break
			last_pos = moves.pop()
			while len(moves) > 0:
				trails_to_discover.append(moves.pop())
		if get_height(input, last_pos) == TRAIL_END:
			trail_ends.add(last_pos)
			routes += 1

	if input.part == 2:
		return routes
	return len(trail_ends)


def part1(input):
	
	input.result = sum(find_trail(input, head) for head in input.trailheads)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	input.part = 2
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
