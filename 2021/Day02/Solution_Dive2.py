f = open('input.txt', 'r')
input = str.splitlines(f.read())

x = 0
y = 0
aim = 0

for element in input:
    command = str.split(element, ' ')
    action = command[0]
    number = int(command[1])
    if action == 'forward':
        x += number
        y += number*aim
    elif action == 'down':
        aim += number
    elif action == 'up':
        aim -= number

print(x*y)

