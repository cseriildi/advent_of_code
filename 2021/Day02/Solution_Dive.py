f = open('input.txt', 'r')
input = str.splitlines(f.read())

x = 0
y = 0

for element in  input:
    command = str.split(element, ' ')
    action = command[0]
    number = int(command[1])    
    
    if action == 'forward':
        x += number
    elif action == 'down':
        y += number
    elif action == 'up':
        y -= number

print(x*y)

