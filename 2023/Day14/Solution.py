###############
## IMPORTING ##
###############

import numpy as np

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#####################
## PART 1 SOLUTION ##
#####################

transposed = [''.join(i) for i in zip(*input)]

tilted = list()
for line in transposed:
    new_line = line
    while ".O" in new_line:
        new_line = new_line.replace(".O", "O.")

    tilted.append(new_line)
tilted = [''.join(i) for i in zip(*tilted)]

load = sum([line.count("O") * (len(tilted) - index) for index, line in enumerate(tilted)])

print("Part 1 Solution: ", load)

#####################
## PART 2 SOLUTION ##
#####################

print("Part 2 Solution: ", "in progress...")