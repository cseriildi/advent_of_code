input = str.split(open('input.txt', 'r').read(), ',')
days=80
for i in range(days):
    for index, fish in enumerate(input):
        if fish == 0:
            input[index]=6
            input.append(9)
        else:
            input[index]= int(input[index]) -1

print(len(input))

