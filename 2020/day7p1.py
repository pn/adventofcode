bags = {}
for line in open('input7.txt').read().splitlines():
    containing, _list = line.split(' bags contain ', 2)
    if _list.endswith('no other bags.'):
        continue
    for item in _list.split(', '):
        contained = ' '.join(item.split(' ')[1:-1])
        bags[contained] = bags.get(contained, {})
        bags[contained][containing] = True

all_containing = []
def find_containing(name):
    for bag in bags.get(name, []):
        if bag not in all_containing:
            all_containing.append(bag)
            find_containing(bag)
find_containing('shiny gold')
print(len(all_containing))
