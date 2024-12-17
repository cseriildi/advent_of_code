from os import path
import sys
import re

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
		self.result = ""
		self.parse_data()
		self.program_len = len(self.program)
		self.program_str = ','.join([str(i) for i in self.program])
	
	def parse_data(self):
		with open(self.filename, 'r') as infile:
			self.A = int(re.search(r'\d+', infile.readline()).group(0))
			self.B = int(re.search(r'\d+', infile.readline()).group(0))
			self.C = int(re.search(r'\d+', infile.readline()).group(0))
			self.program = [int(i) for i in re.findall(r'\d+', infile.read())]
	
	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = ""

#####################
## PART 1 SOLUTION ##
#####################

def adv(nominator, denominator):
	return nominator >> denominator

def xor(a, b):
	return a ^ b

def mod8(num):
	return num & 7

def get_combo(operand, A, B, C):

	if operand in range(4):
		return operand
	elif operand == 4:
		return A
	elif operand == 5:
		return B
	elif operand == 6:
		return C

def execute(input, A, B, C):

	result = []
	i = 0
	while i < input.program_len:
		opcode = input.program[i]
		literal_operand = input.program[i+1]
		i += 2
		match opcode:
			case 0: #adv
				A = adv(A, get_combo(literal_operand, A, B, C))
			case 1: #bxl
				B = xor(B,literal_operand)
			case 2: #bst
				B = mod8( get_combo(literal_operand, A, B, C))
			case 3: #jnz
				if A != 0:
					i = literal_operand
			case 4: #bxc
				B = xor(B, C)
			case 5: #out
				result.append(mod8( get_combo(literal_operand, A, B, C)))
			case 6: #bdv
				B = adv(A,  get_combo(literal_operand, A, B, C))
			case 7: #cdv
				C = adv(A,  get_combo(literal_operand, A, B, C))
	return result

def part1(input):

	input.result = ','.join([str(num) for num in execute(input, input.A, input.B, input.C)])
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################


def compute_minA(input):
	min_A = 8 ** (input.program_len)
	to_check = [[0, 1]]
	while to_check:
		A, char = to_check.pop()
		for A in range(A, A + 8):
			result = execute(input, A, input.B, input.C)
			if result == input.program[-char:]:
				to_check.append([A * 8, char + 1])
			if result == input.program and A < min_A:
				min_A = A
	return str(min_A)

def part2(input):

	input.result = compute_minA(input)
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
