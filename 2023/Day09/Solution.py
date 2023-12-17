###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = [[int(i) for i in line.split()] for line in f.read().splitlines()]

#######################
## Defining function ##
#######################

def predicting(histories, direction ):
    
    prediction =  0
    for history in histories:

        map = [history]
        while list(set(map[-1])) != [0]:
            map.append([map[-1][k + 1] - map[-1][k] for k in range(len(map[-1]) - 1)])

        p = 0
        for i in range(2, len(map)+1):
            if direction == 1:
                p += map[-i][-1] 
            else:
                p = map[-i][0] - p

        prediction += p

    return prediction  

#####################
## PART 1 SOLUTION ##
#####################

next = 1
print( "Part 1 Solution: ", predicting(input, next))

#####################
## PART 2 SOLUTION ##
#####################

previous = -1
print( "Part 2 Solution: ", predicting(input, previous))