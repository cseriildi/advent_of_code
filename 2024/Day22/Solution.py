from os import path
import sys
from collections import defaultdict

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

		self.secret_numbers = [int(num) for num in content.splitlines()]

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

def mix(num, secret_num):
	return num ^ secret_num

def prune(num):
	return num % 16777216

def get_new_num(num):
	num = mix(num * 64, num)
	num = prune(num)
	num = mix(num // 32, num)
	num = prune(num)
	num = mix(num * 2048, num)
	num = prune(num)
	return num

def calculate_new_secret_number(num, count):
	while count > 0:
		num = get_new_num(num)
		count -= 1
	return num

def part1(input):
	input.result = sum(calculate_new_secret_number(num, 2000) for num in input.secret_numbers)
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################
def generate_sequances(num, count, monkey_book):
	
	prev = num % 10
	sequences = set()
	seq = ()
	while count > 0:
		
		num = get_new_num(num)
		last = num % 10
		s = last - prev
		if len(seq) == 4:
			seq = seq[1:] + (s,)
			if seq not in sequences:
				monkey_book[seq] += last
				sequences.add(seq)
		else:
			seq += (s,)
		prev = last
		count -= 1

def part2(input):

	monkey_book = defaultdict(int)
	for num in input.secret_numbers:
		generate_sequances(num, 2000, monkey_book)

	input.result = max(monkey_book.values())
	input.print_solution()

##########
## MAIN ##
##########

dirname = path.dirname(__file__)
EXAMPLE_FILE_NAME = path.join(dirname, "example.txt")
EXAMPLE_FILE_NAME2 = path.join(dirname, "example2.txt")
INPUT_FILE_NAME = path.join(dirname, "input.txt")

if __name__ == "__main__":
	
	try:
		example1 = Data(EXAMPLE_FILE_NAME, "Example")
	except:
		example1 = False
		print("\033[1;91mSave puzzle example to", EXAMPLE_FILE_NAME, "\033[0m", file=sys.stderr)
	
	try:
		example2 = Data(EXAMPLE_FILE_NAME2, "Example")
		example2.part = 2
	except:
		example2 = False
		print("\033[1;91mSave puzzle example to", EXAMPLE_FILE_NAME2, "\033[0m", file=sys.stderr)
	
	try:
		input = Data(INPUT_FILE_NAME, "Solution")
	except:
		print("\033[1;91mSave puzzle input to", INPUT_FILE_NAME, "\033[0m", file=sys.stderr)
		sys.exit(1)

	if example1: part1(example1)
	part1(input)
	if example2: part2(example2)
	part2(input)
