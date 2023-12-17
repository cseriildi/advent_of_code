import re

f = open('input.txt', 'r')
input = f.read()

numbers = str.split(str.splitlines(input)[0], ',')

input = (str.split(input, '\n\n'))[1:]
bo = []
for i in input:
    bo.append(str.splitlines(i))

boards = []

for i in range(len(bo)):
    boards.append([])
    for j in bo[i]:
        boards[i].append(str.split(j))

result = []

for index, num in enumerate(numbers):

    for index1, board in enumerate(boards):
        unmarkedsum = 0

        for index2, row in enumerate(board):
            for index3, element in enumerate(row):

                if element == num:

                    boards[index1][index2][index3] = 'X'
                   
                    if row.count('X') == 5 or (board[0][index3], board[1][index3], board[2][index3], board[3][index3], board[4][index3] ).count('X') == 5:
                        
                        
                        for r in board:
                            for e in r:
                             
                                if e != 'X':
                                    unmarkedsum += int(e)
                                
                                board[board.index(r)][r.index(e)] = 'i'

                        result.append(unmarkedsum*int(num))
                        
                        
                        



print(result[0])
