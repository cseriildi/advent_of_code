input = [ [] for i in range(len(str.splitlines(open('input.txt', 'r').read())))]

for index, row in enumerate(str.splitlines(open('input.txt', 'r').read())):
    input[index] = [int(num) for num in row]

risklevel = 0

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
 
# If the number is lower than the smallest neighbour, than it's a lowpoint and the risklevel is value + 1
        if num < min(neighbours): 
            risklevel += num + 1
        
print(risklevel)