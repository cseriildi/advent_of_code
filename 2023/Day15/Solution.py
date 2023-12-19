###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().split(",")

#########################
## FUNCTION DEFINITION ##
#########################

def hashmap(string):
    current_value = 0
    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256
    return current_value

#####################
## PART 1 SOLUTION ##
#####################

print("Part 1 Solution: ", sum([hashmap(step) for step in input]))

#####################
## PART 2 SOLUTION ##
#####################

boxes = [dict() for i in range(265)]

for step in input:
    
    if "-" in step:
        label = step.strip("-")
        box_index = hashmap(label)

        if label in boxes[box_index]:
            del boxes[box_index][label]
    else:
        label, focal_length = step.split("=")
        box_index = hashmap(label)

        boxes[box_index][label] = int(focal_length)
            
focusing_power = 0
for box_index, box in enumerate(boxes, start = 1):
    for slot, focal_length in enumerate(box.values(), start = 1):
        focusing_power += box_index * slot * focal_length

print("Part 2 Solution: ", focusing_power)