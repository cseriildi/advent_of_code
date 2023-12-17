###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#########################
## Function definition ##
#########################

def getPossibilies(times, distances):

    races = dict()
    for i in range(len(times)):
        races[i] = {"time": int(times[i]), "distance": int(distances[i])}

    possibilities = 1

    for race in range(len(races)):
        button_press_time = 0
        # speed = button_press_time
        # time_left = races[race]["time"] - button_press_time
        # new_distance = time_left * speed

        while (races[race]["time"] - button_press_time) * button_press_time <= races[race]["distance"] :
            button_press_time += 1

        # The number of winning possiblities are between the minimum and the maximum press time
        # min_time = button_press_time
        # max_time = races[race]["time"] - button_press_time
        
        possibilities *= len(range(button_press_time, races[race]["time"] - button_press_time))
        
    return possibilities

#####################
## PART 1 SOLUTION ##
#####################

part1_times = input[0].split(":")[1].split()
part1_distances = input[1].split(":")[1].split()

print("Part 1 Solution: ", getPossibilies(part1_times, part1_distances))

#####################
## PART 2 SOLUTION ##
#####################

"""
In part 2 we have to ignore the spaces between the numbers, hence there'll be only 1 race
"""

part2_times = input[0].split(":")[1].replace(" ", "").split()
part2_distances = input[1].split(":")[1].replace(" ", "").split()

print("Part 1 Solution: ", getPossibilies(part2_times, part2_distances))