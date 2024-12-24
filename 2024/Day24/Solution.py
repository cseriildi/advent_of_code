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
		self.variables  = {}
		vars, instr = content.split("\n\n")
		for line in vars.splitlines():
			var, val = line.split(": ")
			self.variables[var] = int(val)
		self.instructions =  []
		for line in instr.splitlines():
			operation, result = line.split(" -> ")
			var1, op, var2 = operation.split(" ")
			self.instructions.append([result, var1, op, var2])

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

def find_var_to_calc(instr, vars):
	for index, (_, var1, _, var2) in enumerate(instr):
		if var1 in vars.keys() and var2 in vars.keys():
			return instr.pop(index)
	return ()

def do_calculation(instr, vars):
	while instr:
		element = find_var_to_calc(instr, vars)
		if not element:
			break
		result, var1, op, var2 = element
		if op == "AND":
			vars[result] = vars[var1] & vars[var2]
		elif op == "OR":
			vars[result] = vars[var1] | vars[var2]
		elif op == "XOR":
			vars[result] = vars[var1] ^ vars[var2]

def get_bits(vars, var):
	return sorted([k for k in vars.keys() if k.startswith(var)], reverse=True)

def get_value(vars, var):
	bin = ''.join(str(vars[bit]) for bit in get_bits(vars, var))
	return int(bin, 2)

def part1(input):
	do_calculation(input.instructions, input.variables)
	input.result = get_value(input.variables, "z")
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

from itertools import combinations

def part2(input):
	input.parse_data()

	inst = [row[:] for row in input.instructions]
	vars = {key: value for key, value in input.variables.items()}

	for pairs in combinations(list(combinations(range(len(inst)), 2)), 2):
		if len({x for pair in pairs for x in pair}) == 4:
			(a, b), (c, d) = pairs#, (e, f), (g, h) = pairs
			input.result = ','.join(sorted([inst[a][0], inst[b][0], inst[c][0], inst[d][0]]))#, inst[e][0], inst[f][0], inst[g][0], inst[h][0]]))
			inst[a][0], inst[b][0] = inst[b][0], inst[a][0]
			inst[c][0], inst[d][0] = inst[d][0], inst[c][0]
			#inst[e][0], inst[f][0] = inst[f][0], inst[e][0]
			#inst[g][0], inst[h][0] = inst[h][0], inst[g][0]
			do_calculation(inst, vars)
			if get_value(vars, "z") == get_value(vars, "x") & get_value(vars, "y"):
				break
			inst = [row[:] for row in input.instructions]
			vars = {key: value for key, value in input.variables.items()}
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
