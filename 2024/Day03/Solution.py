###################
## INPUT PARSING ##
###################

def parse():
	with open("input.txt", 'r') as infile:
		input = infile.read()
		return input

#####################
## PART 1 SOLUTION ##
#####################

def get_mul(str):

	end = str.find(")")
	if end != -1:
		mul = str[:end].split(",")

		if len(mul) == 2 and all(num.isdigit() for num in mul):
			return int(mul[0]) * int(mul[1])
	return 0
	
def part1(input):

	return sum(get_mul(mul) for mul in input[input.find("mul("):].split("mul("))

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	result = 0
	do = 0
	while do != -1:
		dont = input.find("don't()", do)
		result += part1(input[do:dont])
		if dont == -1:
			break
		do = input.find("do()", dont + 7)

	return result

if __name__ == "__main__":
	input = parse()
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Solution: ", part2(input))
