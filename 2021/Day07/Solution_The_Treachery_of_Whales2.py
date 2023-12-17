import statistics, math

crab_positions = [int(i) for i in str.split(open('input.txt', 'r').read(), ',')]


avg1= math.floor(statistics.mean(crab_positions)) #round down average
avg2 = math.ceil(statistics.mean(crab_positions)) #round up average

fuel1 = 0 
fuel2 = 0

for position in crab_positions:
    # n*(n+1)/2 formula, where n is the distance between the crabs current positions and the possible best position
    fuel1 += (abs(avg1 - position) * (abs(avg1 - position) + 1)) / 2
    fuel2 += (abs(avg2 - position) * (abs(avg2 - position) + 1)) / 2

print(int(min(fuel1, fuel2)))