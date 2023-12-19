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

def cycling(pattern):
    return east(south(west(north(pattern)))) 

def load(pattern):
    return sum([line.count("O") * index for index, line in enumerate(reversed(pattern), start = 1)])

#####################
## PART 1 SOLUTION ##
#####################

print("Part 1 Solution: ", load(north(input)))

#####################
## PART 2 SOLUTION ##
#####################

pattern_changes = [input]

while len(pattern_changes) < 1000000000:
    pattern = cycling(pattern_changes[-1])

    if pattern in pattern_changes:
        break
    pattern_changes.append(pattern)

sequence_start = pattern_changes.index(pattern) 
sequence_end = len(pattern_changes) 
sequence_length = sequence_end - sequence_start 

print("Part 2 Solution: ", load(pattern_changes[(1000000000 - sequence_start) % sequence_length + sequence_start]))