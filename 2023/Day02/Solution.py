###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()
games= dict()

for line in input:
    game_number = int(line.split(": ")[0][5:])
    sets = line.split(": ")[1].split("; ")

    games[game_number]= dict()
    games[game_number]["red"] = list()
    games[game_number]["green"] = list()
    games[game_number]["blue"] = list()
    
    for cubes in sets:
        for cubes in  cubes.split(", "):
            for color in games[game_number].keys():
                if color in cubes:
                    games[game_number][color].append(int(cubes.split(" ")[0]))

#####################
## PART 1 SOLUTION ##
#####################

sum = 0
for id in games:
    if max(games[id]["red"]) <= 12 and max(games[id]["green"]) <= 13 and max(games[id]["blue"]) <= 14:
        sum += id

print("Part 1 Solution: ", sum)

#####################
## PART 2 SOLUTION ##
#####################

sum = 0
for id in games:

    sum += max(games[id]["red"]) * max(games[id]["green"]) * max(games[id]["blue"])

print("Part 2 Solution: ", sum)