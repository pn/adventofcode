groups = [[]]
for line in open('input6.txt').read().splitlines():
    if not line:
        groups.append([])
        continue
    groups[-1].append(set(c for c in line))

total = 0
for group in groups:
    i = 0
    s = group[0]
    for j in range(1, len(group)):
        s = s.intersection(group[j])
    total += len(s)

print(total)
