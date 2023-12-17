f = open('input.txt', 'r')
input = str.splitlines(f.read())

oxygen = input.copy()
co2 = input.copy()

for i in range(len(input[0])):
    count_ones = 0
    common = ''
    leastcommon = ''

    for number in oxygen:
        count_ones += int(number[i])
    
    if  count_ones >= len(oxygen)/2:
        common = '1'
    else:
        common = '0'

    count_ones = 0

    for number in co2:
        count_ones += int(number[i])

    if  count_ones >= len(co2)/2:
        leastcommon = '0'
    else:
        leastcommon = '1'

    for number in input:
        if number[i] != common and (number in oxygen) and len(oxygen)> 1:
            oxygen.remove(number)
            
        if number[i] != leastcommon and (number in co2) and len(co2)>1:
            co2.remove(number)

print(oxygen, co2)
print(int(''.join(oxygen),2) * int(''.join(co2),2))
    