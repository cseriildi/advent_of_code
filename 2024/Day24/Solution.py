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

def create_dot_file(inst, vars):
	with open("graph.dot", "w") as dotfile:
		dotfile.write("digraph G {\n")
		for var, value in vars.items():
			dotfile.write(f'  "{var}"[label="{var}", fontcolor="{"red" if value == 1 else "blue"}"];\n')
		
		for result, var1, op, var2 in inst:
			dotfile.write(f'  "{var1}" -> "{result}"[label="{op}", color="{"red" if vars[var1] == 1 else "blue"}"];\n')
			dotfile.write(f'  "{var2}" -> "{result}"[label="{op}", color="{"red" if vars[var2] == 1 else "blue"}"];\n')
		dotfile.write("}\n")

def find_wrong_ones(vars):
	x_s = get_bits(vars, "x")
	y_s = get_bits(vars, "y")
	z_s = get_bits(vars, "z")
	remainder = 0
	z = ""
	actual_z = ''.join(str(vars[bit]) for bit in z_s)
	for x, y in zip(x_s[::-1], y_s[::-1]):
		z = str((vars[x] + vars[y] + remainder) % 2) + z
		remainder =  (vars[x] + vars[y] + remainder) > 1
	if remainder:
		z = "1" + z
	for z1, z2 in zip(z, actual_z):
		if z1 != z2:
			print("\033[91m", end="")
		print(z1, end="\033[0m")
	print()

def part2(input):
	input.parse_data()

	inst = [row[:] for row in input.instructions]
	do_calculation(input.instructions, input.variables)
	create_dot_file(inst, input.variables)

	find_wrong_ones(input.variables)
	input.result = "I solved this manually, using dot visualization, will code it later"
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
