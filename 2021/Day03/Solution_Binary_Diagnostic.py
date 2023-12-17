f = open('input.txt', 'r')
input = str.splitlines(f.read())

gamma = [0 for i in range(len(input[0]))]
epsilon = ''

for i in range(len(input[0])):
    for number in input:
        gamma[i] += int(number[i])

    if  gamma[i]/len(input) > 0.5:
        gamma[i] = '1'
        epsilon += '0'
    else:
        gamma[i] = '0'
        epsilon += '1'
g = int(''.join(gamma), 2)
e = int(epsilon, 2)

print(e*g)





