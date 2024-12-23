from os import path
import sys
from collections import defaultdict
from itertools import combinations

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
		self.connections = [set(line.split("-")) for line in content.splitlines()]

	def print_solution(self):
		color = "\033[90m" if self.part == 1 else "\033[33m"
		print(f"{color}Part {self.part} {self.type}: {self.result}\033[0m")
		self.part += 1
		self.result = 0

#####################
## PART 1 SOLUTION ##
#####################

def find_groups_of_three(connections):
	""" Find at least 3 computers that are connected to each other """
	groups = set()
	for (a, b), (c, d) in combinations(connections, 2):
		if (a == c and {b, d} in connections) or (a == d and {b, c} in connections):
			groups.add(frozenset((a, b, c, d)))
	return groups

def group_has_computer_with_t(group):
	""" Check if any computer in the group starts with 't' """
	return any(computer.startswith('t') for computer in group)

def part1(input):
	input.result = sum(group_has_computer_with_t(group) for group in find_groups_of_three(input.connections))
	input.print_solution()

#####################
## PART 2 SOLUTION ##
#####################

def count_occurrences(networks, group):
	""" Count how many times the group appears in the networks """
	return sum(group.issubset(network) for network in networks)

def find_networks(connections):
	""" Find all connections between computers """
	networks = defaultdict(set)
	for a, b in connections:
		networks[a].add(a)
		networks[a].add(b)
		networks[b].add(b)
		networks[b].add(a)
	return networks.values()

def find_biggest_network(networks):
	""" Find the biggest fully connected network """
	max_len = max(len(network) for network in networks)

	while max_len > 1:
		for network in networks:
			for group in combinations(network, max_len):
				if count_occurrences(networks, set(group)) == max_len:
					return ','.join(sorted(group))
		max_len -= 1
	return ""

def part2(input):
	input.result = find_biggest_network(networks=find_networks(input.connections))
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
