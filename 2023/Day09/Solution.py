###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = [[int(i) for i in line.split()] for line in f.read().splitlines()]

#######################
## Defining function ##
#######################

def predicting(history, direction = 1):
    
    map = [history]
    while list(set(map[-1])) != [0]:
        map.append([map[-1][k + 1] - map[-1][k] for k in range(len(map[-1]) - 1)])

    prediction = 0
    for i in range(2, len(map)+1):
        if direction == 1:
            prediction += map[-i][-1] 
        else:
            prediction = map[-i][0] - prediction

    return prediction  

#####################
## PART 1 SOLUTION ##
#####################

prediction = sum([predicting(history) for history in input])

print( "Part 1 Solution: ", prediction)

#####################
## PART 2 SOLUTION ##
#####################

previous = -1
prediction = sum([predicting(history, previous) for history in input])

print( "Part 2 Solution: ", prediction)