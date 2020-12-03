slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = open('input3.txt').read().split('\n')
result, width = 1, len(lines[0])
for slope in slopes:
    trees = position = 0
    for i in range(0, len(lines), slope[1]):
        if lines[i][position % width] == '#':
            trees += 1
        position = (position + slope[0]) % width
    result *= trees
print(result)

# alternative solution

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = open('input3.txt').read().split('\n')
result, width = 1, len(lines[0])
for slope in slopes:
    trees = 0
    for i in range(0, len(lines), slope[1]):
        if lines[i][(i // slope[1] * slope[0]) % width] == '#':
            trees += 1
    result *= trees
print(result)

# alternative solution

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = open('input3.txt').read().split('\n')
result = 1
for slope in slopes:
    result *= [l[(i // slope[1] * slope[0]) % len(l)] for i, l in enumerate(lines) if (i % slope[1]) == 0].count('#')
print(result)

# alternative solution

import math
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = open('input3.txt').read().split('\n')
print(math.prod([[l[(i // slope[1] * slope[0]) % len(l)] for i, l in enumerate(lines) if (i % slope[1]) == 0].count('#') for slope in slopes]))

# alternative solution

import math
print(math.prod([[l[(i // slope[1] * slope[0]) % len(l)] for i, l in enumerate(open('input3.txt').read().split('\n')) if (i % slope[1]) == 0].count('#') for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
