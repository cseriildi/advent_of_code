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
	return int(str(num1)  + str(num2))

def is_good(result, nums, to_combine=False):

	results = {nums[0]}
	for i in range(1, len(nums)):
		curr = set()
		for num in results:
			curr.add(add(num, nums[i]))
			curr.add(mul(num, nums[i]))
			if to_combine:
				curr.add(combine(num, nums[i]))
		results = curr

	return result in results

def part1(input):
	results, nums = input
		
	return sum(result for i, result in enumerate(results) if is_good(result, nums[i]))

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):
	results, nums = input
		
	return sum(result for i, result in enumerate(results) if is_good(result, nums[i], True))

if __name__ == "__main__":
	input = parse("input.txt")
	example = parse("example.txt")
	print("Part 1 Example: ", part1(example))
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Example: ", part2(example))
	print("Part 2 Solution: ", part2(input))
