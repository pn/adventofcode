bags = {}
for line in open('input7.txt').read().splitlines():
    containing, _list = line.split(' bags contain ', 2)
    bags[containing] = {}
    if _list.endswith('no other bags.'):
        continue
    for item in _list.split(', '):
        contained = ' '.join(item.split(' ')[1:-1])
        bags[containing][contained] = int(item[0])

l = ['shiny gold']
for j in range(len(bags)):
    for bag in bags:
        for i in l:
            contains = bags[bag].get(i, '')
            if contains and bags[i] not in l:
                if bag not in l:
                    l.append(bag)
print(len(set(l)) - 1)
