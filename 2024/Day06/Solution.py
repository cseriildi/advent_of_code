###################
## INPUT PARSING ##
###################

def parse(filename):
	with open(filename, 'r') as infile:
		return [list(row) for row in infile.read().splitlines()]

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

DIRECTIONS = {
    "^": NORTH,
    "v": SOUTH,
    ">": EAST,
    "<": WEST,
}

CHANGE_DIR = {NORTH : EAST, EAST : SOUTH, SOUTH : WEST, WEST : NORTH}

#####################
## PART 1 SOLUTION ##
#####################


def move(guard, dir):
	return (guard[0] + dir[0], guard[1] + dir[1])

def is_in(rows, cols, position):

	return position[0] not in (0, rows - 1) and position[1] not in (0, cols - 1)

def find_guard(input):

	for i, row in enumerate(input):
		for j, element in enumerate(row):
			if element in DIRECTIONS.keys():
				return (i, j), DIRECTIONS[element]
			
def walk(input, rows, cols, guard, dir):

	visited = {(guard, dir)}
	
	while is_in(rows, cols, guard):
		plan = move(guard, dir)
		while input[plan[0]][plan[1]] == '#':
			dir = CHANGE_DIR[dir]
			plan = move(guard, dir)
		guard = plan
		if (guard, dir) in visited:
			return {}
		visited.add((guard, dir))

	return {pos[0] for pos in visited}

def part1(input):

	rows = len(input)
	cols = len(input[0])
	guard, dir = find_guard(input)	
		
	return len(walk(input, rows, cols, guard, dir))

#####################
## PART 2 SOLUTION ##
#####################

def part2(input):

	rows = len(input)
	cols = len(input[0])
	guard, dir = find_guard(input)

	to_check = walk(input, rows, cols, guard, dir)
	to_check.remove(guard)

	result = 0
	for row, col in to_check:
		input[row][col] = '#'
		result += walk(input, rows, cols, guard, dir) == {}
		input[row][col] = '.'

	return result

if __name__ == "__main__":
	input = parse("input.txt")
	example = parse("example.txt")
	print("Part 1 Example: ", part1(example))
	print("Part 1 Solution: ", part1(input))
	print("Part 2 Example: ", part2(example))
	print("Part 2 Solution: ", part2(input))
