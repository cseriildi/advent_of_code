from os import path
import sys
import re
from sympy import symbols, Eq, solve, Integer

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):
		with open(filename, 'r') as infile:
			content = infile.read()
		self.machines = content.split("\n\n")
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

def solve_equation_system(machine):
	x1, y1, x2, y2, prize1, prize2 = machine

	a, b = symbols('a b')

	equation1 = Eq(x1 * a + y1 * b, prize1)
	equation2 = Eq(x2 * a + y2 * b, prize2)

	solution = solve((equation1, equation2), (a, b))
	if isinstance(solution[a], Integer) and isinstance(solution[b], Integer):
		return solution[a], solution[b]
	return 0, 0

def parse_machine(machine, input):
	x1, x2, y1, y2, prize1, prize2 = map(int, re.findall(r'\d+', machine))

	if input.part == 2:
		prize1 += PRIZE_INCREMENT
		prize2 += PRIZE_INCREMENT

	return x1, y1, x2, y2, prize1, prize2

def part1(input):
	for machine in input.machines:
		a, b = solve_equation_system(parse_machine(machine, input))
		input.result += a * 3 + b
		
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

PRIZE_INCREMENT = 10000000000000

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
