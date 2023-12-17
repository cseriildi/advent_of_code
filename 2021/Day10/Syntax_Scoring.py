input = str.splitlines(open('input.txt', 'r').read())

result = 0
for row in input:
    actual = row
    while '()' in actual or '[]' in actual or '{}' in actual or '<>' in actual:
            actual = actual.replace('()', '')
            actual = actual.replace('[]', '')
            actual = actual.replace('{}', '')
            actual = actual.replace('<>', '')


    for char in actual:
        if char  == ')':
            result += 3
            break
        if char  == ']':
            result += 57
            break
        if char  == '}':
            result += 1197
            break
        if char  == '>':
            result += 25137
            break
  
          
print(result)