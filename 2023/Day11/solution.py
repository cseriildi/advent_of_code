###############
## IMPORTING ##
###############

import itertools 

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = [list(line) for line in f.read().splitlines()]

#########################
## FUNCTION DEFINITION ##
#########################

def find_galaxies(universe, expansion_size):

    empty_rows  = [row for row in range(len(universe)) if set(universe[row]) == set(".")]
    empty_columns = [column for column in range(len(universe[0])) if set([universe[i][column] for i in range(len(universe))]) == set(".")]
    
    galaxies = list()

    for row in range(len(universe)):
        for column in range(len(universe[0])):

            if universe[row][column] == "#":
                galaxy_row = row + sum([expansion_size - 1 for empty_row in empty_rows if row > empty_row]) 
                galaxy_column = column + sum([expansion_size - 1 for empty_column in empty_columns if column > empty_column])

                galaxies.append([galaxy_row, galaxy_column])

    return galaxies

def shortest_path(galaxy_list):

    sum_of_shortest_paths = 0
    for pair in itertools.combinations(galaxy_list, 2):
        sum_of_shortest_paths += abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1]) 
        
    return sum_of_shortest_paths

#####################
## PART 1 SOLUTION ##
#####################

growth = 2

print("Part 1 Solution: ", shortest_path(find_galaxies(input, growth)))

#####################
## PART 2 SOLUTION ##
#####################

growth = 1000000

print("Part 2 Solution: ", shortest_path(find_galaxies(input, growth)))