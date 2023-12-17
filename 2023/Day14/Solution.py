###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#########################
## FUNCTION DEFINITION ##
#########################

def west(pattern):
    tilted = list()
    for line in pattern:
        new_line = line
        while ".O" in new_line:
            new_line = new_line.replace(".O", "O.")
        tilted.append(new_line)
    return tilted

def north(pattern):
    return [''.join(j) for j in zip(*west([''.join(i) for i in zip(*pattern)]))]

def east(pattern):
    tilted = list()
    for line in pattern:
        new_line = line
        while "O." in new_line:
            new_line = new_line.replace("O.", ".O")
        tilted.append(new_line)
    return tilted

def south(pattern):
    return [''.join(j) for j in zip(*east([''.join(i) for i in zip(*pattern)]))]

def load(pattern):
    return sum([line.count("O") * (len(pattern) - index) for index, line in enumerate(pattern)])

#####################
## PART 1 SOLUTION ##
#####################

print("Part 1 Solution: ", load(north(input)))

#####################
## PART 2 SOLUTION ##
#####################
pattern = input
for cycle in range(1000000000):
    pattern = east(south(west(north(pattern))))

print("Part 2 Solution: ", "in progress" )