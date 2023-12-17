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

sum_result = 0

for i in range(len(input3)):
    decoder = {}


## These 4 number is obvious because of their lenghts

    for number in input3[i][0]:


        if len(number) == 2:
            decoder['1'] = number
            

        elif len(number) == 3:
            decoder['7'] = number
            

        elif len(number)== 4:
            decoder['4'] = number
            

        elif len(number) == 7:
            decoder['8'] =  number
            


## The other 6 number can be guessed from the first 4  

    for number in input3[i][0]:
        if len(number) == 5:

            if set(decoder['1']).issubset(set(number)):
                decoder['3'] = number
              
            elif (set(decoder['4'])-set(decoder['1'])).issubset(set(number)):
                decoder['5'] = number
                
            else:
                decoder['2'] = number
               
            

        elif len(number) == 6:

            if set(decoder['4']).issubset(set(number)):
                decoder['9'] = number            
            
            elif set(decoder['1']).issubset(set(number)):
                decoder['0'] = number
             
            else:
                decoder['6'] = number

## Now we have the decoder, lets use it to decode the new numbers

    result = ''

    for new_number in input3[i][1]:
         
        for number, code in decoder.items():
            if set(code) == set(new_number):
                result += number

    sum_result += int(result)
           
print(sum_result)


    
    



