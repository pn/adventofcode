trees = position = 0
for line in open('input3.txt').read().split('\n'):
    if line[position] == '#':
        trees += 1
    position = (position + 3) % len(line)
print(trees)
