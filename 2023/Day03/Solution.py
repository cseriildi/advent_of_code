###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

numbers = [[] for i in range(len(input)) ]
symbols = []

for y, line in enumerate(input):
    num =""
    for x, char in enumerate(line):

        if char.isdigit():
            num += char
            if x == len(line) -1 :

                for j in range(len(num)):
                    numbers[y].append(int(num)) 
        else:
            if num != "":
                for j in range(len(num)):
                    numbers[y].append(int(num))
               
                num = ""
            
            numbers[y].append('')

        if char.isdigit() == False and char != ".":
            symbols.append([char, y, x])

#####################
## PART 1 SOLUTION ##
#####################

parts = 0
for sym in symbols:

    for y in range(-1, 2):

        if numbers[sym[1] + y][sym[2]]: 
            parts += numbers[sym[1] + y][sym[2]]
        
        else:
            for x in range(-1, 2, 2):

                if numbers[sym[1]+ y][sym[2] + x]:
                    parts += numbers[sym[1] + y][sym[2] + x]
                
print("Part 1 Solution: ", parts)

#####################
## PART 2 SOLUTION ##
#####################

parts = 0

for sym in symbols:
    if sym[0]== "*":
        counter = 0
        product = 1

        for y in range(-1, 2):
            if numbers[sym[1] + y][sym[2]]:
                counter +=1
                product *= numbers[sym[1] + y][sym[2]]
            
            else:
                for x in range(-1, 2, 2):
                    if numbers[sym[1]+ y][sym[2] + x]:
                        product *= numbers[sym[1] + y][sym[2] + x]
                        counter += 1
        if counter == 2:
            parts += product
                
print("Part 2 Solution: ", parts)