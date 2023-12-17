###############
## IMPORTING ##
###############

import math

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

# Renaming the left/right direction to 0/1 for easier usage
direction = input[0].replace("L", "0").replace("R", "1")

map = dict()
for i in input[2:]:
    map[i.split(" = ")[0]]= [i.split(" = ")[1][1:4], i.split(" = ")[1][6:9]]

#######################
## Defining function ##
#######################

def a_z_distance(dir, start, end):
    
    step_count = list()
    for node in start:
        step = 0
        current = node
        
        while current[-len(end) : ] != end:
            if step == len(dir):
                dir += dir

            current = map[current][int(dir[step])]
            step += 1  

        step_count.append(step)

    return step_count

#####################
## PART 1 SOLUTION ##
#####################

start = ["AAA"]
end = "ZZZ"

print("Part 1 Solution: ",  a_z_distance(direction, start, end ))

#####################
## PART 2 SOLUTION ##
#####################

start = [node for node in map if node[-1] == "A"]
end = "Z"

"""
We have multiple starting points and for those it takes different amount of steps to get to a node that's endig with "Z". 
So to get to a point where all nodes have "Z" ending we would have to loop through a couple of times and that's not efficient. 
Instead we calculate the Least Common Muliple of the different step amounts and that gives us the desired step count.
"""

print("Part 2 Solution: ",  math.lcm(*a_z_distance(direction, start, end)))