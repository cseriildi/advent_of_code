###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
numbers = [int(i) for i in str.splitlines(f.read())]

#########################
## FUNCTION DEFINITION ##
#########################

def increase_count(list_of_numbers):

    return sum([1 for index in range(len(list_of_numbers) - 1) if list_of_numbers[index] < list_of_numbers[index + 1]])
              
#####################
## PART 1 SOLUTION ##
#####################
         
print("Part 1 Solution: ", increase_count(numbers))

#####################
## PART 2 SOLUTION ##
#####################

sliding = [sum(numbers[i : i + 3]) for i in range(len(numbers) - 2)]

print("Part 2 Solution: ", increase_count(sliding))