input = [ [] for i in range(len(str.splitlines(open('input.txt', 'r').read())))]

for index, row in enumerate(str.splitlines(open('input.txt', 'r').read())):
    input[index] = [int(num) for num in row]


lowpoints = []
for i, row in enumerate(input):
    for j, num in enumerate(row):
        neighbours = set()


# Check if the element is in the corner or on the edge and get the neigbours 
        try:
            if i == 0: # i-1 would be -1, and that is a valid index, but that's not a neighbour
                raise(ValueError) 
            neighbours.add(input[i-1][j])
        except:
            pass
        
        try:
            neighbours.add(input[i+1][j])
        except:
            pass
            
        try:
            if j == 0: # j-1 would be -1, and that is a valid index, but that's not a neighbour
                raise(ValueError) 
            neighbours.add(input[i][j-1])
        except:
            pass

        try:
            neighbours.add(input[i][j+1])
        except:
            pass
 
# If the number is lower than the smallest neighbour, than it's a lowpoint 
        if num < min(neighbours): 
            lowpoints.append([i, j])




top3basin = [0, 0, 0]

# Loop over the lowpoints, check the surrounding fields, count fields between the nines
for lowpoint in lowpoints:

    neighbours = [lowpoint]
    actualbasin = [lowpoint]

    while len(neighbours) > 0:
        for actual in neighbours:
        
            i = actual[0]
            j = actual[1]
            try:
                if i == 0: # i-1 would be -1, and that is a valid index, but that's not a neighbour
                    raise(ValueError) 
                elif [i-1, j] not in actualbasin and input[i-1][j] < 9:
                    neighbours.append([i-1, j])
                    actualbasin.append([i-1, j])
            except:
                pass
            
            try:
                if [i+1, j] not in actualbasin and input[i+1][j] < 9:
                    neighbours.append([i+1, j])
                    actualbasin.append([i+1, j])
            except:
                pass
                
            try:
                if j == 0: # j-1 would be -1, and that is a valid index, but that's not a neighbour
                    raise(ValueError) 
                elif [i, j-1] not in actualbasin and input[i][j-1] < 9:
                    neighbours.append([i, j-1])
                    actualbasin.append([i, j-1])
            except:
                pass

            try:
                if [i, j+1] not in actualbasin and input[i][j+1] < 9:
                        neighbours.append([i, j+1])
                        actualbasin.append([i, j+1])
            except:
                pass

            
        neighbours.remove(actual)

    top3basin.sort()

# Get the three biggest basinsize
    if len(actualbasin) > top3basin[0]:
        top3basin[0] = len(actualbasin)
    

print(top3basin[0] * top3basin[1] * top3basin[2])

