import itertools
import re

###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

pattern = list()
damages = list()
for line in input:
        
    pattern.append(line.split()[0])
    damages.append(line.split()[1].split(","))

print(pattern, damages)
#########################
## FUNCTION DEFINITION ##
#########################









'''



possibilities = 0
for line in input:
    condition = line.split()[0]
    arrangement = [int(i) for i in line.split()[1].split(",")]

    need = sum(arrangement) - condition.count("#")
    q = condition.count("?")
    change = list(set([*itertools.permutations("#"*need + "."*(q-need), q)]))

    

    
    for c in change:
        new_condition = ""
        n = list(c)
        for char in condition:
            if char == "?":
                new_condition += n.pop(0)

            else:
                new_condition += char


        
        if (new_condition.replace(".", " ")).split() == ["#"*i for i in arrangement]:
            possibilities += 1


print(possibilities)

'''

possibilities = 0

for line in input:
    condition = (line.split()[0]).strip(".")
    arrangement = [int(i) for i in line.split()[1].split(",")]
    print(line,condition)
    q = re.findall("?", condition)
    #h = re.findall("#", condition)
    #print(line, q, h)

    need = sum(arrangement)
    have = condition.count("#")
    missing = need - have
    print(need + len(arrangement) -1, len(condition))


    for n in [*itertools.combinations(q, missing)]:
        new_condition = list(condition.replace("?", "."))
        for m in n:
            new_condition[m] = "#"
        

        if ("".join(new_condition)).replace(".", " ").split() == ["#"*int(i) for i in arrangement.split(",")]:
            possibilities += 1


print(possibilities)
