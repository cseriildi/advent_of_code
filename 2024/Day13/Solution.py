from os import path
import sys
import numpy as np
import re

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

def find_combo(ax, ay, bx, by, pricex, pricey, input):

	if input.part == 1:
		a = [i for i in range(100)]
		#min(101, pricex // ax, pricey // ay))]
		b = [i for i in range(100)]
		#min(101, pricex // bx, pricey // by))]
	else:
		a = [i for i in range(min(pricex // ax, pricey // ay), 0, -1)]
		b = [i for i in range(min(101, pricex // bx, pricey // by), 0, -1)]

	needed_a = -1
	needed_b = -1


	for i in a:
		for j in b:
			if i * ax + j * bx == pricex and i * ay + j * by == pricey:
				needed_a = i
				needed_b = j
				break
	return needed_a, needed_b,


def parse_machine(machine):
	a, b, price = machine.split("\n")
	ax, ay = a.split(",")
	ax = int(''.join(re.findall(r'\d', ax)))
	ay = int(''.join(re.findall(r'\d', ay)))
	bx, by = b.split(",")
	bx = int(''.join(re.findall(r'\d', bx)))
	by = int(''.join(re.findall(r'\d', by)))
	pricex, pricey = price.split(",")
	pricex = int(''.join(re.findall(r'\d', pricex)))
	pricey = int(''.join(re.findall(r'\d', pricey)))

	return ax, ay, bx, by, pricex, pricey


def part1(input):

	for machine in input.machines:
		ax, ay, bx, by, pricex, pricey = parse_machine(machine)

		a, b = find_combo(ax, ay, bx, by, pricex, pricey, input)
		if a != -1 and b != -1:
			input.result += a * 3 + b
		
	
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	for machine in input.machines:
		ax, ay, bx, by, pricex, pricey = parse_machine(machine)

		pricex += 10000000000000
		pricey += 10000000000000
		a, b = find_combo(ax, ay, bx, by, pricex, pricey, input)
		if a != -1 and b != -1:
			input.result += a * 3 + b
		
	
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
