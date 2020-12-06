from functools import reduce

groups = [[]]
for line in open('input6.txt').read().splitlines():
    if not line:
        groups.append([])
        continue
    groups[-1].append(set(list(line)))
print(sum(len(reduce(lambda a, b: a.union(b), group)) for group in groups))

# alternative solution

groups = [(list(set(list(ans)) for ans in group.split('\n'))) for group in open('input6.txt').read().split('\n\n')]
print(sum(len(group[0].union(*group[1:])) for group in groups))
