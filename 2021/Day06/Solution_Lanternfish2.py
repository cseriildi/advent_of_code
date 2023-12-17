import math
input = str.split(open('input.txt', 'r').read(), ',')
fishes = [0 for i in range(9)]
days =256

for fish in input:
    fishes[int(fish)] += 1

for day in range(days):

    placeholder = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + placeholder
    fishes[7] = fishes[8]
    fishes[8] = placeholder
    

print(sum(fishes))