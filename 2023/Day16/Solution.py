###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#########################
## FUNCTION DEFINITION ##
#########################

def vector_distance(first, second = (0, 0)):
    return (first[0] + second[0],  first[1] + second[1])

def count_energy(start, pattern):
    max_row = len(pattern)
    max_column = len(pattern[0])

    right = (0, 1)
    left = (0, -1)
    up = (-1, 0)
    down = (1, 0)
  
    symbols = {"\\": {right: [down], up: [left], left: [up], down: [right]},
           "/": {right: [up], up: [right], left:[down], down:[left]},
           "|": {right: [up, down], left: [up, down], up:[up], down: [down]},
           "-": {up: [right, left], down: [right, left], left: [left], right: [right]},
           ".": {up: [up], down: [down], left:[left], right: [right]}}
    
    coordinates = set()
    been_there = set()
    to_check = [start]

    for p in to_check:
        if p not in been_there:
            been_there.add(p)

            row, column = p[0]
            
            direction = p[1]

            new_directions = symbols[pattern[row][column]][direction]
                
            for dir in new_directions:

                new_row, new_column = vector_distance((row, column), dir)

                if new_row in range(max_row) and new_column in range(max_column):
                    to_check.append(((new_row, new_column), dir))

            coordinates.add((row, column))
    return len(coordinates)

#####################
## PART 1 SOLUTION ##
#####################

starting_coordinate = ((0, 0), (0, 1))
energy = count_energy(starting_coordinate, input)

print("Part 1 Solution: ", energy)

#####################
## PART 2 SOLUTION ##
#####################

starting_coordinates = [((0, i), (1, 0)) for i in range(len(input[0]))] + [((len(input) - 1, i), (-1, 0)) for i in range(len(input[0]))] + [((i, 0), (0, 1)) for i in range(len(input))] + [((i, len(input) - 1), (0, -1)) for i in range(len(input))]

energy = max([count_energy(start, input) for start in starting_coordinates])

print("Part 2 Solution: ", energy)