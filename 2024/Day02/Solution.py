###################
## INPUT PARSING ##
###################

def parse():
	with open("input.txt", 'r') as infile:
		input = infile.read().splitlines()
		input = [[int(num) for num in row.split()] for row in input]
		return input

#####################
## PART 1 SOLUTION ##
#####################

def is_safe(report):

	dir = report[1] > report[0]
	for i in range(len(report) - 1):
		distance = report[i + 1] - report[i]
		if (abs(distance) not in range(1, 4)) or dir != (distance > 0):
			return False, i
	return True, 0

def part1(input):

	return sum(is_safe(report)[0] for report in input)

#####################
## PART 2 SOLUTION ##
#####################

def is_almost_safe(report):

	safe, j = is_safe(report)
	if safe:
		return True
	
	to_check = [report[:j] + report[j + 1:]] + [report[:j + 1] + report[j + 2:]]
	if j != 0:
		to_check += [report[1:]]

	return any(is_safe(alt)[0] for alt in to_check)

def part2(input):

	return sum(is_almost_safe(report) for report in input)


if __name__ == "__main__":
	input = parse()
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Solution: ", part2(input))
