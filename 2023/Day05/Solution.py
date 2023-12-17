###############
## IMPORTING ##
###############

import re
import copy

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
unsorted_seeds = [int(i) for i in f.readline().split()[1:]]
seeds = sorted(unsorted_seeds)

map = []
for i in re.sub(r'[^ \n0-9/]+', '', f.read()).split("\n\n"):
    map.append(str.splitlines(i))

levels = []
for i in range(len(map)):
    levels.append([])
    for j in map[i]:
        if j.split() != []:
            levels[i].append([int(k) for k in j.split()])

    levels[i] = sorted(levels[i], key = lambda x: x[1])

seed_ranges = list()

for i in range(len(unsorted_seeds)):
    if i % 2 ==0:
      seed_ranges.append([unsorted_seeds[i], unsorted_seeds[i] + unsorted_seeds[i+1]])

locations = sorted(seed_ranges, key=lambda x: x[0])


#####################
## PART 1 SOLUTION ##
#####################

location_list = list()
for seed in seeds:
    location = seed
    for level in levels:
        for row in level:
            if location in range(row[1],row[1]+ row[2]):
                location = location - row[1]  + row[0]
                break
    location_list.append(location)

print("Part 1 Solution: ", min(location_list))


#####################
## PART 2 SOLUTION ##
#####################

for level in levels:
    locations_with_breakpoints =copy.deepcopy(locations)

    breakpoints = set()
    for i in level:
        breakpoints.add(i[1])
        breakpoints.add(i[1]+i[2])

    for point in breakpoints:
        for id,  seed in enumerate(locations):     

            if point >seed[0] and point< seed[-1]-1:
                locations_with_breakpoints[id].append(point)

    locations_sliced = list()
    for n in locations_with_breakpoints:
        n.sort()
        for index in range(len(n)-1):
            locations_sliced.append([n[index], n[index+1]])

    locations= copy.deepcopy(locations_sliced)

    for ind, loc in enumerate(locations):   
        for row in level:
           
            if loc[0]>= row[1] and loc[-1]<= row[1]+ row[2]:
                locations_sliced[ind][0] =  loc[0] - row[1]  + row[0]
                locations_sliced[ind][-1] = locations_sliced[ind][0]+ loc[-1] - loc[0]
                break
    locations= copy.deepcopy(locations_sliced)
    
print("Part 2 Solution: ", min([i[0] for i in locations]))

            
           

