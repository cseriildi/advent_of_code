###################
## INPUT PARSING ##
###################

def parse(filename):
	with open(filename, 'r') as infile:
		input = infile.read().split("\n\n")
		rules = [[int(i) for i in row.split("|")] for row in input[0].splitlines()]
		updates = [[int(i)for i in row.split(",")] for row in input[1].splitlines()]
		return rules, updates

#####################
## PART 1 SOLUTION ##
#####################

def is_correct(rules, update):

	return all([update[ind], update[ind + 1]] in rules for ind in range(len(update) - 1))

def get_middle(arr):
	return arr[len(arr) // 2]

def part1(input):
	rules, updates = input

	return sum(get_middle(update) for update in updates if is_correct(rules, update))

#####################
## PART 2 SOLUTION ##
#####################

def fix_update(rules, update):

	swapped = True
	while swapped:
		swapped = False
		for ind in range(len(update) - 1):
			if [update[ind + 1], update[ind]] in rules:
				update[ind], update[ind + 1] = update[ind + 1], update[ind]
				swapped = True

	return update

def part2(input):
	
	rules, updates = input

	return sum(get_middle(fix_update(rules, update)) for update in updates if not is_correct(rules, update))

if __name__ == "__main__":
	from os import path
	dirname = path.dirname(__file__)

	input = parse(dirname + "/input.txt")
	example = parse(dirname + "/example.txt")
	print("Part 1 Example: ", part1(example))
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Example: ", part2(example))
	print("Part 2 Solution: ", part2(input))
