###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#########################
## FUNCTION DEFINITION ##
#########################

def vector_distance(first, second = (0, 0)):
    return [first[0] + second[0],  first[1] + second[1]]

def count_energy(start_list, pattern):
    max_row = len(pattern)
    max_column = len(pattern[0])
  
    symbols = {"\\": {(0, 1): [(1, 0)], (-1, 0): [(0, -1)], (0, -1): [(-1, 0)], (1, 0): [(0, 1)]},
           "/": {(0, 1): [(-1, 0)], (-1, 0): [(0, 1)], (0, -1):[(1, 0)], (1, 0):[(0, -1)]},
           "|": {(0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)], (-1, 0):[(-1, 0)], (1, 0): [(1, 0)]},
           "-": {(-1, 0): [(0, 1), (0, -1)], (1, 0): [(0, 1), (0, -1)], (0, -1): [(0, -1)], (0, 1): [(0, 1)]},
           ".": {(-1, 0): [(-1, 0)], (1, 0): [(1, 0)], (0, -1):[(0, -1)], (0, 1): [(0, 1)]}}
    
    max_energy = 0
 
    for j in start_list:
        coordinates = [j]

        for coord in coordinates:

            row, column = coord[0]
            direction = coord[1]
            new_directions = symbols[pattern[row][column]][direction]

            for dir in new_directions:
                new_row, new_column = vector_distance((row, column), dir)
                
                if new_row in range(max_row) and new_column in range(max_column) and [(new_row, new_column), dir] not in coordinates:
                    coordinates.append([(new_row, new_column), dir])
                elif [(row, column), (dir[0] * -1, dir[1] * -1)] in start_list:
                    start_list.remove([(row, column), (dir[0] * -1, dir[1] * -1)])


        max_energy = max(len(list(set(i[0] for i in coordinates))), max_energy)

    return max_energy

#####################
## PART 1 SOLUTION ##
#####################

starting_coordinate = [[(0, 0), (0, 1)]]
energy = count_energy(starting_coordinate, input)

print("Part 1 Solution: ", energy)

#####################
## PART 2 SOLUTION ##
#####################
print("Part 2 with brute force, running time around 3 minutes, please wait for the result")
starting_coordinates = [[(0, i), (1, 0)] for i in range(len(input[0]))] + [[(len(input) - 1, i), (-1, 0)] for i in range(len(input[0]))] + [[(i, 0), (0, 1)] for i in range(len(input))] + [[(i, len(input) - 1), (0, -1)] for i in range(len(input))]

energy = count_energy(starting_coordinates, input)

print("Part 2 Solution: ", energy)