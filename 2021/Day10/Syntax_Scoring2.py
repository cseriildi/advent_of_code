input = str.splitlines(open('input.txt', 'r').read())

result = []
for row in input:
    total = 0
    actual = row
    while '()' in actual or '[]' in actual or '{}' in actual or '<>' in actual:
            actual = actual.replace('()', '')
            actual = actual.replace('[]', '')
            actual = actual.replace('{}', '')
            actual = actual.replace('<>', '')


    if not(')' in actual or ']' in actual or '}' in actual or '>' in actual):
        for char in reversed(actual):
            if char  == '(':
                total = total * 5 + 1

            if char  == '[':
                total = total * 5 + 2

            if char  == '{':
                total = total * 5 + 3

            if char  == '<':
                total = total * 5 + 4

    if total > 0:
        result.append(total)

print(sorted(result)[len(result) // 2])