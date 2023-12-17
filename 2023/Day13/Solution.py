###############
## IMPORTING ##
###############

import numpy as np

###################
## INPUT PARSING ##
###################

# Get the input from https://adventofcode.com/2023/day/13
f = open('input.txt', 'r')
input = ([np.array([list(map(int, line.replace(".", "0").replace("#", "1" ))) for line in i.splitlines()]) for i in f.read().split("\n\n")])

#########################
## FUNCTION DEFINITION ##
#########################

def find_symmetry(pattern, differences = 0):

    for index in range(len(pattern) - 1):
            slice1 = pattern[max(0, 2 * (index + 1) - len(pattern) ) : index + 1]
            slice2 = np.flipud(pattern[index + 1 : min(2 * (index + 1), len(pattern))])
            subtract = list((slice1 - slice2).flatten())

            if len(subtract) - subtract.count(0) == differences:
                return index + 1

#####################
## PART 1 SOLUTION ##
#####################
            
sum = 0                
for pattern in input:
    if find_symmetry(pattern) == None:
         sum += find_symmetry(pattern.transpose()) 
    else:
         sum += find_symmetry(pattern) * 100

print("Part 1 Solution: ", sum)

#####################
## PART 2 SOLUTION ##
#####################

smudges = 1

sum = 0                
for pattern in input:
    if find_symmetry(pattern, smudges) == None:
         sum += find_symmetry(pattern.transpose(), smudges) 
    else:
         sum += find_symmetry(pattern, smudges) * 100

print("Part 2 Solution: ", sum)