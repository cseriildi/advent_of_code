###################
## INPUT PARSING ##
###################

def parse(filename):
	with open(filename, 'r') as infile:
		lines = [line.split(": ") for line in infile.read().splitlines()]
	results = [int(line[0]) for line in lines]
	nums = [[int(num) for num in line[1].split(" ")] for line in lines]
	return results, nums

#####################
## PART 1 SOLUTION ##
#####################

def add(num1, num2):
	return num1 + num2

def mul(num1, num2):
	return num1 * num2

def combine(num1, num2):
	return int(str(num1) + str(num2))

def can_produce_result(result, nums, to_combine=False):

	results = {}
	for num in nums:
		if not results:
			results = {num}
			continue
		curr = set()
		for prev_num in results:
			if prev_num <= result:
				curr.add(add(prev_num, num))
				curr.add(mul(prev_num, num))
				if to_combine:
					curr.add(combine(prev_num, num))
		if not curr:
			return False
		results = curr

	return result in results

def part1(input):
	results, nums = input
		
	return sum(result for i, result in enumerate(results) if can_produce_result(result, nums[i]))

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	results, nums = input
		
	return sum(result for i, result in enumerate(results) if can_produce_result(result, nums[i], True))

if __name__ == "__main__":
	from os import path
	dirname = path.dirname(__file__)

	input = parse(dirname + "/input.txt")
	#example = parse(dirname + "/example.txt")
	
#print("Part 1 Example: ", part1(example))
	print("Part 1 Solution: ", part1(input))
#	print("Part 2 Example: ", part2(example))
	print("Part 2 Solution: ", part2(input))
