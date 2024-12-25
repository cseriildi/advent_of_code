from os import path
import sys

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
		self.schematics  = content.split("\n\n")

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

def is_valid_key(key, lock):
	for i in range(len(lock)):
		for j in range(len(lock[i])):
			if lock[i][j] == '#' and key[i][j] == '#':
				return False
	return True

def part1(input):

	locks = []
	keys = []
	for schematics in input.schematics:
		sc = [list(row) for row in schematics.splitlines()]
		if '.' not in sc[0]:
			locks.append(sc)
		else:
			keys.append(sc)

	input.result = sum(is_valid_key(key, lock) for key in keys for lock in locks)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	input.result = "You only need to solve Part 1 for this day, sadly"
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
