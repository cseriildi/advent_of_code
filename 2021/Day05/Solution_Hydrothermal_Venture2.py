import re
f = open('input.txt', 'r')
input = re.split('\n| -> |,',f.read())

for i in range(len(input)):
    input[i] = int(input[i])

matrix = []

for i in range(max(input)+1):
    matrix.append([])
    for j in range(max(input)+1):
        matrix[i].append(0)

for i in range(0,len(input), 4):
    xmarker = input[i]
    ymarker = input[i+1]

    for j in range(max(abs(input[i]-input[i+2]),abs(input[i+1]-input[i+3]))+1):
        
        if input[i]- input[i+2] < 0 :
            xmarker = input[i] + j
        elif input[i]- input[i+2] > 0 :
            xmarker = input[i] - j

        if input[i+1]- input[i+3] < 0 :
            ymarker = input[i+1] + j
        elif input[i+1]- input[i+3] > 0 :
            ymarker = input[i+1] - j
    
        matrix[xmarker][ymarker] +=1

counter = 0
for i in  matrix:
    for j in i:
        if j > 1:
            counter += 1

print(counter)

