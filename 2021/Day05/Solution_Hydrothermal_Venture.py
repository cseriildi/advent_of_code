import re
f = open('input.txt', 'r')
input = re.split('\n| -> |,',f.read())

input2 = []

for i in range(0,len(input), 4):
    if input[i] == input[i+2] or input[i+1] == input[i+3]:
        input2.append(int(input[i]))
        input2.append(int(input[i+1]))
        input2.append(int(input[i+2]))
        input2.append(int(input[i+3]))

matrix = []

for i in range(max(input2)+1):
    matrix.append([])
    for j in range(max(input2)+1):
        matrix[i].append(0)

for i in range(0,len(input2), 4):
    xmarker = input2[i]
    ymarker = input2[i+1]

    for j in range(max(abs(input2[i]-input2[i+2]),abs(input2[i+1]-input2[i+3]))+1):
        
        if input2[i]- input2[i+2] < 0 :
            xmarker = input2[i] + j
        elif input2[i]- input2[i+2] > 0 :
            xmarker = input2[i] - j

        if input2[i+1]- input2[i+3] < 0 :
            ymarker = input2[i+1] + j
        elif input2[i+1]- input2[i+3] > 0 :
            ymarker = input2[i+1] - j
    
        matrix[xmarker][ymarker] +=1

counter = 0
for i in  matrix:
    for j in i:
        if j > 1:
            counter += 1

print(counter)

