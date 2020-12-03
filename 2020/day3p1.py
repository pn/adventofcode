trees = position = 0
for line in open('input3.txt').read().split('\n'):
    if line[position] == '#':
        trees += 1
    position = (position + 3) % len(line)
print(trees)

# alternative solution

lines = open('input3.txt').read().split('\n')
print([line[(i * 3) % len(line)] for i, line in enumerate(lines)].count('#'))

# one-liner

print([l[(i * 3) % len(l)] for i, l in enumerate(open('input3.txt').read().split('\n'))].count('#'))
