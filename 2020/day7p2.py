bags = {}
for line in open('input7.txt').read().splitlines():
    containing, _list = line.split(' bags contain ', 2)
    bags[containing] = {}
    if _list.endswith('no other bags.'):
        continue
    for item in _list.split(', '):
        contained = ' '.join(item.split(' ')[1:-1])
        bags[containing][contained] = int(item[0])

def count_bags(containing):
    return sum(bags[containing][contained] * (1 + count_bags(contained)) for contained in bags[containing])
print(count_bags('shiny gold'))


