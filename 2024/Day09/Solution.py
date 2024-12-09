from os import path
import sys

###################
## INPUT PARSING ##
###################

class Data:
	def __init__(self, filename):
		with open(filename, 'r') as infile:
			content = infile.read()

		self.line = [int(num) for num in content.strip("\n")]
		self.len = len(self.line)
		
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

def part1(input):

	new_line = []
	index = 0
	for i, num in enumerate(input.line):
		if i % 2 == 0:
			new_line.extend([index] * num)
			index += 1
		else:
			new_line.extend(['.'] * num)

	for i, value in enumerate(new_line):
		while new_line[-1] == '.':
			new_line.pop()
		if value == '.':
			new_line[i] = new_line.pop()

	input.result = sum(i * num for i, num in enumerate(new_line))
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	
	MEM = 0
	SPACE = 1
	new_line = []
	index = 0
	for i, num in enumerate(input.line):
		if i % 2 == 0:
			new_line.append((MEM, num, index))
			index += 1
		else:
			new_line.append((SPACE, num))

	mem_index = len(new_line) -1

	while mem_index > 0:
		mem = new_line[mem_index]
		if mem[0] == MEM:
			for space_index, space in enumerate(new_line):
				if mem_index <= space_index:
					mem_index -= 1
					break
				if space[0] == SPACE:
					if mem[1] <= space[1]:
						new_line[space_index] = (SPACE, space[1] - mem[1])
						new_line.insert(space_index, new_line.pop(mem_index))
						new_line.insert(mem_index, (SPACE, new_line[space_index][1]))
						break
		else:
			mem_index -= 1

	index = 0
	result = 0
	for element in new_line:
		if element[0] == SPACE:
			index += element[1]
		else:
			for _ in range(element[1]):
				result += (index * element[2])
				index += 1

	input.result = result
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
