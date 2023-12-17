import statistics

crab_positions = [int(i) for i in str.split(open('input.txt', 'r').read(), ',')]

fuel = 0

for position in crab_positions:
    #sum all distance between the crabs positions and the best position
    fuel += abs(position - statistics.median(crab_positions))

print(fuel)