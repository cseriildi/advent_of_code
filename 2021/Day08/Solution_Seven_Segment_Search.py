## Make the intput usable

input = str.splitlines(open('input.txt', 'r').read())

input2 = []

for i in input:
    input2.append(str.split(i, ' | '))

input3 = []

for i in range(len(input2)):
    input3.append([])
    for j in input2[i]:
        input3[i].append(str.split(j))

## Solution

counter = 0
for line in input3:
    for number in line[1]:
        if len(number) in [2, 3, 4, 7]:
            counter += 1
            
print(counter)
        