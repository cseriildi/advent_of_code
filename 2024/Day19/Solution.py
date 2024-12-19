from os import path
import sys
from functools import cache

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
		self.towels, self.patterns = content.split('\n\n')
		self.towels = set(self.towels.split(', '))
		self.patterns = self.patterns.splitlines()

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

def is_possible(towels, pattern):

	length = len(pattern) - 1
	towels = {t for t in towels if t in pattern}
	i = 0
	to_check = {(t, i) for t in towels if t == pattern[i : i + len(t)]}
	while to_check:
		towel, i = to_check.pop()
		i += len(towel)
		if i == length:
			return True
		to_check |=  {(t, i) for t in towels if t == pattern[i : i + len(t)]}

	return False

def part1(input):

	input.result = sum([is_possible(input.towels, pattern) for pattern in input.patterns])
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def count_all_possibilities(towels, pattern):

	@cache
	def count_possibilities_from_index(i):
		if i == length:
			return 1
		return sum(count_possibilities_from_index(i + len(towel)) for towel in matching_towels[i])
	
	length = len(pattern)
	towels = {t for t in towels if t in pattern}
	matching_towels = {i: [] for i in range(length)}
	for i in range(length):
		for towel in towels:
			if pattern[i:i + len(towel)] == towel:
				matching_towels[i].append(towel)

	return count_possibilities_from_index(0)

def part2(input):

	input.result = sum([count_all_possibilities(input.towels, pattern) for pattern in input.patterns])
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
