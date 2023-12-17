###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().split()

#####################
## PART 1 SOLUTION ##
#####################

sum = 0
for line in input:
    only_numbers = "".join(filter(str.isdigit, line))
    
    if only_numbers:
        sum += int(only_numbers[0]+ only_numbers[-1])

print("Part 1 Solution: ", sum)

#####################
## PART 2 SOLUTION ##
#####################

numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", 
           "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}

sum = 0
for line in input:
    first_num = ""
    last_num = ""    
    i = 0

    while (first_num== "" or last_num== "") and i <= len(line)+1:
        for num in numbers.keys():
        
            if first_num == "" and num in line[:i]:
                first_num = numbers[num]

            if last_num == "" and num in line[-i-1:]:
                last_num = numbers[num]
        i += 1

    sum += int(first_num + last_num)
    
print("Part 2 Solution: ", sum)