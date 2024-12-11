from os import path
import sys
import math
from functools import cache

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):
		with open(filename, 'r') as infile:
			content = infile.read()
		self.stones = [int(num) for num in content.strip('\n').split()]
		self.nm_of_stones = len(self.stones)

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

#####################
## PART 1 SOLUTION ##
#####################

@cache
def len_of_int(stone):
	return int(math.log10(stone)) + 1 if stone > 0 else 1

@cache
def split_num_in_half(num, stone_len):

	divisor = 10 ** (stone_len // 2)
	left = num // divisor
	right = num % divisor
	return [left, right]

@cache
def get_new_stones(stone):
	
	stone_len = len_of_int(stone)
	if stone == 0:
		return [1]
	elif stone_len % 2 == 0:
		return split_num_in_half(stone, stone_len)
	else:
		return [stone * 2024]

@cache
def blink(stone, level):
	count = 1
	while level > 0:
		level -= 1
		stone_len = len_of_int(stone)
		if stone == 0:
			stone = 1
		elif stone_len % 2 == 0:
			stone, right = split_num_in_half(stone, stone_len)
			count += blink(right, level)
		else:
			stone *= 2024
	return count

def part1(input):
	input.result = sum(blink(stone, 25) for stone in input.stones)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	input.result = sum(blink(stone, 75) for stone in input.stones)
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
