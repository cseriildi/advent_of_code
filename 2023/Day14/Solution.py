###############
## IMPORTING ##
###############

import numpy as np
import pprint as pp

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()


transposed = [''.join(i) for i in zip(*input)]

done = list()

for line in transposed:

    new_line = line
    while ".O" in new_line:
        new_line = new_line.replace(".O", "O.")


    done.append(new_line)
tilted = [''.join(i) for i in zip(*done)]

sum = 0
for index, line in enumerate(tilted):
    sum += line.count("O")*(len(tilted)-index)


print(sum)

