###################
## INPUT PARSING ##
###################

def parse():
	with open("input.txt", 'r') as infile:
		input = infile.read().split("\n\n")
		rules = [[int(i) for i in row.split("|")] for row in input[0].splitlines()]
		updates = [[int(i)for i in row.split(",")] for row in input[1].splitlines()]
		return rules, updates

#####################
## PART 1 SOLUTION ##
#####################

def is_correct(rules, update):

	return all(False for ind in range(len(update) - 1) if ([update[ind + 1], update[ind]] in rules))

def get_middle(arr):
	return arr[int(len(arr)/ 2)]

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
	input = parse()
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Solution: ", part2(input))
