###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

#########################
## FUNCTION DEFINITION ##
#########################

# https://en.wikipedia.org/wiki/Even–odd_rule
def even_odd_rule(x, y, polygon):

    j = len(polygon) - 1
    is_in = False
    for i in range(len(polygon)):
        if (x == polygon[i][0]) and (y == polygon[i][1]):
            return True
        if (polygon[i][1] > y) != (polygon[j][1] > y):
            slope = (x - polygon[i][0]) * (polygon[j][1] - polygon[i][1]) - (polygon[j][0] - polygon[i][0]) * (y - polygon[i][1])
            if slope == 0:
                return True
            if (slope < 0) != (polygon[j][1] < polygon[i][1]):
                is_in = not is_in
        j = i
    return is_in

#####################
## PART 1 SOLUTION ##
#####################

direction = str()
coordinates = []
x, y = 0, 0

# Finding the "S" which is the start of the pipeline, and one of the directions where it goes
while len(coordinates) == 0:
    if "S" in input[y]:
        x = input[y].index("S")
        coordinates.append((y, x))
    
        if input[y][x + 1] in ["-", "7", "J"]:
            x  += 1
            direction = "right"

        elif input[y][x - 1] in ["-", "L", "F"]:
            x -= 1
            direction = "left"

        else:
            y +=1
            direction = "down"

    else:
        y += 1

# Finding every part of the pipeline
while input[y][x] != "S":
    coordinates.append((y, x))

    if direction == "right":
        x += 1
        if input[y][x] == "7":
            direction = "down"

        elif input[y][x] == "J":
            direction = "up"

    elif direction == "left":
        x -= 1
        if input[y][x] == "F":
            direction = "down"

        elif input[y][x] == "L":
            direction = "up"

    elif direction == "up":
        y -= 1
        if input[y][x] == "F":
            direction = "right"

        elif input[y][x] == "7":
            direction = "left"

    else:
        y += 1
        if input[y][x] == "L":
            direction = "right"

        elif input[y][x] == "J":
            direction = "left"

tube_length = len(coordinates)

print("Part 1 Solution: ", tube_length // 2)

#####################
## PART 2 SOLUTION ##
#####################

# Using the even/odd rule count the enclosed elements excluding the parts of the pipeline
enclosed = sum([even_odd_rule(y, x, coordinates) for x in range(len(input[0])) for y in range(len(input))]) - tube_length

print("Part 2 Solution: ", enclosed)