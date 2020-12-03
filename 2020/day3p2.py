slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = open('input3.txt').read().split('\n')
result, width = 1, len(lines[0])
for slope in slopes:
    trees = position = 0
    for i in range(0, len(lines), slope[1]):
        if lines[i][position] == '#':
            trees += 1
        position = (position + slope[0]) % width
    result *= trees
print(result)
